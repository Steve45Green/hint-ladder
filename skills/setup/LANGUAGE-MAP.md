# Language map: course unit → stack → agent

Used by `/setup` to classify each course unit from its name. Match case-insensitively and ignoring accents; a unit matches a row when its name contains any of the row's patterns. When several rows match, the longest matching pattern wins ("Segurança em Redes de Comunicação" matches `redes` and `segurança`: security wins; "Cálculo Numérico" matches `cálculo` and `cálculo numérico`: numerical methods wins). Patterns cover Portuguese (PT and BR), English and Spanish names.

Library agents: `c-expert`, `csharp-expert`, `java-expert`, `linux-expert`, `php-expert`, `python-expert`, `sql-expert`, `web-expert`. A stack outside the library gets an agent generated from `AGENT-TEMPLATE.md` (named in the Generated column).

Platform agents are not matched by unit name: `/setup` picks one from the student's computer (Windows → `windows-expert`, macOS → `macos-expert`, Linux → `linux-expert`), records it on the `OS:` line of `CURRICULUM.md`, and every unit uses it to install and fix its toolchain. Units about Windows Server or PowerShell also list `windows-expert` as support.

**Ask?** = yes means the unit is ambiguous: `/setup` asks the student, recommending the first candidate, or the language the same school uses in the unit this one depends on (the answer for Introduction to Programming usually settles Data Structures; the answer for OOP usually settles Software Engineering).

| # | Patterns | Domain | Candidate stacks (default first) | Primary agent | Support agents | Generated when | Ask? |
|---|---|---|---|---|---|---|---|
| 1 | introdução à programação, introducao a programacao, programação i, programação 1, fundamentos de programação, algoritmos e programação, lógica de programação, introduction to programming, programming i, programming 1, introducción a la programación | programming fundamentals | Java · C · Python | by answer | — | — | yes |
| 2 | orientada a objetos, orientada por objetos, orientação a objetos, poo, object-oriented, object oriented, orientada a objetos (es) | object-oriented programming | Java · C# · C++ | by answer | — | C++ → `cpp-expert` | yes |
| 3 | estruturas de dados, algoritmos e estruturas de dados, data structures, algorithms, estructuras de datos | data structures and algorithms | the school's IP/OOP language | by answer | — | — | only if not implied |
| 4 | bases de dados, base de dados, bancos de dados, banco de dados, databases, database systems, bases de datos | databases | SQL in the school's DBMS | `sql-expert` | — | — | DBMS only |
| 5 | sistemas de informação, information systems, sistemas de información | information systems | SQL + data modelling | `sql-expert` | — | — | no |
| 6 | sistemas operativos, sistemas operacionais, operating systems | operating systems | C + shell | `c-expert` | `linux-expert` | — | no |
| 7 | arquitetura de computadores, arquitectura de computadores, organização de computadores, computer architecture, computer organization, arquitectura de computadoras | computer architecture | C + Assembly (MIPS · x86 · ARM · RISC-V) | `c-expert` | generated assembly agent | mostly Assembly → `assembly-<isa>-expert` | ISA only |
| 8 | sistemas digitais, eletrónica digital, electrónica digital, eletrônica digital, circuitos lógicos, digital systems, digital logic, sistemas digitales | digital logic | logic design (Logisim) · VHDL · Verilog | — | — | VHDL/Verilog → `vhdl-expert`/`verilog-expert` | HDL only |
| 9 | redes de computadores, redes, computer networks, networking, redes de computadoras | networks | network tools + shell (Packet Tracer, Wireshark) | `linux-expert` | — | — | no |
| 10 | segurança, seguranca, cibersegurança, security, cybersecurity, seguridad | security | shell + network and web tools | `linux-expert` | `web-expert` | — | no |
| 11 | administração de sistemas, administracao de sistemas, system administration, systems administration, sysadmin, administración de sistemas | systems administration | Linux shell · Windows Server/PowerShell | `linux-expert` | `windows-expert` | — | no |
| 12 | tecnologias web, tecnologias para a web, programação web, desenvolvimento web, aplicações web, web development, web applications, web programming, desarrollo web | web development | PHP · C# (ASP.NET) · JavaScript (Node) · Java · Python, plus HTML/CSS/JS | `php-expert` · `csharp-expert` · `web-expert` (Node) · `java-expert` · `python-expert`, by answer | `web-expert`, `sql-expert` | — | yes |
| 13 | interação pessoa-computador, interacção pessoa-computador, interação humano-computador, interacção homem-máquina, human-computer interaction, hci, ihc, usabilidade, usability | human-computer interaction | HTML/CSS/JS + prototyping | `web-expert` | — | — | no |
| 14 | dispositivos móveis, dispositivos moveis, aplicações móveis, computação móvel, mobile | mobile development | Kotlin · Java · Dart (Flutter) · Swift · C# (MAUI) | Java → `java-expert`; C# → `csharp-expert` | `sql-expert` | Kotlin/Dart/Swift → `kotlin-expert`/`dart-expert`/`swift-expert` | yes |
| 15 | engenharia de software, software engineering, ingeniería de software | software engineering | the school's OOP language | `java-expert` or `csharp-expert` | — | — | only if not implied |
| 16 | linguagens de programação, paradigmas de programação, programming languages, programming paradigms, lenguajes de programación | programming languages | several (Haskell, Prolog, Scheme, Python, Java…) | the main language's agent | — | Haskell/Prolog/Scheme → `<lang>-expert` | yes (which languages) |
| 17 | compiladores, compilers | compilers | C · Java · Python + lex/yacc or ANTLR | by answer | — | — | yes |
| 18 | matemática computacional, métodos numéricos, análise numérica, cálculo numérico, numerical methods, numerical analysis, métodos numéricos (es) | numerical methods | Python · MATLAB/Octave | Python → `python-expert` | — | MATLAB/Octave → `matlab-expert` | yes |
| 19 | probabilidades, estatística, estatistica, statistics, probability, estadística | statistics | Python · R · spreadsheet/SPSS | Python → `python-expert` | — | R → `r-expert` | yes |
| 20 | inteligência artificial, inteligencia artificial, machine learning, aprendizagem automática, aprendizado de máquina, data science, ciência de dados | artificial intelligence and data | Python | `python-expert` | — | — | no |
| 21 | computação gráfica, computer graphics, computación gráfica | computer graphics | C++ (OpenGL) · JavaScript (WebGL/three.js) · Python | JS → `web-expert`; Python → `python-expert` | — | C++ → `cpp-expert` | yes |
| 22 | programação concorrente, programação paralela, sistemas distribuídos, concurrent programming, parallel programming, distributed systems | concurrency and distribution | Java · C · Go | by answer | `linux-expert` | Go → `go-expert` | yes |
| 23 | cloud, computação em nuvem, devops, virtualização, virtualization | cloud and operations | shell + containers | `linux-expert` | — | — | no |
| 24 | projeto integrado, projecto integrado, projeto final, trabalho final, estágio, estagio, capstone, internship, final project, proyecto final | project or internship | the project's stack | by answer (can be left for `/course`) | the stack's support agents | the stack's generated agent | yes (can defer) |
| 25 | análise matemática, analise matematica, cálculo, calculo, álgebra, algebra, matemática discreta, lógica, logic, física, fisica, physics, eletricidade, electricidade, mathematics, matemáticas | mathematics and physics | — | — (tutor + `/lesson` + `/exam`) | — | — | no |
| 26 | comunicação, dinâmica de grupos, empreendedorismo, marketing, gestão, management, ética, ethics, direito, regulação, law, inglês, english, soft skills | non-technical | — | — (tutor + `/lesson` + `/exam`) | — | — | no |

No row matches → classify by the discipline's usual content, mark the row `inferred` in `CURRICULUM.md`, and include it in the round of questions.

When a school's plan shows the language elsewhere (the unit description, a course sheet in the folder, the student's answer for a related unit), that evidence beats the default order above.
