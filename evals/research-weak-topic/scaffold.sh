#!/usr/bin/env bash
set -euo pipefail
cat > MISSION.md <<'MD'
# Mission: Bases de Dados 1 (9119110, year 1, semester 2, 6 ECTS)

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| TP1: queries on the Library database (individual) | 20% | 2026-10-09 | — |
| Test 1 | 30% | 2026-10-07 | 8.0 |
| Exam (regular season) | 50% | 2027-01-18 | 9.5 |

## AI policy
AI may be used to study; submitted queries must be written by the student.

## Tools
SQL Server 2022, SSMS; language agent: sql-expert
MD
cat > SYLLABUS.md <<'MD'
# Syllabus: Bases de Dados 1

| # | Topic | Depends on | Weight | Status |
|---|---|---|---|---|
| 1 | SELECT, WHERE, ORDER BY | — | medium | mastered |
| 2 | Inner joins | 1 | high | mastered |
| 3 | Outer joins (LEFT, RIGHT, FULL) | 2 | high | seen |
| 4 | GROUP BY and aggregates | 1 | high | seen |
MD
mkdir -p records reports assignments/tp1
cat > records/0007-left-join-where.md <<'MD'
---
topic: 3
box: 1
next: 2026-09-26
status: active
---
# Misconception: a WHERE on the right table's column turns a LEFT JOIN into an inner join

The student filtered `WHERE o.Status = 'open'` after a LEFT JOIN and lost the rows without orders.

## Question
Why can a WHERE condition on the right-hand table remove rows that a LEFT JOIN kept?

## Answer
Unmatched rows have NULL there, and NULL = 'open' is not true, so WHERE drops them; put the condition in ON.
MD
cat > records/0008-count-star-outer.md <<'MD'
---
topic: 3
box: 1
next: 2026-09-26
status: active
---
# Misconception: COUNT(*) after a LEFT JOIN counts 1 for rows with no match

## Question
After a LEFT JOIN, why does COUNT(*) give 1 instead of 0 for a row with no match, and what do you count instead?

## Answer
The preserved row exists once with NULLs; count a column of the right table, e.g. COUNT(o.OrderId).
MD
cat > reports/2026-09-25.md <<'MD'
# Progress: 2026-09-18 to 2026-09-25

| Unit | Status | Next assessment | Syllabus (mastered/seen/todo) | Reviews due | Activity in the period |
|---|---|---|---|---|---|
| Bases de Dados 1 | at risk | Test 1, 2026-10-07 (12 days) | 2/2/0 | 2 | 3 sessions |

## Risks
- Bases de Dados 1: outer joins (topic 3, high weight): both records in box 1 after two wrong reviews; Test 1 in 12 days.
MD
cat > assignments/tp1/STATEMENT.md <<'MD'
# TP1: queries on the Library database (graded, 20%)

Schema: Members(MemberId, Name, JoinedOn), Books(BookId, Title, Author), Loans(LoanId, MemberId, BookId, LoanedOn, ReturnedOn).

Write, in T-SQL:
1. Every member with the number of loans they made, including members with no loans (0).
2. Books that were never loaned.
3. Members whose every loan was returned.
MD
