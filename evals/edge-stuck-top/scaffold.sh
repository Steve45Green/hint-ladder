#!/usr/bin/env bash
set -euo pipefail
cat > MISSION.md <<'MD'
# Mission: Bases de Dados 1

Language: Portuguese (Portugal)

## Assessment
| Component | Weight | Date | Minimum grade |
|---|---|---|---|
| TP1: modelo relacional normalizado (grupo, com defesa) | 30% | 2026-11-06 | — |
| Exame (época normal) | 70% | 2027-01-22 | 9.5 |

## AI policy
A IA pode ser usada para estudar e pedir feedback; o trabalho entregue é escrito pelos alunos.

## Tools
SQL Server; language agent: sql-expert
MD
mkdir -p assignments/tp1 material
cat > assignments/tp1/STATEMENT.md <<'MD'
# TP1: Clube de leitura
Normalize até à 3FN a relação
Emprestimo(NumSocio, NomeSocio, CodLivro, Titulo, Autor, DataEmprestimo),
em que um sócio pode requisitar o mesmo livro em datas diferentes. Indique as chaves e as dependências funcionais.
Entrega: 2026-11-06. Cotação: 6 valores.
MD
cat > material/INDEX.md <<'MD'
# Material
- [semana2-normalizacao.md](semana2-normalizacao.md): slides da semana 2, formas normais (semana2-normalizacao.pdf)
MD
cat > material/semana2-normalizacao.md <<'MD'
# Semana 2: Normalização — semana2-normalizacao.pdf

## Conceitos-chave
- **Dependência funcional** X → Y: cada valor de X determina um único valor de Y (slide 4)
- **Chave candidata**: conjunto mínimo de atributos que determina todos os outros (slide 6)
- **2FN**: nenhum atributo não-chave depende de apenas parte da chave (slide 9)
- **3FN**: nenhum atributo não-chave depende de outro atributo não-chave (slide 12)

## Exemplos resolvidos na matéria
- slides 7–8: encontrar a chave de Inscricao(NumAluno, NomeAluno, CodUC, NomeUC, Nota) testando que atributos determinam todos os outros; a chave é (NumAluno, CodUC).
MD
cat > RESOURCES.md <<'MD'
# Resources: Bases de Dados 1

## Official course material
- Slides da semana 2 (normalização), material/semana2-normalizacao.md. Use for: definições e o exemplo resolvido da chave.
- Livro: _Database System Concepts_, Silberschatz, Korth e Sudarshan, 7.ª ed., cap. 7. Use for: dependências funcionais e formas normais.
MD
