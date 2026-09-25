# hint-ladder

A Claude Code plugin that tutors any Computer Engineering student: they paste their course units, `/setup` wires each unit to a language agent, and the skills teach and give feedback without ever doing graded work for them. Portuguese higher education is the default locale (0–20 grading, regular/resit/special seasons); other locales come from `CURRICULUM.md`.

## Layout

- `skills/<name>/SKILL.md`: one skill per directory. `tutor` is the only model-invoked skill; every other skill sets `disable-model-invocation: true`.
- `skills/tutor/SKILL.md`: modes, hint ladder, policy order (`COURSE-POLICY.md` > `MISSION.md` > defaults) and the **feedback formats** (code, process, idea). The single source for all of them.
- `skills/tutor/WORKSPACE.md`: the single source for workspace and study-root file formats. Other skills link to it (`../tutor/WORKSPACE.md`) instead of restating it.
- `skills/setup/`: `/setup` (course units → `CURRICULUM.md` + one workspace per active unit + agent wiring), `LANGUAGE-MAP.md` (unit name → stack → agent) and `AGENT-TEMPLATE.md` (the skeleton every language agent follows).
- `skills/go/SKILL.md`: the user-invoked entry point, routing to this pack's skills, agents and optional complements.
- `agents/<lang>-expert.md`: curated language agents. Each preloads `tutor` (applies when run as a subagent) and tells itself to invoke `tutor` when run as the main agent (preloading does not apply there).
- `agents/windows-expert.md`, `agents/macos-expert.md`: platform agents, picked by the student's OS (`OS:` line in `CURRICULUM.md`), for toolchain setup and Windows/macOS course topics.
- `skills/research/`: `/research`, the step after `/progress`: study packs on weak topics (other explanations, worked examples from easy to exam level, practice, checked sources), analogous only when a graded assignment overlaps.
- `skills/analyze/`: course material → study notes with page references; `scripts/extract_text.py` extracts PPTX/DOCX/ODT/HTML text (and PDF through `pdftotext` when installed).
- `skills/save-chat/`: saves a session to `chats/` with link, resume command and summary; `scripts/export_chat.py` turns the session JSONL (`~/.claude/projects/<cwd-slug>/<id>.jsonl`) into Markdown and redacts secrets.
- `skills/lesson/templates/`: lesson template and the shared `style.css` / `quiz.js` components.
- `skills/slides/`: `/slides` (study decks written in full; graded talks get only a skeleton, feedback and rehearsal) and `templates/deck.html`, the self-contained deck engine (fixed 1600×900 stage, step reveals, notes, print to PDF). Decks copy the engine; change it only in the template.
- `skills/exam/scripts/review.py`: Leitner scheduler over `records/`.
- `docs/site/index.html`: the live-demo landing page; `.github/workflows/pages.yml` publishes it with `docs/assets/` and `examples/` on the public `main` branch.
- `scripts/validate_skills.py`: linter for skills and agents (`--agents DIR` also lints generated agents).

## Conventions

- Skills and agents are written in English. What they produce is in the language recorded as `Language:` in `MISSION.md` or `CURRICULUM.md`; with none recorded, the language the student writes in (English if unclear). The only Portuguese words inside skills are trigger terms in the `tutor` description and unit-name patterns in `LANGUAGE-MAP.md`.
- Docs are in English with a European Portuguese (PT-PT) mirror, changed together: `README.md` ↔ `README.pt-PT.md`, `docs/GUIDE.md` ↔ `docs/GUIA.pt-PT.md`, `docs/for-lecturers.md` ↔ `docs/para-docentes.pt-PT.md`, and every `docs/tutorials/<name>.md` ↔ `docs/tutorials/<name>.pt-PT.md`. A new or renamed command goes into both READMEs' command tables, both guides and the tutorial that covers it. `docs/launch.md` (the owner's GitHub checklist) is PT-PT only. Keep all docs generic: no personal data about any student.
- `examples/` holds real outputs from test runs, paths shortened to `~/course`; `evals/` holds the `claude plugin eval` suite and `evals/RESULTS.md`, whose numbers come only from real runs.
- Each agent is the single source of its language's style rules; `/critique` defers to the session's agent.
- `LANGUAGE-MAP.md` and the `agents/` library change together: a new curated agent means updating the map's Primary and Generated columns, both READMEs' expert tables, both guides, and adding an integrity eval.
- Every step ends on a checkable completion criterion ("Done when").
- Graded work stops at hint-ladder rung 5, unless `COURSE-POLICY.md` or the AI policy in `MISSION.md` says otherwise. Preserve this in any edit.
- Scripts use the Python standard library only and carry a runnable self-test.
- A new skill is user-invoked unless the agent must reach it on its own.

## Checks

Run before committing:

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_skills.py --test
for s in skills/*/scripts/*.py; do python3 "$s" --test; done
python3 evals/summarize.py --test
```
