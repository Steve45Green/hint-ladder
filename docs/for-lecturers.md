# Hint Ladder for lecturers

*[Português](para-docentes.pt-PT.md)*

Your students already use AI. Hint Ladder is an AI tutor for Claude Code that is built to make them learn: on graded work it **teaches and gives feedback, and does not write the solution**, unless your course policy says otherwise.

## What it does on graded work

| The student asks | Hint Ladder does |
|---|---|
| "Write the code for my lab" | Climbs a hint ladder: asks the student to restate the task, names the concept, solves a *different* analogous problem, gives a skeleton with gaps, then reviews the student's own attempt. It never goes past that. |
| "Why does my code crash?" | Code feedback: severity, `file:line`, problem, rule broken and a **question** that leads to the fix. No corrected code. |
| "Is my project idea good?" | A `go / adjust / rethink` verdict, risks and questions. No design written for them. |
| Before the oral defence | A mock defence that questions every module and design decision. |

Every help on graded work is logged in `assignments/<assignment>/AI-USE.md` with the date and how far up the ladder it went, so students can declare AI use honestly.

## Set the rules for your course

Publish a `COURSE-POLICY.md` ([template](COURSE-POLICY.template.md)) on your course page; students put it in the course folder. It outranks every other setting:

- **No AI at all** on graded work: the tutor only explains general concepts with its own examples.
- **Hints only** (the default).
- **AI-generated code allowed with a declaration**: the tutor helps fully and keeps the log.
- **Your style rules**: they override the language agent's defaults and are cited in feedback.

## Evidence

The repository has an eval suite that runs each case with and without the plugin, on the same model. The latest results, with the method and cost, are in [evals/RESULTS.md](../evals/RESULTS.md).

## Limits, honestly

- Hint Ladder supports students who want to learn. A student determined to cheat can use a plain chatbot instead; oral defences and in-class work stay the strongest checks.
- `AI-USE.md` is written by the tool on the student's machine; it is a declaration aid, not tamper-proof evidence.
- `COURSE-POLICY.md` is followed as written; the student is the one who places it in the folder.

## Privacy

Everything runs on the student's computer, in their own folders. The plugin has no telemetry and sends nothing to lecturers or to the project.

## Feedback

Tell us what would make it useful in your course: [open an issue](https://github.com/Steve45Green/hint-ladder/issues).
