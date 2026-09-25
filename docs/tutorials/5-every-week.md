# 5. Every week: `/progress` then `/research`

*[Português](5-every-week.pt-PT.md) · [All tutorials](README.md)*

**Time:** 20 minutes, once a week (Sunday evening works well). **You need:** a few days of use in at least one unit.

## Step 1: `/progress`, where you stand

In the course folder (the one with `CURRICULUM.md`, above the units):

```bash
cd ~/Documents/engenharia-informatica
claude
```

```
/progress
```

With several units it reads them in parallel, in the background, and you can keep working. It writes `reports/<date>.md`:

- a table with every unit: **on track**, **at risk** or **behind**, the next assessment and the days left, topics mastered / seen / to do, reviews due;
- **Wins** and **Risks**, each with the evidence ("both outer-join cards back in box 1; Test 1 in 12 days");
- feedback you got and whether you acted on it;
- AI use in the period, ready for a declaration;
- **three next actions**, as commands you can type.

It changes nothing except that report. If the folder is a git repository, it offers to save the week's work (a commit).

## Step 2: `/research`, fix the weak topics

Right after, in the same place:

```
/research
```

It takes the weak topics from the report (the risks, the cards you keep getting wrong, the same mistake in several feedbacks), up to three, and writes one study pack per topic in `research/`:

- why this topic now (the evidence);
- the idea in one paragraph, then from three angles: formal, a picture, an analogy;
- **worked examples from easy to exam level**, step by step, with the usual mistake at each step;
- a table of common mistakes and how to spot them in your own work;
- **practice exercises with the answers hidden**;
- sources it opened and checked: your course material first, then official documentation and university open courseware.

If a graded assignment is open on the same topic, the examples are on a different problem (the tutor's rung 3), so nothing in the pack is your assignment's answer.

You can also name a topic: `/research outer joins`.

## Step 3: Turn it into practice

The reply ends with the next command, for example:

```
/slides research/0001-outer-joins.md     a deck to revise the pack
/lesson outer joins                      exercises with instant feedback
/exam drill                              the week's reviews
```

## Automatic weekly report (optional)

`/progress` can run on its own every week, without opening Claude Code. Ask it: "how do I automate this report?" It shows the exact line for your system (cron on macOS and Linux, Task Scheduler on Windows).

Something not working? [Troubleshooting](troubleshooting.md).
