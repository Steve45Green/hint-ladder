# lab1 NPE review

- **Date:** 2026-09-25 11:01 → 2026-09-25 11:11
- **Session:** `10edd82b-03e4-598c-bad1-43071611ee73`
- **Resume:** `claude --resume 10edd82b-03e4-598c-bad1-43071611ee73`
- **Link:** https://claude.ai/code/session_demo123
- **Folder:** `~/course/introducao-a-programacao` · branch `HEAD`
- **Agent:** `cs-tutor:java-expert`

## Summary
- Asked: code feedback on `assignments/lab1` (graded), which throws `NullPointerException` for input `2 15 Ana 12 Rui`.
- Reproduced the crash (`javac -Xlint:all` clean, then ran with that input) and found five blocker-level bugs in `Main.java`: `nomes` array never allocated (NPE root cause, line 8), off-by-one loop bound `i <= n`, `Scanner.nextInt()`/`nextLine()` leftover-newline, and `==` used instead of `.equals` on `String`; plus one design note (unneeded `static` field) and three style flags (STYLE-2, STYLE-5, STYLE-9).
- Since this is graded work, feedback was given as a question/hint table (hint ladder), not a fixed solution — student was pointed to fix the `nomes` allocation first, then re-test.
- Files created: `feedback/0001-code-lab1-npe.md` (the feedback) and `assignments/lab1/AI-USE.md` (AI-use log).
- Open follow-up: student still needs to apply the fixes in order and answer the retrieval-check question on correct loop bounds for reading `n` students.

---
### You · 2026-09-25 11:01

O meu lab1 (conta para nota) em assignments/lab1 dá NullPointerException quando corro com input '2 15 Ana 12 Rui'. Dá-me feedback de código.

### Claude · 2026-09-25 11:01

> Did: Skill `cs-tutor:tutor`; Bash `ls -la && echo "---MISSION---" && cat MISSION.md 2>/dev/null && echo "---CURRICULUM(par...`; Bash `ls -la && echo "---MISSION---" && cat MISSION.md 2>/dev/null && echo "---SYLLABUS---" &...`; Bash `cd assignments/lab1 && find . -type f | head -100`; Read `assignments/lab1/STATEMENT.md`; Read `assignments/lab1/Main.java`; Bash `java -version 2>&1 && javac -version 2>&1 && mkdir -p out && javac -Xlint:all -d out Ma...`; Bash `printf '2 15 Ana 12 Rui' | java -cp out Main 2>&1 | grep -v JAVA_TOOL_OPTIONS`; Bash `cd ~/course/…`; Bash `mkdir -p "feedback"`; Write `feedback/0001-code-lab1-npe.md`; Write `assignments/lab1/AI-USE.md`

Compiles clean. Now let's reproduce the crash with the given input.

No `feedback/` dir yet and no `AI-USE.md`. I'll create both after giving the review.

Let me also double check the leftover-newline issue is real for this specific input by tracing manually, and confirm STYLE rule numbers against the style guide before citing them.

**Code feedback** — lab1 counts toward your grade, so this is findings and questions, not a fixed version.

Verified: `javac -Xlint:all -d out Main.java` compiles clean with no warnings; the code itself is fine. Running `printf '2 15 Ana 12 Rui' | java -cp out Main` reproduces your crash exactly:
```
Exception in thread "main" java.lang.NullPointerException: Cannot store to object array because "Main.nomes" is null
	at Main.main(Main.java:8)
```

| # | Severity | Where | Problem | Rule | Question or fix |
|---|---|---|---|---|---|
| 1 | blocker | Main.java:8 | `nomes` is declared (`static String[] nomes;`) but never assigned an array before you index into it. | Correctness — NPE source | `notas` gets `new int[n]` on line 7. Where's the equivalent for `nomes`? What does an array variable hold before you call `new` on it? |
| 2 | blocker | Main.java:8 | The loop is `for (int i = 0; i <= n; i++)` — that's `n + 1` iterations, but valid indices only go `0..n-1`. | Correctness — off-by-one, array length vs loop bound | Compare this condition to the loop on line 10. Which one is right, and why does the other one overshoot? |
| 3 | blocker | Main.java:8 | `sc.nextInt()` leaves the trailing newline in the buffer; the next `sc.nextLine()` immediately consumes that leftover instead of the actual name. | Correctness — `Scanner.nextInt()` + `nextLine()` leftover newline | After `nextInt()` returns, where is the scanner's cursor relative to the `\n` after the number? What call would skip past it? |
| 4 | blocker | Main.java:11 | `nomes[best] == ""` compares references, not text. | Correctness — `==` vs `.equals` on `String` | For two separately-built `String`s with identical characters, does `==` compare content? |
| 5 | major | Main.java:3 | `nomes` is a `static` field of `Main`, but it's only used inside `main`. | Design — unnecessary static state | `notas` is local. What forces `nomes` to be a field instead? |
| 6 | minor | Main.java:2, 8 | Wildcard import (STYLE-5); two statements on one loop-body line (STYLE-2); `Scanner` never closed (STYLE-9). | STYLE-2, STYLE-5, STYLE-9 | Import `Scanner` explicitly, one statement per line, and close `sc` with try-with-resources. |

**Next step:** fix row 1 first (allocate `nomes`), recompile, rerun with the same input — you should land on row 2's crash next, confirming the fix order.

Saved to `feedback/0001-code-lab1-npe.md`, and logged in `assignments/lab1/AI-USE.md`.

Retrieval check: with `notas` correctly sized to `n`, what is the correct loop condition to read exactly `n` students, and why does `i <= n` go one past the end?

### You · 2026-09-25 11:11

`/cs-tutor:save-chat https://claude.ai/code/session_demo123 lab1 NPE review`

### Claude · 2026-09-25 11:11

> Did: Bash `cd "~/course/…`; Bash `cd "~/course/…`; Read `MISSION.md`; Bash `cd "~/course/…`; Bash `python3 <plugin>/skills/save-chat/scripts/export_chat.py --help`

MISSION.md is here, so this is the course workspace — `chats/` is the target directory. Let me check MISSION.md for language, and check the chats folder and skill directory.
