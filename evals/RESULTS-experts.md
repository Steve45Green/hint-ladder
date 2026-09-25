# Eval results

- **Date:** 2026-09-25 · **Claude Code:** 2.1.282 · **Model:** sonnet
- **Runs:** 2 per case per arm, with the plugin and without it (same model) · **Cases:** 8 · **Cost:** 3.90 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

The `experts` suite (`--tag experts`). A separate re-run of `feedback-java` alone, on the same day (0.48 USD), passed all four graders in both runs with the plugin; without it, only `finds-both-mistakes` passed, as in this run.

## Every case

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

## Every grader

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
