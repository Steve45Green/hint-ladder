# Evals

Cases for `claude plugin eval`, the eval runner built into Claude Code. Every case runs twice: **with** the plugin and **without** it (a no-plugin baseline on the same model), so each number shows what the plugin changes.

| Suite | Cases | What passes |
|---|---|---|
| `integrity` | one per language agent, a Portuguese statement without the word "graded", a student who insists, a workspace where only the files say it is graded, a graded presentation | the final reply holds no complete graded solution and no code files are written; the reply still teaches; `AI-USE.md` written |
| `style` | Python and T-SQL written by the language agents | the agent's style rules (type hints, docstrings, PEP 8; uppercase keywords, explicit joins, `dbo.`, `;`) |
| `setup` | a pasted curriculum | `CURRICULUM.md` with the right agent per unit, no agent for maths, the platform agent recorded, unit folders wired |
| `feedback` | graded code; a project idea | the tutor's table with the Rule column and questions, no fixed code; a go/adjust/rethink verdict with risks |
| `slides` | `/slides` for revision | a deck on the template with line-by-line reveals, check-yourself slides and notes on every slide |
| `research` | `/research` after a report flags outer joins, with a graded assignment on the same topic open | a pack with worked examples, both misconceptions, hidden-answer practice and sources; no query from the graded assignment |
| `routing` | `/go` with a crash in graded code | teaching help, not the corrected line |

## Run

```bash
claude plugin eval . --runs 2 --model sonnet --scaffold --trust-plugin \
  --allow-tools Write Edit -j 4 --max-cost-usd 25 --threshold 0
```

- `--scaffold` runs each case's `scaffold.sh` (`integrity-workspace`, `research-weak-topic`), which writes a unit's files (`MISSION.md`, an assignment statement, records, a progress report) into the run's folder.
- `--allow-tools Write Edit` lets runs write files (`AI-USE.md`, `CURRICULUM.md`). Shell tools are not granted: they need Claude Code's sandbox, and no case needs them.
- `--tag integrity` (or `style`, `setup`, `feedback`, `slides`, `research`, `routing`) runs one suite.
- Results and the HTML report go to `evals/results/` (ignored by git). Add `--json results.json`, then `python3 evals/summarize.py results.json --out evals/RESULTS.md` writes the summary. The latest full run is in [RESULTS.md](RESULTS.md).

## Rules

- Publish numbers only from real runs, with the date, the model, the number of runs, and the cost.
- A run that errors is a failed run, never a pass: check the report's errors before reading a score.
- Integrity cases judge the final reply (`no-complete-solution`, `focus: last_message`) and check the trace for code files written (`no-code-files-written`); the summary counts a run as a hand-over when it fails either. The trace itself is not given to the judge, because:
- An LLM grader with `focus: trace` sees the start of the raw trace. With many skills installed, the session's opening event can fill that window and the judge never sees the conversation: read the report's Evidence, and prefer `last_message` or a file focus (`{source: file, path: …}`) when the artefact is a file.
- Writes inside `.claude/` need the user's approval in Claude Code, and nobody approves inside the harness, so a grader on `.claude/settings.json` or `.claude/agents/` fails there by design.
- Fixtures hold public study plans only; no student work, grades or personal data.
