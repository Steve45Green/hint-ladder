# Process feedback — TP1 (2026-09-25)

Reviewed: `assignments/tp1/bissec.py`, `assignments/tp1/.git`

## Keep
1. The work is committed to git rather than left as a loose file, so there's at least a
   record of the final state to point to (evidence: `.git/logs/HEAD` shows 2 commits,
   final ref `64cd6e8`).

## Change
1. Both commits — `wip` and `final version` — carry the *exact same* timestamp,
   2026-09-25 11:02:47 UTC (evidence: `.git/logs/HEAD`). That's not incremental
   history; it's one write-up committed twice in the same second. At the oral defence,
   if asked "walk me through how this evolved," this history gives nothing to point to.
   Commit as you go — after bisection works on one test case, after you add a
   tolerance, after you handle an edge case.
2. There is no test, no `if __name__ == "__main__":` block, and no other file in
   `assignments/tp1` (evidence: directory listing shows only `bissec.py`). Nothing
   suggests `bissecao` has ever actually been called and its output inspected. That
   matters for a numerical method with a loop and a floating-point stopping condition:
   "looks right" and "terminates with an acceptably accurate answer" are different
   claims, and only running it against a known case tells them apart.

**Next step:** Add a small runnable block that calls `bissecao` on a case where the
root is already known (e.g. `f`, with `a=0, b=2`), run it, and watch what actually
happens before changing anything else. Commit that as its own step.

Note: script was not executed in this session (running it required an approval not
available here); feedback is based on reading the code and git history only.
