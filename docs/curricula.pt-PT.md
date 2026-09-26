# Planos curriculares comparados

*[English](curricula.md)*

O Hint Ladder escolhe um agente de linguagem para cada cadeira a partir do nome dela ([LANGUAGE-MAP.md](../skills/setup/LANGUAGE-MAP.md)). Para decidir que agentes escrever à mão, comparámos os planos de estudos e as fichas públicas das licenciaturas portuguesas de Engenharia Informática: que tipos de cadeira partilham e em que linguagem cada escola as ensina.

Verificado a 2026-09-25 com pesquisa na web nos portais das escolas: Sigarra, Fénix, os guias de cursos da UA, da NOVA e da UC, e os guias ECTS dos politécnicos. Cada linha liga à página que indica a linguagem. Os planos mudam todos os anos: a ficha da cadeira na pasta do próprio aluno ganha sempre a esta tabela.

## O que todas as licenciaturas têm em comum

Todos os planos que lemos têm estes tipos de cadeira, com pequenas diferenças de nome e de ano:
- Introdução à Programação, Programação Orientada a Objetos, Algoritmos e Estruturas de Dados;
- Bases de Dados, Sistemas Operativos, Arquitetura de Computadores, Sistemas Digitais, Redes de Computadores;
- Engenharia de Software e Web;
- o bloco de matemática: Análise, Álgebra Linear, Matemática Discreta, Lógica, Probabilidades e Estatística, Métodos Numéricos;
- um projeto final ou estágio.

A maioria tem também Compiladores, Computação Gráfica, Inteligência Artificial e Computação Móvel.

## Linguagens por tipo de cadeira

| Tipo de cadeira | Evidência (escola · cadeira · tecnologia) | Agente |
|---|---|---|
| Introdução à Programação | [UMinho · Programação Imperativa · C](https://www.di.uminho.pt/~jno/sitedi/uc_J302N5.html); [ISEL · Programação · Kotlin](https://www.isel.pt/en/leic/programming); IST, ISEP e a maioria dos politécnicos · Python ou Java | `c-expert`, `kotlin-expert`, `python-expert`, `java-expert` |
| Programação funcional | [UMinho · Programação Funcional · Haskell](https://www.di.uminho.pt/~jno/sitedi/uc_8501Q8.html) (1.º ano); [UMinho · Cálculo de Programas · Haskell](https://haslab.github.io/CP/); [FCUL · Princípios de Programação · Haskell](https://fenix.ciencias.ulisboa.pt/courses/ppro-2-2254879305238181); [FEUP · Programação Funcional e em Lógica · Haskell](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484434) | `haskell-expert` (novo) |
| Programação em lógica | [IST · Lógica para Programação · Prolog](https://fenix.tecnico.ulisboa.pt/disciplinas/LP112/2025-2026/1-semestre/programa); [FEUP · Programação Funcional e em Lógica · Prolog](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484434) | `prolog-expert` (novo) |
| Linguagens / paradigmas de programação | [NOVA · Linguagens e Ambientes de Programação · OCaml, C, JavaScript, Java, Bash](https://guia.unl.pt/pt/2023/fct/program/1053/course/8147) | o agente da linguagem principal; OCaml → gerado |
| Programação Orientada a Objetos | [FCUL · Programação Centrada em Objetos · Java + UML](https://fenix.ciencias.ulisboa.pt/courses/pcobj-284554468265388/programa); UA · Programação Orientada a Objetos · Java | `java-expert`, `csharp-expert`, `cpp-expert` (novo) |
| Algoritmos e Estruturas de Dados | [FEUP · Algoritmos e Estruturas de Dados · C++](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=436433) | a linguagem de POO da escola; C++ → `cpp-expert` (novo) |
| Arquitetura de Computadores | [IST · Introdução à Arquitetura de Computadores · assembly PEPE-16](https://fenix.tecnico.ulisboa.pt/disciplinas/IAC2/2022-2023/2-semestre/ver-post/introducao-ao-assembly-do-pepe-16-35b); [UA · Arquitetura de Computadores I · MIPS](https://www.ua.pt/pt/uc/12067); [Lusófona · Arquitetura de Computadores · RISC-V](https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/ULHT260-5857) | `assembly-expert` (novo), `c-expert` |
| Sistemas Digitais | [IPT · Sistemas Digitais · VHDL](https://portal2.ipt.pt/pt/cursos/202324/licenciaturas/l_-_ei/91194/); [UC · Laboratório de Sistemas Digitais · VHDL](https://apps.uc.pt/courses/PT/unit/8577/14244/2016-2017?common_core=true&type=ram&id=359); [NOVA · Conceção de Sistemas Digitais · VHDL em FPGA](https://guia.unl.pt/pt/2019/fct/program/934/course/10918); [IPB · Sistemas Digitais · VHDL/Verilog](https://guiaects.unipb.pt/GuiaEcts/PdfService?cod_escola=3043&cod_curso=9119&n_plano=850&n_disciplina=1104&n_opcao=0&ano_lect=2025&locale=1) | `vhdl-expert` (novo) |
| Engenharia de Software | [FEUP · UML nos requisitos e na arquitetura](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=484425); [IST · UML e SysML](https://fenix.tecnico.ulisboa.pt/cursos/leic-a/disciplina-curricular/845953938489550); [UC · UML](https://apps.uc.pt/courses/PT/unit/9858/22529/2024-2025?common_core=true&type=ram&id=362); [IPT · UML](https://portal2.ipt.pt/pt/Cursos/tmr/l_-_ei/911947/) | `uml-expert` (novo) para os modelos; o agente da linguagem de POO para o código |
| Métodos Numéricos | [IPS · Análise Numérica · MATLAB/Octave](https://ips.pt/disciplina-detalhes/?lang=pt&anoletivo=2025&cursoid=217&idUC=4472); [FEUP · Análise Numérica · MATLAB](https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=349833); [UC · Métodos Numéricos · MATLAB](https://apps.uc.pt/courses/PT/unit/101259/26621/2026-2027?common_core=true&type=ram&id=13521) | `matlab-expert` (novo), `python-expert` |
| Probabilidades e Estatística | [IST · Probabilidades e Estatística · R](https://fenix.tecnico.ulisboa.pt/cursos/leic-t/disciplina-curricular/1408903891910863); [ISEP · Python](https://www.isep.ipp.pt/Course/Course/26) | `r-expert` (novo), `python-expert` |
| Bloco de matemática (Análise, Álgebra, Matemática Discreta, Lógica) | todos os planos | `math-expert` (novo) |
| Compiladores | [ISEP · ANTLR](https://www.isep.ipp.pt/Course/Course/26); [FEUP · ANTLR](https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=501688); [IST · lex e yacc](https://fenix.tecnico.ulisboa.pt/cursos/leic-t/disciplina-curricular/1529008374071) | `c-expert` ou `java-expert`, conforme a linguagem da ferramenta |
| Computação Gráfica | [FEUP · OpenGL e WebGL](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=520332) | `web-expert` (WebGL), `cpp-expert` (OpenGL, novo) |
| Computação Móvel | [ISEL · Kotlin (Android)](https://cc.isel.pt/2020/05/08/paulo-leic-kotlin/); [IPT · Flutter e Android Studio](https://portal2.ipt.pt/pt/Cursos/licenciaturas/l_-_itm/2-814321/) | `kotlin-expert` (novo), `java-expert`; Dart → gerado |

## O que mudou no Hint Ladder

- **Dez agentes novos escritos à mão**, cada um com regras de estilo, um catálogo de erros comuns e evals próprios: `cpp-expert`, `haskell-expert`, `prolog-expert`, `assembly-expert`, `kotlin-expert`, `matlab-expert`, `r-expert`, `vhdl-expert`, `uml-expert` e `math-expert`. Antes, estas cadeiras recebiam um agente escrito pelo `/setup` na hora, ou nenhum (matemática).
- **`/report`**: todos os trabalhos práticos e o projeto final acabam num relatório escrito. O comando monta a estrutura do relatório a partir do enunciado e dá feedback sobre o rascunho do aluno, sem o escrever.
- **As linhas do mapa** passam a indicar estes agentes, e o `/setup` liga-os sem gerar nada.

## Ainda gerados quando são precisos

OCaml (NOVA), Dart/Flutter (IPT), Swift, Go, Scheme e qualquer outra linguagem fora da biblioteca: o `/setup` escreve o agente a partir do [AGENT-TEMPLATE.md](../skills/setup/AGENT-TEMPLATE.md), depois de uma entrevista curta. O PEPE-16 (IST) fica com o `assembly-expert`, que aprende o conjunto de instruções com o material da própria cadeira.
