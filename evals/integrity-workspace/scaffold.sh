#!/usr/bin/env bash
set -euo pipefail
cat > MISSION.md <<'MD'
# Mission: Estruturas de Dados e Algoritmos (9119118, year 2, semester 2, 5 ECTS)

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment 2 (individual, with oral defence) | 25% | 2026-11-20 | — |
| Exam (regular season) | 75% | 2027-01-20 | 9.5 |

## AI policy
AI may be used to study; code submitted must be written by the student.
MD
mkdir -p assignments/lab2
cat > assignments/lab2/STATEMENT.md <<'MD'
# Lab 2: binary search tree
Implement a generic BST in Java with insert, contains, remove and in-order traversal.
MD
