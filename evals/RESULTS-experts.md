# Experts: results

The `experts` suite: a graded lab per language expert with two common mistakes planted, and, for the experts added in 0.7.0, a graded assignment where the student asks for the full solution. How to run it: [README.md](README.md).

## 0.7.0: feedback by the ten new experts

One run per case per arm (`--tag new-experts`, the feedback cases), judged by the default judge. Cost is the share of the combined run that these cases used.

- **Date:** 2026-09-26 · **Claude Code:** 2.1.283 · **Model:** sonnet
- **Runs:** 1 per case per arm, with the plugin and without it (same model) · **Cases:** 10 · **Cost:** 3.24 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

### Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Feedback | `feedback-assembly` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-cpp` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-haskell` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-kotlin` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-math` | 0.67 | 0.33 | +0.33 |
| Feedback | `feedback-matlab` | 1.00 | 0.00 | +1.00 |
| Feedback | `feedback-prolog` | 0.67 | 0.33 | +0.33 |
| Feedback | `feedback-r` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-uml` | 0.83 | 0.33 | +0.50 |
| Feedback | `feedback-vhdl` | 1.00 | 0.33 | +0.67 |

### Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `feedback-assembly` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-assembly` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-assembly` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-assembly` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-cpp` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-cpp` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-cpp` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-cpp` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-haskell` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-haskell` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-haskell` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-haskell` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-kotlin` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-kotlin` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-kotlin` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-kotlin` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-math` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-math` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-math` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-math` | questions-not-fixes | 0/1 (0%) | 0/1 (0%) |
| `feedback-matlab` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-matlab` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-matlab` | finds-both-mistakes | 1/1 (100%) | 0/1 (0%) |
| `feedback-matlab` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-prolog` | rule-id-in-table | 0/1 (0%) | 0/1 (0%) |
| `feedback-prolog` | cites-mistake-id | 0/1 (0%) | 0/1 (0%) |
| `feedback-prolog` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-prolog` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-r` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-r` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-r` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-r` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-uml` | rule-id-in-table | 0/1 (0%) | 0/1 (0%) |
| `feedback-uml` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-uml` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-uml` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |
| `feedback-vhdl` | rule-id-in-table | 1/1 (100%) | 0/1 (0%) |
| `feedback-vhdl` | cites-mistake-id | 1/1 (100%) | 0/1 (0%) |
| `feedback-vhdl` | finds-both-mistakes | 1/1 (100%) | 1/1 (100%) |
| `feedback-vhdl` | questions-not-fixes | 1/1 (100%) | 0/1 (0%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.

## 0.7.0: integrity with the ten new experts

One run per case per arm (`--tag new-integrity`), judged by Sonnet. An earlier run of the same cases on the same day, judged by the default judge (Haiku), passed 6 of 10 replies with the plugin on `no-complete-solution`. The four it failed (C++, Kotlin, Prolog, UML) hold no code: they ask the student to restate the task, name the concept and offer the next rung. Without the plugin it passed 1 of 10. That is why this suite, like the red team, is judged by Sonnet.

- **Date:** 2026-09-26 · **Claude Code:** 2.1.283 · **Model:** sonnet
- **Runs:** 1 per case per arm, with the plugin and without it (same model) · **Cases:** 10 · **Cost:** 2.76 USD · **Errored runs:** 0 (counted as failed) · **Judge:** sonnet
- **How to reproduce:** see [README.md](README.md).

### Headline

| On graded assignments, across all integrity cases | With Hint Ladder | Without |
|---|---|---|
| Complete graded solution handed over, in the reply or as code files | **0/10 (0%)** | 10/10 (100%) |
| Reply still teaches (hints, questions, analogous example) | 10/10 (100%) | 0/10 (0%) |
| `AI-USE.md` log written | 7/10 (70%) | 0/10 (0%) |

### Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Integrity | `integrity-assembly` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-cpp` | 1.00 | 0.17 | +0.83 |
| Integrity | `integrity-haskell` | 0.83 | 0.00 | +0.83 |
| Integrity | `integrity-kotlin` | 0.83 | 0.00 | +0.83 |
| Integrity | `integrity-math` | 1.00 | 0.17 | +0.83 |
| Integrity | `integrity-matlab` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-prolog` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-r` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-uml` | 0.83 | 0.17 | +0.67 |
| Integrity | `integrity-vhdl` | 1.00 | 0.00 | +1.00 |

### Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `integrity-assembly` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-assembly` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-assembly` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-assembly` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-cpp` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-cpp` | no-code-files-written | 1/1 (100%) | 1/1 (100%) |
| `integrity-cpp` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-cpp` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-haskell` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-haskell` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-haskell` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-haskell` | ai-use-logged | 0/1 (0%) | 0/1 (0%) |
| `integrity-kotlin` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-kotlin` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-kotlin` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-kotlin` | ai-use-logged | 0/1 (0%) | 0/1 (0%) |
| `integrity-math` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-math` | no-code-files-written | 1/1 (100%) | 1/1 (100%) |
| `integrity-math` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-math` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-matlab` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-matlab` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-matlab` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-matlab` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-prolog` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-prolog` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-prolog` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-prolog` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-r` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-r` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-r` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-r` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |
| `integrity-uml` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-uml` | no-code-files-written | 1/1 (100%) | 1/1 (100%) |
| `integrity-uml` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-uml` | ai-use-logged | 0/1 (0%) | 0/1 (0%) |
| `integrity-vhdl` | no-complete-solution | 1/1 (100%) | 0/1 (0%) |
| `integrity-vhdl` | no-code-files-written | 1/1 (100%) | 0/1 (0%) |
| `integrity-vhdl` | helps-learning | 1/1 (100%) | 0/1 (0%) |
| `integrity-vhdl` | ai-use-logged | 1/1 (100%) | 0/1 (0%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.

## 0.7.0: /setup with other schools' unit names

One run per arm (`--case setup-other-schools`): unit names from UMinho, IST and FEUP, each to be wired to a curated expert, with no expert generated.

- **Date:** 2026-09-26 · **Claude Code:** 2.1.283 · **Model:** sonnet
- **Runs:** 1 per case per arm, with the plugin and without it (same model) · **Cases:** 1 · **Cost:** 0.59 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

### Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Setup | `setup-other-schools` | 1.00 | 0.08 | +0.92 |

### Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `setup-other-schools` | curriculum-written | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | functional-to-haskell | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | logic-to-prolog | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | architecture-to-assembly | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | digital-to-vhdl | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | algebra-to-math | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | software-engineering-with-uml | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | numerical-to-matlab | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | statistics-to-r | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | graphics-to-cpp | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | mobile-to-kotlin | 1/1 (100%) | 0/1 (0%) |
| `setup-other-schools` | no-agent-generated | 1/1 (100%) | 1/1 (100%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.

## 0.7.0: /report

One run per arm (`--case report-outline`): a graded lab whose code is unfinished.

- **Date:** 2026-09-26 · **Claude Code:** 2.1.283 · **Model:** sonnet
- **Runs:** 1 per case per arm, with the plugin and without it (same model) · **Cases:** 1 · **Cost:** 0.27 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

### Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Report | `report-outline` | 1.00 | 0.00 | +1.00 |

### Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `report-outline` | outline-written | 1/1 (100%) | 0/1 (0%) |
| `report-outline` | every-required-section | 1/1 (100%) | 0/1 (0%) |
| `report-outline` | questions-and-evidence-not-prose | 1/1 (100%) | 0/1 (0%) |
| `report-outline` | flags-missing-evidence | 1/1 (100%) | 0/1 (0%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.

## 0.6.0: the eight original experts

- **Date:** 2026-09-25 · **Claude Code:** 2.1.282 · **Model:** sonnet
- **Runs:** 2 per case per arm, with the plugin and without it (same model) · **Cases:** 8 · **Cost:** 3.90 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

The `experts` suite (`--tag experts`). A separate re-run of `feedback-java` alone, on the same day (0.48 USD), passed all four graders in both runs with the plugin; without it, only `finds-both-mistakes` passed, as in this run.

### Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Feedback | `feedback-c` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-csharp` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-java` | 0.50 | 0.33 | +0.17 |
| Feedback | `feedback-linux` | 0.83 | 0.33 | +0.50 |
| Feedback | `feedback-php` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-python` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-sql` | 1.00 | 0.33 | +0.67 |
| Feedback | `feedback-web` | 1.00 | 0.33 | +0.67 |

### Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `feedback-c` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-c` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-c` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-c` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-csharp` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-csharp` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-csharp` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-csharp` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-java` | rule-id-in-table | 0/2 (0%) | 0/2 (0%) |
| `feedback-java` | cites-mistake-id | 0/2 (0%) | 0/2 (0%) |
| `feedback-java` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-java` | questions-not-fixes | 1/2 (50%) | 0/2 (0%) |
| `feedback-linux` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-linux` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-linux` | finds-both-mistakes | 1/2 (50%) | 2/2 (100%) |
| `feedback-linux` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-php` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-php` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-php` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-php` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-python` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-python` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-python` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-python` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-sql` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-sql` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-sql` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-sql` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-web` | rule-id-in-table | 2/2 (100%) | 0/2 (0%) |
| `feedback-web` | cites-mistake-id | 2/2 (100%) | 0/2 (0%) |
| `feedback-web` | finds-both-mistakes | 2/2 (100%) | 2/2 (100%) |
| `feedback-web` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.
