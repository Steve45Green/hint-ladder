# Resolução de problemas

*[English](troubleshooting.md) · [Todos os tutoriais](README.pt-PT.md)*

## `claude`: comando não encontrado

- Fecha o terminal e abre outro: o instalador acrescenta o `claude` ao caminho, e as janelas antigas não o veem.
- Continua a faltar: corre `claude doctor` se existir, ou segue [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install).
- No Windows, se o PowerShell disser que `irm` não é reconhecido, estás no CMD e não no PowerShell: abre o **Windows PowerShell** e cola outra vez a linha de instalação.

## "O Claude Code não está incluído no teu plano"

O plano gratuito do Claude não inclui o Claude Code. Precisas do Pro ou superior, ou de uma conta Anthropic Console com créditos de API.

## O `/plugin marketplace add` falha: repositório não encontrado

- Confirma a escrita: `Steve45Green/hint-ladder`.
- O repositório tem de ser público para se instalar a partir dele. Se és o dono e ainda está privado ou com outro nome, segue os passos 1 a 3 de [docs/launch.md](../launch.md).
- Para experimentar enquanto o repositório é privado, carrega-o a partir de um clone em vez de o instalar: `git clone https://github.com/Steve45Green/hint-ladder.git` (o Git pede-te o login do GitHub) e depois, na pasta do curso, `claude --plugin-dir <caminho do clone>`.

## "Plugins aren't available in this environment"

Escreveste `/plugin …` numa sessão na cloud (claude.ai/code, ou um ambiente cloud da app do Claude). O Hint Ladder instala-se no Claude Code do teu computador: abre um terminal, escreve `claude` ([tutorial 1](1-install.pt-PT.md)) e escreve lá as duas linhas `/plugin`. O `/setup moodle` também precisa do teu computador: o login no Moodle faz-se no teu próprio terminal, e uma sessão na cloud não chega ao Moodle da maioria das escolas.

## Os comandos não aparecem

- Escreve `/exit` e volta a abrir o `claude`: os plugins carregam quando a sessão começa.
- Escreve `/plugin` e confirma que o `hint-ladder` está instalado e ativo. No terminal: `claude plugin list`.
- Experimenta o nome longo: `/hint-ladder:go`. Se esse funcionar e o `/go` não, há outro plugin ou skill com o mesmo nome; o nome longo funciona sempre.

## A sessão não abre como o especialista da cadeira

- Abre o Claude Code **dentro** da pasta da cadeira (primeiro `cd <curso>/<cadeira>`).
- A pasta tem de ter `.claude/settings.json` com `{"agent": "<especialista>"}` (por exemplo `{"agent": "sql-expert"}`). Falta? Cria-o com essa linha, ou pede ao `/setup` na pasta do curso que volte a ligar essa cadeira; nunca apaga o teu trabalho.
- Arranca-o à mão: `claude --agent sql-expert` (ou `java-expert`, `c-expert`…).

## "Não me dá a resposta"

É de propósito nos trabalhos avaliados: vê o [Tutorial 4](4-graded-work.pt-PT.md). Se o exercício **não** for avaliado (prática, um exame antigo, um exercício do livro), di-lo ("isto é prática, não conta para a nota"): passa a explicar à vontade e mostra a solução completa depois de tentares.

## As respostas vêm na língua errada

A língua é a linha `Language:` do `CURRICULUM.md` (todas as cadeiras) ou do `MISSION.md` da cadeira. Muda-a aí (ou pede ao Claude que a mude).

## Os slides ou a aula não abrem

Faz duplo clique no ficheiro `.html` na pasta `slides/` ou `lessons/` da cadeira: abre no browser e funciona sem internet. No GitHub, descarrega primeiro o ficheiro (o botão ⬇ "Download raw file"); o GitHub mostra o código dos ficheiros HTML em vez de os correr.

## A conversa ficou lenta ou confusa

O `/compact` resume-a e continua. Para começar do zero, `/clear`; os teus ficheiros ficam.

## Quanto custa?

O Hint Ladder é gratuito e open source. O Claude Code gasta o uso do teu plano Claude (ou os teus créditos de API, se entrares com uma conta Console); sessões longas e relatórios em segundo plano gastam mais.

## Continuas encravado

Abre uma issue com o que escreveste e o que viste (tira tudo o que for privado): [issues](https://github.com/Steve45Green/hint-ladder/issues).
