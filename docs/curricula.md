# Curricula compared

*[Português](curricula.pt-PT.md)*

Hint Ladder picks a language agent for each course unit from its name ([LANGUAGE-MAP.md](../skills/setup/LANGUAGE-MAP.md)). To choose which agents to write by hand, we compared the public study plans and course sheets of Portuguese Computer Engineering degrees: which unit types they share and which language each school teaches them in.

Checked on 2026-09-25 through web search of the schools' course portals (Sigarra, Fénix, the UA, NOVA and UC course guides, polytechnic ECTS guides). Every row links the page that names the language. Plans change every year: the course sheet in the student's own folder always wins over this table.

## What every degree shares

Every plan we read has these unit types, with small differences in name and year: Introduction to Programming, Object-Oriented Programming, Data Structures and Algorithms, Databases, Operating Systems, Computer Architecture, Digital Systems, Computer Networks, Software Engineering, Web, the maths block (Calculus, Linear Algebra, Discrete Mathematics, Logic, Probability and Statistics, Numerical Methods), a final project or internship. Most also have Compilers, Computer Graphics, Artificial Intelligence and Mobile Development.

## Languages by unit type

| Unit type | Evidence (school · unit · stack) | Agent |
|---|---|---|
| Introduction to Programming | [UMinho · Programação Imperativa · C](https://www.di.uminho.pt/~jno/sitedi/uc_J302N5.html); [ISEL · Programação · Kotlin](https://www.isel.pt/en/leic/programming); IST, ISEP and most polytechnics · Python or Java | `c-expert`, `kotlin-expert`, `python-expert`, `java-expert` |
| Functional programming | [UMinho · Programação Funcional · Haskell](https://www.di.uminho.pt/~jno/sitedi/uc_8501Q8.html) (year 1); [UMinho · Cálculo de Programas · Haskell](https://haslab.github.io/CP/); [FCUL · Princípios de Programação · Haskell](https://fenix.ciencias.ulisboa.pt/courses/ppro-2-2254879305238181); [FEUP · Programação Funcional e em Lógica · Haskell](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484434) | `haskell-expert` (new) |
| Logic programming | [IST · Lógica para Programação · Prolog](https://fenix.tecnico.ulisboa.pt/disciplinas/LP112/2025-2026/1-semestre/programa); [FEUP · Programação Funcional e em Lógica · Prolog](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484434) | `prolog-expert` (new) |
| Programming languages / paradigms | [NOVA · Linguagens e Ambientes de Programação · OCaml, C, JavaScript, Java, Bash](https://guia.unl.pt/pt/2023/fct/program/1053/course/8147) | the main language's agent; OCaml → generated |
| Object-Oriented Programming | [FCUL · Programação Centrada em Objetos · Java + UML](https://fenix.ciencias.ulisboa.pt/courses/pcobj-284554468265388/programa); UA · Programação Orientada a Objetos · Java | `java-expert`, `csharp-expert`, `cpp-expert` (new) |
| Data Structures and Algorithms | [FEUP · Algoritmos e Estruturas de Dados · C++](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=436433) | the school's OOP language; C++ → `cpp-expert` (new) |
| Computer Architecture | [IST · Introdução à Arquitetura de Computadores · PEPE-16 assembly](https://fenix.tecnico.ulisboa.pt/disciplinas/IAC2/2022-2023/2-semestre/ver-post/introducao-ao-assembly-do-pepe-16-35b); [UA · Arquitetura de Computadores I · MIPS](https://www.ua.pt/pt/uc/12067); [Lusófona · Arquitetura de Computadores · RISC-V](https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/ULHT260-5857) | `assembly-expert` (new), `c-expert` |
| Digital Systems | [IPT · Sistemas Digitais · VHDL](https://portal2.ipt.pt/pt/cursos/202324/licenciaturas/l_-_ei/91194/); [UC · Laboratório de Sistemas Digitais · VHDL](https://apps.uc.pt/courses/PT/unit/8577/14244/2016-2017?common_core=true&type=ram&id=359); [NOVA · Conceção de Sistemas Digitais · VHDL on FPGA](https://guia.unl.pt/pt/2019/fct/program/934/course/10918); [IPB · Sistemas Digitais · VHDL/Verilog](https://guiaects.unipb.pt/GuiaEcts/PdfService?cod_escola=3043&cod_curso=9119&n_plano=850&n_disciplina=1104&n_opcao=0&ano_lect=2025&locale=1) | `vhdl-expert` (new) |
| Software Engineering | [FEUP · UML for requirements and architecture](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484425); [IST · UML and SysML](https://fenix.tecnico.ulisboa.pt/cursos/leic-a/disciplina-curricular/845953938489550); [UC · UML](https://apps.uc.pt/courses/PT/unit/9858/22529/2024-2025?common_core=true&type=ram&id=362); [IPT · UML](https://portal2.ipt.pt/pt/Cursos/tmr/l_-_ei/911947/) | `uml-expert` (new) for the models, the OOP language's agent for the code |
| Numerical Methods | [IPS · Análise Numérica · MATLAB/Octave](https://ips.pt/disciplina-detalhes/?lang=pt&anoletivo=2025&cursoid=217&idUC=4472); [FEUP · Análise Numérica · MATLAB](https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=349833); [UC · Métodos Numéricos · MATLAB](https://apps.uc.pt/courses/PT/unit/101259/26621/2026-2027?common_core=true&type=ram&id=13521) | `matlab-expert` (new), `python-expert` |
| Probability and Statistics | [IST · Probabilidades e Estatística · R](https://fenix.tecnico.ulisboa.pt/cursos/leic-t/disciplina-curricular/1408903891910863); [ISEP · Python](https://www.isep.ipp.pt/Course/Course/26) | `r-expert` (new), `python-expert` |
| Maths block (Calculus, Algebra, Discrete Mathematics, Logic) | every plan | `math-expert` (new) |
| Compilers | [ISEP · ANTLR](https://www.isep.ipp.pt/Course/Course/26); [FEUP · ANTLR](https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=501688); [IST · lex and yacc](https://fenix.tecnico.ulisboa.pt/cursos/leic-t/disciplina-curricular/1529008374071) | `c-expert` or `java-expert`, by the tool's language |
| Computer Graphics | [FEUP · OpenGL and WebGL](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=520332) | `web-expert` (WebGL), `cpp-expert` (OpenGL, new) |
| Mobile Development | [ISEL · Kotlin (Android)](https://cc.isel.pt/2020/05/08/paulo-leic-kotlin/); [IPT · Flutter and Android Studio](https://portal2.ipt.pt/pt/Cursos/licenciaturas/l_-_itm/2-814321/) | `kotlin-expert` (new), `java-expert`; Dart → generated |

## What changed in Hint Ladder

- **Ten new curated agents**, each with style rules, a catalogue of common mistakes and its own evals: `cpp-expert`, `haskell-expert`, `prolog-expert`, `assembly-expert`, `kotlin-expert`, `matlab-expert`, `r-expert`, `vhdl-expert`, `uml-expert` and `math-expert`. Before, these units got an agent written by `/setup` on the day, or none at all (maths).
- **`/report`**: every lab assignment and the final project end in a written report. The command builds the report's outline from the statement and gives feedback on the student's draft, without writing it.
- **The map's rows** now name these agents, so `/setup` wires them without generating anything.

## Still generated on demand

OCaml (NOVA), Dart/Flutter (IPT), Swift, Go, Scheme and any other language outside the library: `/setup` writes the agent from [AGENT-TEMPLATE.md](../skills/setup/AGENT-TEMPLATE.md) after a short interview. PEPE-16 (IST) is handled by `assembly-expert`, which learns the instruction set from the course's own material.
