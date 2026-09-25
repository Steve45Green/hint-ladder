# The expert interview: `/setup add` for a unit with no expert

A real reply, from a headless test run on 2026-09-25, to:

```
/setup add Computação Gráfica 9119140 3º ano 2º semestre 6 ECTS TP:30 PL:30
```

in a study root that already had [CURRICULUM.md](CURRICULUM.md). No library agent covers C++, so `/setup` asks what kind of expert to build, in one round, each question with a recommendation. In an interactive session these come as Claude Code's question picker (arrow keys, the recommended option first); this headless run shows the text form. With the answers (C++17 and OpenGL 3.3 core; CMake, GLFW, GLAD and GLM in VS Code on Windows; no lecturer style guide; labs and a group project with an oral defence) it wrote the unit's folder and a validated [cpp-expert](.claude/agents/cpp-expert.md).

---

Computação Gráfica matches the map's computer-graphics row, and its default stack (C++) has no library agent — that needs a generated `cpp-expert`. Per the setup rules, I'll ask the stack question and the C++ interview together so we don't end on the stack question alone; skip the interview if you pick JavaScript or Python instead.

**1 · Stack.** Computação Gráfica: C++ (OpenGL), JavaScript (WebGL/three.js), or Python?
> Recommended: **C++ (OpenGL)** — the map's default for this discipline, and the most common choice for a dedicated graphics course.

**If you pick C++, also answer these (skip if you pick JavaScript or Python):**

**2 · Language and version.** Which C++ standard and graphics stack?
> Recommended: **C++17, core-profile OpenGL via GLFW (windowing/context) + GLAD (loader)** — the standard modern-OpenGL academic setup; unlike legacy immediate-mode OpenGL, it matches what current courses teach.

**3 · Environment.** IDE, build tool, and where the work runs?
> Recommended: **CMake + VS Code, running on your own computer** — cross-platform, no lock-in to a specific OS; tell me if the course provides its own project template or lab-machine setup instead.

**4 · Style.** Any style rules from the lecturer, or should I use a reference guide?
> Recommended: **C++ Core Guidelines** (no lecturer rules known yet) — the closest thing to a canonical modern-C++ style reference; I'll switch to the lecturer's rules the moment you share them.

**5 · Assessment shape.** Labs, a project (with oral defence?), or code written by hand in an exam?
> Recommended: **practical lab assignments building up a small renderer** — typical for graphics courses, but confirm exact weights/dates later with `/course`.
