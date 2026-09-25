# Code feedback — assignments/lab1/Main.java

Date: 2026-09-25
Files reviewed: assignments/lab1/Main.java
Commands run:
- `javac -Xlint:all -d out Main.java` → compiles clean, no warnings.
- `printf '2 15 Ana 12 Rui' | java -cp out Main` → `Exception in thread "main" java.lang.NullPointerException: Cannot store to object array because "Main.nomes" is null` at `Main.java:8`.

| # | Severity | Where | Problem | Rule | Question or fix |
|---|---|---|---|---|---|
| 1 | blocker | Main.java:8 | `nomes` is declared (`static String[] nomes;`) but never assigned an array before you index into it. | Correctness — NullPointerException source | `notas` gets `new int[n]` on line 7. Where is the equivalent line for `nomes`? What does an array variable hold before you call `new` on it? |
| 2 | blocker | Main.java:8 | The loop header is `for (int i = 0; i <= n; i++)`, so it runs `n + 1` times (`i` reaches `n`), but both arrays only have valid indices `0..n-1`. | Correctness — off-by-one, array length vs loop bound | You have `n` students. What is the smallest number of iterations that visits index `0` through `n - 1` and no further? Compare your condition to the one in the second loop on line 10. |
| 3 | blocker | Main.java:8 | `sc.nextInt()` reads the number but leaves the newline after it in the buffer; the very next `sc.nextLine()` then reads that leftover empty line instead of the student's name. | Correctness — `Scanner.nextInt()` + `nextLine()` leftover-newline pitfall | After `sc.nextInt()` returns, where is the scanner's cursor positioned relative to the `\n` that follows the number? What would you need to call to consume that leftover before reading the name? |
| 4 | blocker | Main.java:11 | `nomes[best] == ""` compares object references, not text content, so this check can never do what its name suggests. | Correctness — `==` vs `.equals` on `String` | For two separately-created `String` objects with the same characters, does `==` compare the characters or the reference? What method compares content? |
| 5 | major | Main.java:3 | `nomes` is a `static` field of `Main` even though it is only ever used inside `main`. | Design — shared mutable `static` state / unnecessary field scope | `notas` is a local variable of `main`. What forces `nomes` to be a field instead of also being local? |
| 6 | minor | Main.java:2, 8 | Style: `import java.util.*;` is a wildcard import (STYLE-5); the loop body packs two statements on one line (STYLE-2, "one statement per line"); the `Scanner` is never closed (STYLE-9, try-with-resources for `AutoCloseable`). | STYLE-2, STYLE-5, STYLE-9 | Rewrite the import as an explicit `java.util.Scanner`, split the loop body across two lines, and wrap the scanner creation in a `try (Scanner sc = ...)` block — what changes at the end of `main`? |

Next step: fix row 1 first (allocate `nomes`), recompile, and re-run with the same input — you should immediately hit row 2's crash next, which tells you the fix order is correct.
