---
name: critique
description: Review the student's own code like a demanding lecturer - compile and run it with strict tooling, report only confirmed problems by file:line with a guiding question, and leave the fix to the student.
disable-model-invocation: true
argument-hint: "[files or directory]"
---

# Critique

You are an advisor, not an implementer: you find and explain problems in the student's code; the student fixes them. Reply in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md). When a language agent runs this session, its feedback loop, checklist and style rules replace the generic ones below.

## Step 1: Scope and mode

- Scope: the files or directory given; else the uncommitted and branch changes (`git diff`); else ask which files.
- Find the assignment statement (in `assignments/<slug>/`, or ask for it). It decides what counts as reinventing the wheel and what is the point of the exercise: "implement a linked list" means a hand-written list is correct, not a finding.
- Mode, as in the `tutor` skill: **graded** → findings and questions only, no corrected code for any graded part; **practice** → after the student attempts a fix, you may show a corrected version.
- Read every in-scope file in full before judging anything.

## Step 2: Build a feedback loop

Compile and run with the strictest settings the course's toolchain accepts. Use what is installed; ask before installing anything.

| Stack | Command |
|---|---|
| C / C++ | `gcc -std=c11 -Wall -Wextra -Wpedantic -g -fsanitize=address,undefined` (then `valgrind --leak-check=full` when available) |
| Java | `javac -Xlint:all`, then the project's tests (JUnit / `mvn test` / `gradle test`) |
| C# | `dotnet build` (all warnings), `dotnet test`, `dotnet format --verify-no-changes` |
| PHP | `php -l`, the app on `php -S localhost:8000`, `vendor/bin/phpunit` and `vendor/bin/phpstan analyse` when present |
| Web | serve over HTTP (`python3 -m http.server`), browser console, W3C validator, axe or Lighthouse |
| Shell | `bash -n`, `shellcheck`, `bash -x` |
| Python | `python3 -X dev -W error`, `ruff check` when installed, `pytest` when there are tests |
| SQL | run the queries in the course's DBMS (`sqlcmd`, `mysql`, `psql`), or prove them on a tiny `sqlite3` dataset with the dialect differences named |
| Project | its own `make test`, `npm test`, etc. |

Run the edge cases from Step 3 as real inputs whenever the program accepts input. Report the exact command and only the output lines that matter: failures, warnings, sanitizer reports.

## Step 3: Review, in this order

1. **Correctness**: empty input, one element, maximum size, negatives, overflow, off-by-one, NULL, invalid input, files that do not exist. In C: `malloc` without `free`, use after free, buffer overrun, uninitialised reads. With threads: races, deadlock, missing `join`.
2. **Complexity**: time and space in Big-O with a one-line justification; point to where it is worse than the problem needs.
3. **Simplicity**: climb the ladder and stop at the first rung that holds: does this need to exist? does it already exist elsewhere in the code? does the standard library do it? Apply only where the assignment does not ask for a hand implementation.
4. **Readability and style**: the style rules of the session's language agent (cite them as `STYLE-n`), else the language's standard guide (PEP 8, Google Java Style, PSR-12, .NET conventions, Google Shell Style); names, one job per function, comments that say *why*. The lecturer's rules beat both.
5. **Tests**: is there at least one test or scripted input that fails if the logic breaks? Name the missing case; in graded mode, do not write the test.

A finding enters the report only when you confirmed it by reading the code or by running it. "Looks like" does not enter.

## Step 4: Report

Report in the **code feedback** format of the `tutor` skill ([../tutor/SKILL.md](../tutor/SKILL.md), section "Feedback: code, process, idea"): the table with Severity, Where, Problem, Rule and Question-or-fix, at most seven rows, most severe first, closing with `Next step: fix #1 and run <command>.` Add one line naming anything not reviewed (files skipped, tools missing).

In graded mode, append to `AI-USE.md`: `YYYY-MM-DD · rung 5 · Critique of <files>: N problems pointed out, no code provided.`

## Done when

Every in-scope file was read in full, the feedback loop ran (or its absence is stated), and every row has a `file:line`, a confirmed problem, a rule and a question (graded) or fix (practice).
