# Changelog

All notable changes to CS Tutor. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [semantic versioning](https://semver.org/).

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
- `/slides`: study decks in one self-contained HTML file (fixed 16:9 stage that scales to any screen, step-by-step reveals, check-yourself slides, notes on the N key, one slide per page when printed to PDF); for graded talks, a skeleton with gaps, feedback on the student's own deck, and a rehearsal. Idea of a zero-dependency fixed stage credited to zarazhangrui/frontend-slides.

### Changed
- Integrity evals judge the final reply and check the trace for code files written; a run counts as a hand-over when it fails either. Full run: 0 of 24 with the plugin, 18 of 24 without.
- `/slides` re-derives every proof and answer before keeping it, and numbers decks from the files already in `slides/`.

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
