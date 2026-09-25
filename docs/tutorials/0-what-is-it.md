# 0. What is Hint Ladder?

*[Português](0-what-is-it.pt-PT.md) · [All tutorials](README.md)*

**In one sentence:** Hint Ladder turns Claude (Anthropic's AI) into a private tutor for a Computer Engineering degree: it explains, asks questions, schedules reviews and gives feedback, and it refuses to do graded work for you.

## The problem it solves

An AI can write a university lab assignment in ten seconds. The student hands it in, and then meets the written exam and the oral defence alone, without having learned it. Hint Ladder is built for those days: it helps you learn the course, and on graded work it stops at hints.

## What it is, in plain words

| Word | What it means here |
|---|---|
| **Claude** | Anthropic's AI assistant. |
| **Claude Code** | Claude as a program on your computer. You talk to it in a **terminal** (the black text window every computer has), and it can read and write the files in the folder you open it in. |
| **Plugin** | An add-on for Claude Code. Hint Ladder is one: it adds commands and experts. |
| **Command** | Something you type that starts with `/`, such as `/go` or `/lesson`. |
| **Course unit** | One subject of the degree ("Databases 1", "Operating Systems"). |
| **Expert** | A version of Claude specialised in one programming language, with that language's style rules. Each course unit gets the right one: Java for OOP, SQL for Databases… |
| **Workspace** | The folder of one course unit, where Hint Ladder keeps your lessons, notes, reviews and feedback. |

## What a student does with it

1. **Once a year**, pastes the list of course units from the university portal. Hint Ladder creates one folder per unit and gives each one its expert.
2. **Every day**, opens the folder of a unit and types `/go`. Hint Ladder looks at what is due (reviews, a test next week, a new PDF from class) and starts the right thing: a ten-minute lesson, slides for revision, exercises, a mock exam.
3. **On graded work** (a lab, a project, a presentation) it gives hints, asks questions and reviews what the student wrote, and it writes down every help in a file the student can show the lecturer.
4. **Once a week**, `/progress` says where they stand in every unit, and `/research` brings more explanations and examples for the weak topics.

![How it works](../assets/how-it-works-light.svg)

## What it is not

- It is not a website or an app: it runs inside Claude Code, on your computer.
- It does not do your homework. That is the point.
- It does not send your work anywhere. Your files stay on your computer (or in your private GitHub repository, if you choose that). The only thing that goes over the internet is the conversation with Claude, as with any use of Claude.

## What you need

- A computer with Windows 10 or newer, macOS 13 or newer, or Linux.
- A **paid** Claude plan (Pro or higher) or an Anthropic Console account: the free plan does not include Claude Code. Hint Ladder itself is free and open source.
- About 20 minutes the first time.

Next: [1. Install Claude Code and Hint Ladder](1-install.md).
