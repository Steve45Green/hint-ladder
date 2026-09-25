---
name: course
description: Set up the study workspace for one course unit - mission, assessment dates, AI policy, syllabus map, sources and study pace.
disable-model-invocation: true
argument-hint: "[course unit name]"
---

# Course

Set up (or deepen) the workspace for one course unit in the current directory. File formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md): read it first. Reply and write in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear).

The grading scale, pass mark and exam seasons come from the `Locale:` line in `CURRICULUM.md`. With none recorded, assume the Portuguese system: tests, lab assignments, projects with an oral defence, exams in the regular, resit and special seasons, graded 0–20 with a pass at 9.5.

## Step 1: Gather facts

Finding facts is your job, never the student's. Before asking anything, search the current directory for:

- the course sheet / syllabus / regulations (`*.pdf`, `*.md`, `*.txt`, `*.docx`);
- slides, lecture notes, assignment statements, `past-exams/`;
- an existing `MISSION.md` (then this is an update: read the whole workspace and change only what is new);
- this unit's row in `CURRICULUM.md` in a parent directory (written by `/setup`): code, year, semester, ECTS, contact hours, stack, agent, DBMS;
- a `COURSE-POLICY.md` from the lecturer (it settles the AI policy).

Read what you find. If the student gives a URL for the course page, fetch it. Everything these answer is settled and never becomes a question.

## Step 2: Interview in rounds

Map what is still unknown as a tree of decisions. Each round, ask every question whose prerequisites are settled, each with your recommended answer, as the tutor skill's "Asking the student" says ([../tutor/SKILL.md](../tutor/SKILL.md)): choices through the AskUserQuestion tool, four per call; open questions (why, biggest worry) in plain text. Then wait.

Cover, until each is settled or explicitly marked "to confirm":
- **Why**: push past "pass the course" to the concrete outcome (target grade, exam season, what the course unlocks: internship, courses that depend on it).
- **Assessment**: every component, weight, date, minimum grade, group or individual, oral defence or not.
- **AI policy**: what the regulations or the lecturer say. Unknown → "unknown — confirm with the lecturer".
- **Tools**: languages, versions, IDE, compiler, DBMS (confirm what `CURRICULUM.md` recorded).
- **Constraints**: hours per week actually available, shift pattern, peaks from other courses.
- **Prior knowledge**: what they already know, and how deeply (becomes records at box 2).
- **Biggest worry**: the topic they fear most (weights the syllabus).

The interview is done when every branch above is settled or marked "to confirm".

## Step 3: Write the workspace

1. `MISSION.md` with every section, including **Pace**: count the topics not yet `mastered`, divide by the weeks to each assessment, and check it against the hours available. When it does not fit, say so plainly and propose what to cut (lowest weight first).
2. `SYLLABUS.md` covering **every** item of the official programme, ordered by dependency, with weights from past exams or the lecturer.
3. `RESOURCES.md`: official course material first, then at most five canonical sources you have confirmed exist, then communities (course forum or Moodle, the lecturer's office hours, course Discord).
4. `GLOSSARY.md` (header only), `NOTES.md` (preferences heard in the interview).
5. `records/` for declared prior knowledge (box 2, next = tomorrow).
6. When the unit has a language agent and `.claude/settings.json` does not name it yet, write `{"agent": "<agent>"}` there (merge with existing keys; ask before replacing a different agent), and update the Stack and Agent cells of the unit's row in `CURRICULUM.md` if the interview changed them.

## Done when

- `MISSION.md` has every assessment date and the AI policy, or each is marked "to confirm".
- `SYLLABUS.md` has a row for every programme item.
- `RESOURCES.md` has the official bibliography.

Then show the student a five-line summary (next assessment, pace, three highest-weight topics) and the first recommended lesson as `/lesson <topic>`.
