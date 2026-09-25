---
name: progress
description: Review everything done so far across the course workspaces - learning, reviews due, deadlines, feedback given and acted on, AI use - and write a progress report with the next actions. Can run in the background.
disable-model-invocation: true
argument-hint: "[all | <unit folder>] [since YYYY-MM-DD]"
---

# Progress

Look back over the work done in the student's workspaces, by the student and by the tutor and language agents, and write one report that says where each unit stands and what to do next. Read-only: the only file you write is the report. Reply and write in the language recorded as `Language:` in `CURRICULUM.md` or `MISSION.md`; when none is recorded, the language the student writes in (English if unclear). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md).

## Step 1: Scope

- **Units**: at a study root (`CURRICULUM.md`), every `active` unit; inside a workspace, that unit; an argument naming a folder or `all` overrides.
- **Period**: since the date of the latest file in `reports/`, else the last 7 days; `since YYYY-MM-DD` overrides.

## Step 2: Gather, in the background when possible

With more than two units, dispatch one subagent per unit, in parallel and in the background when the host allows it, so the student can keep working; tell them in one line that the report is running. Each subagent gets this checklist, the unit folder, the period, and the instruction to return numbers and evidence only, without changing any file:

- `MISSION.md`: the next assessments with dates and days left; the Pace line.
- `SYLLABUS.md`: topics `todo`, `seen`, `mastered`; high-weight topics not yet mastered.
- `records/`: output of `python3 <review script> <unit folder>` (due today, next review), where the review script is `../exam/scripts/review.py` resolved from this skill's directory (give subagents its absolute path); records per box; records created in the period; misconception records.
- `lessons/`, `mocks/`: files created in the period; mock grades.
- `feedback/`: feedback given in the period by kind. For each code feedback, whether the files it cites changed afterwards (`git log --since=<feedback date> -- <files>`, or file dates) and whether the blocker rows look fixed on reading the code now.
- `assignments/*/AI-USE.md`: entries in the period and the highest rung per assignment.
- Git history in the workspace or its assignments: commits in the period, their size, the date of the last commit.
- `NOTES.md`: lecturer rules added in the period.

With one or two units, gather directly yourself.

## Step 3: Assess each unit

| Status | When |
|---|---|
| **on track** | none of the conditions below |
| **at risk** | an assessment within 14 days with high-weight topics not mastered; reviews overdue by more than 3 days; code feedback with blockers not acted on; no activity in the period with an assessment within 30 days |
| **behind** | fewer topics mastered than the Pace line requires by now, or an assessment within 7 days with most topics still `todo` |

## Step 4: Write the report

Write `reports/YYYY-MM-DD.md` at the study root (or in the workspace when run inside one):

```md
# Progress: <period>

<three-line summary>

| Unit | Status | Next assessment | Syllabus (mastered/seen/todo) | Reviews due | Activity in the period |
|---|---|---|---|---|---|

## Wins
- <evidence-backed: "8 records moved to box 3 in Databases 2">

## Risks
- <unit: risk, with the evidence>

## Feedback follow-up
- <feedback file: acted on / not yet, with the evidence>

## AI use this period
- <assignment: N entries, highest rung R>, ready to copy into an AI-use declaration

## Next actions
1. <a command to type, e.g. `cd bases-de-dados-2 && claude`, then `/exam drill`, or `/research <weak topic>`>
2. …
3. …
```

Then reply with the summary, the unit table and the path to the report, and offer `/research` on the topics under Risks: it brings other explanations, more worked examples and checked sources for exactly those. When the study root is a git repository with uncommitted work, offer to commit it (`git add -A && git commit -m "Week of <date>"`) and to push when it has a remote; do it only on a yes.

## Scheduling

To have the report written without opening a session, the student can schedule a headless run at the study root. Weekly with cron, for example:

```
0 20 * * 0  cd ~/course && claude -p "/progress" --allowedTools "Read" "Glob" "Grep" "Write" "Agent" "Bash(python3:*)" "Bash(git log:*)"
```

Or, inside a long session, `/loop 7d /progress`. Show these only when the student asks how to automate the report.

## Done when

The report exists with a row for every unit in scope, every number traces to a file or command, every risk names its evidence, and the next actions are commands the student can type.
