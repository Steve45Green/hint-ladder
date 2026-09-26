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
