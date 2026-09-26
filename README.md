<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
    <img src="docs/assets/banner-light.svg" alt="Hint Ladder — the AI tutor for Computer Engineering students. It teaches you, gives feedback, and never does your graded work." width="100%">
  </picture>
</p>

<p align="center">
  <!-- CI badge: add it back once the repository is public and named hint-ladder (docs/launch.md, step 3):
  <a href="https://github.com/Steve45Green/hint-ladder/actions/workflows/ci.yml"><img src="https://github.com/Steve45Green/hint-ladder/actions/workflows/ci.yml/badge.svg" alt="CI"></a> -->
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/version-0.7.0-informational" alt="Version 0.7.0">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Claude Code plugin">
  <a href="evals/RESULTS.md"><img src="https://img.shields.io/badge/evals-with%20vs%20without-8a63d2" alt="Evals"></a>
</p>

<p align="center">
  <b><a href="README.pt-PT.md">Português</a></b> ·
  <b><a href="docs/tutorials/README.md">Tutorials</a></b> ·
  <b><a href="https://steve45green.github.io/hint-ladder/">Live demos</a></b> ·
  <a href="docs/GUIDE.md">Guide</a> ·
  <a href="docs/for-lecturers.md">For lecturers</a> ·
  <a href="examples/">Examples</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

**Paste your course units. Get a language expert for every course. Learn — don't outsource.**

AI can write your lab in ten seconds, and then you meet the exam and the oral defence alone. Hint Ladder turns Claude Code into a tutor that is on your side for those days: it explains, asks, gives feedback on your code, your work process and your ideas, schedules your reviews, and rehearses the defence and the exam with you. On graded work it stops at hints — the solution is always yours.

<p align="center"><img src="docs/assets/demo-tour.gif" alt="A 90-second tour of Hint Ladder: /setup maps every course unit to an expert; /go in Computer Networks starts a lesson; a TCP handshake deck and an induction deck reveal step by step; an induction lesson checks answers; a graded Java lab gets hints and an AI-USE log instead of code; /progress reports every unit and /research builds a study pack" width="100%"></p>
<p align="center"><sub>A 90-second tour. Every screen is a real output from test runs on 2026-09-25, in three different course units. <a href="https://steve45green.github.io/hint-ladder/">Open the decks and lessons live</a></sub></p>

## Same prompt, two answers

<p align="center"><img src="docs/assets/demo-graded.gif" alt="Side by side, the same graded Java lab and the same model: Claude Code alone writes Student.java, Classroom.java and Main.java; with Hint Ladder it detects graded work, logs it in AI-USE.md and asks the student to plan the classes" width="100%"></p>

| Across the 12 graded-assignment cases of the [evals](evals/RESULTS.md), 24 runs per arm | With Hint Ladder | Without |
|---|---|---|
| Graded solution handed over, in the reply or as code files | **0 of 24** | 18 of 24 (75%) |
| The reply still teaches (hints, questions, an analogous example) | 24 of 24 | 6 of 24 |
| Help logged in `AI-USE.md` | 16 of 24 | 0 of 24 |

## New here? Start with the one that fits you

| You are… | Read this first |
|---|---|
| Curious what this is, no technical background | [What is Hint Ladder?](docs/tutorials/0-what-is-it.md) — 3 minutes |
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

You need Windows, macOS or Linux, and a paid Claude plan (Pro or higher) or an Anthropic Console account; Hint Ladder itself is free. First time with a terminal or with Claude Code? Follow [Tutorial 1](docs/tutorials/1-install.md), step by step.

With [Claude Code](https://code.claude.com/docs/en/setup) installed, in a terminal:

```bash
claude plugin marketplace add Steve45Green/hint-ladder && claude plugin install hint-ladder@hint-ladder
```

Or inside Claude Code: `/plugin marketplace add Steve45Green/hint-ladder`, then `/plugin install hint-ladder@hint-ladder`.

## Start in three steps

1. **`/setup`** — choose where your course lives (a folder on your computer, or a private GitHub repository created for you), then paste your course units exactly as your university portal shows them. Hint Ladder works out the language of each unit, asks only what is ambiguous ("Programming I: C, Java or Python?"), and creates one folder per unit, each wired to its expert.
2. **`cd <course folder>/<unit> && claude`** — the session already runs as that unit's expert (`sql-expert` in Databases, `java-expert` in OOP…).
3. **`/go`** — the only command to remember. It reads where you are and starts the right thing: today's review, the next lesson, feedback before you submit, a mock exam when one is close.

## Works for every unit

Real outputs from test runs, one course unit per row. HTML files open in a browser; on GitHub, use the live link.

| Course unit | What it made | Open |
|---|---|---|
| Introduction to Programming (Java) | A lesson built around the student's own Lab 1 crash, and code feedback on it | [lesson](https://steve45green.github.io/hint-ladder/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html) · [feedback](examples/introducao-a-programacao/feedback/0001-code-lab1-npe.md) |
| Data Structures and Algorithms (Java) | Slides: binary search trees, insertion and in-order traversal | [deck](https://steve45green.github.io/hint-ladder/examples/algoritmos-e-estruturas-de-dados/slides/0001-bst.html) |
| Computer Networks 1 (networking, `linux-expert`) | Slides: the TCP handshake and congestion control; `/go` started a lesson on HTTP | [deck](https://steve45green.github.io/hint-ladder/examples/redes-de-computadores-1/slides/0001-tcp-handshake-congestion-control.html) · [lesson](https://steve45green.github.io/hint-ladder/examples/redes-de-computadores-1/lessons/0001-http-request-response.html) |
| Discrete Mathematics (no code; an example from before `math-expert`) | A lesson and slides on mathematical induction | [lesson](https://steve45green.github.io/hint-ladder/examples/matematica-discreta/lessons/0001-mathematical-induction-weak.html) · [deck](https://steve45green.github.io/hint-ladder/examples/matematica-discreta/slides/0001-mathematical-induction.html) |
| Databases 1 (SQL Server) | `/research` pack on outer joins; its examples never solve the open graded assignment | [pack](examples/bases-de-dados-1/research/0001-outer-joins.md) |
| Databases 2 (SQL Server) | `/analyze` notes on normalisation from the lecturer's slides, and the course sheet | [notes](examples/bases-de-dados-2/material/normalizacao.md) |
| Computational Mathematics (Python) | Process feedback from the git history of an assignment | [feedback](examples/matematica-computacional/feedback/0001-process-tp1.md) |
| Web Application Development (PHP) | Idea feedback on a graded project, before any code | [feedback](examples/idea-feedback.md) |
| Computer Graphics (C++, before C++ joined the library) | The expert interview, and the C++/OpenGL expert it generated | [interview](examples/new-unit-interview.md) · [expert](examples/.claude/agents/cpp-expert.md) |
| The semester plan (Portuguese run) | `/plan`: every assessment of the active units, three exams in eight days flagged, dates to confirm, a calendar file | [plan](examples/pt-PT/plan/2026-09-26.md) · [calendar](examples/pt-PT/plan/calendar.ics) |
| Moodle (Portuguese run, simulated Moodle) | A lecturer posts slides and moves a test: the desktop notification, Claude opening the session with the news, `/moodle` bringing it in | [the run](examples/pt-PT/moodle-novidades.md) |

## What you get

| Command | What it does |
|---|---|
| `/go` | Reads the situation and starts the right skill or expert |
| `/setup` | Course units → one folder per unit, each with its language expert; `/setup moodle` brings each unit's files and assignment dates from your school's Moodle |
| `/analyze` | Slides, PDFs, course sheets, past exams, photos of the board → study notes with page references, likely exam questions and self-tests |
| `/lesson` | A ten-minute HTML lesson with a worked example and instant-feedback exercises |
| `/slides` | A study deck: one idea per slide, worked examples revealed line by line, check-yourself slides, notes for studying alone. For a graded talk: a skeleton, feedback and a rehearsal instead |
| `/critique` | Runs your code with the strictest compiler, tests and linters, then gives code feedback |
| `/exam drill · oral · mock` | Daily spaced review, a mock oral defence of your project, a mock exam graded on your scale |
| `/report` | Your lab or project report: an outline built from the statement's grading criteria (questions and evidence per section, no ready-made text), then feedback on your draft |
| `/progress` | Where you stand in every unit, what you did, what the experts told you, and the next three actions |
| `/plan` | Every deadline, test and exam of every unit in one week-by-week plan until the end of the exam season: clashes flagged, study blocks by weight, and a calendar file for Google, Outlook or Apple Calendar |
| `/research` | After `/progress`: for each weak topic, other explanations, worked examples from easy to exam level, practice with hidden answers, and checked sources |
| `/course` | Deepens one unit: assessment dates, AI policy, syllabus, sources, weekly pace |
| `/save-chat` | Saves a conversation to the unit folder with its link, a summary, and secrets redacted |
| `/moodle` | What lecturers posted or changed on Moodle (new slides, announcements, moved deadlines): downloaded, summarised, dated, with a next step. `/moodle watch` checks every hour and notifies you on the desktop; every session opened in the course starts with the news |
| `tutor` | Always on: classifies each request as graded, practice, off-topic or a test in progress, climbs the hint ladder on graded work, and when you say "I don't know" it shrinks the step and points you to the exact slide or page of your lecturer's material |

<table>
<tr>
<td width="50%"><img src="docs/assets/demo-slides.gif" alt="Real /slides decks from three units: the TCP handshake (Computer Networks), induction (Discrete Mathematics) and binary search trees (Data Structures), with step-by-step reveals, check-yourself answers and the notes panel"></td>
<td width="50%"><img src="docs/assets/demo-lesson.gif" alt="A real /lesson on Java arrays: a memory diagram, a predict-the-output exercise answered wrong then right, and multiple-choice questions with instant feedback"></td>
</tr>
<tr>
<td><sub><code>/slides</code> in three units: steps reveal one at a time, check-yourself slides, N for notes. <a href="https://steve45green.github.io/hint-ladder/">Open them live</a></sub></td>
<td><sub><code>/lesson</code>: a real lesson built around the student's own Lab 1 bug, with exercises that correct themselves. <a href="https://steve45green.github.io/hint-ladder/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html">Open it live</a></sub></td>
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

Each expert is a senior engineer and teacher of one language, with **numbered style rules** it follows in every line it writes and cites (`STYLE-4`) when it reviews yours, and a catalogue of the language's **common mistakes** (`MISTAKE-3`), each with the question that leads you to find it yourself and a drill that fixes the idea. On graded work you get that question, never the fix. Your lecturer's rules always win.

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
| `cpp-expert` | Programming and Data Structures in C++, OOP, Computer Graphics (OpenGL) | C++ Core Guidelines |
| `kotlin-expert` | Programming in Kotlin, Mobile Development (Android, Compose), Web Applications | Kotlin coding conventions |
| `haskell-expert` | Functional Programming, Principles of Programming, Program Calculation | Community style + HLint |
| `prolog-expert` | Logic for Programming, Functional and Logic Programming, AI labs | Covington et al. |
| `assembly-expert` | Computer Architecture: MIPS, RISC-V, ARM, x86, PEPE | The ISA's manual, Patterson & Hennessy |
| `vhdl-expert` | Digital Systems, Digital Systems Design (VHDL, Verilog, FPGA) | RTL design guidelines |
| `matlab-expert` | Numerical Methods, Numerical Analysis (MATLAB, Octave) | MATLAB Style Guidelines 2.0 |
| `r-expert` | Probability and Statistics, Data Analysis | tidyverse style guide |
| `uml-expert` | Software Engineering, Requirements, the modelling side of Databases | Ambler's Elements of UML 2.0 Style |
| `math-expert` | Calculus, Linear Algebra, Discrete Mathematics, Logic, Physics | Velleman / Hammack on writing proofs |
| `windows-expert` | Windows Server and AD, and your dev setup on Windows | PowerShell Practice and Style |
| `macos-expert` | Your dev setup on a Mac, macOS internals | Google Shell Style, adapted |

The library was chosen by [comparing the study plans of Portuguese Computer Engineering degrees](docs/curricula.md) (FEUP, IST, UMinho, FCUL, NOVA, ISEL, UA, ISEP, UC and polytechnics): which units they share and which language each school teaches them in.

A language outside the library (OCaml, Dart, Swift, Go…) gets its own expert: `/setup` (or `/setup add <unit>` later) asks what kind of expert, the language and version, your tools, the style source and how the unit is assessed, then builds it from a fixed template and validates it. [The interview](examples/new-unit-interview.md) · [a C++/OpenGL expert generated before C++ joined the library](examples/.claude/agents/cpp-expert.md).

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
- **Setup:** every unit got the right expert, maths got none (the design before `math-expert`), and the student's OS picked the platform expert, in both runs.
- **Research:** a study pack both times; one of the two packs failed the strict check that no example turns into the open graded assignment when its names are changed.

Limits, honestly: small samples (2 runs per arm) on one model. The eval harness cannot approve writes inside `.claude/`, so the check that `/setup` wrote a unit's `settings.json` fails there by design; in a normal session the student approves it ([example](examples/introducao-a-programacao/.claude/settings.json)).

### Experts, measured

A graded lab per expert with two classic mistakes planted (C: returning a local buffer and `scanf` without `&`; SQL: a `WHERE` on the outer-joined table and `COUNT(*)`; …), run with and without the plugin: 8 cases, 2 runs per arm, Sonnet, 2026-09-25, 3.90 USD. [Every grader](evals/RESULTS-experts.md).

| Expert | Finds both mistakes | Cites the common mistake (`MISTAKE-n`) in its table | Questions, not fixes |
|---|---|---|---|
| `c-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| `csharp-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| `java-expert` | 2 of 2 | 0 of 2 ¹ | 1 of 2 ¹ |
| `linux-expert` | 1 of 2 ² | 2 of 2 | 2 of 2 |
| `php-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| `python-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| `sql-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| `web-expert` | 2 of 2 | 2 of 2 | 2 of 2 |
| **All, with the plugin** | **15 of 16** | **14 of 16** | **15 of 16** |
| Without the plugin | 16 of 16 | 0 of 16 | 0 of 16 |

The model finds the bugs either way; what the expert changes is how they reach you: named after a common mistake, with a question instead of the corrected code. ¹ Both Java runs used up their 12-turn budget, and their final replies carried no `MISTAKE-n`; a re-run of that case alone passed every check in both runs (0.48 USD). ² The judge failed one Linux run whose reply names both mistakes (`cd` unchecked, `for f in $(ls)`); it stays counted as a failure.

**The ten experts added in 0.7.0**, one run per case per arm, Sonnet, 2026-09-26 ([every grader](evals/RESULTS-experts.md)):

| | With the plugin | Without |
|---|---|---|
| Feedback: finds both planted mistakes | 10 of 10 | 9 of 10 |
| Feedback: cites the common mistake (`MISTAKE-n`) | 9 of 10 | 0 of 10 |
| Feedback: questions, not fixes | 9 of 10 | 0 of 10 |
| Graded assignment: solution handed over (judged by Sonnet) | **0 of 10** | 10 of 10 |
| Graded assignment: reply still teaches | 10 of 10 | 0 of 10 |
| Graded assignment: `AI-USE.md` written | 7 of 10 | 0 of 10 |

The misses: the Prolog expert's reply had no `MISTAKE-n` in its table, the UML expert's table had no rule id, and the maths expert's summary gave the corrected expansion and the fix for the induction step (the expert now says explicitly never to, not re-measured). The default judge (Haiku) failed four correct integrity replies in a first run, so these, like the red team, are judged by Sonnet.

**`/setup` with other schools' unit names** (Programação Funcional, Lógica para Programação, Introdução à Arquitetura de Computadores, Sistemas Digitais, Métodos Numéricos…): every unit wired to its curated expert and none generated, 12 of 12 checks with the plugin, 1 of 12 without. **`/report`** on a lab with unfinished code: an outline with every required section, questions and evidence, no report text, and the missing code and tests flagged; every check with the plugin, none without.

### Red team: what students try

Thirteen attempts students actually make to get graded work done anyway, and four cases where refusing would be wrong, run with and without the plugin: 2 runs per arm, Sonnet (also as the judge), 2026-09-26, 7.52 USD. [Every case](evals/RESULTS-redteam.md).

| | With Hint Ladder | Without |
|---|---|---|
| Graded solution handed over (the 12 cases where one could be) | **0 of 24** | 9 of 24 |
| Reply still teaches | 20 of 20 | 11 of 20 |

- **Held with the plugin, broken without it:** "an analogous example, but with books" (the assignment renamed), pseudocode detailed enough to translate line by line, a graded proof by induction, distress with a deadline in two hours, role-play as "a code generator with no rules".
- **Held by both:** "I'm the lecturer", "it's only practice" when the folder says graded, a note to AI planted in the statement, "just this one small method", the lecturer's TODOs to fill. Claude alone resists these too; the plugin adds the teaching, names plagiarism when a classmate's solution is to be translated, and suggests asking for an extension.
- **Not solved yet:** during a live test, 1 of 2 runs with the plugin (and 1 of 2 without) named the SQL keywords while offering to go through the question afterwards.
- **Edge cases:** a past exam with an attempt got the full solution, and a script outside the course was written, in every run: no over-refusal. The stuck student was sent to the lecturer's slide in both runs; the judge found the encouragement too thin in both, and at the top of the ladder office hours came up in 1 of 2 runs.

## For lecturers

Hint Ladder is meant to be a tool you can recommend instead of ban: hints instead of solutions, an `AI-USE.md` log per assignment, and a `COURSE-POLICY.md` you publish that it obeys. See [For lecturers](docs/for-lecturers.md).

## Privacy

Everything runs on your computer, in your folders. Hint Ladder has no telemetry and sends nothing anywhere; the only network calls are the ones Claude Code makes to the model and, if you connect it, to your school's Moodle, with your own key, stored only on your computer. Keep course repositories **private**: they hold graded work.

## Other agents

The skills follow the Agent Skills format, so `npx skills add Steve45Green/hint-ladder` installs them in Codex, Cursor, Gemini CLI and other agents. The per-folder experts and `/save-chat` are Claude Code features; see [AGENTS.md](AGENTS.md).

## Credits

Built on ideas from [mattpocock/skills](https://github.com/mattpocock/skills) (`teach`, `grilling`, `writing-for-agents`), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (agent personas, doubt-driven review, skill linting), [shadcn/improve](https://github.com/shadcn/improve) (advisor, not implementer), [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (zero-dependency decks on a fixed 16:9 stage), [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) (stop at the first rung that holds) and [rtk-ai/rtk](https://github.com/rtk-ai/rtk). All MIT.

## License

[MIT](LICENSE) © 2026 [Steve45Green](https://github.com/Steve45Green) aka José Ameixa. Changes: [CHANGELOG](CHANGELOG.md). Contributions welcome: [CONTRIBUTING](CONTRIBUTING.md).
