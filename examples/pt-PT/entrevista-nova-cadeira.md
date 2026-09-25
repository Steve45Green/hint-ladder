# A entrevista do especialista: `/setup add` para uma cadeira sem especialista

Uma resposta real, de uma execução de teste sem interface em 2026-09-25, a:

```
/setup add Computação Gráfica 9119140 3º ano 2º semestre 6 ECTS TP:30 PL:30
```

numa raiz de curso com `Language: Portuguese (Portugal)` no [CURRICULUM.md](CURRICULUM.md). Nenhum agente da biblioteca cobre C++, por isso o `/setup` pergunta que especialista criar, numa só ronda e com uma recomendação em cada pergunta. Numa sessão interativa as perguntas aparecem no seletor do Claude Code (setas, a opção recomendada primeiro); esta execução mostra a forma em texto.

---

A UC "Computação Gráfica" tem várias pilhas possíveis e por agora não há agente C++ na biblioteca — preciso da tua escolha e, já agora, dos detalhes para o agente caso seja essa a escolha.

**1 · Pilha.** Computação Gráfica: C++ (OpenGL), JavaScript (WebGL/three.js) ou Python?
> Recomendado: **C++ (OpenGL)** — é a pilha mais usada nesta cadeira e não há nenhuma UC relacionada no teu curso que aponte para outra.

Se escolheres C++ (recomendado), preciso também disto — **se escolheres JavaScript ou Python, salta estas**, pois já há agente (`web-expert` / `python-expert`) para essas:

**2 · Linguagem e versão.** Que versão de C++ e que biblioteca gráfica?
> Recomendado: **C++17, com OpenGL (core profile) + GLFW/GLAD** para janela e loading — o combo mais comum neste tipo de UC.

**3 · Ambiente.** IDE/compilador, sistema de build, e onde corre o código (o teu computador, máquinas do laboratório, ou uma VM)?
> Recomendado: **VS Code + g++/CMake**, a correr na tua própria máquina — mas diz-me se a escola usa outra coisa (Visual Studio, laboratório específico, etc.) ou se não sabes ainda.

**4 · Estilo.** Há alguma norma de estilo dada pelo docente (documento, código nos slides, "seguimos X")?
> Recomendado: **nenhuma conhecida** → uso o *C++ Core Guidelines* como referência, até dizeres o contrário.

**5 · Forma de avaliação.** Trabalhos de laboratório, projeto com defesa oral, ou exame escrito à mão?
> Recomendado: **trabalhos de laboratório + projeto com defesa oral** — o mais comum nesta cadeira, mas confirma se sabes o formato real.

---

Com as respostas (C++17 com OpenGL 3.3 core profile; CMake, GLFW, GLAD e GLM no VS Code, num portátil Windows; sem guia de estilo do docente; trabalhos de laboratório e um projeto de grupo com defesa oral), a segunda execução respondeu:

---

**Computação Gráfica** adicionada: linha nova em `CURRICULUM.md` (status `active`), pasta `computacao-grafica/` com `MISSION.md`, `SYLLABUS.md` e `.claude/settings.json`.

- Agente gerado: `cpp-expert` (C++17, OpenGL 3.3 core, CMake/GLFW/GLAD/GLM em VS Code no Windows, estilo baseado nas C++ Core Guidelines por não haver guia do docente) — validado sem erros.
- A marcar `to confirm` em `MISSION.md`: datas e pesos da avaliação, "Why", "Constraints", "Pace" e "Success looks like" — corre `/course` dentro da pasta para preencher.

Próximos passos: `cd computacao-grafica && claude` já abre a sessão como `cpp-expert`; depois `/course` e `/go`. Tudo foi commitado.

O especialista gerado está em [.claude/agents/cpp-expert.md](.claude/agents/cpp-expert.md): regras de estilo numeradas e 10 erros comuns de OpenGL, cada um com a pergunta que leva o aluno a encontrá-lo. Passa no validador. A pasta da cadeira está em [computacao-grafica/](computacao-grafica/).
