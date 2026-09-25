# Troubleshooting

*[Português](troubleshooting.pt-PT.md) · [All tutorials](README.md)*

## `claude`: command not found

- Close the terminal and open a new one: the installer adds `claude` to the path, and old windows don't see it.
- Still missing: run `claude doctor` if it exists, or follow [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install).
- On Windows, if PowerShell says `irm` is not recognised, you are in CMD, not PowerShell: open **Windows PowerShell** and paste the install line again.

## "Claude Code is not included in your plan"

The free Claude plan doesn't include Claude Code. You need Pro or higher, or an Anthropic Console account with API credits.

## `/plugin marketplace add` fails: repository not found

- Check the spelling: `Steve45Green/hint-ladder`.
- The repository must be public to install from it. If you are its owner and it is still private or has another name, follow [docs/launch.md](../launch.md) steps 1 to 3.

## The commands don't appear

- Type `/exit` and start `claude` again: plugins load when a session starts.
- Type `/plugin` and check that `hint-ladder` is installed and enabled. From the terminal: `claude plugin list`.
- Try the long name: `/hint-ladder:go`. If that works and `/go` doesn't, another installed plugin or skill uses the same name; the long name always works.

## The session doesn't open as the unit's expert

- Open Claude Code **inside** the unit's folder (`cd <course>/<unit>` first).
- The folder must have `.claude/settings.json` with `{"agent": "<expert>"}` (for example `{"agent": "sql-expert"}`). Missing? Create it with that line, or ask `/setup` in the course folder to wire that unit again; it never deletes your work.
- Start it by hand: `claude --agent sql-expert` (or `java-expert`, `c-expert`…).

## "It won't give me the answer"

That is intended on graded work: see [Tutorial 4](4-graded-work.md). If the exercise is **not** graded (practice, a past exam, a book exercise), say so ("this is practice, not graded"): it then explains freely and shows the full solution after your attempt.

## The replies are in the wrong language

The language is the `Language:` line in `CURRICULUM.md` (all units) or in the unit's `MISSION.md`. Change it there (or ask Claude to change it).

## A slide deck or lesson doesn't open

Double-click the `.html` file in the unit's `slides/` or `lessons/` folder: it opens in your browser and works offline. From GitHub, download the file first (the ⬇ "Download raw file" button); GitHub shows the code of HTML files instead of running them.

## The conversation got slow or confused

`/compact` summarises it and continues. To start clean, `/clear`; your files stay.

## How much does it cost?

Hint Ladder is free and open source. Claude Code uses your Claude plan's usage (or your API credits, if you log in with a Console account); long sessions and background reports use more.

## Still stuck

Open an issue with what you typed and what you saw (remove anything private): [issues](https://github.com/Steve45Green/hint-ladder/issues).
