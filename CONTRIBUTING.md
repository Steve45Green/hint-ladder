# Contributing to CS Tutor

Thanks for helping students learn instead of outsourcing. The most useful contributions:

1. **Your university's course units** — so `/setup` classifies them correctly.
2. **A language agent** for a language taught in your course that the library lacks.
3. **Bug reports** from real study sessions: what you asked, what the tutor did, what it should have done.

Every contribution must keep the core promise: **on graded work the tutor teaches and gives feedback; it never writes the solution**, unless the lecturer's `COURSE-POLICY.md` or the course's AI policy says otherwise.

## Setup

```bash
git clone https://github.com/Steve45Green/cs-tutor
cd cs-tutor
claude --plugin-dir .          # run Claude Code with your working copy of the plugin
```

Checks (the same ones CI runs):

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_skills.py --test
for s in skills/*/scripts/*.py; do python3 "$s" --test; done
claude plugin validate .
```

## Add your university's course units

1. Open [`skills/setup/LANGUAGE-MAP.md`](skills/setup/LANGUAGE-MAP.md).
2. Add your unit names as patterns to the matching row (lowercase; accents are ignored when matching), or add a row for a new kind of unit.
3. Add your curriculum as a fixture in `evals/fixtures/curricula/<school>.txt` (the public study plan, as pasted from the portal) with the expected agent per unit in a comment at the top.
4. Run `/setup` on it with `claude --plugin-dir .` and check `CURRICULUM.md`.

## Add a language agent

1. Copy the skeleton in [`skills/setup/AGENT-TEMPLATE.md`](skills/setup/AGENT-TEMPLATE.md) to `agents/<lang>-expert.md`.
2. Base the **style rules** on the language's reference style guide, name it, and write 10–14 numbered, checkable rules. The agent follows them in all code it writes and cites them as `STYLE-n` in feedback.
3. Fill the **feedback loop** with commands you really ran: version check, build with the strictest warnings, tests, linter.
4. Add the agent to `LANGUAGE-MAP.md` (Primary or Generated column), to the agent tables in the READMEs and to the guide.
5. Add an integrity eval in `evals/integrity-<lang>/case.yaml` (copy an existing one).
6. `python3 scripts/validate_skills.py` must report 0 errors.

## Change a skill

- Skills and agents are written in English; what they produce follows the student's `Language:` setting.
- Every step ends on a checkable "Done when".
- A new skill is user-invoked (`disable-model-invocation: true`) unless the agent must reach it on its own: every model-invoked skill costs context on every turn.
- One source of truth: feedback formats live in `skills/tutor/SKILL.md`, workspace formats in `skills/tutor/WORKSPACE.md`; link to them instead of restating.
- Scripts use the Python standard library only and carry a `--test` self-test.

## Evals

`evals/` holds cases for `claude plugin eval`, which runs each case with and without the plugin. They call the model, so they cost money: run a subset while developing.

```bash
claude plugin eval . --tag integrity --runs 1 --model sonnet --scaffold \
  --allow-tools Write Edit --max-cost-usd 5
```

Report numbers only from real runs, with the model, the number of runs and the date: `python3 evals/summarize.py <results.json> --out evals/RESULTS.md` writes them from the run's JSON. See [`evals/README.md`](evals/README.md).

## Pull requests

- One topic per PR; describe what a student will notice.
- Run the checks above; CI runs them again.
- Never include real student work, grades or personal data in fixtures or examples.
