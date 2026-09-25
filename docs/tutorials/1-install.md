# 1. Install Claude Code and Hint Ladder

*[Português](1-install.pt-PT.md) · [All tutorials](README.md)*

**Time:** 10 minutes. **You need:** a paid Claude plan (Pro or higher) or an Anthropic Console account, and an internet connection.

## Step 1: Open a terminal

| System | How |
|---|---|
| Windows | Start menu → type `PowerShell` → open **Windows PowerShell**. The line starts with `PS C:\Users\<you>>`. |
| macOS | ⌘ + Space → type `Terminal` → Enter. |
| Linux | Ctrl + Alt + T, or your distribution's Terminal app. |

Never used a terminal? Anthropic's [terminal guide](https://code.claude.com/docs/en/terminal-guide) shows every click.

## Step 2: Install Claude Code

Copy the line for your system, paste it into the terminal and press Enter.

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**macOS, Linux, or WSL on Windows:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows, also install [Git for Windows](https://git-scm.com/downloads/win) (keep the default options): Claude Code then runs Bash commands, and the course's compilers and scripts behave as in the lab.

**It worked when** closing the terminal, opening a new one and typing

```
claude --version
```

prints a version number, such as `2.1.282 (Claude Code)`. If it says the command is not found, see [Troubleshooting](troubleshooting.md#claude-command-not-found).

Other ways to install (Homebrew, WinGet, apt): [official setup page](https://code.claude.com/docs/en/setup).

## Step 3: Log in

Type `claude` and press Enter. The first time, a browser window opens: log in with your Claude account and come back to the terminal.

**It worked when** you see Claude Code's welcome box and a `>` prompt where you can type.

## Step 4: Install Hint Ladder

Still inside Claude Code, type these two lines, one at a time, pressing Enter after each:

```
/plugin marketplace add Steve45Green/hint-ladder
/plugin install hint-ladder@hint-ladder
```

The first adds the place where Hint Ladder is published; the second installs it for your user, so it works in every folder. If Claude Code asks where to install it, choose the option for you (user).

Prefer to do it from the terminal, outside Claude Code? One line:

```bash
claude plugin marketplace add Steve45Green/hint-ladder && claude plugin install hint-ladder@hint-ladder
```

## Step 5: Check it

Type `/exit` to leave, then `claude` to start again, and type `/` : the list of commands shows `/go`, `/setup`, `/lesson`, `/slides`, `/research` and the others (sometimes as `/hint-ladder:go`, which is the same command).

**It worked when** `/go` appears in the list. If it doesn't, see [Troubleshooting](troubleshooting.md#the-commands-dont-appear).

## Keeping it up to date

Claude Code updates itself. To update Hint Ladder, run in the terminal:

```bash
claude plugin marketplace update hint-ladder && claude plugin update hint-ladder@hint-ladder
```

Next: [2. Set up your course](2-set-up-your-course.md).
