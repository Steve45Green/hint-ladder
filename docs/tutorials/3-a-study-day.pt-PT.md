# 3. Um dia de estudo

*[English](3-a-study-day.md) · [Todos os tutoriais](README.pt-PT.md)*

**Tempo:** 15 a 30 minutos. **Precisas de:** a pasta de uma cadeira, do [Tutorial 2](2-set-up-your-course.pt-PT.md).

## O único comando a decorar

```bash
cd <curso>/<cadeira>
claude
```

```
/go
```

O `/go` vê onde estás (revisões pendentes, o próximo teste, ficheiros novos da aula) e começa uma coisa. O que costuma escolher, e o que também podes pedir diretamente:

| Situação | O `/go` começa | Ou escreve |
|---|---|---|
| Revisões para hoje | revisão espaçada: perguntas sobre o que aprendeste antes, respondidas de memória | `/exam drill` |
| PDF ou slides novos da aula na pasta | apontamentos com as páginas e perguntas de autoteste | `/analyze <ficheiro>` |
| Um tema que ainda não estudaste | uma aula de dez minutos no browser, com exercícios que se corrigem sozinhos | `/lesson <tema>` |
| Queres rever um tema | slides que se revelam passo a passo, com slides de autoteste | `/slides <tema>` |
| Um teste daqui a 14 dias ou menos | um exame simulado, com nota na tua escala | `/exam mock` |

## Uns 20 minutos típicos

1. `/go` → **5 min de revisões**: ele pergunta, tu respondes sem olhar, e cada cartão sobe ou desce (1, 3, 7, 14, 30 dias).
2. **10 min de matéria nova**: uma `/lesson`, ou `/slides` sobre o tema da aula de hoje.
3. **5 min**: uma pergunta para confirmares que te lembras do que acabaste de ver. Responde sem voltar atrás: é isso que fixa a matéria.

## Slides para rever

```
/slides árvores binárias de pesquisa
```

Escreve `slides/0001-….html` e diz-te como o abrir (duplo clique no ficheiro, ou abre-o por ti). No browser: → ou espaço para avançar, N para a explicação de cada slide, F para ecrã inteiro. Para imprimir ou ler em papel: imprimir para PDF, horizontal, sem margens, um slide por página.

Um real: [examples/…/slides/0001-bst.html](../../examples/algoritmos-e-estruturas-de-dados/slides/0001-bst.html) (descarrega-o e abre-o num browser).

![Visão geral de um baralho real feito pelo /slides](../assets/slides-bst.png)

## Onde fica tudo guardado

Na pasta da cadeira: `lessons/`, `slides/`, `records/` (os teus cartões de revisão), `material/` (apontamentos dos PDFs), `feedback/`. Não se perde nada quando fechas o Claude Code, e da próxima vez o `/go` continua a partir daí.

## Dicas

- Pergunta o que quiseres, por palavras tuas; não precisas de comando. "Não percebo apontadores para apontadores" funciona.
- A conversa ficou longa, lenta ou confusa? O `/compact` resume-a e continua.
- Queres guardar uma conversa importante? `/save-chat`.

A seguir: [4. Trabalhos avaliados](4-graded-work.pt-PT.md).
