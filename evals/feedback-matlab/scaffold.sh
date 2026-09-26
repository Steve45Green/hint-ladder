#!/usr/bin/env bash
set -euo pipefail
mkdir -p .claude
printf '{"agent": "matlab-expert"}\n' > .claude/settings.json
cat > MISSION.md <<'MD'
# Mission: Métodos Numéricos

Language: English

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Lab assignment (individual, graded) | 20% | 2026-11-06 | — |

## AI policy
AI may be used to study and for feedback; submitted work must be written by the student.

## Tools
GNU Octave 8; language agent: matlab-expert
MD
