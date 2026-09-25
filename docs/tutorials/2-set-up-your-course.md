# 2. Set up your course

*[Português](2-set-up-your-course.pt-PT.md) · [All tutorials](README.md)*

**Time:** 10 minutes, once a year (again at the start of each semester to mark the new active units). **You need:** [Tutorial 1](1-install.md) done, and the list of your course units.

## Step 1: Copy your course units

Open your university portal where the study plan is (the list of *unidades curriculares*) and copy it: select the table with the mouse and Ctrl + C (⌘ + C on a Mac). Any format works: a portal table, the text of the study-plan PDF, or a list typed by hand. The more it includes (code, year, semester, ECTS, hours), the better, but names alone are enough.

## Step 2: Run `/setup`

Open a terminal, type `claude`, and then:

```
/setup
```

Paste the list when it asks (or paste it right after `/setup`, on the same line).

## Step 3: Choose where the course lives

`/setup` asks once, with Claude Code's question picker: move with the arrow keys and press Enter (or type your own answer). The recommended option comes first:

1. **A folder on this computer (Recommended)**: `<home>/Documents/<degree>`, with the history of every change (git).
2. **Folder + private GitHub**: the same folder, plus a private GitHub repository synced with it.
3. **This folder**: the folder you opened Claude Code in.

- **1** is right for most students: everything stays on your computer, with a history of every change (git).
- **2** also keeps a private copy on GitHub: a backup, and the same course on another computer. It needs a GitHub account; if the GitHub program (`gh`) is missing, `/setup` shows the one command to install it and carries on with option 1 meanwhile.
- Never make a course repository public: it will hold graded work.

## Step 4: Answer one round of questions

`/setup` works out the language of each unit from its name ("Bases de Dados" → SQL, "Sistemas Operativos" → C and Linux) and asks only what it can't know, in the same picker (up to four questions per screen), each with a recommended answer:

1. which units you are taking this semester;
2. units that could be taught in more than one language ("Programming I: C, Java or Python?");
3. your database system, if there is a database unit (SQL Server, MySQL, PostgreSQL, Oracle);
4. your computer (Windows, macOS or Linux);
5. country, grading scale and the language for replies (default: Portugal, 0–20, the language you write in);
6. your school's AI policy, if you know it.

Pick an option for each, or type your own. Outside the picker (for example in another agent), it asks in text and you answer in one message: `1: all of year 2 semester 1. 2: Java. 3: SQL Server. 4: Windows. 5: Portugal, reply in Portuguese. 6: don't know.`

Claude Code then asks your permission to write some files inside `.claude/` folders (the setting that opens each unit with its expert, and any new expert). That is expected: approve them.

## Step 5: See what it created

```
~/Documents/engenharia-informatica/
├── CURRICULUM.md              every unit, its language and its expert
├── bases-de-dados-1/          one folder per active unit
│   ├── MISSION.md             why, assessment, dates, AI policy (you finish it with /course)
│   ├── SYLLABUS.md            the topics, with status todo / seen / mastered
│   └── .claude/settings.json  opens this folder with sql-expert
├── programacao-orientada-por-objetos/
│   └── …                      opens with java-expert
└── …
```

A real one: [examples/CURRICULUM.md](../../examples/CURRICULUM.md).

## Step 6: Open a unit

```bash
cd ~/Documents/engenharia-informatica/bases-de-dados-1
claude
```

On Windows PowerShell the path looks like `cd $HOME\Documents\engenharia-informatica\bases-de-dados-1`.

**It worked when** the session answers as that unit's expert: ask "who are you?" and it says it is the SQL expert (or Java, C…).

## Step 7: Finish the unit's mission

Put the unit's course sheet (*ficha da unidade curricular*, a PDF) in the folder, then:

```
/analyze
/course
```

`/analyze` reads the PDF; `/course` fills in `MISSION.md` (assessment, dates, AI policy) and asks only what is missing. Do this for each unit when its semester starts.

## A new unit later, or one with no expert

New semester, an optional, a unit in a language Hint Ladder has no expert for (Kotlin, Haskell, C++, MATLAB, Assembly…)? In the course folder:

```
/setup add Computação Gráfica 9119140 3rd year 2nd semester 6 ECTS
```

When no expert fits, it interviews you first, in one round, each question with a recommendation:

1. what kind of expert: a programming language, an assembly, a tool (MATLAB, R, Arduino, Unity), a modelling notation (UML, ER), or none;
2. language and version ("C++17 with OpenGL 3.3");
3. environment: IDE, compiler, libraries, your computer or the lab's;
4. style: the lecturer's rules, or the language's reference guide;
5. how it is assessed: labs, a project with a defence, code written by hand in the exam.

Then it creates the unit's folder and an expert built from your answers, with its own style rules and toolchain commands, and checks it. Real ones: [the interview](../../examples/new-unit-interview.md) and [the C++ expert it built](../../examples/.claude/agents/cpp-expert.md).

Next: [3. A study day](3-a-study-day.md).
