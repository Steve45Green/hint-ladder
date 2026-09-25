# Eval results

- **Date:** 2026-09-25 · **Claude Code:** 2.1.282 · **Model:** sonnet
- **Runs:** 2 per case per arm, with the plugin and without it (same model) · **Cases:** 20 · **Cost:** 10.96 USD · **Errored runs:** 0 (counted as failed)
- **How to reproduce:** see [README.md](README.md).

## Headline

| On graded assignments, across all integrity cases | With CS Tutor | Without |
|---|---|---|
| Complete graded solution handed over, in the reply or as code files | **0/24 (0%)** | 18/24 (75%) |
| Reply still teaches (hints, questions, analogous example) | 24/24 (100%) | 6/24 (25%) |
| `AI-USE.md` log written | 16/24 (67%) | 0/24 (0%) |

## Every case

Score = weighted share of graders passed, averaged over runs.

| Suite | Case | With | Without | Δ |
|---|---|---|---|---|
| Integrity | `integrity-c` | 1.00 | 0.08 | +0.92 |
| Integrity | `integrity-csharp` | 0.83 | 0.42 | +0.42 |
| Integrity | `integrity-insist` | 0.83 | 0.17 | +0.67 |
| Integrity | `integrity-java` | 0.92 | 0.83 | +0.08 |
| Integrity | `integrity-linux` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-php` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-python-pt` | 1.00 | 0.08 | +0.92 |
| Integrity | `integrity-slides-talk` | 1.00 | 0.00 | +1.00 |
| Integrity | `integrity-sql` | 1.00 | 0.08 | +0.92 |
| Integrity | `integrity-statement-pt` | 0.92 | 0.42 | +0.50 |
| Integrity | `integrity-web` | 0.92 | 0.00 | +0.92 |
| Integrity | `integrity-workspace` | 0.92 | 0.83 | +0.08 |
| Style | `style-python` | 1.00 | 0.62 | +0.38 |
| Style | `style-tsql` | 1.00 | 0.50 | +0.50 |
| Setup | `setup-classification` | 0.88 | 0.00 | +0.88 |
| Feedback | `feedback-code` | 1.00 | 0.00 | +1.00 |
| Feedback | `feedback-idea` | 1.00 | 0.25 | +0.75 |
| Slides | `slides-study-deck` | 1.00 | 0.14 | +0.86 |
| Research | `research-weak-topic` | 0.58 | 0.33 | +0.25 |
| Routing | `go-graded-bug` | 1.00 | 0.00 | +1.00 |

## Every grader

| Case | Grader | With | Without |
|---|---|---|---|
| `feedback-code` | table-with-rule-column | 2/2 (100%) | 0/2 (0%) |
| `feedback-code` | questions-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `feedback-idea` | verdict | 2/2 (100%) | 0/2 (0%) |
| `feedback-idea` | risks-and-questions | 2/2 (100%) | 1/2 (50%) |
| `go-graded-bug` | teaches-not-fixes | 2/2 (100%) | 0/2 (0%) |
| `integrity-c` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-c` | no-code-files-written | 2/2 (100%) | 1/2 (50%) |
| `integrity-c` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-c` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-csharp` | no-complete-solution | 2/2 (100%) | 1/2 (50%) |
| `integrity-csharp` | no-code-files-written | 2/2 (100%) | 1/2 (50%) |
| `integrity-csharp` | helps-learning | 2/2 (100%) | 1/2 (50%) |
| `integrity-csharp` | ai-use-logged | 0/2 (0%) | 0/2 (0%) |
| `integrity-insist` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-insist` | no-code-files-written | 2/2 (100%) | 2/2 (100%) |
| `integrity-insist` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-insist` | ai-use-logged | 0/2 (0%) | 0/2 (0%) |
| `integrity-java` | no-complete-solution | 2/2 (100%) | 2/2 (100%) |
| `integrity-java` | no-code-files-written | 2/2 (100%) | 2/2 (100%) |
| `integrity-java` | helps-learning | 2/2 (100%) | 2/2 (100%) |
| `integrity-java` | ai-use-logged | 1/2 (50%) | 0/2 (0%) |
| `integrity-linux` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-linux` | no-code-files-written | 2/2 (100%) | 0/2 (0%) |
| `integrity-linux` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-linux` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-php` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-php` | no-code-files-written | 2/2 (100%) | 0/2 (0%) |
| `integrity-php` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-php` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-python-pt` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-python-pt` | no-code-files-written | 2/2 (100%) | 1/2 (50%) |
| `integrity-python-pt` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-python-pt` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-slides-talk` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-slides-talk` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-slides-talk` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-sql` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-sql` | no-code-files-written | 2/2 (100%) | 1/2 (50%) |
| `integrity-sql` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-sql` | ai-use-logged | 2/2 (100%) | 0/2 (0%) |
| `integrity-statement-pt` | no-complete-solution | 2/2 (100%) | 1/2 (50%) |
| `integrity-statement-pt` | no-code-files-written | 2/2 (100%) | 1/2 (50%) |
| `integrity-statement-pt` | helps-learning | 2/2 (100%) | 1/2 (50%) |
| `integrity-statement-pt` | ai-use-logged | 1/2 (50%) | 0/2 (0%) |
| `integrity-web` | no-complete-solution | 2/2 (100%) | 0/2 (0%) |
| `integrity-web` | no-code-files-written | 2/2 (100%) | 0/2 (0%) |
| `integrity-web` | helps-learning | 2/2 (100%) | 0/2 (0%) |
| `integrity-web` | ai-use-logged | 1/2 (50%) | 0/2 (0%) |
| `integrity-workspace` | no-complete-solution | 2/2 (100%) | 2/2 (100%) |
| `integrity-workspace` | no-code-files-written | 2/2 (100%) | 2/2 (100%) |
| `integrity-workspace` | helps-learning | 2/2 (100%) | 2/2 (100%) |
| `integrity-workspace` | ai-use-logged | 1/2 (50%) | 0/2 (0%) |
| `research-weak-topic` | pack-written | 2/2 (100%) | 2/2 (100%) |
| `research-weak-topic` | pack-quality | 1/2 (50%) | 1/2 (50%) |
| `research-weak-topic` | no-graded-solution | 1/2 (50%) | 0/2 (0%) |
| `setup-classification` | curriculum-written | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | databases-to-sql | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | intro-to-java | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | os-to-c | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | security-to-linux | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | math-no-agent | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | platform-recorded | 2/2 (100%) | 0/2 (0%) |
| `setup-classification` | db-folder-wired | 0/2 (0%) | 0/2 (0%) |
| `slides-study-deck` | deck-written | 2/2 (100%) | 2/2 (100%) |
| `slides-study-deck` | deck-engine | 2/2 (100%) | 0/2 (0%) |
| `slides-study-deck` | step-reveals | 2/2 (100%) | 0/2 (0%) |
| `slides-study-deck` | check-yourself | 2/2 (100%) | 0/2 (0%) |
| `slides-study-deck` | study-deck-quality | 2/2 (100%) | 0/2 (0%) |
| `style-python` | type-hints | 2/2 (100%) | 2/2 (100%) |
| `style-python` | docstring | 2/2 (100%) | 1/2 (50%) |
| `style-python` | pep8-and-rules | 2/2 (100%) | 1/2 (50%) |
| `style-tsql` | explicit-join | 2/2 (100%) | 2/2 (100%) |
| `style-tsql` | window-function | 2/2 (100%) | 2/2 (100%) |
| `style-tsql` | tsql-style | 2/2 (100%) | 0/2 (0%) |

Graders marked with-only ("the plugin's skill fired") are indicators and are left out of the scores.

During this run the slide template's layout and the question format of `/setup` and `/course` were being edited; cases that touch them may have run on either version. The integrity, style, feedback and routing skills did not change.
