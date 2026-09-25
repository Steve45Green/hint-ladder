<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.svg">
    <img src="docs/assets/banner-light.svg" alt="CS Tutor — o tutor de IA para alunos de Engenharia Informática. Ensina-te, dá-te feedback e nunca te faz o trabalho avaliado." width="100%">
  </picture>
</p>

<p align="center">
  <!-- Badge de CI: voltar a pôr quando o repositório for público e se chamar cs-tutor (docs/launch.md, passo 3):
  <a href="https://github.com/Steve45Green/cs-tutor/actions/workflows/ci.yml"><img src="https://github.com/Steve45Green/cs-tutor/actions/workflows/ci.yml/badge.svg" alt="CI"></a> -->
  <a href="LICENSE"><img src="https://img.shields.io/badge/licen%C3%A7a-MIT-blue" alt="Licença MIT"></a>
  <img src="https://img.shields.io/badge/vers%C3%A3o-0.6.0-informational" alt="Versão 0.6.0">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-d97757" alt="Plugin do Claude Code">
  <a href="evals/RESULTS.md"><img src="https://img.shields.io/badge/evals-com%20vs%20sem-8a63d2" alt="Evals"></a>
</p>

<p align="center">
  <b><a href="README.md">English</a></b> ·
  <b><a href="docs/tutorials/README.pt-PT.md">Tutoriais</a></b> ·
  <b><a href="https://steve45green.github.io/cs-tutor/">Demos ao vivo</a></b> ·
  <a href="docs/GUIA.pt-PT.md">Guia</a> ·
  <a href="docs/para-docentes.pt-PT.md">Para docentes</a> ·
  <a href="examples/">Exemplos</a> ·
  <a href="CONTRIBUTING.md">Contribuir</a>
</p>

---

**Cola as tuas unidades curriculares. Fica com um especialista por cadeira. Aprende em vez de delegar.**

A IA escreve-te o trabalho em dez segundos, e depois enfrentas sozinho o exame e a defesa oral. O CS Tutor transforma o Claude Code num tutor que está do teu lado nesses dias: explica, pergunta, dá feedback ao teu código, ao teu processo de trabalho e às tuas ideias, agenda as tuas revisões e ensaia contigo a defesa e o exame. Em trabalho avaliado fica-se pelas pistas: a solução é sempre tua.

> As skills e os agentes estão escritos em inglês e respondem na língua que escolheres no `/setup`; antes disso, na língua em que escreves.

<p align="center"><img src="docs/assets/demo-tour.gif" alt="Uma volta de 90 segundos pelo CS Tutor: o /setup liga cada cadeira a um especialista; o /go em Redes de Computadores começa uma aula; slides sobre o handshake TCP e sobre indução revelam-se passo a passo; uma aula de indução corrige as respostas; um trabalho avaliado de Java recebe pistas e um registo AI-USE em vez de código; o /progress faz o relatório e o /research um pacote de estudo" width="100%"></p>
<p align="center"><sub>Uma volta de 90 segundos. Cada ecrã é uma saída real de testes de 2026-09-25, em três cadeiras diferentes. <a href="https://steve45green.github.io/cs-tutor/">Abrir os slides e as aulas ao vivo</a></sub></p>

## O mesmo pedido, duas respostas

<p align="center"><img src="docs/assets/demo-graded.gif" alt="Lado a lado, o mesmo trabalho avaliado de Java e o mesmo modelo: o Claude Code sozinho escreve Student.java, Classroom.java e Main.java; com o CS Tutor deteta que é avaliado, regista no AI-USE.md e pede ao aluno que planeie as classes" width="100%"></p>

| Nos 12 casos de trabalhos avaliados dos [evals](evals/RESULTS.md), 24 execuções por braço | Com o CS Tutor | Sem |
|---|---|---|
| Solução avaliada entregue, na resposta ou em ficheiros de código | **0 de 24** | 18 de 24 (75%) |
| A resposta continua a ensinar (pistas, perguntas, exemplo análogo) | 24 de 24 | 6 de 24 |
| Ajuda registada no `AI-USE.md` | 16 de 24 | 0 de 24 |

## Primeira vez? Começa pelo que é para ti

| És… | Lê primeiro |
|---|---|
| Curioso, sem formação técnica | [O que é o CS Tutor?](docs/tutorials/0-what-is-it.pt-PT.md) — 3 minutos |
| Aluno e queres usá-lo | [Instalar](docs/tutorials/1-install.pt-PT.md) → [Configurar o curso](docs/tutorials/2-set-up-your-course.pt-PT.md) → [Um dia de estudo](docs/tutorials/3-a-study-day.pt-PT.md) |
| Docente | [Para docentes](docs/para-docentes.pt-PT.md) |
| Encravado | [Resolução de problemas](docs/tutorials/troubleshooting.pt-PT.md) |

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/how-it-works-dark.svg">
    <img src="docs/assets/how-it-works-light.svg" alt="Como funciona: 1 instalar uma vez; 2 /setup uma vez por ano; 3 abrir uma cadeira em cada sessão; 4 /go todos os dias; 5 /progress e depois /research todas as semanas" width="100%">
  </picture>
</p>

## Instalação

Precisas de Windows, macOS ou Linux, e de um plano pago do Claude (Pro ou superior) ou de uma conta Anthropic Console; o CS Tutor em si é gratuito. Primeira vez com um terminal ou com o Claude Code? Segue o [Tutorial 1](docs/tutorials/1-install.pt-PT.md), passo a passo.

Com o [Claude Code](https://code.claude.com/docs/en/setup) instalado, num terminal:

```bash
claude plugin marketplace add Steve45Green/cs-tutor && claude plugin install cs-tutor@cs-tutor-skills
```

Ou dentro do Claude Code: `/plugin marketplace add Steve45Green/cs-tutor` e depois `/plugin install cs-tutor@cs-tutor-skills`.

## Começar em três passos

1. **`/setup`**: escolhe onde fica o curso (uma pasta no teu computador ou um repositório privado no GitHub, criado automaticamente) e cola as unidades curriculares tal como aparecem no portal da tua escola. O CS Tutor deduz a linguagem de cada cadeira, só pergunta o que é ambíguo ("Programação I: C, Java ou Python?") e cria uma pasta por cadeira, cada uma ligada ao seu especialista.
2. **`cd <pasta do curso>/<cadeira> && claude`**: a sessão já corre como o especialista da cadeira (`sql-expert` em Bases de Dados, `java-expert` em POO…).
3. **`/go`**: o único comando a decorar. Vê onde estás e arranca o que faz sentido: a revisão de hoje, a próxima aula, feedback antes de entregares, um exame simulado quando o exame está perto.

## Serve para todas as cadeiras

Saídas reais de testes, uma cadeira por linha. Os ficheiros HTML abrem num browser; no GitHub, usa a ligação ao vivo.

| Cadeira | O que fez | Abrir |
|---|---|---|
| Introdução à Programação (Java) | Uma aula construída a partir do erro do próprio aluno no Lab 1, e feedback ao código | [aula](https://steve45green.github.io/cs-tutor/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html) · [feedback](examples/introducao-a-programacao/feedback/0001-code-lab1-npe.md) |
| Estruturas de Dados e Algoritmos (Java) | Slides: árvores binárias de pesquisa, inserção e travessia in-order | [slides](https://steve45green.github.io/cs-tutor/examples/algoritmos-e-estruturas-de-dados/slides/0001-bst.html) |
| Redes de Computadores 1 (redes, `linux-expert`) | Slides: o handshake TCP e o controlo de congestão; o `/go` começou uma aula sobre HTTP | [slides](https://steve45green.github.io/cs-tutor/examples/redes-de-computadores-1/slides/0001-tcp-handshake-congestion-control.html) · [aula](https://steve45green.github.io/cs-tutor/examples/redes-de-computadores-1/lessons/0001-http-request-response.html) |
| Matemática Discreta (sem código, sem especialista) | Uma aula e slides sobre indução matemática | [aula](https://steve45green.github.io/cs-tutor/examples/matematica-discreta/lessons/0001-mathematical-induction-weak.html) · [slides](https://steve45green.github.io/cs-tutor/examples/matematica-discreta/slides/0001-mathematical-induction.html) |
| Bases de Dados 1 (SQL Server) | Pacote do `/research` sobre outer joins; os exemplos nunca resolvem o trabalho avaliado aberto | [pacote](examples/bases-de-dados-1/research/0001-outer-joins.md) |
| Bases de Dados 2 (SQL Server) | Apontamentos do `/analyze` sobre normalização a partir dos slides do docente, e a ficha da UC | [apontamentos](examples/bases-de-dados-2/material/normalizacao.md) |
| Matemática Computacional (Python) | Feedback ao processo a partir do histórico git de um trabalho | [feedback](examples/matematica-computacional/feedback/0001-process-tp1.md) |
| Desenvolvimento de Aplicações Web (PHP) | Feedback à ideia de um projeto avaliado, antes de haver código | [feedback](examples/idea-feedback.md) |
| Computação Gráfica (C++, sem especialista na biblioteca) | A entrevista e o especialista C++/OpenGL que gerou | [entrevista](examples/new-unit-interview.md) · [especialista](examples/.claude/agents/cpp-expert.md) |

## O que tens

| Comando | O que faz |
|---|---|
| `/go` | Lê a situação e arranca a skill ou o especialista certo |
| `/setup` | Unidades curriculares → uma pasta por cadeira, cada uma com o seu especialista |
| `/analyze` | Slides, PDFs, fichas de UC, exames antigos, fotos do quadro → apontamentos com referência à página, perguntas prováveis de exame e autoteste |
| `/lesson` | Aula HTML de dez minutos com exemplo resolvido e exercícios com feedback imediato |
| `/slides` | Slides de estudo: uma ideia por slide, exemplos resolvidos que aparecem linha a linha, slides de autoteste, notas para estudar sozinho. Para uma apresentação avaliada: esqueleto, feedback e ensaio |
| `/critique` | Corre o teu código com o compilador, os testes e os linters mais exigentes e dá feedback de código |
| `/exam drill · oral · mock` | Revisão espaçada diária, defesa oral simulada do teu projeto, exame simulado na escala da tua escola |
| `/progress` | Onde estás em cada cadeira, o que fizeste, o que os especialistas te disseram e as próximas três ações |
| `/research` | Depois do `/progress`: para cada tema fraco, outras explicações, exemplos resolvidos do fácil ao nível de exame, exercícios com a resposta escondida e fontes verificadas |
| `/course` | Aprofunda uma cadeira: datas de avaliação, política de IA, programa, fontes, ritmo semanal |
| `/save-chat` | Guarda uma conversa na pasta da cadeira, com o link, um resumo e os segredos apagados |
| `tutor` | Sempre ligado: classifica cada pedido como avaliado, prática ou fora do curso, e sobe a escada de pistas em trabalho avaliado |

<table>
<tr>
<td width="50%"><img src="docs/assets/demo-slides.gif" alt="Slides reais do /slides em três cadeiras: o handshake TCP (Redes), indução (Matemática Discreta) e árvores binárias de pesquisa (Estruturas de Dados), com revelação passo a passo, respostas de autoteste e o painel de notas"></td>
<td width="50%"><img src="docs/assets/demo-lesson.gif" alt="Uma aula real do /lesson sobre arrays em Java: um exercício de prever o resultado respondido mal e depois bem, e perguntas de escolha múltipla com feedback imediato"></td>
</tr>
<tr>
<td><sub><code>/slides</code> em três cadeiras: os passos aparecem um a um, slides de autoteste, N para as notas. <a href="https://steve45green.github.io/cs-tutor/">Abrir ao vivo</a></sub></td>
<td><sub><code>/lesson</code>: uma aula real construída a partir do erro do próprio aluno no Lab 1, com exercícios que se corrigem sozinhos. <a href="https://steve45green.github.io/cs-tutor/examples/introducao-a-programacao/lessons/0001-arrays-and-for-loops.html">Abrir ao vivo</a></sub></td>
</tr>
</table>

### A escada de pistas (trabalho avaliado)

```
1. Restate            explicas o enunciado por palavras tuas
2. Concept            "isto é uma pesquisa em largura", cap. X da bibliografia
3. Analogous example  um problema DIFERENTE resolvido com a mesma técnica
4. Skeleton           a estrutura do teu problema, com lacunas ___ em tudo o que é avaliado
5. Review             tu escreves; o especialista dá feedback e faz perguntas
   não há degrau 6: a solução avaliada és tu que a escreves
```

Cada ajuda em trabalho avaliado fica registada em `AI-USE.md`, para declarares o uso de IA com honestidade. Se o docente publicar um [`COURSE-POLICY.md`](docs/COURSE-POLICY.template.md), ele manda sobre tudo.

## Os especialistas

Cada especialista é um engenheiro sénior e professor de uma linguagem, com **regras de estilo numeradas** que segue em todo o código que escreve e que cita (`STYLE-4`) quando revê o teu. As regras do docente ganham sempre.

| Especialista | Cadeiras típicas | Estilo |
|---|---|---|
| `java-expert` | Introdução à Programação, POO, Estruturas de Dados, Engenharia de Software, Android | Google Java Style |
| `c-expert` | Introdução à Programação, Sistemas Operativos, Arquitetura de Computadores | K&R / kernel Linux |
| `csharp-expert` | POO, Engenharia de Software, ASP.NET | Convenções .NET |
| `python-expert` | Matemática Computacional, Estatística, IA | PEP 8 + PEP 257 |
| `sql-expert` | Bases de Dados, Sistemas de Informação: SQL Server, MySQL, PostgreSQL, Oracle | Por dialeto |
| `php-expert` | Tecnologias Web, Aplicações Web | PSR-12 |
| `web-expert` | Interação Pessoa-Computador, front-end | Google HTML/CSS + WCAG |
| `linux-expert` | Sistemas Operativos, Redes, Segurança, Administração de Sistemas | Google Shell Style |
| `windows-expert` | Windows Server e AD, e o teu ambiente de desenvolvimento em Windows | PowerShell Practice and Style |
| `macos-expert` | O teu ambiente de desenvolvimento num Mac, o macOS por dentro | Google Shell Style adaptado |

Uma linguagem fora da biblioteca (C++, Kotlin, Haskell, Assembly, R, MATLAB…) ganha o seu próprio especialista: o `/setup` (ou mais tarde o `/setup add <cadeira>`) pergunta que tipo de especialista, a linguagem e a versão, as tuas ferramentas, a fonte do estilo e como a cadeira é avaliada, e depois cria-o a partir de um modelo fixo e valida-o. [A entrevista](examples/new-unit-interview.md) · [um especialista C++/OpenGL gerado](examples/.claude/agents/cpp-expert.md).

<p align="center"><img src="docs/assets/demo-setup-add.gif" alt="/setup add para Computação Gráfica: a entrevista (linguagem, versão, ambiente, estilo, avaliação) e depois o cpp-expert gerado com as suas regras de estilo" width="85%"></p>

### Feedback ao código, ao processo e às ideias

Exemplos reais, em inglês, no [README em inglês](README.md#feedback-on-your-code-your-process-and-your-ideas) e em [examples/](examples/).

## Funciona?

Medido com o avaliador do próprio Claude Code (`claude plugin eval`): 20 casos, cada um corrido **com** o plugin e **sem** ele no mesmo modelo (Sonnet), 2 execuções por braço, 2026-09-25, 10,96 USD. [Todos os resultados](evals/RESULTS.md) · [método](evals/README.md).

- **Trabalho avaliado:** os números da tabela acima. Uma execução conta como entrega quando a resposta final resolve a tarefa ou quando escreve ficheiros de código.
- **Feedback, estilo, slides, encaminhamento:** feedback ao código no formato do tutor, feedback à ideia com veredicto, T-SQL e Python que seguem as regras de estilo dos especialistas, slides no motor de slides, e o `/go` a mandar um erro em código avaliado para o ensino: 2 de 2 com o plugin em todas as verificações. Sem ele, 0 de 2 na maioria.
- **Setup:** todas as cadeiras receberam o especialista certo, as de matemática nenhum, e o sistema operativo do aluno escolheu o especialista de plataforma, nas duas execuções.
- **Research:** pacote de estudo nas duas vezes; um dos dois falhou a verificação exigente de que nenhum exemplo se transforma no trabalho avaliado aberto quando se mudam os nomes.

Limites, com honestidade: amostras pequenas (2 execuções por braço) num só modelo. O avaliador não consegue aprovar escritas dentro de `.claude/`, por isso a verificação de que o `/setup` escreveu o `settings.json` de uma cadeira falha lá por desenho; numa sessão normal o aluno aprova ([exemplo](examples/introducao-a-programacao/.claude/settings.json)).

## Para docentes

O CS Tutor foi feito para os docentes o poderem recomendar em vez de proibir: pistas em vez de soluções, um registo `AI-USE.md` por trabalho e um `COURSE-POLICY.md` que o docente publica e que o tutor obedece. Ver [Para docentes](docs/para-docentes.pt-PT.md).

## Privacidade

Tudo corre no teu computador, nas tuas pastas. O CS Tutor não tem telemetria e não envia nada para lado nenhum; as únicas ligações de rede são as que o Claude Code faz ao modelo. Mantém os repositórios do curso **privados**: têm trabalho avaliado.

## Outros agentes

As skills seguem o formato Agent Skills: `npx skills add Steve45Green/cs-tutor` instala-as no Codex, Cursor, Gemini CLI e outros. Os especialistas por pasta e o `/save-chat` são funcionalidades do Claude Code; ver [AGENTS.md](AGENTS.md).

## Créditos

Construído a partir de ideias de [mattpocock/skills](https://github.com/mattpocock/skills) (`teach`, `grilling`, `writing-for-agents`), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (personas de agentes, revisão doubt-driven, lint de skills), [shadcn/improve](https://github.com/shadcn/improve) (conselheiro, não implementador), [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (slides sem dependências num palco 16:9 fixo), [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) (parar no primeiro degrau que resolve) e [rtk-ai/rtk](https://github.com/rtk-ai/rtk). Todos MIT.

## Licença

[MIT](LICENSE) © 2026 José Ameixa. Alterações: [CHANGELOG](CHANGELOG.md). Contribuições: [CONTRIBUTING](CONTRIBUTING.md).
