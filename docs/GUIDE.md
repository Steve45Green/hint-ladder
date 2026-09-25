# Guide: how to use Hint Ladder

*[Português](GUIA.pt-PT.md)*

This guide is the reference: which command for which situation. First time? The [tutorials](tutorials/README.md) go step by step, from installing to a weekly routine.

## Start here

Two commands:

```
/setup    once: paste your course units, get one folder per unit wired to the right expert
/go       every day: reads where you are and starts the right skill or expert
```

And also:
- `/analyze`: whenever you get slides, PDFs, the course sheet or past exams, turn them into notes with page references and self-test questions;
- `/slides`: review a topic as a deck that reveals one step at a time, with check-yourself slides; for a graded presentation it gives a skeleton, feedback and a rehearsal, never the content;
- `/save-chat`: keep an important conversation, with its link, in the unit's folder;
- `/progress`, once a week: reviews what you did (and what the experts told you) across all units and says what to do next;
- `/research`, right after `/progress`: for each weak topic, other explanations, more worked examples and checked sources.

Your first week:

| Day | Do |
|---|---|
| 1 | `/setup`: choose where the course lives (a folder on your computer, or a private GitHub repository) and paste your course units |
| 2 | Open one unit (`cd <unit> && claude`), drop the course sheet there, run `/analyze`, then `/course` |
| 3 | `/lesson` |
| 4 onwards | `/go` every day, 15 minutes: it sends you to your reviews when some are due |
| When an assignment arrives | `/go feedback idea` before you start; paste the statement; `/critique` before you submit; `/exam oral` before the defence |

Terminal shortcuts (`~/.bashrc` or `~/.zshrc`):

```bash
alias cgo='claude "/go"'
alias cdrill='claude "/go drill"'
```

In PowerShell (`$PROFILE`): `function cgo { claude "/go" }`.

---

## By kind of course

| Kind | Examples | What matters most |
|---|---|---|
| **Programming** | Intro to Programming, OOP, Data Structures, Software Engineering, Web, Mobile | The language expert (opens by itself in the folder), `/critique`, code feedback, `/exam oral` |
| **Databases** | Databases 1 and 2, Information Systems | `sql-expert` in your school's dialect; predict-the-result-set drills; idea feedback on the ER model |
| **Systems and networks** | Operating Systems, Networks, Security, System Administration | `linux-expert` (and `c-expert` in OS); labs in a VM; `/lesson` for subnetting and processes |
| **Maths and physics** | Calculus, Linear Algebra, Discrete Maths, Statistics, Physics | No expert: `/lesson` + `/exam drill` daily + `/exam mock`. Statistics and numerical methods in Python → `python-expert` |
| **Interfaces** | Human-Computer Interaction | `web-expert`: usability heuristics, accessibility, prototypes |
| **Projects and internships** | Capstone, internship, final project | Idea feedback before starting, process feedback every week, `/exam oral` before the defence |
| **Non-technical** | Communication, Entrepreneurship, IT Law and Regulation | `/lesson` + `/exam`; `/research` for regulations and official sources |

---

## The experts

Eight curated language experts: `java-expert`, `c-expert`, `csharp-expert`, `python-expert`, `sql-expert`, `php-expert`, `web-expert`, `linux-expert`. Two platform experts, `windows-expert` and `macos-expert`: `/setup` picks the one for your computer, and it installs and fixes your tools ("javac is not recognized", XAMPP won't start, PATH, Homebrew). For any other language, `/setup` generates an expert from a fixed template, stored in `.claude/agents/` in your course folder.

Each expert has:
- **Numbered style rules** it follows in all code it writes and cites in feedback (`STYLE-3`). Your lecturer's rules come first and are recorded in `NOTES.md`.
- **The language's commands** (compiler with all warnings, tests, linter). It runs them before claiming anything.
- **The tutor's rules**: on graded work it gives hints and feedback, never the solution.

Three ways to use them:
1. **Automatic**: in a folder created by `/setup`, `claude` starts as the unit's expert (`.claude/settings.json`).
2. **By hand**: `claude --agent java-expert` anywhere. With aliases: `alias cjava='claude --agent java-expert'`.
3. **Delegation**: in a normal session, a one-off question ("explain this Java stack trace") goes to the right expert, or run `/go` with the question.

---

## Feedback: code, process and idea

| You ask | You get |
|---|---|
| `/go feedback code` or `/critique` | A table: severity, `file:line`, problem, rule, a question (graded work) or the fix (practice) |
| `/go feedback process` | Three things to keep and three to change, each with its evidence (commits, tests, deadline), and the next step |
| `/go feedback idea` | A `go`, `adjust` or `rethink` verdict, strengths, risks, up to three questions, alternatives to know about |

---

## Recipes

| Situation | Type |
|---|---|
| I opened Claude Code and don't know what to do | `/go` |
| Start of the semester | `/setup` (or `/setup` again to update your active units) |
| Lab assignment to submit | `/go feedback idea` → paste the statement → you write → `/critique` → `/exam oral` |
| Test on Friday | `/lesson <topic>` → `/go drill` every day → `/exam mock` the day before |
| My graded code crashes | paste the error: the expert guides you without fixing it for you |
| Am I working the wrong way? | `/go feedback process` |
| I want to review a topic as slides | `/slides <topic>` (or `/slides lessons/0001-….html`) |
| I have to give a graded presentation | `/slides talk 10` with the brief: skeleton, then feedback on your deck, then rehearsal |
| I got slides or a PDF from class | `/analyze <file>` (or `/analyze` for everything you haven't read) |
| I have past exams | put them in `past-exams/` and run `/analyze past-exams/`: you get the topics that come up most |
| I want to keep this conversation | `/save-chat <chat link>` |
| Java, XAMPP or SQL Server won't work on my computer | `/go` + the error: it goes to your system's expert |
| Where do I stand in each unit? | `/progress` in the course folder (runs in the background with several units) |
| A new unit this semester, or one in a language with no expert | `/setup add <unit>`: it interviews you (kind of expert, language and version, tools, style, assessment) and builds the expert |
| A lecturer posted slides, an announcement or a new deadline on Moodle | `/moodle`: downloads and summarises what changed, updates the dates in `MISSION.md` after asking, and suggests one next step; `/moodle watch` adds an hourly check with a desktop notification, and every session opened in the course starts with the news |
| Your school uses Moodle | `/setup moodle`: you sign in once with your own Moodle key, in your terminal; it downloads each unit's files into `material/moodle/` (kept out of git) and takes the assignment statements and due dates |
| I don't get a topic from the slides; I need more examples | `/research <topic>`, or `/research` alone for the weak topics in the last report |
| A weekly report without opening Claude | schedule `claude -p "/progress"` with cron or Task Scheduler (ask `/progress` how to automate it) |
| My lecturer published AI rules | save them as `COURSE-POLICY.md` in the unit's folder |
| Long session, answers getting worse | `/compact` |

---

## Add-ons and conflicts

Optional add-ons `/go` uses when they are installed:
- `grilling` and `diagnosing-bugs` from [mattpocock/skills](https://github.com/mattpocock/skills). If you also installed its `research`, type `/hint-ladder:research` for this pack's;
- [rtk](https://github.com/rtk-ai/rtk) (`rtk init -g`): compresses command output and saves tokens.

Watch out for:
- **Always-on plugins** that enforce "code first, little explanation", such as [ponytail](https://github.com/dietrichgebert/ponytail): they clash with the tutor's hints and explanations. Turn them off in your course folders.
- **Skills that write code on their own** for any logic request (for example addyosmani's `test-driven-development`): on graded work they compete with the tutor.
- **Too many auto-invoked skills.** Claude Code reserves 1% of the context window for the skill list (about 8,000 characters at 200k tokens). Above that it shortens descriptions, and skills trigger less reliably. Hint Ladder has a single auto-invoked skill (`tutor`); check your total with `/context`.
- **Duplicate names**: mattpocock's `code-review` has the same name as Claude Code's built-in `/code-review`.
