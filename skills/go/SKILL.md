---
name: go
description: One entry point for everything - read the situation, pick the single best skill or language agent, and start it.
disable-model-invocation: true
argument-hint: "[what you want, or: setup | progress | plan | analyze | slides | save-chat | drill | lesson | critique | feedback | report | oral | mock | course | idea | bug | research | review]"
---

# Go

The student wants to remember one command: this one. Work out the situation, pick **one** skill or agent, and start it now. You route; you do not answer the request yourself, not even as an aside: on graded work a one-line "it should be `i < n`" is the solution. Reply in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear).

What you can route to:
- this pack's skills: `setup`, `progress`, `research`, `analyze`, `slides`, `save-chat`, `tutor`, `course`, `lesson`, `critique`, `exam`, `report`, `plan`, `moodle`;
- this pack's language agents: `assembly-expert`, `c-expert`, `cpp-expert`, `csharp-expert`, `haskell-expert`, `java-expert`, `kotlin-expert`, `linux-expert`, `math-expert`, `matlab-expert`, `php-expert`, `prolog-expert`, `python-expert`, `r-expert`, `sql-expert`, `uml-expert`, `vhdl-expert`, `web-expert`, the platform agents `windows-expert` and `macos-expert`, plus any agent `/setup` generated in the study root's `.claude/agents/`;
- optional complementary skills, when installed: `grilling`, `diagnosing-bugs`;
- Claude Code's built-in commands.

## Step 1: Keyword fast path

When the argument starts with one of these keywords, skip Step 2:

| Keyword | Start |
|---|---|
| `setup` | `setup` |
| `progress [all\|unit]` | `progress` |
| `analyze [file\|folder]` | `analyze` |
| `slides [topic\|file]` | `slides` |
| `save-chat [link]` | `save-chat` |
| `drill` | `exam`, drill mode |
| `lesson [topic]` | `lesson` |
| `critique [files]` | `critique` |
| `feedback [code\|process\|idea]` | the tutor's feedback of that kind (ask which kind if missing), given by the session's language agent when one runs |
| `oral [project]` | `exam`, oral mode |
| `mock` | `exam`, mock mode |
| `course [name]` | `course` |
| `idea` | idea feedback when it is coursework; `grilling` for anything else |
| `bug` | graded course code → `critique`; otherwise `diagnosing-bugs` |
| `research [topic]` | `research` |
| `report [assignment]` | `report` |
| `plan [semester\|exams]` | `plan` |
| `review` | graded course code → `critique`; otherwise `/code-review` |

## Step 2: Read the situation

Settle it from the environment, cheapest check first, and ask nothing you can look up:

1. **The argument as free text** comes first. "I have a bug in my linked list" is a bug; "is my project idea good" is idea feedback. Route it with the table in Step 3, whether or not a workspace exists: a missing workspace never blocks help (the tutor works without one), so mention `/setup` in one line at most.
2. **No argument, and no `CURRICULUM.md` in this directory or a parent, and no `MISSION.md`** → `setup`.
   The session's opening context holds a Hint Ladder Moodle notice → mention it first and start `moodle`, unless the student asked for something else.
3. **A course workspace** (`MISSION.md` here or in a parent):
   - run `python3 ../exam/scripts/review.py <workspace>` from this skill's directory; records due → `exam` drill;
   - an assessment in `MISSION.md` within 14 days → `exam` mock, or `exam` oral when it has an oral defence;
   - code in `assignments/` changed since the last `AI-USE.md` entry → `critique`;
   - `SYLLABUS.md` still empty → a course sheet in the folder not yet analysed → `analyze` it; otherwise `course`;
   - PDFs, slides or documents not listed in `material/INDEX.md` → `analyze`;
   - otherwise → `lesson` on the next topic.
4. **A study root** (`CURRICULUM.md`, no `MISSION.md` here) → no report in `reports/` for 7 days → `progress`; otherwise ask which unit, then tell the student to `cd <folder> && claude` so the unit's agent runs.
5. **A code repository outside the course** (`.git`, `package.json`, `pom.xml`, `*.csproj`, `Makefile`, `src/`):
   - uncommitted changes or a branch ahead of the default branch → `/code-review`;
   - an error or failing test in the argument → `diagnosing-bugs`;
   - otherwise ask the one question below.
6. **Still unclear** → ask exactly one question and wait:
   `What are you doing? 1) course: graded work 2) course: studying 3) feedback on code, process or an idea 4) something outside the course`

## Step 3: Routing table

| Situation | Start |
|---|---|
| No curriculum yet | `setup` |
| A new course unit (a new semester, an optional), or a unit with no expert yet | `setup`, with `add <unit>` |
| New or empty course workspace | `course` |
| The session opened with a Moodle notice (new files, announcements, moved deadlines), or "what's new on Moodle?" | `moodle` |
| "What have I done / where do I stand?" | `progress` |
| "What is due when?", the exam season, several deadlines in the same week, planning the weeks ahead | `plan` |
| A report or write-up to structure, or a draft to review | `report` |
| Weak topics, "I need more examples", a better explanation than the slides | `research` |
| Slides, PDFs, course sheet, past exams to read | `analyze` |
| Study a topic as slides, or prepare a presentation | `slides` |
| Keep this conversation | `save-chat` |
| Course, graded work | `tutor`; before submitting `critique`; before the defence `exam` oral |
| Course, studying | reviews due → `exam` drill; exam within 14 days → `exam` mock; else `lesson` |
| Feedback on code, process or an idea | the tutor's feedback of that kind, by the session's language agent |
| Installing, configuring or fixing the toolchain on the student's computer ("javac is not recognised", XAMPP won't start, Homebrew, PATH) | the platform agent from the `OS:` line of `CURRICULUM.md` (`windows-expert`, `macos-expert`, or `linux-expert`); no line → ask which system |
| A question about one language outside a workspace that runs its agent | delegate to that language's agent as a subagent (e.g. a Java stack trace → `java-expert`) |
| Planning a personal project or a decision | `grilling` |
| Facts from primary sources (official docs, standards, regulations) | `research` |
| Something broken outside graded work | `diagnosing-bugs` |
| Review outside graded work | `/code-review`; personal data or logins → also `/security-review` |
| Anything else | no skill: do the work directly |

Graded course work always routes to `tutor`, `critique` or the tutor's feedback, never to a skill that fixes or writes the code.

## Step 4: Start it

Say the choice in one line, `→ <skill or agent>: <reason in a few words>`, then start it:

- **This pack's skills**: read `../<name>/SKILL.md` from this skill's directory with the Read tool and follow it now, passing on the argument. This is how `/go` starts them: it is allowed and expected, even though those skills are user-invoked.
- **Language agents**: delegate with the Agent tool (`subagent_type` = the agent's name); for a whole study session, suggest `cd <unit folder> && claude`, or `claude --agent <name>`.
- **Complementary and built-in skills**: invoke them with the Skill tool.
- **Not installed**: do the work directly, and say in one line which skill would have handled it.

## Done when

Exactly one skill, agent or piece of direct work is running with a one-line reason, after at most one question to the student.
