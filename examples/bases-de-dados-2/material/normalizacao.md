# Normalização — aula03-normalizacao.pptx, slides 1–3

## Summary
Three slides covering the goal of normalisation and the ladder from 1NF to BCNF. Slide 1 states the goal: remove redundancy and update anomalies. Slide 2 gives the 1NF and 2NF conditions. Slide 3 gives 3NF and BCNF and one worked relation, `Aluno(Num, Nome, CodCurso, NomeCurso)`, but does not carry the example through to a solution — the deck stops at stating the definitions. This is a short review deck; it is not part of the four numbered items in `ficha-uc.pdf`'s programme (SQL avançado, procedimentos/triggers, transações, índices), so treat it as BD1 recap rather than new BD2 syllabus content.

## Key concepts
- **Normalização (normalisation)**: the goal is to eliminate redundancy and update anomalies (slide 1).
- **1FN (1NF)**: attributes are atomic; no repeating groups (slide 2).
- **2FN (2NF)**: relation is in 1NF and has no partial dependency on the key — every non-key attribute depends on the *whole* candidate key, not just part of it (slide 2). *(The "part of a composite key" phrasing is not spelled out on the slide; added for precision — not in the material.)*
- **3FN (3NF)**: relation is in 2NF and has no transitive dependency — no non-key attribute depends on another non-key attribute (slide 3).
- **BCNF**: every determinant (left side of a functional dependency) is a candidate key (slide 3).
- **Determinante (determinant)**: the left-hand side `X` of a functional dependency `X → Y` (slide 3, implied by the BCNF definition).

## Formulas and algorithms
No formal FD notation or algorithm is given on the slides (e.g. no closure `X⁺`, no synthesis/decomposition algorithm). The deck states each normal form as a condition in prose only (slides 2–3).

## Worked examples in the material
- Slide 3: `Aluno(Num, Nome, CodCurso, NomeCurso)` is given as *"Exemplo"* with no accompanying functional dependencies, no stated key, and no resolution shown. Reading it against the definitions just given: `Num` is the natural key (student number); `Num → Nome, CodCurso` holds, and `CodCurso → NomeCurso` also holds. Since `CodCurso` is not a candidate key of `Aluno`, `NomeCurso` depends transitively on `Num` through `CodCurso` — a 3NF violation, fixed by splitting off `Curso(CodCurso, NomeCurso)`. *(This resolution is not on the slide — it is the standard textbook reading of the example, added for completeness. Confirm the lecturer's intended FDs before treating it as the "official" answer, since the slide states no FDs explicitly.)*

## Where students go wrong
*(Not stated on the slides — flagging the standard mistakes for this ladder, not in the material)*
- Confusing 2NF's partial dependency with 3NF's transitive dependency — 2NF only matters when the key is composite; a relation with a single-attribute key is automatically in 2NF once it is in 1NF.
- Reading BCNF as "stricter 3NF" without checking it: BCNF can fail even when 3NF holds, when a determinant is not a candidate key but the dependent attribute happens to be part of some key (the classic overlapping-candidate-keys case).
- Stopping at "does a decomposition look 3NF" without checking the decomposition is lossless (join-preserving) — the slides do not mention lossless-join or dependency-preserving decomposition at all, so this is a gap to watch for in a fuller lecture or the textbook.

## Likely exam questions
1. Given a relation and a set of functional dependencies, identify the highest normal form it satisfies (1NF/2NF/3NF/BCNF) and justify with the specific dependency that violates the next form up.
2. Decompose `Aluno(Num, Nome, CodCurso, NomeCurso)` (or an equivalent relation) into BCNF/3NF, stating the resulting relations, their keys, and the foreign key that ties them together.
3. Define a normal form in one sentence and give a two-line counter-example that satisfies the lower form but violates it.

## Self-test
1. What is the stated goal of normalisation on slide 1?
2. A relation is in 1NF and has a single-attribute primary key. Is it automatically in 2NF? Why?
3. In `Aluno(Num, Nome, CodCurso, NomeCurso)` with `Num → Nome, CodCurso` and `CodCurso → NomeCurso`, which normal form is violated, and by which dependency?
4. State the BCNF condition in one sentence.

<details><summary>Answers</summary>

1. Eliminate redundancy and update anomalies (slide 1).
2. Yes — 2NF only forbids *partial* dependency on a composite key; with a single-attribute key there is no "part of the key" to depend on partially (slide 2, reasoned from the definition).
3. 3NF, violated by the transitive dependency `Num → CodCurso → NomeCurso` (slide 3, worked through above — not resolved on the slide itself).
4. Every determinant of every functional dependency in the relation is a candidate key (slide 3).

</details>

## Syllabus
`SYLLABUS.md` is not yet populated (still the placeholder from `/course`). This deck does not correspond to any of the 4 programme items in `ficha-uc.pdf` (SQL avançado, procedimentos/triggers, transações, índices) — it reads as Bases de Dados 1 review material. When `/course` populates `SYLLABUS.md`, add it as a prerequisite/review row, not as a weighted BD2 exam topic, unless the lecturer confirms it is examined again.
Glossary candidates: normalização, 1FN, 2FN, 3FN, BCNF, dependência funcional, determinante.
