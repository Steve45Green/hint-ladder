---
topic: 3
box: 1
next: 2026-09-26
status: active
---
# Misconceção: um WHERE sobre uma coluna da tabela da direita transforma o LEFT JOIN numa junção interna

O aluno filtrou `WHERE e.Estado = 'aberta'` depois de um LEFT JOIN e perdeu as linhas sem encomendas.

## Pergunta
Porque é que uma condição no WHERE sobre a tabela da direita pode eliminar linhas que o LEFT JOIN manteve?

## Resposta
As linhas sem correspondência têm NULL nessa coluna, e NULL = 'aberta' não é verdadeiro, por isso o WHERE descarta-as; a condição vai para o ON.
