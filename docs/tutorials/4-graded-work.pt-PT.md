# 4. Trabalhos avaliados: o que faz e o que não faz

*[English](4-graded-work.md) · [Todos os tutoriais](README.pt-PT.md)*

**Tempo:** 10 minutos a ler, depois em cada trabalho. **Para:** trabalhos práticos, projetos, relatórios, fichas e apresentações que contam para a nota.

## A regra

No que é avaliado, o Hint Ladder **ensina e revê; quem escreve és tu**. Nunca entrega a solução avaliada, mesmo que insistas, porque vais defendê-la sozinho na oral e vais encontrar o mesmo tema no exame. Di-lo numa linha e oferece a pista seguinte.

Deteta sozinho o que é avaliado: um enunciado com data de entrega ou cotação, um ficheiro em `assignments/`, ou palavras como "trabalho prático", "projeto", "TP". Na dúvida faz uma pergunta: "Isto conta para a nota?"

## A escada de pistas

Sobe um degrau de cada vez, só quando já tentaste e continuas encravado:

| Degrau | O que recebes |
|---|---|
| 1. Reformular | explicas o enunciado por palavras tuas; ele aponta o que leste mal |
| 2. Conceito | o nome da técnica e onde está na matéria da cadeira |
| 3. Exemplo análogo | um problema *diferente*, resolvido por inteiro com a mesma técnica |
| 4. Esqueleto | a estrutura do teu problema, com lacunas `___` em tudo o que é avaliado |
| 5. Revisão | tu escreves; ele dá feedback e faz perguntas |

Não há degrau 6.

## Um trabalho típico

1. **Põe o enunciado na pasta da cadeira**: `assignments/tp2/STATEMENT.md` (ou o PDF lá dentro, e depois `/analyze`).
2. **Antes de começar**: `/go feedback idea`, e descreve o teu plano. Recebes um veredicto (avançar, ajustar ou repensar), os riscos e até três perguntas.
3. **Enquanto trabalhas**: pergunta quando encravares. Conta com pistas e perguntas, não com código.
4. **Antes de entregar**: `/critique`. Compila e corre o teu código com as opções mais exigentes e depois dá uma tabela de problemas, cada um com uma pergunta e a regra de estilo que falha.
5. **Antes da defesa**: `/exam oral`. Uma defesa oral simulada: pergunta o que um júri perguntaria sobre o *teu* código.

Numa **apresentação avaliada**: `/slides talk 10` (10 = minutos) dá um esqueleto com lacunas e um plano de tempos; depois de fazeres os teus slides, dá feedback e ensaia contigo as perguntas. Não escreve o conteúdo dos slides.

## O registo de uso de IA

Cada ajuda num trabalho avaliado fica em `assignments/<nome>/AI-USE.md`, com a data e o degrau:

```
2026-10-12 · rung 2 · Identified the problem as breadth-first search; pointed to CLRS ch. 22.
2026-10-14 · rung 5 · Critique of queue.c: 3 problems pointed out, no code provided.
```

Quando o docente pedir a declaração de uso de IA, copias daí.

## Quando as regras são outras

- **O docente publicou regras para a IA** (um `COURSE-POLICY.md` na pasta): o Hint Ladder segue-as à letra, acima de tudo o resto. Os docentes podem usar [este modelo](../COURSE-POLICY.template.md).
- **A cadeira proíbe IA**: explica conceitos gerais com exemplos próprios, diferentes do trabalho, e diz porquê.
- **A cadeira permite código gerado por IA** (escrito no `COURSE-POLICY.md` ou confirmado no `MISSION.md`): segue essa regra e mantém o registo.

A seguir: [5. Todas as semanas](5-every-week.pt-PT.md).
