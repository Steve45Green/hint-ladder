# Semana 2: Normalização — semana2-normalizacao.pdf, p. 1

## Resumo
Apresenta as três primeiras formas normais (1FN, 2FN, 3FN) com as respetivas definições e um exemplo de dependência transitiva que viola a 3FN, resolvido por decomposição em duas relações.

## Conceitos-chave
- **1FN**: todos os atributos são atómicos, sem grupos repetidos (p. 1)
- **2FN**: cumpre a 1FN e nenhum atributo não-chave depende de apenas parte da chave (p. 1)
- **3FN**: cumpre a 2FN e nenhum atributo não-chave depende de outro atributo não-chave (dependência transitiva) (p. 1)

## Fórmulas e algoritmos
Sem fórmulas; definições apresentadas em texto (p. 1).

## Exemplos resolvidos na matéria
- p. 1: `Encomenda(NumEnc, NumCliente, NomeCliente, Data)` viola a 3FN porque `NomeCliente` depende de `NumCliente` (dependência transitiva de um atributo não-chave). Solução: decompor em `Cliente(NumCliente, NomeCliente)` e `Encomenda(NumEnc, NumCliente, Data)`.

## Onde os alunos costumam errar
- Confundir dependência transitiva (viola 3FN) com dependência parcial da chave (viola 2FN) *(not in the material)*

## Perguntas prováveis de exame
1. Dado um esquema de relação, identificar a forma normal mais alta que cumpre e justificar.
2. Decompor uma relação que viola a 3FN, indicando as chaves primárias e estrangeiras resultantes.

## Autoavaliação
1. Que forma normal exige que todos os atributos sejam atómicos?
2. Porque é que `Encomenda(NumEnc, NumCliente, NomeCliente, Data)` viola a 3FN?
3. Depois de decompor o exemplo da matéria, qual é a chave estrangeira em `Encomenda`?

<details><summary>Respostas</summary>

1. 1FN (p. 1)
2. Porque `NomeCliente` depende de `NumCliente`, que não é a chave primária de `Encomenda` — dependência transitiva entre atributos não-chave (p. 1)
3. `NumCliente` (p. 1)
</details>

## Programa
Cobre um tema ainda não listado em SYLLABUS.md (normalização/formas normais) — a confirmar com o aluno se deve ser acrescentado. Termos candidatos a glossário: 1FN, 2FN, 3FN, dependência transitiva.
