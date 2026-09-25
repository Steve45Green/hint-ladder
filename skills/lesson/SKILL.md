---
name: lesson
description: Give one short HTML lesson on a course topic, with instant-feedback exercises, then record only what the student demonstrably learned.
disable-model-invocation: true
argument-hint: "[topic]"
---

# Lesson

One lesson = one self-contained HTML file teaching one tightly scoped skill, completable in about ten minutes, ending in a tangible win. Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md). Reply and write in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear).

## Step 1: Load context

Read `MISSION.md`, `SYLLABUS.md`, `GLOSSARY.md`, `NOTES.md`, the active `records/`, and list `assets/`, `lessons/` and `reference/`. No workspace → give the lesson anyway in the current directory and suggest `/course` in one line.

## Step 2: Pick the topic

With an argument, teach that. Otherwise pick from the **zone of proximal development**: the first `SYLLABUS.md` topic not yet `mastered` whose dependencies are all `seen` or `mastered`; tie-break by higher weight, then nearest assessment date.

A topic too big for ten minutes ("trees") gets sliced; teach the first slice ("insertion into a binary search tree") and add the slices to `SYLLABUS.md` as rows.

## Step 3: Ground the knowledge

Take the content from `RESOURCES.md`, official course material first. Match the course's notation and language. If no listed source covers the topic, find one, confirm it exists and add it to `RESOURCES.md` before writing. A claim you cannot back with a source gets flagged in the lesson as such.

## Step 4: Write the lesson

Copy the components from this skill's `templates/` into the workspace's `assets/` when missing (`style.css`, `quiz.js`), then start from `templates/lesson.html`, setting `<html lang>` to the recorded language. Save as `lessons/NNNN-slug.html`.

- **Goal**: one sentence, an action the student can do at the end, tied to the mission.
- **The idea**: only the knowledge the practice needs; difficulty here eats working memory. Draw memory, pointers, trees, stacks, queues and state machines as inline SVG in a `<figure>` with the classes in `assets/style.css` (`.edge`, `.node`, `.label`, `.hl`), and measurements or growth as a chart (`.grid`, `.axis`, `.tick`, `.series`, `.bar`, `.point`) whose points are computed, never guessed: a drawing of memory beats a paragraph about it.
- **Worked example**: step by step. With loops or recursion, add a `table.trace` trace table.
- **Practice**: at least three exercises with instant feedback, built from `assets/quiz.js` components:
  - `.predict`: "what does this code print?", the strongest retrieval drill for programming.
  - `.quiz`: multiple choice. Every option has the same length and form, so formatting never hints at the answer.
  - Every code snippet carries the declarations its behaviour depends on (in Java a field and a local variable give different answers: `null` at run time versus a compile error). When the unit's toolchain is installed, run each snippet in a scratch folder outside the workspace and check that the stated answer matches the real output.
  - When earlier records exist, interleave one exercise from an earlier topic.
- **Main source**: the single best source to go deeper.
- **Footer**: "Questions? Ask your tutor.", plus links to related lessons and `reference/`.

When the topic has syntax, an algorithm or a formula, also create or update `reference/<topic>.html`: a one-page cheat sheet that prints well, linking `../assets/style.css`.

A new reusable widget (a stack visualiser, a truth-table checker) goes into `assets/` as a component, never inlined, so the next lesson reuses it.

## Step 5: Open it

Try `xdg-open` or `open` on the file; if neither works, give the path. Mention once that `/slides` turns the same lesson into a deck for review.

## Step 6: Check learning

After the student has done the lesson, ask one or two retrieval questions in chat, answered from memory with the lesson closed.

- Answer shows understanding → write a record (box 1, next = tomorrow, with `## Question` and `## Answer`); set the topic to `seen` in `SYLLABUS.md`.
- Answer reveals a misconception → correct it, and write a record whose Question targets the misconception.
- A term the student now uses correctly → add it to `GLOSSARY.md`.

## Done when

- The lesson file exists, links `../assets/style.css` and `../assets/quiz.js`, and has at least three exercises each carrying a `data-answer`.
- In every `.quiz`, the options have the same form and roughly the same length: the longest is at most twice the shortest, so length never gives the answer away.
- Every snippet's stated behaviour was confirmed by running it, or the lesson says which snippets could not be run.
- `SYLLABUS.md` reflects the lesson, and every new record rests on an answer the student actually gave.
