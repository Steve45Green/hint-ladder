---
name: plan
description: Plan the weeks ahead across every active course unit - every dated assessment from MISSION.md and Moodle, clashes where deadlines and exams pile up, dates still to confirm, and a week-by-week study plan until the end of the exam season, with a calendar file to import.
disable-model-invocation: true
argument-hint: "[semester | exams]"
---

# Plan

The student has several units and one calendar: deadlines, tests and exams pile up in the same weeks, and the exam season puts three or four exams in two weeks. Write one plan across all active units that says what is due when, where it clashes, and what to study each week. Reply and write in the language recorded as `Language:` in `CURRICULUM.md` or `MISSION.md`; when none is recorded, the language the student writes in (English if unclear). Workspace formats are in [../tutor/WORKSPACE.md](../tutor/WORKSPACE.md).

No shell in this session → read each active unit's `MISSION.md` assessment table yourself, write the plan from it, and say that the calendar file needs `/plan` in a session that can run Python.

The script lives in this skill's directory: `python3 <this skill's directory>/scripts/plan.py <study root>`. It prints JSON with the active units, every dated assessment (`events`), the ones without a date (`to_confirm`), `clashes` (assessments of different units within three days) and `weeks`. `--ics <file>` also writes a calendar file.

## Step 1: Dates

1. Find the study root (`CURRICULUM.md` here or in a parent). None → suggest `/setup` and stop.
2. When `.moodle.json` exists, run `python3 ../moodle/scripts/moodle.py news` from this skill's directory first, so assignment dates are fresh; bring new dates into `MISSION.md` only after the student confirms, as `/moodle` does.
3. Run `plan.py <root>` and read the JSON.
4. List the dates still to confirm (exam seasons, resits, weekly reports) and ask the student once, with one question per unit at most, whether they know them; write the answers into that unit's `MISSION.md`, then run the script again.

Done when every active unit's assessments are either dated or listed as "to confirm".

## Step 2: The plan

Scope: `semester` (the default) runs to the last event of the regular season; `exams` covers only the exam season and its resits.

Write `plan/YYYY-MM-DD.md` at the study root. Every word of it is in the recorded language, headings and table headers included; the `<…>` slots below are what to write, not text to copy:

```md
# <Plan>: <semester> · <written> YYYY-MM-DD

## <Clashes>
- **<from> – <to>**: <unit> <assessment> (<weight>), <unit> <assessment> (<weight>). <Start the heaviest one by date>.

## <Week by week>
| <Week> | <Due> | <Study blocks> | <Daily> |
|---|---|---|---|
| <29 Sep – 5 Oct> | — | <BD1: joins and grouping (Test 1 on 7 Oct, 30%) · SO: processes> | `/exam drill` 15 min |

## <To confirm>
- <unit>: <assessment> — <ask the lecturer or check Moodle>.
```

Address the student the way the rest of the course does (in Portuguese, the informal second person).

- Every assessment in `events` appears in the week it falls in, with its weight.
- Study blocks come from each unit's `SYLLABUS.md` (high-weight topics not yet `mastered`) and the Pace line in `MISSION.md`; units with an assessment in the next two weeks come first, weighted by what the assessment is worth.
- A clash gets a concrete earlier start: the heavier or harder assessment moves its study blocks one or two weeks forward.
- Leave room: at most three study blocks a day on top of classes, and the Constraints line of `MISSION.md` (work shifts, hours available) wins over any rule here.
- Graded assignments get their own blocks with the order of work (read the statement, first version, tests, report, oral defence rehearsal with `/exam oral`), never their content.

Done when every dated assessment is in the plan, every clash has an earlier start, each week has its study blocks, and every heading and label is in the recorded language.

## Step 3: The calendar

Run `plan.py <root> --ics plan/calendar.ics` and tell the student how to import it (Google Calendar: Settings → Import; Outlook: File → Open & export; Apple Calendar: File → Import). Each assessment is an all-day event with a reminder three days before. Say that the file must be imported again after dates change.

## Step 4: Close

Reply with the three nearest assessments, the clashes, and the one thing to do today. Suggest running `/plan` again when a date changes, or weekly with `/progress`.

## Done when

`plan/YYYY-MM-DD.md` and `plan/calendar.ics` exist, the plan holds every dated assessment the script found, and the reply names today's action.
