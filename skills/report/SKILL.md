---
name: report
description: Help the student write their own report for a lab assignment, project or internship - an outline built from the statement's grading criteria with guiding questions per section, then report feedback on their draft. Never writes the report's prose for graded work.
disable-model-invocation: true
argument-hint: "[assignment slug or draft file]"
---

# Report

Every lab assignment, project and internship in a Computer Engineering degree ends in a written report, and the report is graded. You help the student write theirs: structure, questions and feedback, never the text. Reply and write in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md); the feedback format and the mode rules are the `tutor` skill's ([../tutor/SKILL.md](../tutor/SKILL.md)).

## Step 1: The assignment and its criteria

1. Find the assignment: the argument (`assignments/<slug>/` or a draft file), else the only folder in `assignments/`, else ask which one.
2. Read the statement and everything it says about the report: required sections, length, format (template, LaTeX or Word), citation style, deadline, weight. Read the grading criteria in the statement, in `MISSION.md` or in `material/` (the course sheet's assessment section).
3. Mode, as in the `tutor` skill. A report that counts toward the grade is **graded** even when "it's just paperwork" or "the code is mine": the text is assessed and the student defends it.
4. Read what the report is about: the student's code, tests and results in the assignment folder.

Done when the report's requirements are listed and each grading criterion is written down with its weight (or "weight not stated").

## Step 2: The outline

Write `assignments/<slug>/REPORT-OUTLINE.md`:

```md
# Report outline: <assignment>

Due <date> · <length> · <format> · citations: <style> · weight: <weight>

## <Section, in the order the statement asks for>
Criteria it answers: <criterion from the statement>
Questions your text must answer:
- <a question the grader will ask of this section, specific to this assignment: "Why a singly linked list and not an array for `ListaLigada`?">
Evidence to include: <which test output, measurement, figure, table or code excerpt, from the student's own files>
Length: <share of the total>
```

- Sections come from the statement; when it names none, use the course's template or introduction, design decisions, implementation, tests and results, discussion and limitations, conclusion.
- Questions, evidence and length only. No sentence of the report itself, no model paragraph, no "you could write: …". Graded → this holds for every section, including the introduction and the conclusion.
- Point each piece of evidence at a real file in the workspace; when the evidence does not exist yet (no tests, no measurements), say so: that is a finding for the code, not for the text.
- Add a closing section for the AI-use declaration when the course asks for one, built from `AI-USE.md` (dates, rungs, what was given), for the student to check and sign.

Done when every grading criterion appears under at least one section and every section has questions and evidence.

## Step 3: Feedback on the draft

When the student has a draft (a `.md`, `.tex`, `.docx` or `.pdf`; extract text with `../analyze/scripts/extract_text.py` when needed), give **Report feedback** in the tutor's format and save it to `feedback/NNNN-report-<slug>.md`:

- check every criterion against the draft; a missing criterion is the most severe row;
- every claim needs evidence in the report (a test, a measurement, a figure, a citation); claims about the code are checked against the code;
- figures and tables numbered, captioned and referenced in the text; citations complete and in the course's style;
- the AI-use declaration matches `AI-USE.md`.

Graded → each row ends in a question; never a rewritten sentence. Practice (a report that does not count) → after the student's revision, you may rewrite one sentence as an example.

Done when the feedback is saved, has at most seven rows, and closes with one next step.

## Step 4: Before submitting

Offer `/exam oral <assignment>` when the report is defended, and a final check that the report and the code tell the same story (method names, results, complexity).

## Done when

The outline exists with every criterion covered, any draft has saved feedback, and nothing in either is report prose written for the student on graded work.
