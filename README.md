<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
    <img src="docs/assets/banner-light.svg" alt="CS Tutor — the AI tutor for Computer Engineering students. It teaches you, gives feedback, and never does your graded work." width="100%">
  </picture>
</p>

<p align="center">
  <!-- CI badge: add it back once the repository is public and named cs-tutor (docs/launch.md, step 3):
  <a href="https://github.com/Steve45Green/cs-tutor/actions/workflows/ci.yml"><img src="https://github.com/Steve45Green/cs-tutor/actions/workflows/ci.yml/badge.svg" alt="CI"></a> -->
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/version-0.6.0-informational" alt="Version 0.6.0">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Claude Code plugin">
  <a href="evals/RESULTS.md"><img src="https://img.shields.io/badge/evals-with%20vs%20without-8a63d2" alt="Evals"></a>
</p>

<p align="center">
  <b><a href="README.pt-PT.md">Português</a></b> ·
  <b><a href="docs/tutorials/README.md">Tutorials</a></b> ·
  <b><a href="https://steve45green.github.io/cs-tutor/">Live demos</a></b> ·
  <a href="docs/GUIDE.md">Guide</a> ·
  <a href="docs/for-lecturers.md">For lecturers</a> ·
  <a href="examples/">Examples</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

**Paste your course units. Get a language expert for every course. Learn — don't outsource.**

AI can write your lab in ten seconds, and then you meet the exam and the oral defence alone. CS Tutor turns Claude Code into a tutor that is on your side for those days: it explains, asks, gives feedback on your code, your work process and your ideas, schedules your reviews, and rehearses the defence and the exam with you. On graded work it stops at hints — the solution is always yours.

<p align="center"><img src="docs/assets/demo-tour.gif" alt="A 90-second tour of CS Tutor: /setup maps every course unit to an expert; /go in Computer Networks starts a lesson; a TCP handshake deck and an induction deck reveal step by step; an induction lesson checks answers; a graded Java lab gets hints and an AI-USE log instead of code; /progress reports every unit and /research builds a study pack" width="100%"></p>
<p align="center"><sub>A 90-second tour. Every screen is a real output from test runs on 2026-09-25, in three different course units. <a href="https://steve45green.github.io/cs-tutor/">Open the decks and lessons live</a></sub></p>

## Same prompt, two answers

<p align="center"><img src="docs/assets/demo-graded.gif" alt="Side by side, the same graded Java lab and the same model: Claude Code alone writes Student.java, Classroom.java and Main.java; with CS Tutor it detects graded work, logs it in AI-USE.md and asks the student to plan the classes" width="100%"></p>

| Across the 12 graded-assignment cases of the [evals](evals/RESULTS.md), 24 runs per arm | With CS Tutor | Without |
|---|---|---|
| Graded solution handed over, in the reply or as code files | **0 of 24** | 18 of 24 (75%) |
| The reply still teaches (hints, questions, an analogous example) | 24 of 24 | 6 of 24 |
| Help logged in `AI-USE.md` | 16 of 24 | 0 of 24 |

## New here? Start with the one that fits you

| You are… | Read this first |
|---|---|
| Curious what this is, no technical background | [What is CS Tutor?](docs/tutorials/0-what-is-it.md) — 3 minutes |
| A student who wants to use it | [Install](docs/tutorials/1-install.md) → [Set up your course](docs/tutorials/2-set-up-your-course.md) → [A study day](docs/tutorials/3-a-study-day.md) |
| A lecturer | [For lecturers](docs/for-lecturers.md) |
| Stuck | [Troubleshooting](docs/tutorials/troubleshooting.md) |

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/how-it-works-dark.svg">
    <img src="docs/assets/how-it-works-light.svg" alt="How it works: 1 install once; 2 /setup once a year; 3 open a unit every session; 4 /go every day; 5 /progress then /research every week" width="100%">
  </picture>
</p>

## Install

You need Windows, macOS or Linux, and a paid Claude plan (Pro or higher) or an Anthropic Console account; CS Tutor itself is free. First time with a terminal or with Claude Code? Follow [Tutorial 1](docs/tutorials/1-install.md), step by step.

With [Claude Code](https://code.claude.com/docs/en/setup) installed, in a terminal:

```bash
claude plugin marketplace add Steve45Green/cs-tutor && claude plugin install cs-tutor@cs-tutor-skills
```

Or inside Claude Code: `/plugin marketplace add Steve45Green/cs-tutor`, then `/plugin install cs-tutor@cs-tutor-skills`.

## Start in three steps

1. **`/setup`** — choose where your course lives (a folder on your computer, or a private GitHub repository created for you), then paste your course units exactly as your university portal shows them. CS Tutor works out the language of each unit, asks only what is ambiguous ("Programming I: C, Java or Python?"), and creates one folder per unit, each wired to its expert.
2. **`cd <course folder>/<unit> && claude`** — the session already runs as that unit's expert (`sql-expert` in Databases, `java-expert` in OOP…).
3. **`/go`** — the only command to remember. It reads where you are and starts the right thing: today's review, the next lesson, feedback before you submit, a mock exam when one is close.

## Works for every unit

Real outputs from test runs, one course unit per row. HTML files open in a browser; on GitHub, use the live link.

| Course unit | What it made | Open |
|---|---|---|
| Introduction to Programming (Java) | A lesson built around the student's own Lab 1 crash, and code feedback on it | [lesson](https://steve45green.github.io/cs-tutor/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html) · [feedback](examples/introducao-a-programacao/feedback/0001-code-lab1-npe.md) |
| Data Structures and Algorithms (Java) | Slides: binary search trees, insertion and in-order traversal | [deck](https://steve45green.github.io/cs-tutor/examples/algoritmos-e-estruturas-de-dados/slides/0001-bst.html) |
| Computer Networks 1 (networking, `linux-expert`) | Slides: the TCP handshake and congestion control; `/go` started a lesson on HTTP | [deck](https://steve45green.github.io/cs-tutor/examples/redes-de-computadores-1/slides/0001-tcp-handshake-congestion-control.html) · [lesson](https://steve45green.github.io/cs-tutor/examples/redes-de-computadores-1/lessons/0001-http-request-response.html) |
| Discrete Mathematics (no code, no expert) | A lesson and slides on mathematical induction | [lesson](https://steve45green.github.io/cs-tutor/examples/matematica-discreta/lessons/0001-mathematical-induction-weak.html) · [deck](https://steve45green.github.io/cs-tutor/examples/matematica-discreta/slides/0001-mathematical-induction.html) |
| Databases 1 (SQL Server) | `/research` pack on outer joins; its examples never solve the open graded assignment | [pack](examples/bases-de-dados-1/research/0001-outer-joins.md) |
| Databases 2 (SQL Server) | `/analyze` notes on normalisation from the lecturer's slides, and the course sheet | [notes](examples/bases-de-dados-2/material/normalizacao.md) |
| Computational Mathematics (Python) | Process feedback from the git history of an assignment | [feedback](examples/matematica-computacional/feedback/0001-process-tp1.md) |
| Web Application Development (PHP) | Idea feedback on a graded project, before any code | [feedback](examples/idea-feedback.md) |
| Computer Graphics (C++, no expert in the library) | The expert interview, and the C++/OpenGL expert it generated | [interview](examples/new-unit-interview.md) · [expert](examples/.claude/agents/cpp-expert.md) |

## What you get

| Command | What it does |
|---|---|
| `/go` | Reads the situation and starts the right skill or expert |
| `/setup` | Course units → one folder per unit, each with its language expert |
| `/analyze` | Slides, PDFs, course sheets, past exams, photos of the board → study notes with page references, likely exam questions and self-tests |
| `/lesson` | A ten-minute HTML lesson with a worked example and instant-feedback exercises |
| `/slides` | A study deck: one idea per slide, worked examples revealed line by line, check-yourself slides, notes for studying alone. For a graded talk: a skeleton, feedback and a rehearsal instead |
| `/critique` | Runs your code with the strictest compiler, tests and linters, then gives code feedback |
| `/exam drill · oral · mock` | Daily spaced review, a mock oral defence of your project, a mock exam graded on your scale |
| `/progress` | Where you stand in every unit, what you did, what the experts told you, and the next three actions |
| `/research` | After `/progress`: for each weak topic, other explanations, worked examples from easy to exam level, practice with hidden answers, and checked sources |
| `/course` | Deepens one unit: assessment dates, AI policy, syllabus, sources, weekly pace |
| `/save-chat` | Saves a conversation to the unit folder with its link, a summary, and secrets redacted |
| `tutor` | Always on: classifies each request as graded, practice or off-topic, and climbs the hint ladder on graded work |

<table>
<tr>
<td width="50%"><img src="docs/assets/demo-slides.gif" alt="Real /slides decks from three units: the TCP handshake (Computer Networks), induction (Discrete Mathematics) and binary search trees (Data Structures), with step-by-step reveals, check-yourself answers and the notes panel"></td>
<td width="50%"><img src="docs/assets/demo-lesson.gif" alt="A real /lesson on Java arrays: a memory diagram, a predict-the-output exercise answered wrong then right, and multiple-choice questions with instant feedback"></td>
</tr>
<tr>
<td><sub><code>/slides</code> in three units: steps reveal one at a time, check-yourself slides, N for notes. <a href="https://steve45green.github.io/cs-tutor/">Open them live</a></sub></td>
<td><sub><code>/lesson</code>: a real lesson built around the student's own Lab 1 bug, with exercises that correct themselves. <a href="https://steve45green.github.io/cs-tutor/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html">Open it live</a></sub></td>
</tr>
</table>

### The hint ladder (graded work)

```
1. Restate            you explain the assignment in your own words
2. Concept            "this is a breadth-first search", chapter X of your bibliography
3. Analogous example  a DIFFERENT problem solved with the same technique
4. Skeleton           your problem's structure, with ___ gaps in every graded part
5. Review             you write; the expert gives feedback and asks questions
   there is no rung 6: you write the graded solution
```

Every help on graded work is logged in `AI-USE.md`, so you can declare AI use honestly. When your lecturer publishes a [`COURSE-POLICY.md`](docs/COURSE-POLICY.template.md), it outranks everything.

## The experts

Each expert is a senior engineer and teacher of one language, with **numbered style rules** it follows in every line it writes and cites (`STYLE-4`) when it reviews yours. Your lecturer's rules always win.

| Expert | Typical courses | Style base |
|---|---|---|
| `java-expert` | Intro to Programming, OOP, Data Structures, Software Engineering, Android | Google Java Style |
| `c-expert` | Intro to Programming, Operating Systems, Computer Architecture | K&R / Linux kernel |
| `csharp-expert` | OOP, Software Engineering, ASP.NET | .NET conventions |
| `python-expert` | Numerical Methods, Statistics, AI | PEP 8 + PEP 257 |
| `sql-expert` | Databases, Information Systems — SQL Server, MySQL, PostgreSQL, Oracle | Per dialect |
| `php-expert` | Web Technologies, Web Applications | PSR-12 |
| `web-expert` | Human-Computer Interaction, front-end | Google HTML/CSS + WCAG |
| `linux-expert` | Operating Systems, Networks, Security, System Administration | Google Shell Style |
| `windows-expert` | Windows Server and AD, and your dev setup on Windows | PowerShell Practice and Style |
| `macos-expert` | Your dev setup on a Mac, macOS internals | Google Shell Style, adapted |

A language outside the library (C++, Kotlin, Haskell, Assembly, R, MATLAB…) gets its own expert: `/setup` (or `/setup add <unit>` later) asks what kind of expert, the language and version, your tools, the style source and how the unit is assessed, then builds it from a fixed template and validates it. [The interview](examples/new-unit-interview.md) · [a generated C++/OpenGL expert](examples/.claude/agents/cpp-expert.md).

<p align="center"><img src="docs/assets/demo-setup-add.gif" alt="/setup add for Computação Gráfica: the expert interview (stack, version, environment, style, assessment), then the generated cpp-expert with its style rules" width="85%"></p>

### Feedback on your code, your process and your ideas

<details>
<summary><b>Code feedback</b> — a real reply to a graded Java lab that crashed</summary>

| # | Severity | Where | Problem | Rule | Question or fix |
|---|---|---|---|---|---|
| 1 | blocker | Main.java:8 | `nomes` is declared but never assigned an array before you index into it | NPE source | `notas` gets `new int[n]` on line 7. Where's the equivalent for `nomes`? |
| 2 | blocker | Main.java:8 | `i <= n` runs `n + 1` times, but valid indices are `0..n-1` | off-by-one | Compare this condition to the loop on line 10. Which one overshoots? |
| 3 | blocker | Main.java:8 | `nextInt()` leaves the newline; `nextLine()` reads it instead of the name | `Scanner` leftover newline | Where is the cursor after `nextInt()` returns? |
| 4 | blocker | Main.java:11 | `nomes[best] == ""` compares references | `==` vs `equals` | Does `==` compare the characters of two strings? |
| 6 | minor | Main.java:2, 8 | wildcard import; two statements on one line; `Scanner` never closed | STYLE-2, STYLE-5, STYLE-9 | |

**Next step:** fix row 1 first, recompile, rerun with the same input.
</details>

<details>
<summary><b>Idea feedback</b> — a graded web project, before any code</summary>

**Verdict:** adjust — solid idea that hits the right course concepts, but the scope is tight for 6 weeks solo once you account for SQL Server setup and the concurrency a booking system needs.

**Risks:** the PHP → SQL Server driver setup eats the first days; double-booking is a real concurrency problem (transaction or constraint); the approval workflow is a state machine on top of ownership checks (IDOR); e-mail from a dev environment is often blocked.

**Questions:** Is a framework allowed? Does the rubric list required features? What must "admin approval" support?
</details>

<details>
<summary><b>Process feedback</b> — from the git history of a numerical methods assignment</summary>

**Keep:** the work is in git.
**Change:** both commits share the same timestamp — no incremental history to show at the oral defence; no test or entry point calls the bisection function, so nobody has seen it terminate.
**Next step:** add a run on a case with a known root, watch it, and commit that as its own step.
</details>

More in [examples/](examples/).

## Does it work?

Measured with Claude Code's own eval runner (`claude plugin eval`): 20 cases, each run **with** the plugin and **without** it on the same model (Sonnet), 2 runs per arm, 2026-09-25, 10.96 USD. [All results](evals/RESULTS.md) · [method](evals/README.md).

- **Graded work:** the numbers in the table above. A run counts as a hand-over when the final reply solves the task or when code files are written.
- **Feedback, style, slides, routing:** code feedback in the tutor's format, idea feedback with a verdict, T-SQL and Python that follow the experts' style rules, a study deck on the slide engine, and `/go` sending a crash in graded code to teaching: 2 of 2 with the plugin on every check. Without it, 0 of 2 on most of them.
- **Setup:** every unit got the right expert, maths got none, and the student's OS picked the platform expert, in both runs.
- **Research:** a study pack both times; one of the two packs failed the strict check that no example turns into the open graded assignment when its names are changed.

Limits, honestly: small samples (2 runs per arm) on one model. The eval harness cannot approve writes inside `.claude/`, so the check that `/setup` wrote a unit's `settings.json` fails there by design; in a normal session the student approves it ([example](examples/introducao-a-programacao/.claude/settings.json)).

## For lecturers

CS Tutor is meant to be a tool you can recommend instead of ban: hints instead of solutions, an `AI-USE.md` log per assignment, and a `COURSE-POLICY.md` you publish that it obeys. See [For lecturers](docs/for-lecturers.md).

## Privacy

Everything runs on your computer, in your folders. CS Tutor has no telemetry and sends nothing anywhere; the only network calls are the ones Claude Code makes to the model. Keep course repositories **private**: they hold graded work.

## Other agents

The skills follow the Agent Skills format, so `npx skills add Steve45Green/cs-tutor` installs them in Codex, Cursor, Gemini CLI and other agents. The per-folder experts and `/save-chat` are Claude Code features; see [AGENTS.md](AGENTS.md).

## Credits

Built on ideas from [mattpocock/skills](https://github.com/mattpocock/skills) (`teach`, `grilling`, `writing-for-agents`), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (agent personas, doubt-driven review, skill linting), [shadcn/improve](https://github.com/shadcn/improve) (advisor, not implementer), [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (zero-dependency decks on a fixed 16:9 stage), [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) (stop at the first rung that holds) and [rtk-ai/rtk](https://github.com/rtk-ai/rtk). All MIT.

## License

[MIT](LICENSE) © 2026 José Ameixa. Changes: [CHANGELOG](CHANGELOG.md). Contributions welcome: [CONTRIBUTING](CONTRIBUTING.md).
