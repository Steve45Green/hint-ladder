# Guia: como usar o Hint Ladder

*[English](GUIDE.md)*

Este guia é a referência: que comando para cada situação. Primeira vez? Os [tutoriais](tutorials/README.pt-PT.md) vão passo a passo, da instalação à rotina de cada semana.

## Começa aqui

Dois comandos:

```
/setup    uma vez: colas as unidades curriculares, ficas com uma pasta por cadeira ligada ao agente certo
/go       todos os dias: lê onde estás e arranca a skill ou o agente certo
```

E ainda:
- `/analyze`: sempre que recebes slides, PDFs, a ficha da UC ou exames antigos, transforma-os em apontamentos com páginas e perguntas de autoteste;
- `/slides`: revê um tema em slides que se revelam passo a passo, com slides de autoteste; numa apresentação avaliada dá o esqueleto, feedback e um ensaio, nunca o conteúdo;
- `/save-chat`: guarda uma conversa importante, com o link, na pasta da cadeira;
- `/progress`, uma vez por semana: revê o que fizeste (e o que os agentes te disseram) em todas as cadeiras e diz-te o que fazer a seguir;
- `/research`, logo a seguir ao `/progress`: para cada tema fraco, outras explicações, mais exemplos resolvidos e fontes verificadas.

A primeira semana:

| Dia | Faz |
|---|---|
| 1 | `/setup`: escolhe onde fica o curso (pasta no computador ou repositório privado no GitHub) e cola as unidades curriculares |
| 2 | Entra na pasta de uma cadeira (`cd <cadeira> && claude`), põe lá a ficha da UC e faz `/analyze` e depois `/course` |
| 3 | `/lesson` |
| 4 em diante | `/go` todos os dias, 15 minutos: manda-te para a revisão quando há revisões pendentes |
| Quando houver trabalho | `/go feedback idea` antes de começar; cola o enunciado; `/critique` antes de entregar; `/exam oral` antes da defesa |

Atalhos no terminal (`~/.bashrc` ou `~/.zshrc`):

```bash
alias cgo='claude "/go"'
alias cdrill='claude "/go drill"'
```

No PowerShell (`$PROFILE`): `function cgo { claude "/go" }`.

---

## Por tipo de cadeira

| Tipo de cadeira | Exemplos | O que mais conta |
|---|---|---|
| **Programação** | Introdução à Programação, POO, Estruturas de Dados, Engenharia de Software, Web, Dispositivos Móveis | O agente da linguagem (abre sozinho na pasta), `/critique`, feedback de código, `/exam oral` |
| **Bases de dados** | Bases de Dados 1 e 2, Sistemas de Informação | `sql-expert` no dialeto da tua escola; exercícios de "prever o resultado"; feedback de ideia no modelo ER |
| **Sistemas e redes** | Sistemas Operativos, Redes, Segurança, Administração de Sistemas | `linux-expert` (e `c-expert` em SO); laboratórios numa VM; `/lesson` para subnetting e processos |
| **Matemática e física** | Análise, Álgebra, Matemática Discreta, Estatística, Física | Sem agente: `/lesson` + `/exam drill` todos os dias + `/exam mock`. Estatística e métodos numéricos em Python → `python-expert` |
| **Interfaces** | Interação Pessoa-Computador | `web-expert`: heurísticas de usabilidade, acessibilidade, protótipos |
| **Projetos e estágio** | Projeto Integrado, Estágio, Projeto Final | Feedback de ideia antes de começar, feedback de processo todas as semanas, `/exam oral` antes da defesa |
| **Não técnicas** | Comunicação, Empreendedorismo, Regulação/Direito da Informática | `/lesson` + `/exam`; `/research` para regulamentos e fontes oficiais |

---

## Os agentes

Oito agentes de linguagem curados: `java-expert`, `c-expert`, `csharp-expert`, `python-expert`, `sql-expert`, `php-expert`, `web-expert`, `linux-expert`. E dois agentes de plataforma, `windows-expert` e `macos-expert`: o `/setup` escolhe o do teu computador, e é esse que trata de instalar e reparar as ferramentas ("javac não é reconhecido", o XAMPP não arranca, o PATH, o Homebrew). Para outra linguagem, o `/setup` gera um agente a partir de um modelo fixo, que fica em `.claude/agents/` na pasta do curso.

Cada agente tem:
- **Regras de estilo numeradas**, que segue em todo o código que escreve e cita no feedback (`STYLE-3`). As regras do docente têm prioridade e ficam registadas no `NOTES.md`.
- **Os comandos da linguagem** (compilador com avisos no máximo, testes, linter). Corre-os antes de afirmar seja o que for.
- **As regras do tutor**: em trabalho avaliado dá pistas e feedback, nunca a solução.

Três formas de os usar:
1. **Automático**: numa pasta criada pelo `/setup`, o `claude` já arranca com o agente da cadeira (`.claude/settings.json`).
2. **À mão**: `claude --agent java-expert` em qualquer pasta. Com aliases: `alias cjava='claude --agent java-expert'`.
3. **Delegação**: numa sessão normal, uma pergunta pontual ("explica este stack trace de Java") vai para o agente certo, ou fazes `/go` com a pergunta.

---

## Feedback: código, processo e ideia

| Pedes | Recebes |
|---|---|
| `/go feedback code` ou `/critique` | Tabela: gravidade, `ficheiro:linha`, problema, regra, pergunta (trabalho avaliado) ou correção (prática) |
| `/go feedback process` | Três coisas a manter e três a mudar, cada uma com a evidência (commits, testes, prazo), e o próximo passo |
| `/go feedback idea` | Veredicto `go`, `adjust` ou `rethink`, pontos fortes, riscos, até três perguntas, alternativas a conhecer |

---

## Receitas

| Situação | Escreve |
|---|---|
| Abri o Claude Code e não sei o que fazer | `/go` |
| Começo do semestre | `/setup` (ou `/setup` outra vez para atualizar as cadeiras ativas) |
| Trabalho prático para entregar | `/go feedback idea` → cola o enunciado → escreves tu → `/critique` → `/exam oral` |
| Teste na sexta | `/lesson <tema>` → `/go drill` todos os dias → `/exam mock` na véspera |
| O meu código dá erro (trabalho avaliado) | cola o erro: o agente guia-te sem corrigir por ti |
| Estou a trabalhar mal? | `/go feedback process` |
| Quero rever um tema em slides | `/slides <tema>` (ou `/slides lessons/0001-….html`) |
| Tenho de fazer uma apresentação avaliada | `/slides talk 10` com o enunciado: esqueleto, depois feedback aos teus slides, depois ensaio |
| Recebi slides ou um PDF da aula | `/analyze <ficheiro>` (ou `/analyze` para tudo o que ainda não leste) |
| Tenho exames antigos | põe-nos em `past-exams/` e faz `/analyze past-exams/`: dá-te os temas que mais saem |
| Quero guardar esta conversa | `/save-chat <link do chat>` |
| O Java, o XAMPP ou o SQL Server não funcionam no meu computador | `/go` + o erro: vai para o agente do teu sistema |
| Onde estou em cada cadeira? | `/progress` na pasta do curso (corre em segundo plano com várias cadeiras) |
| Uma cadeira nova este semestre, ou numa linguagem sem especialista | `/setup add <cadeira>`: entrevista-te (tipo de especialista, linguagem e versão, ferramentas, estilo, avaliação) e cria o especialista |
| Um docente publicou slides, um anúncio ou um prazo novo no Moodle | `/moodle`: descarrega e resume o que mudou, atualiza as datas no `MISSION.md` depois de perguntar e sugere um próximo passo; `/moodle watch` junta uma verificação de hora a hora com notificação no ambiente de trabalho, e cada sessão aberta no curso começa com as novidades |
| A tua escola usa Moodle | `/setup moodle`: entras uma vez com a tua chave do Moodle, no teu terminal; descarrega os ficheiros de cada cadeira para `material/moodle/` (fora do git) e traz os enunciados e as datas de entrega dos trabalhos |
| Não percebo um tema pelos slides; preciso de mais exemplos | `/research <tema>`, ou só `/research` para os temas fracos do último relatório |
| Relatório automático todas as semanas | agendar `claude -p "/progress"` com cron ou no Agendador de Tarefas (o comando exato está na skill; pergunta ao `/progress` como automatizar) |
| O docente publicou regras de uso de IA | guarda-as como `COURSE-POLICY.md` na pasta da cadeira |
| Sessão longa, respostas a piorar | `/compact` |

---

## Complementos e conflitos

Complementos opcionais que o `/go` usa quando estão instalados:
- `grilling` e `diagnosing-bugs` do [mattpocock/skills](https://github.com/mattpocock/skills). Se também instalaste o `research` dele, escreve `/hint-ladder:research` para usar o deste pack;
- [rtk](https://github.com/rtk-ai/rtk) (`rtk init -g`): comprime o output dos comandos e poupa tokens.

Cuidado com:
- **Plugins sempre ligados** que impõem "código primeiro, pouca explicação", como o [ponytail](https://github.com/dietrichgebert/ponytail): chocam com as pistas e as explicações do tutor. Desliga-os nas pastas do curso.
- **Skills que escrevem código sozinhas** em qualquer pedido de lógica (por exemplo, `test-driven-development` do addyosmani): em trabalho avaliado competem com o tutor.
- **Demasiadas skills automáticas.** O Claude Code reserva para a lista de skills 1% da janela de contexto (cerca de 8 000 caracteres numa janela de 200k). Acima disso encurta as descrições, e as skills disparam pior. O Hint Ladder só tem uma skill automática (`tutor`); confirma o total com `/context`.
- **Nomes repetidos**: o `code-review` do mattpocock tem o mesmo nome que o `/code-review` do Claude Code.
