---
topic: 3
box: 1
next: 2026-09-26
status: active
---
# Misconceção: COUNT(*) depois de um LEFT JOIN conta 1 para linhas sem correspondência

## Pergunta
Depois de um LEFT JOIN, porque é que COUNT(*) dá 1 em vez de 0 para uma linha sem correspondência, e o que se conta em vez disso?

## Resposta
A linha preservada existe uma vez, com NULLs; conta-se uma coluna da tabela da direita, por exemplo COUNT(e.EncomendaId).
