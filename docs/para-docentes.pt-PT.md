# Hint Ladder para docentes

*[English](for-lecturers.md)*

Os alunos já usam IA. O Hint Ladder é um tutor de IA para o Claude Code feito para os fazer aprender: em trabalho avaliado **ensina e dá feedback, mas não escreve a solução**, a não ser que a política da cadeira diga o contrário.

## O que faz em trabalho avaliado

| O aluno pede | O Hint Ladder faz |
|---|---|
| "Escreve-me o código do trabalho" | Sobe uma escada de pistas: pede ao aluno que reformule o enunciado, nomeia o conceito, resolve um problema *diferente* análogo, dá um esqueleto com lacunas e depois revê a tentativa do próprio aluno. Não passa daí. |
| "Porque é que o meu código rebenta?" | Feedback de código: gravidade, `ficheiro:linha`, problema, regra quebrada e uma **pergunta** que leva à correção. Sem código corrigido. |
| "A minha ideia de projeto é boa?" | Um veredicto `go / adjust / rethink`, riscos e perguntas. Não desenha o projeto por eles. |
| Antes da defesa oral | Uma defesa simulada que questiona cada módulo e cada decisão de desenho. |

Cada ajuda em trabalho avaliado fica registada em `assignments/<trabalho>/AI-USE.md`, com a data e o degrau da escada atingido, para o aluno declarar o uso de IA com honestidade.

## Definir as regras da cadeira

Publique um `COURSE-POLICY.md` ([modelo](COURSE-POLICY.template.md)) na página da cadeira; os alunos põem-no na pasta da cadeira. Tem prioridade sobre qualquer outra definição:

- **Sem IA nenhuma** nos trabalhos avaliados: o tutor só explica conceitos gerais com exemplos próprios.
- **Só pistas** (o comportamento por defeito).
- **Código gerado por IA permitido com declaração**: o tutor ajuda por completo e mantém o registo.
- **As suas regras de estilo**: substituem as do agente da linguagem e são citadas no feedback.

## Provas

O repositório tem uma suite de avaliação que corre cada caso com e sem o plugin, no mesmo modelo. Os resultados mais recentes, com o método e o custo, estão em [evals/RESULTS.md](../evals/RESULTS.md).

## Limites, com honestidade

- O Hint Ladder apoia quem quer aprender. Um aluno decidido a copiar pode usar um chatbot simples; a defesa oral e o trabalho em aula continuam a ser as verificações mais fortes.
- O `AI-USE.md` é escrito pela ferramenta no computador do aluno: ajuda a declarar, não é prova à prova de adulteração.
- O `COURSE-POLICY.md` é seguido tal como está escrito; é o aluno que o coloca na pasta.

## Privacidade

Tudo corre no computador do aluno, nas pastas dele. O plugin não tem telemetria e não envia nada aos docentes nem ao projeto. Quando um aluno liga o Moodle, os seus ficheiros são descarregados só para o computador dele, com o acesso dele, para uma pasta que fica fora do git; nada é republicado.

## Sugestões

Diga-nos o que o tornaria útil na sua cadeira: [abra uma issue](https://github.com/Steve45Green/hint-ladder/issues).
