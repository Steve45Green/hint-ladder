---
name: slides
description: Turn a topic, a lesson or analysed course material into a study slide deck (one self-contained HTML file with step-by-step reveals, check-yourself slides and notes), or help the student with a presentation they must give - skeleton, feedback and rehearsal, without writing it for them.
disable-model-invocation: true
argument-hint: "[topic | lesson file | material notes | the student's deck] [talk <minutes>]"
---

# Slides

Two jobs, decided by who presents. Reply and write in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; when none is recorded, the language the student writes in (English if unclear). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md).

| The student wants… | Mode |
|---|---|
| to study a topic, a lesson or a PDF as slides | **study deck**: you write it in full |
| slides for a presentation they must give that counts toward the grade (a talk, a group presentation, a project defence) | **graded talk**: skeleton, feedback, rehearsal; the content is theirs |
| slides for a presentation that is not graded | **study deck** rules, but low density, as a talk |

Unsure → ask one question: "Is this presentation graded?" A lecturer's `COURSE-POLICY.md` overrides this, as in the tutor skill.

## Study deck

1. **Source**: the argument (a topic, `lessons/NNNN-*.html`, `material/*.md`, or a PDF or slides to read first with `/analyze`); nothing given → the next topic in `SYLLABUS.md`, as `/lesson` chooses it. Every claim the student will use in an exam carries its source (book, chapter, page or slide) in a `.source` line.
2. **Write** `slides/NNNN-slug.html`, where NNNN is one more than the highest number already in `slides/` (0001 for the first deck, never the syllabus row), starting from this skill's `templates/deck.html`. Keep its engine and style; add only slides. Set `<html lang>` and `<title>`.
3. **Shape**, 8 to 15 slides:
   - a title slide with the goal: one action the student can do at the end;
   - **one idea per slide**, at most three short bullets or one figure; content that does not fit becomes the next slide, never smaller text (the engine shrinks an overflowing slide as a last resort, which the student sees as small print: plan so it never has to);
   - worked examples built line by line: each code line a `<span class="line step">`, and `hl` on the line being discussed;
   - memory, pointers, trees, tables, pipelines and state machines as inline SVG in a `<figure>`, with the template's classes: `.edge` lines drawn first, then `.node` shapes (they cover the edge ends), `.label` text, `.hl` on the part being discussed; labels sit beside edges and nodes, never on top of a line or another label;
   - a **check-yourself** slide (`.question` with the answer in `.answer.step`) every three or four slides, answered from memory before the reveal;
   - a closing slide with the summary and the single best source;
   - an `<aside class="notes">` on every slide with the full explanation in sentences: the deck must work for studying alone (the N key shows the notes).
4. **Check**: re-derive every worked example, proof and check-yourself answer yourself, step by step, before keeping it: the answer must be correct and complete on its own, and a proof must use the method the slide names (a "strong induction" answer really uses an earlier case than k). Run every code example and check-yourself answer that claims an output or an error, when the unit's toolchain is installed, in a scratch folder outside the workspace; fix the slide when the real result differs. Count the slides, the notes and the check-yourself slides by reading the file, and read each SVG's coordinates for labels that cross a line or each other. Then open it in a browser if you can (`xdg-open` / `open`).
5. **Tell the student**: → or space to advance, N for notes, F for full screen; print to PDF (landscape, no margins) for one slide per page.

## Graded talk

The talk is graded work: the tutor's rules apply, and the log line goes to `AI-USE.md`.

1. **Requirements**: find the brief (in `assignments/<slug>/`, or ask for it): duration, audience, what must be covered, how it is graded.
2. **Skeleton** (hint ladder rung 4): a deck from `templates/deck.html` with a slide per section of the brief (problem, approach, results, what was learned, questions) and only titles plus `___` gaps where the content goes, and a timing plan (about one minute per slide). No content written for them.
3. **Feedback** on the student's own deck: read it (HTML directly; PPTX, ODP or PDF with `/analyze`'s `scripts/extract_text.py` or the Read tool) and give **idea feedback** on the story and **code-style feedback** in the tutor's table on the slides: one idea per slide, words per slide, font size and contrast, figures versus text walls, timing against the duration, the story from problem to result. Questions, not rewrites.
4. **Rehearsal**: go slide by slide as the audience and the jury would; ask what each slide claims, what the evidence is, and the question most likely to be asked there. Then point to `/exam oral` for the full mock defence.

## Done when

- Study deck: the file exists, built on the template, with every slide carrying notes, a check-yourself slide at least every four slides, and a source on every exam-relevant claim.
- Graded talk: the student has the skeleton or the feedback or the rehearsal they asked for, nothing in it is content written for them, and `AI-USE.md` has its line.
