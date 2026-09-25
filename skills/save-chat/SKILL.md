---
name: save-chat
description: Save a whole conversation with Claude as a Markdown file in the course folder, with its link, a resume command and a short summary, and list it in chats/INDEX.md.
disable-model-invocation: true
argument-hint: "[list | <session id> | <chat link>] [title]"
---

# Save chat

Save a conversation the student wants to keep, with everything needed to find it again: the full text, the link to the chat, the command to resume it, and a short summary. Reply in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear).

The exporter lives in this skill's directory: `python3 <this skill's directory>/scripts/export_chat.py`. It reads Claude Code's own transcript, keeps the student's messages, the commands they typed, Claude's replies and one line per tool call, leaves out thinking, tool output and subagent internals, and redacts common secrets (API keys, tokens, passwords).

## Step 1: Which conversation

- No argument → the current session.
- `list` → run the exporter with `--list`, show the recent sessions for this folder, and ask which one.
- A session id → that session.
- Conversation text pasted from the Claude app or claude.ai (not a Claude Code session) → save the pasted text as the body, under the same header; the exporter is not needed.

## Step 2: The link

A Claude Code session always gets its resume command (`claude --resume <id>`). A web link can't be read from the transcript: if the argument has one (claude.ai/code/…, claude.ai/chat/…), use it; otherwise ask once, "Paste the chat's link if you want it saved (or skip)". The link is in the browser's address bar, or in the share menu of the Claude app.

## Step 3: Where

- Inside a course workspace (`MISSION.md` here or in a parent) → that workspace's `chats/`.
- At a study root (`CURRICULUM.md`) → `chats/` there.
- Anywhere else → `chats/` in the current directory.

File name: `chats/YYYY-MM-DD-<slug>.md`, the slug from the title (the argument's title, else the topic of the conversation in a few words).

## Step 4: Export

```
python3 <this skill's directory>/scripts/export_chat.py [--session <id>] --title "<title>" --out chats/YYYY-MM-DD-<slug>.md [--url <link>] --index chats/INDEX.md
```

Then read the file and insert, right after the header block, a `## Summary` with up to five bullets: what was asked, what was learned or decided, files created or changed, open follow-ups. Graded work: note the hint rungs reached, matching `AI-USE.md`.

## Step 5: Report

One line with the path and the link (or "no link given"). Remind the student, once, that chats stay on their machine, and that secrets were redacted but personal data may remain: check before sharing or committing the file to a public repository.

## Done when

The file exists with its header (title, dates, session, resume command, link or "none given", folder, agent), the summary, and the conversation; `chats/INDEX.md` lists it.
