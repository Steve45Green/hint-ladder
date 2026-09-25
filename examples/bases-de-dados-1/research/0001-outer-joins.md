# Outer joins (LEFT, RIGHT, FULL)

Why now: both active records on this topic (0007, 0008) are stuck in box 1 after two wrong reviews, and `reports/2026-09-25.md` flags it as the single risk item, with Test 1 in 12 days (2026-10-07) · Graded overlap: `assignments/tp1` (TP1: queries on the Library database, due 2026-10-09) asks three outer-join queries directly on the `Members`/`Books`/`Loans` schema, so every example and practice item below uses a different schema (`Employees`/`Departments`/`Timesheets`/`Budget`/`Spending`/`Suppliers`/`Contacts`) and a different question shape — none of them count child rows per parent including zero, none filter for parent rows that never match a child, and none check that every related child row satisfies a condition, which are TP1's three tasks · Sources checked on 2026-09-25 (no web access today; see Sources)

## In one paragraph

An outer join keeps rows from a table that an inner join would drop because they have no match on the other side, and fills the missing side's columns with `NULL`. `LEFT JOIN` preserves every row of the table written before it; `RIGHT JOIN` preserves every row of the table written after it (equivalent to swapping the two tables and using `LEFT JOIN`); `FULL OUTER JOIN` preserves rows from both sides regardless of match. Because unmatched rows carry `NULL` in the other table's columns, anything applied afterwards has to account for that `NULL` — a `WHERE` on the "preserved" NULLs turns the outer join back into an inner join by accident (SYLLABUS.md topic 3, `records/0007-left-join-where.md`), and `COUNT(*)` counts that NULL-filled row as one instead of zero (`records/0008-count-star-outer.md`).

## Three ways to see it

- **Formal**: `LEFT JOIN`/`RIGHT JOIN`/`FULL OUTER JOIN` in T-SQL (the course's DBMS per `MISSION.md`, "Tools: SQL Server 2022, SSMS") add rows with NULLs for the non-preserved side's columns whenever the `ON` condition finds no match, then any `WHERE` is evaluated *after* that — general T-SQL/ANSI SQL join behaviour, **not checked against a source today** (no web access; verify against the Microsoft Learn T-SQL join reference before Test 1, see Sources).
- **Picture**: trace a small `LEFT JOIN` by hand. `Employees(1,'Ana',10) (2,'Bo',NULL)` and `Departments(10,'Sales')`:
  ```
  Employees e          Departments d          LEFT JOIN result
  1 Ana  10      -->    10 Sales        -->    1 Ana  10 Sales
  2 Bo   NULL           (no row d=NULL)        2 Bo   NULL NULL   <- kept, filled with NULL
  ```
  An `INNER JOIN` on the same data would simply not produce Bo's row at all.
- **Analogy**: merging two office phone directories — headquarters and the branch office — into one sheet. An entry only in the headquarters list still gets a row, with the branch-only columns left blank, rather than being left off the merged sheet. The analogy stops working for `COUNT`: on paper you'd naturally not "count" a blank branch-office cell as an entry, but `COUNT(*)` in SQL counts the *row*, not the cell, so it happily counts that blank-filled row as one — which is exactly the trap in `records/0008-count-star-outer.md`.

## Worked examples, easy to exam level

### 1. Employees and their department, including the unassigned (easy)

Schema: `Employees(EmployeeId, Name, DepartmentId)`, `Departments(DepartmentId, DepartmentName)`.

Problem: list every employee's name with their department's name. Employees not yet assigned to a department must still appear, with `NULL` for the department name.

```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentId = d.DepartmentId;
```
*(not run — no SQL Server toolchain available in this session)*

Step by step:
1. `Employees` is the table whose rows must all survive, so it is the "preserved" side — it goes first, and the join is `LEFT JOIN`.
2. SQL Server keeps every `Employees` row even when `ON e.DepartmentId = d.DepartmentId` finds no match, filling `d.DepartmentName` with `NULL`.
3. There is no `WHERE` yet, so nothing can undo the `LEFT JOIN` here — that trap comes in example 2.

Usual mistake at this step: writing `JOIN` (inner) out of habit, which silently drops unassigned employees; the query still runs and looks fine until someone checks the row count against `Employees` alone.

Follow-up question (targets the `COUNT(*)` misconception without grouping): does `COUNT(*)` equal `COUNT(d.DepartmentName)` over this result? No — `COUNT(*)` counts every row, including the NULL-filled ones for unassigned employees; `COUNT(d.DepartmentName)` only counts rows where a department was actually matched, so it is smaller whenever anyone is unassigned.

### 2. Fixing a WHERE that undoes a LEFT JOIN (medium)

Schema: `Employees(EmployeeId, Name)`, `Timesheets(TimesheetId, EmployeeId, WorkDate, Hours)`.

Problem: list every employee and, if they logged hours in the week of 2026-09-21 to 2026-09-25, the `WorkDate` and `Hours`. Employees who logged nothing that week must still appear once, with `NULL` hours. A draft query returns the wrong result:

```sql
-- draft (wrong)
SELECT e.Name, t.WorkDate, t.Hours
FROM Employees e
LEFT JOIN Timesheets t ON e.EmployeeId = t.EmployeeId
WHERE t.WorkDate BETWEEN '2026-09-21' AND '2026-09-25';
```

Why it's wrong: for an employee with no timesheet that week, `t.WorkDate` is `NULL`, and `NULL BETWEEN '2026-09-21' AND '2026-09-25'` evaluates to `UNKNOWN`, not `TRUE`, so `WHERE` drops that row — the exact misconception in `records/0007-left-join-where.md`: a condition on the right-hand table's column, left in `WHERE`, turns the `LEFT JOIN` back into an inner join.

```sql
-- fixed
SELECT e.Name, t.WorkDate, t.Hours
FROM Employees e
LEFT JOIN Timesheets t
  ON e.EmployeeId = t.EmployeeId
  AND t.WorkDate BETWEEN '2026-09-21' AND '2026-09-25';
```
*(not run — no SQL Server toolchain available in this session)*

Step by step:
1. Move the date condition into `ON` so it only restricts which `Timesheets` rows are allowed to *match*, not which `Employees` rows *survive*.
2. Now an employee with no timesheet in range still appears once, with `NULL` `WorkDate`/`Hours`.
3. Contrast: if the task had instead been "only employees who logged hours that week" (an inner-join-shaped requirement), the original `WHERE`-based version would have been the correct one — the fix depends on what should happen to the unmatched rows, not on a blanket "conditions go in ON" rule.

Usual mistake at this step: over-correcting and moving *every* condition into `ON`, even ones that really were meant to filter out unmatched rows.

### 3. Reconciling two independent snapshots with FULL OUTER JOIN (exam level)

Schema: `Budget(DepartmentId, DepartmentName, BudgetAmount)`, `Spending(DepartmentId, SpentAmount)` — two exports from different systems that can be out of sync. No past exam file is on record for this unit (`material/past-exam-*` not found), so this follows a typical exam-style reconciliation question rather than a specific past paper.

Problem: produce one row per department appearing in *either* snapshot, with `DepartmentName`, `BudgetAmount`, `SpentAmount`, `Variance` (`BudgetAmount − SpentAmount`), and a `Status` of `'no spending recorded'`, `'unbudgeted spending'`, or `'reconciled'`.

```sql
SELECT
    COALESCE(b.DepartmentId, s.DepartmentId) AS DepartmentId,
    b.DepartmentName,
    b.BudgetAmount,
    s.SpentAmount,
    b.BudgetAmount - s.SpentAmount AS Variance,
    CASE
        WHEN s.DepartmentId IS NULL THEN 'no spending recorded'
        WHEN b.DepartmentId IS NULL THEN 'unbudgeted spending'
        ELSE 'reconciled'
    END AS Status
FROM Budget b
FULL OUTER JOIN Spending s ON b.DepartmentId = s.DepartmentId;
```
*(not run — no SQL Server toolchain available in this session)*

Step by step, with the mistake each step guards against:
1. Neither table's rows may be dropped, so the join must be `FULL OUTER JOIN` — using `LEFT JOIN Spending s` out of habit would silently lose departments that only exist in `Spending`.
2. On a `FULL OUTER JOIN`, the join key itself can be `NULL` on either side, so the row's identifying `DepartmentId` must be `COALESCE`d from both sides — forgetting this (unlike with `LEFT`/`RIGHT`, where one side's key is always present) leaves `NULL` department IDs on every unmatched row.
3. `BudgetAmount - SpentAmount` propagates `NULL` whenever either side is missing — that is the *correct* variance for an unbudgeted or unspent department, not a bug to "fix" with `COALESCE(..., 0)` unless the task actually wants zero-filled arithmetic.
4. The `CASE` reads `IS NULL` on each side the same way a single-direction anti-join `WHERE` would, but does it for both directions in one pass.

## Common mistakes

| Mistake | Why it happens | How to spot it in your own work |
|---|---|---|
| A `WHERE` on the outer-joined (right) table's column drops the rows the outer join was meant to keep | `NULL <comparison> value` is `UNKNOWN`, not `TRUE`, so `WHERE` silently removes it; the join and the filter are read as one step instead of two | Row count with the filter is suspiciously close to (or equal to) an `INNER JOIN`'s; ask "does this condition decide *matching* or *keeping*?" |
| `COUNT(*)` reports 1 for a row with no match instead of 0 | The preserved row exists once, fully populated with `NULL`s, so `COUNT(*)` — which counts rows, not values — counts it | Totals are off by exactly the number of unmatched rows; switch to `COUNT(<a column that is NULL on unmatched rows>)` and compare |
| Comparing an outer-joined column with `= NULL` instead of `IS NULL` | Habit carried over from other languages where `== null`/`== None` works | The condition is always false (or always unknown) no matter what; SSMS/most linters flag `= NULL` as suspicious |
| Swapping table order when converting `RIGHT JOIN` to `LEFT JOIN` (or vice versa) without swapping which table is "preserved" | The rule "swap the tables, swap LEFT/RIGHT" is memorised as a syntax trick rather than understood as "same preserved table, same result" | Compare row counts before and after rewriting; they must match exactly |
| On a `FULL OUTER JOIN`, using one side's join-key column downstream (e.g. in `GROUP BY` or `SELECT`) assuming it is never `NULL` | Habit from `LEFT`/`RIGHT` joins, where the preserved side's key is always present | Check whether any row has `NULL` in *both* sides' keys before and after `COALESCE` |

## Practice (answers hidden)

1. Write a query listing every employee's `Name` and the `WorkDate` of each timesheet they logged (`Employees`/`Timesheets` as above), including employees with none — `NULL` `WorkDate` for them.
   <details><summary>Answer</summary>

   ```sql
   SELECT e.Name, t.WorkDate
   FROM Employees e
   LEFT JOIN Timesheets t ON e.EmployeeId = t.EmployeeId;
   ```
   `Employees` must be the preserved (left) side because every employee has to appear, matched or not.
   </details>

2. A colleague wrote, wanting "every employee, with department name when known, NULL otherwise":
   ```sql
   SELECT e.Name, d.DepartmentName
   FROM Employees e
   LEFT JOIN Departments d ON e.DepartmentId = d.DepartmentId
   WHERE d.DepartmentName IS NOT NULL;
   ```
   It drops unassigned employees. What's wrong, and how do you fix it?
   <details><summary>Answer</summary>

   The `WHERE d.DepartmentName IS NOT NULL` filters out exactly the rows the `LEFT JOIN` was keeping — every unassigned employee has `NULL` there by construction. Remove the `WHERE` clause entirely; there is nothing left to filter, since "department name when known, else NULL" is already what the bare `LEFT JOIN` produces.
   </details>

3. Rewrite this `RIGHT JOIN` as an equivalent `LEFT JOIN` (swap the table order, keep the same preserved rows and result):
   ```sql
   SELECT t.WorkDate, e.Name
   FROM Timesheets t
   RIGHT JOIN Employees e ON t.EmployeeId = e.EmployeeId;
   ```
   <details><summary>Answer</summary>

   ```sql
   SELECT t.WorkDate, e.Name
   FROM Employees e
   LEFT JOIN Timesheets t ON e.EmployeeId = t.EmployeeId;
   ```
   `RIGHT JOIN` preserves the table written *after* it (`Employees`); swapping to `LEFT JOIN` means `Employees` must now be written *before* `Timesheets` for the same rows to survive.
   </details>

4. For employee Dana, who has never logged a timesheet:
   ```sql
   SELECT COUNT(*), COUNT(t.TimesheetId)
   FROM Employees e
   LEFT JOIN Timesheets t ON e.EmployeeId = t.EmployeeId
   WHERE e.Name = 'Dana';
   ```
   What does each `COUNT` return, and why are they different?
   <details><summary>Answer</summary>

   `COUNT(*)` returns 1: the `LEFT JOIN` still produces exactly one row for Dana, with `t.TimesheetId` set to `NULL`. `COUNT(t.TimesheetId)` returns 0: `COUNT(<column>)` ignores `NULL`s, and Dana's row has `NULL` there. This is the general rule behind `records/0008-count-star-outer.md` — to count *matches*, count a column that is `NULL` exactly on unmatched rows, never `*`.
   </details>

5. Two exports keyed by `SupplierId`: `Suppliers(SupplierId, SupplierName)` from the purchasing system and `Contacts(SupplierId, Email)` from the CRM, maintained by a different team and sometimes out of sync. Write a query listing every `SupplierId` that appears in exactly one of the two exports, together with which export it came from.
   <details><summary>Answer</summary>

   ```sql
   SELECT
       COALESCE(s.SupplierId, c.SupplierId) AS SupplierId,
       CASE WHEN c.SupplierId IS NULL THEN 'Suppliers only'
            ELSE 'Contacts only' END AS OnlyIn
   FROM Suppliers s
   FULL OUTER JOIN Contacts c ON s.SupplierId = c.SupplierId
   WHERE s.SupplierId IS NULL OR c.SupplierId IS NULL;
   ```
   `FULL OUTER JOIN` is needed because a mismatch can happen in either direction; the `WHERE` here is safe (doesn't undo the join) because it only excludes rows that matched on *both* sides, which is exactly "appears in both", not "unmatched on the right".
   </details>

6. `Employees` has a self-referencing `ManagerId` column (`NULL` for the one employee with no manager). Write a query listing every employee's `Name` alongside their manager's `Name`, with `NULL` when they have none.
   <details><summary>Answer</summary>

   ```sql
   SELECT e.Name AS EmployeeName, m.Name AS ManagerName
   FROM Employees e
   LEFT JOIN Employees m ON e.ManagerId = m.EmployeeId;
   ```
   This is a self-join: `Employees` is joined to itself under two aliases, `e` for "the employee row" and `m` for "the row that is their manager". `LEFT JOIN` is required because the top-level employee has `ManagerId = NULL`, so an `INNER JOIN` version would silently drop that one employee entirely.
   </details>

## Sources

| Source | Where | Used for | Checked |
|---|---|---|---|
| `SYLLABUS.md` (this workspace) | row 3, "Outer joins (LEFT, RIGHT, FULL)", high weight, status `seen` | Topic scope and weight | Opened 2026-09-25 |
| `MISSION.md` (this workspace) | Assessment table; Tools line | Test 1 date/weight (2026-10-07, 30%); DBMS is SQL Server 2022 → examples use T-SQL | Opened 2026-09-25 |
| `records/0007-left-join-where.md` (this workspace) | Full record | The WHERE-undoes-LEFT-JOIN misconception behind example 2 and practice 2 | Opened 2026-09-25 |
| `records/0008-count-star-outer.md` (this workspace) | Full record | The `COUNT(*)` misconception behind the example 1 follow-up and practice 4 | Opened 2026-09-25 |
| `reports/2026-09-25.md` (this workspace) | Risks section | Evidence that outer joins is the current risk topic | Opened 2026-09-25 |
| `assignments/tp1/STATEMENT.md` (this workspace) | Full statement | Identifying the graded overlap and the three question shapes to avoid | Opened 2026-09-25 |
| T-SQL `LEFT`/`RIGHT`/`FULL OUTER JOIN` syntax and NULL-comparison semantics | general knowledge (would normally be Microsoft Learn's T-SQL `FROM`/join reference) | Formal definition, all worked-example syntax | **Not checked against a source** — no web access this session; verify against the official T-SQL reference before Test 1 |
