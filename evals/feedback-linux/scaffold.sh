#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "linux-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Administração de Sistemas

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment 3 (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted code must be written by the student.

## Tools
Bash; language agent: linux-expert
MD
