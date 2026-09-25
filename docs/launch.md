# Lançamento: o dia de pôr o Hint Ladder no ar (cerca de 15 minutos)

Tudo o que está aqui é feito por ti na interface do GitHub; o código já está preparado. Faz os passos por esta ordem e só partilha o link no fim.

## 0. Estado atual (verificado a 2026-09-25)

| O que está | Consequência | Passo |
|---|---|---|
| O repositório chama-se `claude-skills`, mas a documentação e o comando de instalação usam `Steve45Green/hint-ladder` | os links e a instalação dão 404 até renomeares | 1 |
| O único branch, e o branch por omissão, é `claude/claude-skills-engineering-course-e8d8ga`; não existe `main` | os links para `main` dão 404 | 2 |
| O repositório é **privado** | ninguém além de ti consegue instalar; o site e o badge de CI não funcionam | 3 |
| O histórico foi limpo: um único commit, sem dados pessoais | pode ficar público | — |
| O CI está verde; o workflow `Evals` salta sem o segredo `ANTHROPIC_API_KEY`; o workflow `Pages` só corre em `main` num repositório público | nada a fazer | 4, 9 |

## 1. Renomear o repositório para `hint-ladder`

Settings → General → Repository name → `hint-ladder` → Rename. O GitHub redireciona o endereço antigo.

## 2. Mudar o nome do branch por omissão para `main`

Settings → General → Default branch → lápis (Rename branch) → `main` → Rename. Não é preciso pull request: não há outro branch.

No teu computador, se já tiveres um clone:

```bash
git remote set-url origin https://github.com/Steve45Green/hint-ladder.git
git fetch origin
git branch -m claude/claude-skills-engineering-course-e8d8ga main
git branch -u origin/main main
git remote set-head origin -a
```

A partir daqui, trabalho novo vai para um branch a partir do `main` e entra por pull request.

## 3. Tornar o repositório público

Settings → General → Danger Zone → Change repository visibility → **Make public**. Depois, numa janela privada do browser, abre o README e confirma que os GIFs e o comando de instalação aparecem.

## 4. Ligar o site das demos ao vivo

Settings → Pages → Build and deployment → Source: **GitHub Actions**. Depois, Actions → Pages → Run workflow (branch `main`). Ao fim de um minuto o site está em `https://steve45green.github.io/hint-ladder/`, com os slides e as aulas a abrir no browser. Os links "live" do README passam a funcionar.

## 5. Descrição, site e topics

Na página do repositório, roda dentada ao lado de "About":

- **Description:** `The AI tutor for Computer Engineering students: paste your course units, get a language expert per unit, slides and lessons for every unit. Teaches — never does your graded work. Claude Code plugin.`
- **Website:** `https://steve45green.github.io/hint-ladder/`
- **Topics:** `claude-code`, `claude-code-plugin`, `agent-skills`, `education`, `computer-science`, `computer-engineering`, `academic-integrity`, `tutor`, `spaced-repetition`, `portugal`.

## 6. Imagem de pré-visualização

Settings → General → Social preview → Upload → `docs/assets/social-preview.png` (1280×640, já pronta, com os números dos evals). É a imagem que aparece quando alguém partilha o link.

## 7. Badge de CI

Pede-me para o reativar. Está comentado no topo dos dois READMEs, porque num repositório privado aparece partido.

## 8. Release v0.6.0

Releases → Draft a new release → Choose a tag: `v0.6.0` (criar no `main`) → título `Hint Ladder 0.6.0` → cola a secção 0.6.0 do `CHANGELOG.md` → junta `docs/assets/demo-tour.gif` → Publish.

## 9. Segurança e comunidade

- Settings → Code security → ativar **Private vulnerability reporting** (o `SECURITY.md` e o formulário de issues apontam para lá).
- Settings → General → Features → ativar **Discussions** (o formulário de issues já tem o link).
- Opcional: Settings → Secrets and variables → Actions → `ANTHROPIC_API_KEY`, para os evals semanais (cerca de 11 USD por corrida, com teto de 25).

## 10. Divulgação

- PR para [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), em Community Skills: `- **[Steve45Green/hint-ladder](https://github.com/Steve45Green/hint-ladder)** - AI tutor for Computer Engineering students: a language expert, slides and lessons for every course unit; hints instead of graded solutions (0 of 24 handed over in evals, vs 18 of 24 without).`
- Listar em [skills.sh](https://skills.sh) (`npx skills add Steve45Green/hint-ladder` passa a funcionar sozinho).
- Um post em r/ClaudeAI e r/learnprogramming, e nos núcleos de estudantes de Informática, com o `demo-tour.gif`. Para chamar a atenção, usa o `demo-graded.gif` com a frase "O mesmo pedido, o mesmo modelo: um entrega-te o trabalho, o outro ensina-te", e sempre com o número medido (18 de 24 contra 0 de 24), porque o Claude sozinho nem sempre entrega a solução.
- Pedir a 5 colegas que usem durante duas semanas e abram issues com o que falhou: são os primeiros testemunhos.
- Mostrar a [página para docentes](for-lecturers.md) e o site das demos a um professor teu: um docente que recomenda vale mais do que cem estrelas.
