#!/usr/bin/env python3
"""Export a Claude Code session transcript (JSONL) to readable Markdown.

Claude Code keeps each session in <config>/projects/<cwd-slug>/<session-id>.jsonl
(<config> is $CLAUDE_CONFIG_DIR or ~/.claude). This keeps what a person would
want to reread: the student's messages and slash commands, Claude's replies,
and one line per tool call. Thinking, tool output, subagent internals and
injected skill bodies are left out, and common secrets are redacted.
Standard library only.

Usage:
  export_chat.py                         current session (CLAUDE_CODE_SESSION_ID) or the newest one here
  export_chat.py --list                  recent sessions for this folder and its parents
  export_chat.py --session ID --out chats/2026-09-25-lab1.md --url URL --index chats/INDEX.md
  export_chat.py --test                  self-test
"""
import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import tempfile

SECRETS = [
    (re.compile(r"sk-ant-[A-Za-z0-9_\-]{10,}"), "<REDACTED>"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "<REDACTED>"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}"), "<REDACTED>"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "<REDACTED>"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"), "<REDACTED>"),
    (re.compile(r"(?i)\b(password|passwd|pwd|secret|(?:ws)?token|api[_-]?key)(\s*[:=]\s*)(\"[^\"]*\"|'[^']*'|\S+)"), r"\1\2<REDACTED>"),
    (re.compile(r"\b[0-9a-f]{32}\b"), "<REDACTED>"),  # Moodle web service keys
]
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
COMMAND = re.compile(r"<command-name>\s*(/?[^<\s]+)\s*</command-name>")
COMMAND_ARGS = re.compile(r"<command-args>(.*?)</command-args>", re.S)
TOOL_ARG_KEYS = ["command", "file_path", "path", "pattern", "skill", "description", "url", "query", "prompt"]


def config_dir():
    return pathlib.Path(os.environ.get("CLAUDE_CONFIG_DIR", pathlib.Path.home() / ".claude"))


def slug(path):
    return re.sub(r"[^A-Za-z0-9]", "-", str(path))


def project_dirs(cwd):
    """Transcript folders for cwd and each parent, nearest first."""
    root = config_dir() / "projects"
    here = pathlib.Path(cwd).resolve()
    return [root / slug(p) for p in [here, *here.parents] if (root / slug(p)).is_dir()]


def find_session(session_id):
    matches = sorted((config_dir() / "projects").glob(f"*/{session_id}.jsonl"),
                     key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0] if matches else None


def default_transcript(cwd):
    env_id = os.environ.get("CLAUDE_CODE_SESSION_ID")
    if env_id:
        for d in project_dirs(cwd):
            if (d / f"{env_id}.jsonl").is_file():
                return d / f"{env_id}.jsonl"
    candidates = [p for d in project_dirs(cwd) for p in d.glob("*.jsonl")]
    return max(candidates, key=lambda p: p.stat().st_mtime) if candidates else None


def redact(text):
    for pattern, replacement in SECRETS:
        text = pattern.sub(replacement, text)
    return text


def load(path):
    rows = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def parts(message):
    content = message.get("content") if isinstance(message, dict) else None
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return content if isinstance(content, list) else []


def user_text(row):
    """The student's words or slash command, or None for tool results and injected text."""
    if row.get("isMeta"):
        return None
    texts = [p.get("text", "") for p in parts(row.get("message")) if p.get("type") == "text"]
    if not texts:
        return None
    text = "\n".join(texts)
    command = COMMAND.search(text)
    if command:
        name = command.group(1) if command.group(1).startswith("/") else "/" + command.group(1)
        args = COMMAND_ARGS.search(text)
        args = args.group(1).strip() if args else ""
        return f"`{name} {args}`" if args else f"`{name}`"
    text = REMINDER.sub("", text).strip()
    if not text or text.startswith(("Base directory for this skill", "<local-command", "Caveat:")):
        return None
    return text


def tool_line(part, cwd):
    name = part.get("name", "tool")
    args = part.get("input") or {}
    value = next((str(args[k]) for k in TOOL_ARG_KEYS if k in args and args[k]), "")
    value = value.replace(str(cwd).rstrip("/") + "/", "").splitlines()[0] if value else ""
    if len(value) > 90:
        value = value[:87] + "..."
    return f"{name} `{value}`" if value else name


def when(timestamp):
    try:
        return dt.datetime.fromisoformat(timestamp.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
    except (AttributeError, ValueError):
        return ""


def to_markdown(rows, title=None, url=None):
    convo = [r for r in rows if r.get("type") in ("user", "assistant") and not r.get("isSidechain")]
    session_id = next((r.get("sessionId") for r in rows if r.get("sessionId")), "unknown")
    cwd = next((r.get("cwd") for r in convo if r.get("cwd")), "")
    branch = next((r.get("gitBranch") for r in convo if r.get("gitBranch")), "")
    agent = next((r.get("agentSetting") for r in rows if r.get("type") == "agent-setting" and r.get("agentSetting")), "")
    stamps = [r.get("timestamp") for r in convo if r.get("timestamp")]
    first_user = next((t for t in (user_text(r) for r in convo if r.get("type") == "user") if t), "")
    title = title or (first_user.splitlines()[0][:70] if first_user else "Claude Code session")

    blocks, tools, replies, block_time = [], [], [], ""

    def flush():
        nonlocal tools, replies
        if tools or replies:
            body = []
            if tools:
                body.append("> Did: " + "; ".join(tools))
            body.extend(replies)
            blocks.append((f"### Claude · {block_time}", "\n\n".join(body)))
        tools, replies = [], []

    for row in convo:
        if row.get("type") == "user":
            text = user_text(row)
            if text:
                flush()
                blocks.append((f"### You · {when(row.get('timestamp'))}", text))
            continue
        if not tools and not replies:
            block_time = when(row.get("timestamp"))
        for part in parts(row.get("message")):
            if part.get("type") == "tool_use":
                tools.append(tool_line(part, cwd))
            elif part.get("type") == "text" and part.get("text", "").strip():
                replies.append(part["text"].strip())
    flush()

    header = [
        f"# {title}",
        "",
        f"- **Date:** {when(stamps[0]) if stamps else '?'} → {when(stamps[-1]) if stamps else '?'}",
        f"- **Session:** `{session_id}`",
        f"- **Resume:** `claude --resume {session_id}`",
        f"- **Link:** {url or 'none given'}",
        f"- **Folder:** `{cwd}`" + (f" · branch `{branch}`" if branch else ""),
    ]
    if agent:
        header.append(f"- **Agent:** `{agent}`")
    header += ["", "---", ""]
    body = [f"{heading}\n\n{text}\n" for heading, text in blocks]
    return redact("\n".join(header) + "\n".join(body))


def list_sessions(cwd, limit=10):
    files = sorted((p for d in project_dirs(cwd) for p in d.glob("*.jsonl")),
                   key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    lines = []
    for f in files:
        rows = load(f)
        first = next((t for t in (user_text(r) for r in rows if r.get("type") == "user" and not r.get("isSidechain")) if t), "")
        stamp = dt.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        lines.append(f"{stamp}  {f.stem}  {first.splitlines()[0][:60] if first else '(no messages)'}")
    return "\n".join(lines) or "No sessions found for this folder."


def append_index(index, out, title, url, stamp):
    index = pathlib.Path(index)
    index.parent.mkdir(parents=True, exist_ok=True)
    if not index.exists():
        index.write_text("# Saved chats\n\n", encoding="utf-8")
    rel = os.path.relpath(out, index.parent)
    link = f" · [link]({url})" if url else ""
    with index.open("a", encoding="utf-8") as fh:
        fh.write(f"- {stamp} · [{title}]({rel}){link}\n")


def self_test():
    rows = [
        {"type": "agent-setting", "agentSetting": "java-expert", "sessionId": "s1"},
        {"type": "user", "sessionId": "s1", "cwd": "/w", "gitBranch": "main", "timestamp": "2026-09-25T10:00:00Z",
         "message": {"role": "user", "content": "My lab crashes. token=abc123 wstoken=ws999 key 0123456789abcdef0123456789abcdef"}},
        {"type": "assistant", "sessionId": "s1", "cwd": "/w", "timestamp": "2026-09-25T10:00:05Z",
         "message": {"content": [{"type": "thinking", "thinking": "secret thoughts"},
                                 {"type": "tool_use", "name": "Bash", "input": {"command": "javac /w/Main.java"}}]}},
        {"type": "user", "sessionId": "s1", "timestamp": "2026-09-25T10:00:06Z",
         "message": {"content": [{"type": "tool_result", "content": "compiler output"}]}},
        {"type": "user", "isMeta": True, "sessionId": "s1", "message": {"content": [{"type": "text", "text": "Base directory for this skill: /x"}]}},
        {"type": "assistant", "sessionId": "s1", "timestamp": "2026-09-25T10:00:09Z",
         "message": {"content": [{"type": "text", "text": "Line 8 dereferences null. Key sk-ant-abcdefghijklmnop."}]}},
        {"type": "assistant", "isSidechain": True, "sessionId": "s1", "message": {"content": [{"type": "text", "text": "subagent chatter"}]}},
        {"type": "user", "sessionId": "s1", "timestamp": "2026-09-25T10:01:00Z",
         "message": {"content": "<command-message>go</command-message>\n<command-name>/go</command-name>\n<command-args>drill</command-args>"}},
    ]
    md = to_markdown(rows, url="https://claude.ai/code/session_x")
    for expected in ["# My lab crashes.", "`claude --resume s1`", "https://claude.ai/code/session_x", "**Agent:** `java-expert`",
                     "### You · 2026-09-25 10:00", "> Did: Bash `javac Main.java`", "Line 8 dereferences null.", "`/go drill`",
                     "token=<REDACTED>", "wstoken=<REDACTED>", "key <REDACTED>", "Key <REDACTED>"]:
        assert expected in md, (expected, md)
    for absent in ["secret thoughts", "compiler output", "Base directory", "subagent chatter", "abc123", "ws999",
                   "0123456789abcdef0123456789abcdef", "abcdefghijklmnop"]:
        assert absent not in md, (absent, md)
    with tempfile.TemporaryDirectory() as d:
        out = pathlib.Path(d) / "chats" / "a.md"
        append_index(pathlib.Path(d) / "chats" / "INDEX.md", out, "T", "https://u", "2026-09-25")
        assert "[T](a.md) · [link](https://u)" in (pathlib.Path(d) / "chats" / "INDEX.md").read_text()
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Export a Claude Code session to Markdown.")
    ap.add_argument("--session", help="session id (default: the current or newest session for this folder)")
    ap.add_argument("--transcript", help="path to a .jsonl transcript")
    ap.add_argument("--out", help="write the Markdown here (default: stdout)")
    ap.add_argument("--title", help="title for the export")
    ap.add_argument("--url", help="link to the chat (claude.ai or Claude Code on the web)")
    ap.add_argument("--index", help="append an entry to this index file")
    ap.add_argument("--list", action="store_true", help="list recent sessions for this folder")
    ap.add_argument("--test", action="store_true", help="run the self-test")
    args = ap.parse_args()
    if args.test:
        return self_test()
    cwd = pathlib.Path.cwd()
    if args.list:
        return print(list_sessions(cwd))
    path = pathlib.Path(args.transcript) if args.transcript else (
        find_session(args.session) if args.session else default_transcript(cwd))
    if not path or not path.is_file():
        sys.exit("No transcript found. Use --list to see sessions, or --session ID.")
    rows = load(path)
    md = to_markdown(rows, args.title, args.url)
    if not args.out:
        return print(md)
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    if args.index:
        title = md.splitlines()[0].lstrip("# ").strip()
        append_index(args.index, out, title, args.url, dt.date.today().isoformat())
    print(f"Saved {out} ({len(md.splitlines())} lines) from {path.name}.")


if __name__ == "__main__":
    main()
