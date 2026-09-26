#!/usr/bin/env bash
set -euo pipefail
cat > MISSION.md <<'MD'
# Mission: Algoritmos e Estruturas de Dados (1.º ano, 2.º semestre, 6 ECTS)

Language: Portuguese (Portugal)

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| Trabalho Prático 2 (individual, com defesa oral) | 25% | 2026-11-20 | — |
| Exame (época normal) | 75% | 2027-01-20 | 9.5 |

## AI policy
A IA pode ser usada para estudar; o código e o relatório entregues são escritos pelo aluno.
MD
mkdir -p assignments/tp2
cat > assignments/tp2/STATEMENT.md <<'MD'
# Trabalho Prático 2: lista ligada genérica

Entrega: 2026-11-20 pelo Moodle. Cotação: 5 valores. Defesa oral obrigatória.

Implemente em Java `ListaLigada<T>` com `add(T x)`, `remove(int index)` e `reverse()` (no próprio sítio).

Relatório (2 a 4 páginas, PDF, 25% da nota do trabalho), com as secções: introdução, decisões de
implementação, complexidade de cada método (justificada), testes realizados e conclusões.
Referências no estilo IEEE. Declaração de uso de IA em anexo.
MD
cat > assignments/tp2/ListaLigada.java <<'JAVA'
public class ListaLigada<T> {
    private static class No<T> {
        T valor;
        No<T> seguinte;
        No(T valor) { this.valor = valor; }
    }

    private No<T> cabeca;
    private int tamanho;

    public void add(T x) {
        No<T> novo = new No<>(x);
        if (cabeca == null) {
            cabeca = novo;
        } else {
            No<T> atual = cabeca;
            while (atual.seguinte != null) {
                atual = atual.seguinte;
            }
            atual.seguinte = novo;
        }
        tamanho++;
    }
}
JAVA
cat > assignments/tp2/AI-USE.md <<'MD'
# AI use: TP2

2026-11-02 · rung 2 · Named the technique for reverse (three pointers) and pointed to the week 5 slides.
MD
