# 0. O que é o Hint Ladder?

*[English](0-what-is-it.md) · [Todos os tutoriais](README.pt-PT.md)*

**Numa frase:** o Hint Ladder transforma o Claude (a IA da Anthropic) num explicador particular para um curso de Engenharia Informática: explica, faz perguntas, marca revisões e dá feedback, e recusa-se a fazer os trabalhos avaliados por ti.

## O problema que resolve

Uma IA escreve um trabalho prático da faculdade em dez segundos. O aluno entrega-o e depois enfrenta sozinho o exame escrito e a defesa oral, sem ter aprendido a matéria. O Hint Ladder foi feito para esses dias: ajuda-te a aprender a cadeira e, no que é avaliado, fica-se pelas pistas.

## O que é, em palavras simples

| Palavra | O que quer dizer aqui |
|---|---|
| **Claude** | O assistente de IA da Anthropic. |
| **Claude Code** | O Claude como programa no teu computador. Falas com ele num **terminal** (a janela de texto que todos os computadores têm) e ele consegue ler e escrever os ficheiros da pasta onde o abres. |
| **Plugin** | Uma extensão do Claude Code. O Hint Ladder é uma: acrescenta comandos e especialistas. |
| **Comando** | Algo que escreves a começar por `/`, como `/go` ou `/lesson`. |
| **Cadeira** | Uma unidade curricular do curso ("Bases de Dados 1", "Sistemas Operativos"). |
| **Especialista** | Uma versão do Claude especializada numa linguagem de programação, com as regras de estilo dessa linguagem. Cada cadeira recebe o seu: Java em POO, SQL em Bases de Dados… |
| **Workspace** | A pasta de uma cadeira, onde o Hint Ladder guarda as tuas aulas, apontamentos, revisões e feedback. |

## O que um aluno faz com ele

1. **Uma vez por ano**, cola a lista de cadeiras do portal da universidade. O Hint Ladder cria uma pasta por cadeira e dá a cada uma o seu especialista.
2. **Todos os dias**, abre a pasta de uma cadeira e escreve `/go`. O Hint Ladder vê o que está pendente (revisões, um teste na próxima semana, um PDF novo da aula) e começa o que faz sentido: uma aula de dez minutos, slides para rever, exercícios, um exame simulado.
3. **Nos trabalhos avaliados** (um trabalho prático, um projeto, uma apresentação) dá pistas, faz perguntas e revê o que o aluno escreveu, e regista cada ajuda num ficheiro que o aluno pode mostrar ao docente.
4. **Uma vez por semana**, o `/progress` diz onde está em cada cadeira, e o `/research` traz mais explicações e exemplos para os temas fracos.

![Como funciona](../assets/how-it-works-light.svg)

## O que não é

- Não é um site nem uma app: corre dentro do Claude Code, no teu computador.
- Não faz os teus trabalhos. É essa a ideia.
- Não envia o teu trabalho para lado nenhum. Os ficheiros ficam no teu computador (ou no teu repositório privado do GitHub, se escolheres isso). O que passa pela internet é só a conversa com o Claude, como em qualquer uso do Claude.

## O que precisas

- Um computador com Windows 10 ou mais recente, macOS 13 ou mais recente, ou Linux.
- Um plano **pago** do Claude (Pro ou superior) ou uma conta Anthropic Console: o plano gratuito não inclui o Claude Code. O Hint Ladder em si é gratuito e open source.
- Cerca de 20 minutos da primeira vez.

A seguir: [1. Instalar o Claude Code e o Hint Ladder](1-install.pt-PT.md).
