#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "python-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Matemática Computacional

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment 3 (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted code must be written by the student.

## Tools
Python; language agent: python-expert
MD
