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
A IA pode ser usada para estudar; o código entregue tem de ser escrito pelo aluno (ficha da UC, secção Avaliação).

## Tools
Java 21; language agent: java-expert
MD
mkdir -p assignments/tp2
cat > assignments/tp2/STATEMENT.md <<'MD'
# Trabalho Prático 2: lista ligada genérica

Entrega: 2026-11-20 pelo Moodle. Cotação: 5 valores. Defesa oral obrigatória.

Implemente em Java uma lista simplesmente ligada genérica `ListaLigada<T>` com os métodos
`add(T x)` (no fim), `remove(int index)` (devolve o elemento removido; `IndexOutOfBoundsException`
fora dos limites) e `reverse()` (inverte a lista no próprio sítio, sem criar nós novos).
MD
cat >> assignments/tp2/STATEMENT.md <<'MD'

Relatório (2 a 4 páginas, 25% da nota do trabalho): introdução, decisões de implementação, complexidade de cada método, testes realizados e conclusões.
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
