#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "kotlin-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Programação

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted work must be written by the student.

## Tools
Kotlin 2.0; language agent: kotlin-expert
MD
