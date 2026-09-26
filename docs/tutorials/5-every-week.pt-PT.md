# 5. Todas as semanas: `/progress` e depois `/research`

*[English](5-every-week.md) · [Todos os tutoriais](README.pt-PT.md)*

**Tempo:** 20 minutos, uma vez por semana (domingo à noite funciona bem). **Precisas de:** alguns dias de uso em pelo menos uma cadeira.

## Passo 1: `/progress`, onde estás

Na pasta do curso (a que tem o `CURRICULUM.md`, acima das cadeiras):

```bash
cd ~/Documents/engenharia-informatica
claude
```

```
/progress
```

Com várias cadeiras lê-as em paralelo, em segundo plano, e podes continuar a trabalhar. Escreve `reports/<data>.md`:

- uma tabela com todas as cadeiras: **em dia**, **em risco** ou **atrasada**, a próxima avaliação e os dias que faltam, temas dominados / vistos / por fazer, revisões pendentes;
- **Vitórias** e **Riscos**, cada um com a prova ("os dois cartões de outer joins voltaram à caixa 1; Teste 1 daqui a 12 dias");
- o feedback que recebeste e se já agiste sobre ele;
- o uso de IA no período, pronto para a declaração;
- **três próximas ações**, como comandos que podes escrever.

Não altera nada além desse relatório. Se a pasta for um repositório git, oferece-se para guardar o trabalho da semana (um commit).

## Passo 2: `/research`, corrigir os temas fracos

Logo a seguir, no mesmo sítio:

```
/research
```

Vai buscar ao relatório os temas fracos (os riscos, os cartões que falhas sempre, o mesmo erro em vários feedbacks), até três, e escreve um pacote de estudo por tema em `research/`:

- porquê este tema agora (a prova);
- a ideia num parágrafo, depois de três ângulos: formal, um desenho, uma analogia;
- **exemplos resolvidos do fácil ao nível de exame**, passo a passo, com o erro habitual em cada passo;
- uma tabela de erros comuns e como os apanhar no teu próprio trabalho;
- **exercícios com a resposta escondida**;
- fontes que abriu e verificou: primeiro a matéria da cadeira, depois documentação oficial e cursos abertos de universidades.

Se houver um trabalho avaliado aberto sobre o mesmo tema, os exemplos são de outro problema, com outra pergunta (o degrau 3 do tutor): nada no pacote é a resposta do teu trabalho, nem mudando os nomes.

Também podes indicar o tema: `/research outer joins`.

## Passo 3: Passar à prática

A resposta acaba com o comando seguinte, por exemplo:

```
/slides research/0001-outer-joins.md     slides para rever o pacote
/lesson outer joins                      exercícios com feedback imediato
/exam drill                              as revisões da semana
```

## Passo 4: As próximas semanas, com o `/plan`

No início do semestre e sempre que uma data muda, o `/plan` junta todas as avaliações com data de todas as cadeiras ativas (de cada `MISSION.md` e, se estiver ligado, do Moodle), assinala as semanas em que se acumulam, pergunta pelas datas ainda por confirmar e escreve `plan/<data>.md`: uma tabela semana a semana até ao fim da época de exames, com blocos de estudo pesados pelo valor de cada avaliação. O `plan/calendar.ics` importa-se no Google, no Outlook ou no Calendário da Apple, com um aviso três dias antes de cada uma.

## Relatório semanal automático (opcional)

O `/progress` pode correr sozinho todas as semanas, sem abrires o Claude Code. Pergunta-lhe: "como automatizo este relatório?" Ele mostra a linha exata para o teu sistema (cron no macOS e Linux, Agendador de Tarefas no Windows).

Algo não funciona? [Resolução de problemas](troubleshooting.pt-PT.md).
