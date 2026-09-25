# 1. Instalar o Claude Code e o Hint Ladder

*[English](1-install.md) · [Todos os tutoriais](README.pt-PT.md)*

**Tempo:** 10 minutos. **Precisas de:** um plano pago do Claude (Pro ou superior) ou uma conta Anthropic Console, e ligação à internet.

## Passo 1: Abrir um terminal

| Sistema | Como |
|---|---|
| Windows | Menu Iniciar → escreve `PowerShell` → abre o **Windows PowerShell**. A linha começa por `PS C:\Users\<tu>>`. |
| macOS | ⌘ + Espaço → escreve `Terminal` → Enter. |
| Linux | Ctrl + Alt + T, ou a app Terminal da tua distribuição. |

Nunca usaste um terminal? O [guia do terminal](https://code.claude.com/docs/en/terminal-guide) da Anthropic mostra cada clique.

## Passo 2: Instalar o Claude Code

Copia a linha do teu sistema, cola-a no terminal e carrega em Enter.

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS, Linux, ou WSL no Windows:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

No Windows, instala também o [Git for Windows](https://git-scm.com/downloads/win) (com as opções por omissão): o Claude Code passa a correr comandos Bash, e os compiladores e scripts das cadeiras comportam-se como no laboratório.

**Correu bem quando**, depois de fechares o terminal, abrires outro e escreveres

```
claude --version
```

aparece um número de versão, por exemplo `2.1.282 (Claude Code)`. Se disser que o comando não existe, vê a [Resolução de problemas](troubleshooting.pt-PT.md#claude-comando-não-encontrado).

Outras formas de instalar (Homebrew, WinGet, apt): [página oficial](https://code.claude.com/docs/en/setup).

## Passo 3: Entrar na conta

Escreve `claude` e carrega em Enter. Da primeira vez abre-se o browser: entra com a tua conta Claude e volta ao terminal.

**Correu bem quando** vês a caixa de boas-vindas do Claude Code e um `>` onde podes escrever.

## Passo 4: Instalar o Hint Ladder

Ainda dentro do Claude Code, escreve estas duas linhas, uma de cada vez, com Enter no fim de cada uma:

```
/plugin marketplace add Steve45Green/hint-ladder
/plugin install hint-ladder@hint-ladder
```

A primeira acrescenta o sítio onde o Hint Ladder está publicado; a segunda instala-o para o teu utilizador, para funcionar em todas as pastas. Se o Claude Code perguntar onde instalar, escolhe a opção para ti (user).

Preferes fazer tudo no terminal, fora do Claude Code? Uma linha:

```bash
claude plugin marketplace add Steve45Green/hint-ladder && claude plugin install hint-ladder@hint-ladder
```

## Passo 5: Confirmar

Escreve `/exit` para sair, depois `claude` para voltar a entrar, e escreve `/` : a lista de comandos mostra `/go`, `/setup`, `/lesson`, `/slides`, `/research` e os outros (às vezes como `/hint-ladder:go`, que é o mesmo comando).

**Correu bem quando** o `/go` aparece na lista. Se não aparecer, vê a [Resolução de problemas](troubleshooting.pt-PT.md#os-comandos-não-aparecem).

## Manter atualizado

O Claude Code atualiza-se sozinho. Para atualizar o Hint Ladder, corre no terminal:

```bash
claude plugin marketplace update hint-ladder && claude plugin update hint-ladder@hint-ladder
```

A seguir: [2. Configurar o teu curso](2-set-up-your-course.pt-PT.md).
