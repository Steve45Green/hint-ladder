# 2. Configurar o teu curso

*[English](2-set-up-your-course.md) · [Todos os tutoriais](README.pt-PT.md)*

**Tempo:** 10 minutos, uma vez por ano (e outra vez no início de cada semestre, para marcar as cadeiras ativas). **Precisas de:** o [Tutorial 1](1-install.pt-PT.md) feito e a lista das tuas cadeiras.

## Passo 1: Copiar as cadeiras

Abre o portal da universidade onde está o plano de estudos (a lista de unidades curriculares) e copia-o: seleciona a tabela com o rato e Ctrl + C (⌘ + C num Mac). Qualquer formato serve: a tabela do portal, o texto do PDF do plano de estudos, ou uma lista escrita à mão. Quanto mais trouxer (código, ano, semestre, ECTS, horas), melhor, mas só os nomes chegam.

## Passo 2: Correr o `/setup`

Abre um terminal, escreve `claude` e depois:

```
/setup
```

Cola a lista quando ele pedir (ou logo a seguir ao `/setup`, na mesma linha).

## Passo 3: Escolher onde fica o curso

O `/setup` pergunta uma vez, com o seletor de perguntas do Claude Code: escolhe com as setas e carrega em Enter (ou escreve outra resposta). A opção recomendada vem primeiro:

1. **Uma pasta neste computador (recomendada)**: `<home>/Documents/<curso>`, com o histórico de cada alteração (git).
2. **Pasta + GitHub privado**: a mesma pasta, mais um repositório privado no GitHub sincronizado com ela.
3. **Esta pasta**: a pasta onde abriste o Claude Code.

- **1** serve para a maioria: fica tudo no teu computador, com o histórico de cada alteração (git).
- **2** guarda também uma cópia privada no GitHub: uma cópia de segurança, e o mesmo curso noutro computador. Precisa de uma conta GitHub; se faltar o programa do GitHub (`gh`), o `/setup` mostra o comando para o instalar e continua com a opção 1 entretanto.
- Nunca tornes público o repositório de um curso: vai ter trabalhos avaliados.

## Passo 4: Responder a uma ronda de perguntas

O `/setup` deduz a linguagem de cada cadeira pelo nome ("Bases de Dados" → SQL, "Sistemas Operativos" → C e Linux) e pergunta só o que não consegue saber, no mesmo seletor (até quatro perguntas por ecrã), cada pergunta com uma resposta recomendada:

1. que cadeiras tens este semestre;
2. cadeiras que podem ser dadas em mais de uma linguagem ("Programação I: C, Java ou Python?");
3. o sistema de base de dados, se houver uma cadeira de BD (SQL Server, MySQL, PostgreSQL, Oracle);
4. o teu computador (Windows, macOS ou Linux);
5. país, escala de notas e a língua das respostas (por omissão: Portugal, 0–20, a língua em que escreves);
6. a política de IA da tua escola, se a souberes.

Escolhe uma opção em cada uma, ou escreve a tua. Fora do seletor (por exemplo noutro agente), pergunta em texto e respondes numa só mensagem: `1: todas do 2º ano, 1º semestre. 2: Java. 3: SQL Server. 4: Windows. 5: Portugal, responde em português. 6: não sei.`

A seguir o Claude Code pede autorização para escrever alguns ficheiros dentro de pastas `.claude/` (a definição que abre cada cadeira com o seu especialista, e algum especialista novo). É normal: aprova.

## Passo 5: Ver o que foi criado

```
~/Documents/engenharia-informatica/
├── CURRICULUM.md              todas as cadeiras, a linguagem e o especialista de cada uma
├── bases-de-dados-1/          uma pasta por cadeira ativa
│   ├── MISSION.md             porquê, avaliação, datas, política de IA (completas com /course)
│   ├── SYLLABUS.md            os temas, com estado todo / seen / mastered
│   └── .claude/settings.json  abre esta pasta com o sql-expert
├── programacao-orientada-por-objetos/
│   └── …                      abre com o java-expert
└── …
```

Um exemplo real: [examples/CURRICULUM.md](../../examples/CURRICULUM.md).

## Passo 6: Abrir uma cadeira

```bash
cd ~/Documents/engenharia-informatica/bases-de-dados-1
claude
```

No PowerShell do Windows o caminho fica `cd $HOME\Documents\engenharia-informatica\bases-de-dados-1`.

**Correu bem quando** a sessão responde como o especialista dessa cadeira: pergunta "quem és?" e ele diz que é o especialista de SQL (ou Java, C…).

## Passo 7: Completar a missão da cadeira

Põe na pasta a ficha da unidade curricular (um PDF) e depois:

```
/analyze
/course
```

O `/analyze` lê o PDF; o `/course` preenche o `MISSION.md` (avaliação, datas, política de IA) e pergunta só o que falta. Faz isto em cada cadeira quando o semestre dela começar.

## Uma cadeira nova mais tarde, ou uma sem especialista

Semestre novo, uma optativa, uma cadeira numa linguagem para a qual o CS Tutor não tem especialista (Kotlin, Haskell, C++, MATLAB, Assembly…)? Na pasta do curso:

```
/setup add Computação Gráfica 9119140 3º ano 2º semestre 6 ECTS
```

Quando nenhum especialista serve, primeiro entrevista-te, numa só ronda, cada pergunta com uma recomendação:

1. que tipo de especialista: uma linguagem de programação, um assembly, uma ferramenta (MATLAB, R, Arduino, Unity), uma notação de modelação (UML, ER), ou nenhum;
2. linguagem e versão ("C++17 com OpenGL 3.3");
3. ambiente: IDE, compilador, bibliotecas, o teu computador ou o do laboratório;
4. estilo: as regras do docente, ou o guia de referência da linguagem;
5. como é avaliada: laboratórios, projeto com defesa, código escrito à mão no exame.

Depois cria a pasta da cadeira e um especialista feito a partir das tuas respostas, com as suas regras de estilo e os comandos das ferramentas, e valida-o. Exemplos reais: [a entrevista](../../examples/new-unit-interview.md) e [o especialista de C++ que criou](../../examples/.claude/agents/cpp-expert.md).

A seguir: [3. Um dia de estudo](3-a-study-day.pt-PT.md).
