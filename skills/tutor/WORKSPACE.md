# Workspace format

A workspace is one directory per course unit. `/setup` creates them under a **study root** that holds `CURRICULUM.md` (every unit of the degree, with its stack and agent, plus the `Language:`, `Locale:`, `DBMS:` and `OS:` lines), `.claude/agents/` for any generated language agents, and `reports/` for the progress reports `/progress` writes. Create files and directories lazily, when first needed.

```
<course>/
├── .claude/settings.json   {"agent": "<language agent>"}: sessions here run as that agent
├── COURSE-POLICY.md        optional, published by the lecturer: overrides every other policy
├── MISSION.md              why, assessment, dates, AI policy, pace
├── SYLLABUS.md             the official syllabus as a topic list with status
├── RESOURCES.md            official bibliography, trusted sources, communities
├── GLOSSARY.md             terms the student already masters
├── NOTES.md                the student's teaching preferences, your working notes
├── records/0001-*.md       learning records, one per review card
├── lessons/0001-*.html     lessons
├── slides/0001-*.html      study decks (/slides)
├── research/0001-*.md      study packs on weak topics (/research)
├── reference/*.html        one-page cheat sheets
├── assets/                 style.css, quiz.js and other shared lesson components
├── past-exams/             past exams the student drops here
├── material/               /analyze notes on slides, course sheet, past exams; INDEX.md lists them
│   └── moodle/             files downloaded from Moodle by /setup and /moodle (not versioned: they are the lecturers')
├── chats/                  saved conversations (/save-chat); INDEX.md lists them
├── mocks/0001*.md          mock exams
├── feedback/0001-<kind>-*.md  code, process and idea feedback, saved as given
└── assignments/<slug>/     graded work: statement, the student's code, AI-USE.md
```

The study root may also hold `.moodle.json`, written by `moodle.py` (not versioned, no secrets): the Moodle course linked to each unit folder, what was already seen and notified, and the last check. The student's Moodle key is never in the course; it lives in `~/.config/hint-ladder/moodle.json`.

Numbered files (`records/`, `lessons/`, `slides/`, `research/`, `mocks/`, `feedback/`): scan for the highest number and add one.

## MISSION.md

The compass. Every teaching decision traces back to it. Keep it to one screen.

```md
# Mission: <course unit> (<code>, year <n>, semester <n>, <ECTS> ECTS, <contact hours>)

Language: English

## Why
<1–3 sentences with the concrete outcome. "Pass Operating Systems with ≥14 in the regular exam season so it does not carry over into year 3" beats "understand OS".>

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment 1 (group, with oral defence) | 20% | 2026-11-03 | — |
| Test 1 | 30% | 2026-11-20 | 8.0 |
| Exam (regular season) | 50% | 2027-01-15 | 9.5 |

Resit exam: <date or "to confirm">. Pass mark: <from the Locale line; 9.5 out of 20 in Portugal>.

## AI policy
<What the regulations, the course sheet or the lecturer say, with the source. Otherwise: "unknown — confirm with the lecturer". While unknown, graded work follows the hint ladder.>

## Tools
<languages, versions, IDE, OS, compiler, DBMS, simulators the course uses; language agent: <name>>

## Constraints
<hours per week actually available, work shifts, other courses peaking at the same time>

## Pace
<N topics left in M weeks until <assessment> → ~K topics per week + 15 min daily of /exam drill>

## Success looks like
- <observable thing: "implement a round-robin scheduler in C without looking at notes">
```

## SYLLABUS.md

The official syllabus as a checklist. Every item of the official programme appears here; split an item into several rows when it is too big for one lesson.

```md
# Syllabus: <course unit>

| # | Topic | Depends on | Weight | Status |
|---|---|---|---|---|
| 1 | Processes and threads | — | high | mastered |
| 2 | Scheduling: FCFS, SJF, round-robin | 1 | high | seen |
| 3 | Synchronisation: mutexes, semaphores | 1 | high | todo |
```

Status moves `todo` → `seen` (a lesson was given or the student showed partial understanding) → `mastered` (every active record of the topic is in box ≥ 3, i.e. recalled correctly across spaced reviews). Weight is the topic's weight in assessment, `high | medium | low`, from past exams or what the lecturer said.

## RESOURCES.md

```md
# Resources: <course unit>

## Official course material
- Lecturer's slides, <location>. Use for: notation and what comes up in the exam.
- [Book: _Operating System Concepts_, Silberschatz et al., 10th ed.](https://...) — ch. 3–7. Use for: <when to reach for it>.

## Knowledge
- <trusted source + one line: what it covers and when to reach for it>

## Wisdom (communities)
- <course forum or Moodle, course Discord, the lecturer's office hours, study group>

## Gaps
- <syllabus topics with no good source>
```

Only list sources you have confirmed exist: never an invented book, edition, chapter or URL. Annotate every entry. Prune weak ones.

## GLOSSARY.md

```md
# Glossary: <course unit>

**Race condition**:
An outcome that depends on the execution order of threads that access shared data without synchronisation.
_Avoid_: conflict, collision
```

Add a term only once the student uses it correctly. One or two sentences: what it is, not how to use it. Pick one word per concept and list the rest under _Avoid_. Use glossary terms inside other definitions.

## records/NNNN-slug.md

Learning records, and at the same time the review cards for `/exam drill`.

```md
---
topic: 2
box: 1
next: 2026-09-26
status: active
---
# The round-robin quantum trades response time for context-switch overhead

<1–3 sentences: what is now known and why it changes what to teach next.>

## Question
<retrieval question that needs the concept, not a repeat of the sentence above>

## Answer
<short answer, used for grading>
```

- `topic`: row number in `SYLLABUS.md`. `box`: Leitner box 1–5. `next`: next review date. New records start at box 1, next = tomorrow.
- `status`: `active`, or `superseded by NNNN` when a later record corrects this one. Never delete a record; the history of how understanding changed is signal.

Write a record when:
1. The student **showed** non-trivial understanding (answered, solved, explained). Coverage is not learning; wait for evidence.
2. The student **declared prior knowledge**. Start it at box 2 so it gets checked soon.
3. A **misconception was corrected**. Highest value: it predicts future stumbles. Put the misconception in the Question.
4. The **mission changed**. Update `MISSION.md` too, after confirming with the student.

Not a record: material merely covered, a session log, a term already in `GLOSSARY.md`.

## NOTES.md

Free-form: how the student likes to be taught ("prefers examples in C", "studies on the train, short lessons"), and your working notes.

## assignments/<slug>/AI-USE.md

```md
# AI use: <assignment>

2026-10-12 · rung 2 · Identified the problem as breadth-first search; pointed to CLRS ch. 22.
2026-10-14 · rung 5 · Critique of queue.c: 3 problems pointed out, no code provided.
```
