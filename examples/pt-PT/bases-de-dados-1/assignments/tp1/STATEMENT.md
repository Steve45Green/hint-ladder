# TP1: consultas à base de dados Biblioteca (avaliado, 20%)

Esquema: Socios(SocioId, Nome, DataAdesao), Livros(LivroId, Titulo, Autor), Emprestimos(EmprestimoId, SocioId, LivroId, DataEmprestimo, DataDevolucao).

Escreve, em T-SQL:
1. Todos os sócios com o número de empréstimos que fizeram, incluindo os sócios sem empréstimos (0).
2. Os livros que nunca foram emprestados.
3. Os sócios cujos empréstimos foram todos devolvidos.
