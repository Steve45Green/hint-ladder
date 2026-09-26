#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "vhdl-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Sistemas Digitais

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted work must be written by the student.

## Tools
VHDL-2008, GHDL; language agent: vhdl-expert
MD
