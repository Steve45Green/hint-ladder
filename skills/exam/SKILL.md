---
name: exam
description: Prepare for assessments - spaced review of learning records (drill), mock oral defence of a project (oral), and a mock exam graded on the course's scale (mock).
disable-model-invocation: true
argument-hint: "[drill | oral <project> | mock]"
---

# Exam

Three modes; no argument means `drill`. Reply and write in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear). Grades use the scale in the `Locale:` line of `CURRICULUM.md` (default 0–20, pass at 9.5). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md). You are the examiner here: questions come without hints or recommended answers.

The review script lives in this skill's directory: `python3 <this skill's directory>/scripts/review.py <workspace>`. Run it with `--help` for options.

## drill

Daily spaced retrieval over the records in `records/`. Fifteen minutes is enough.

1. Run `review.py <workspace>`: it lists the records due today with their Question.
2. Ask in rounds of up to five questions, **interleaved**: mix topics within a round rather than grouping by topic. Wait for the answers.
3. Mark each answer: **right** when the essential idea is correct in the student's own words; **wrong** otherwise. Give the correct answer and one line of why. Then run `review.py <workspace> --right NNNN` or `--wrong NNNN`.
4. Wrong on a record that was already in box 1 → the student lacks the concept, not the recall: suggest `/lesson` on that topic.
5. Nothing due → the script prints the next review date. Offer three fresh questions on the `seen` topics of highest weight in `SYLLABUS.md`; each correct answer becomes a new record.
6. A topic whose active records are all in box ≥ 3 becomes `mastered` in `SYLLABUS.md`.

Done when every due record was asked and moved by the script. Close with: `N/M right · next review: <date>`.

## oral <project>

A mock oral defence. The lecturer is checking that the student built the project and understands it.

1. Read the whole project first: assignment statement, code, report. You are the examining panel.
2. Map a question tree over the project:
   - **decisions**: "why this data structure and not another?"
   - **behaviour**: "what happens if the file does not exist? and with two clients at the same time?"
   - **location**: "show me the line where you free this memory"
   - **complexity**: "what does this function cost in the worst case?"
   - **change**: "how would you change this to support N users?"
   - **course concepts** behind the implementation.
3. Ask one to three questions at a time. A vague answer gets a follow-up ("show me in the code") before you move on. Descend each branch until it is answered or the student is stuck.
4. At the end give an indicative grade on the course's scale on three criteria: command of the code, justification of decisions, course concepts. List the weak points; each becomes a record whose Question is the one they missed, or a `/lesson` suggestion.

Done when every module and every major design decision of the project was questioned at least once.

## mock

A mock exam in the course's format.

1. Take the format from `MISSION.md` (duration, open or closed book, question types) and from `past-exams/`: imitate their style and the spread of weight over `SYLLABUS.md` topics. Say plainly that the questions are yours, written in the style of past exams.
2. Write `mocks/NNNN.md` with the questions and their marks summing to the scale's maximum (20 by default), and the grading criteria in `mocks/NNNN-criteria.md`. Tell the student to leave the criteria file closed.
3. The student answers in `mocks/NNNN-answers.md` or in chat, respecting the duration: record the start time.
4. Grade against the criteria, question by question, with the marks earned and one line of justification. Give the total on the course's scale and compare it to the minimum grade in `MISSION.md`.
5. Each missed question → `--wrong` on the matching record, or a new record when none exists.

Done when every question has a grade with justification and the total is compared to the minimum.
