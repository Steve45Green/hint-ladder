#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "assembly-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Arquitetura de Computadores

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted work must be written by the student.

## Tools
MIPS on MARS 4.5; language agent: assembly-expert
MD
