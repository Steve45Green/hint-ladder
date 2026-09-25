#!/usr/bin/env python3
"""Spaced review (Leitner system) over a workspace's learning records.

Each records/NNNN-slug.md carries frontmatter
    box: 1..5        Leitner box
    next: date       next review (ISO)
    status: active   anything else (e.g. "superseded by 0007") is skipped
and a "## Question" section. Standard library only.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys
import tempfile

INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}  # days until next review, per box
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
QUESTION = re.compile(r"^## Question[ \t]*\n(.*?)(?=^## |\Z)", re.S | re.M)


def read(path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    meta = {}
    for line in (m.group(1).splitlines() if m else []):
        key, sep, value = line.partition(":")
        if sep:
            meta[key.strip()] = value.strip()
    return text, meta


def question(text):
    m = QUESTION.search(text)
    return " ".join(m.group(1).split()) if m else "(no ## Question section)"


def records(workspace):
    return sorted((workspace / "records").glob("[0-9][0-9][0-9][0-9]-*.md"))


def active(workspace, today):
    """Yield (path, text, box, next_date) for every active record."""
    for p in records(workspace):
        text, meta = read(p)
        if meta.get("status", "active") != "active":
            continue
        try:
            box = int(meta.get("box", 1))
            next_date = dt.date.fromisoformat(meta.get("next", today.isoformat()))
        except ValueError as e:
            sys.exit(f"{p}: invalid frontmatter ({e})")
        yield p, text, box, next_date


def due(workspace, today):
    everything = list(active(workspace, today))
    pending = [r for r in everything if r[3] <= today]
    if not pending:
        if not everything:
            return f"No active records in {workspace / 'records'}."
        p, _, _, next_date = min(everything, key=lambda r: r[3])
        return f"Nothing due today. Next review: {next_date} ({p.name[:4]})."
    lines = [f"{len(pending)} due today ({today}):"]
    for p, text, box, _ in pending:
        lines.append(f"{p.name[:4]} [box {box}] {question(text)}")
    return "\n".join(lines)


def move(workspace, number, right, today):
    target = [p for p in records(workspace) if p.name.startswith(number.zfill(4) + "-")]
    if not target:
        sys.exit(f"Record {number} not found in {workspace / 'records'}.")
    p = target[0]
    text, meta = read(p)
    box = min(int(meta.get("box", 1)) + 1, 5) if right else 1
    next_date = today + dt.timedelta(days=INTERVALS[box])
    m = FRONTMATTER.match(text)
    updates = {"box": str(box), "next": next_date.isoformat()}
    lines = []
    for line in (m.group(1).splitlines() if m else []):
        key = line.partition(":")[0].strip()
        lines.append(f"{key}: {updates.pop(key)}" if key in updates else line)
    lines += [f"{k}: {v}" for k, v in updates.items()]
    body = text[m.end():] if m else text
    p.write_text("---\n" + "\n".join(lines) + "\n---\n" + body, encoding="utf-8")
    return f"{p.name[:4]} → box {box}, next review {next_date}."


def self_test():
    today = dt.date(2026, 9, 25)
    with tempfile.TemporaryDirectory() as d:
        workspace = pathlib.Path(d)
        (workspace / "records").mkdir()

        def write(name, meta, q):
            (workspace / "records" / name).write_text(
                f"---\n{meta}\n---\n# Title\n\nText.\n\n## Question\n{q}\n\n## Answer\nX\n",
                encoding="utf-8")

        write("0001-due.md", "topic: 1\nbox: 1\nnext: 2026-09-25\nstatus: active", "Question one?")
        write("0002-later.md", "topic: 1\nbox: 2\nnext: 2026-09-30\nstatus: active", "Question two?")
        write("0003-old.md", "topic: 1\nbox: 1\nnext: 2026-09-01\nstatus: superseded by 0001", "Old?")

        out = due(workspace, today)
        assert "0001 [box 1] Question one?" in out, out
        assert "0002" not in out and "0003" not in out, out

        move(workspace, "1", True, today)
        _, meta = read(workspace / "records" / "0001-due.md")
        assert meta["box"] == "2" and meta["next"] == "2026-09-28", meta
        assert meta["topic"] == "1" and meta["status"] == "active", meta
        assert list(meta) == ["topic", "box", "next", "status"], meta  # key order kept

        move(workspace, "0002", False, today)
        _, meta = read(workspace / "records" / "0002-later.md")
        assert meta["box"] == "1" and meta["next"] == "2026-09-26", meta

        for _ in range(6):
            move(workspace, "1", True, today)
        _, meta = read(workspace / "records" / "0001-due.md")
        assert meta["box"] == "5", meta

        assert due(workspace, today).startswith("Nothing due today. Next review: 2026-09-26 (0002)")
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description="Spaced review (Leitner) of a workspace's learning records.")
    ap.add_argument("workspace", nargs="?", default=".", help="workspace directory (default: current)")
    action = ap.add_mutually_exclusive_group()
    action.add_argument("--right", metavar="NNNN", help="right answer: move up one box")
    action.add_argument("--wrong", metavar="NNNN", help="wrong answer: back to box 1")
    action.add_argument("--test", action="store_true", help="run the self-test")
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today(), help="reference date (YYYY-MM-DD)")
    args = ap.parse_args()

    if args.test:
        return self_test()
    workspace = pathlib.Path(args.workspace)
    if args.right or args.wrong:
        print(move(workspace, args.right or args.wrong, bool(args.right), args.today))
    else:
        print(due(workspace, args.today))


if __name__ == "__main__":
    main()
