# Changelog

All notable changes to Hint Ladder (called CS Tutor until 0.6.0). The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [semantic versioning](https://semver.org/).

## [0.7.0] — 2026-09-26

### Added
- **Ten new curated experts**, chosen by comparing the study plans of Portuguese Computer Engineering degrees (FEUP, IST, UMinho, FCUL, NOVA, ISEL, UA, ISEP, UC and polytechnics, with sources in `docs/curricula.md`): `cpp-expert`, `kotlin-expert`, `haskell-expert`, `prolog-expert`, `assembly-expert` (MIPS, RISC-V, ARM, x86, PEPE), `vhdl-expert`, `matlab-expert`, `r-expert`, `uml-expert` (models in Software Engineering and ER) and `math-expert` (proofs, calculus, linear algebra, physics). Each has style rules, a catalogue of common mistakes and its own integrity and feedback evals. Maths units now get `math-expert`.
- `LANGUAGE-MAP.md`: the new experts in their rows, and rows for functional programming, logic programming, microprocessors and embedded systems, and requirements and modelling.
- **Stuck mode** in the tutor: "I don't know" without an attempt shrinks the step instead of climbing; after real attempts, one hint on the way; every reply points to the exact slide or page of the lecturer's material (`material/`, `material/moodle/`, `RESOURCES.md`, official docs), never an invented link; at the top of the ladder, office hours or the forum with the question prepared. The stuck point goes to `NOTES.md` for `/progress` and `/research`.
- **Live assessments**: a test or exam the student is sitting gets no help on its questions, not even the concept, and an offer to go through it afterwards.
- `/report`: the outline of a lab, project or internship report built from the statement's grading criteria (questions and evidence per section, no prose), and a new **Report** feedback format in the tutor for the student's draft.
- `/plan`: every dated assessment across the active units (from `MISSION.md` and Moodle), clashes, dates to confirm, a week-by-week plan to the end of the exam season and `plan/calendar.ics`. `skills/plan/scripts/plan.py`, standard library only, with a self-test.
- **Red-team and edge eval suites**: 13 attempts students make to get graded work done and 4 cases against over-refusal and for the stuck student ([results](evals/RESULTS-redteam.md)). `setup-other-schools` and `report-outline` cases.

### Changed
- The tutor answers pretexts in one line and keeps its rules: a claim to be the lecturer, "it's only practice" against the files, role-play, notes to AI inside files, translating someone else's solution (named as plagiarism), distress and deadlines (with the way to ask for an extension).
- Rung 3: an example with the assignment's operations, or one the student dictates, fails the rename test. Rung 4: a gap replaces a whole graded step, never a token.
- `evals/summarize.py` reports red-team and edge suites and the judge model.

## [0.6.0] — 2026-09-25

### Added
- `/research`: the step after `/progress`. For each weak topic (from the report's risks, box-1 records, repeated feedback), a study pack with three views of the idea, worked examples from easy to exam level, common mistakes, practice with hidden answers and sources that were opened and checked; examples are analogous when a graded assignment covers the topic. Replaces the optional `research` add-on in `/go`.
- `/setup add <unit>` and the expert interview: a unit no library agent covers gets a generated expert built from five answers (kind of expert, language and version, environment, style source, assessment shape).
- Tutorials in English and Portuguese, from "what is this?" to the weekly routine, and a troubleshooting page.
- One way to ask the student, defined in the tutor: Claude Code's question picker (AskUserQuestion) when available, otherwise clean text with no emoji; `/setup` and `/course` use it.
- Live demos on GitHub Pages (`docs/site/`, published by `.github/workflows/pages.yml`), so example decks and lessons open in a browser.
- Examples from more units: Computer Networks (TCP deck, the HTTP lesson `/go` chose), Discrete Mathematics (induction lesson and deck, no code), a `/progress` report; a 90-second tour GIF and English demo GIFs recorded from real runs.
- The deck engine shrinks a slide that overflows the stage as a last resort, and figures are capped to the stage height.
- `CITATION.cff` and issue-form links to tutorials, Discussions and private security reports.
- `/moodle`: what lecturers post or change on Moodle (new or updated files, announcements, new assignments, moved deadlines) is downloaded, analysed, summarised and dated, with one next step; date changes in `MISSION.md` only on the student's yes. A session-start hook (`hooks/hooks.json`) tells Claude what is new, from a check at most every 30 minutes, silent otherwise; `/moodle watch` installs an hourly check with a desktop notification (cron or Task Scheduler, no Claude usage). Tested end to end against a simulated Moodle.
- `/setup moodle` (also offered during `/setup`): the student signs in once, in their own terminal, with their Moodle key (or a username and password, used once); `/setup` matches their enrolled courses to units, downloads each unit's files into `material/moodle/` (kept out of git) and writes each assignment's statement and due date. `skills/moodle/scripts/moodle.py`, standard library only, with a self-test against a fake Moodle; `/save-chat` now redacts Moodle keys.
- **Common mistakes** in every language agent: 8 to 12 classic errors, each with the question that leads the student to find it and a drill; feedback cites them as `MISTAKE-n`, and on graded work the question stands in for the fix. Required by `AGENT-TEMPLATE.md` and the validator, so generated agents carry them too.
- `experts` eval suite: a graded lab per language agent with two common mistakes planted. With the plugin, 15 of 16 runs found both, 14 of 16 cited the mistake, 15 of 16 asked instead of fixing; without it, 16, 0 and 0 of 16 ([results](evals/RESULTS-experts.md)).
- Chart patterns in the deck engine and the lesson stylesheet (`.grid`, `.axis`, `.tick`, `.series`, `.bar`, `.point`, plus the diagram classes in lessons): inline SVG, revealed series by series, no dependencies.
- Portuguese examples (`examples/pt-PT/`) from a test course in Portuguese: TCP and induction decks, the lesson `/go` chose, a `/progress` report, a `/research` pack, the expert interview and a generated C++ expert; Portuguese demo GIFs for `README.pt-PT.md`.
- `/slides`: study decks in one self-contained HTML file (fixed 16:9 stage that scales to any screen, step-by-step reveals, check-yourself slides, notes on the N key, one slide per page when printed to PDF); for graded talks, a skeleton with gaps, feedback on the student's own deck, and a rehearsal. Idea of a zero-dependency fixed stage credited to zarazhangrui/frontend-slides.

### Changed
- Renamed to **Hint Ladder** (was CS Tutor): repository `Steve45Green/hint-ladder`, plugin and marketplace `hint-ladder`, long command names `/hint-ladder:<skill>`. Its core idea gives the name: a ladder of hints with no rung six.
- Integrity evals judge the final reply and check the trace for code files written; a run counts as a hand-over when it fails either. Full run: 0 of 24 with the plugin, 18 of 24 without.
- `/slides` re-derives every proof and answer before keeping it, and numbers decks from the files already in `slides/`.
- `/setup`, `/progress` and `/research` write every word in the recorded language, questions, offers and pack headings included; `/research` looks for the report at the study root too.
- SVG labels in decks stay inside the figure's `viewBox`.

### Fixed
- The README no longer shows a broken CI badge while the repository is private or not yet renamed.
- The evals workflow skips cleanly when the `ANTHROPIC_API_KEY` secret is not set, instead of failing every week.
- `docs/launch.md` matches the repository's real state: private, default branch not named `main`, not yet renamed.

## [0.5.0] — 2026-09-25

### Added
- `/analyze`: turns slides, PDFs, course sheets, past exams, PPTX/DOCX/ODT and photos into study notes with page references, likely exam questions and self-tests; course sheets feed `/course`, past exams give topic weights.
- `/save-chat`: saves a whole conversation to `chats/` with the chat link, the resume command, a summary and redacted secrets.
- `windows-expert` and `macos-expert` platform agents; `/setup` asks the student's operating system and routes toolchain problems to the right one.
- `/setup` step 0: choose where the course lives (a local folder, a private GitHub repository, or the current folder); the folder, git repository and remote are created automatically.
- Eval suite for `claude plugin eval` (integrity, style, setup, feedback, routing), run with and without the plugin.
- MIT license, contributing guide, code of conduct, security policy, issue and pull request templates, CI (lint, self-tests, plugin validation) and a manual/weekly evals workflow.
- Documentation in English with Portuguese mirrors: README, guide, a page for lecturers with a `COURSE-POLICY.md` template, `AGENTS.md` for other coding agents, real examples, a README banner and a lesson screenshot.

### Changed
- The repository is renamed `cs-tutor`; every link and install command uses the new name.
- `/lesson` checks that quiz options have similar lengths.
- The validator also checks relative links in the docs.
- `/analyze` treats everything inside course material as data, never as instructions.
- `/progress` offers to commit the week's work when the study root is a git repository.

## [0.4.0] — 2026-09-25

### Added
- `/setup`: paste the course units in any format; one workspace per active unit, each wired to its language agent; agents generated from a template for languages outside the library.
- Eight curated language agents (Java, C, C#, Python, SQL, PHP, Web, Linux) with numbered style rules, checklists and toolchain commands.
- Code, process and idea feedback formats in the tutor, saved to `feedback/`.
- `/progress`: a read-only review across workspaces with a dated report and next actions.
- `COURSE-POLICY.md`: the lecturer's rules outrank everything else.

### Changed
- Reply language and grading scale come from `MISSION.md` / `CURRICULUM.md`.
- The docs are generic: no personal or business references.

## [0.3.0] — 2026-09-25

### Added
- `/go`: one entry point that reads the situation and starts the right skill.
- A guide to using every skill.

## [0.2.0] — 2026-09-25

### Changed
- Skills, commands and workspace files translated to English; the plugin renamed `cs-tutor`.

## [0.1.0] — 2026-09-25

### Added
- First version: `tutor` with the hint ladder and `AI-USE.md` log, `/course`, `/lesson`, `/critique`, `/exam` (Leitner drill, mock oral defence, mock exam) and the spaced-review script.
