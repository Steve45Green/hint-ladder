# Security

## Reporting a vulnerability

Please report security issues privately through [GitHub private vulnerability reporting](https://github.com/Steve45Green/hint-ladder/security/advisories/new), not in public issues. You will get a reply within 7 days.

## What counts

- A script in `scripts/` or `skills/*/scripts/` that can read, write or delete files outside what it is documented to touch.
- A skill or agent instruction that leads the agent to run destructive or privileged commands without the student's confirmation.
- Prompt injection: course material (`/analyze`), saved chats or workspace files that can make the agent follow instructions hidden inside them.
- Leaks: `/save-chat` exports that keep secrets its redaction should remove, or any path that sends student data off the machine.

## Design commitments

- Everything runs locally in the student's folders; the plugin has no telemetry and makes no network calls of its own, except to the student's own Moodle when they choose to connect it: the key is typed by the student in their terminal, stored in `~/.config/hint-ladder/moodle.json` with mode 0600, never printed, sent only over https, and redacted by `/save-chat`.
- Workspace files and course material are data, never instructions.
- Offensive security tools are used only on the student's own machines or on lab networks the lecturer authorised.
