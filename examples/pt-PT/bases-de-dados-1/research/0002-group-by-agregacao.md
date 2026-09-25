# GROUP BY e funções de agregação

Porquê agora: tema 4 do SYLLABUS.md tem peso "alto" e estado "seen" (visto, ainda não "mastered"), depende do tema 1 (já "mastered"), e ainda não há registos de repetição espaçada sobre ele; ao mesmo tempo é a base direta da pergunta 1 do TP1 e o Teste 1 (30%, mínimo 8,0) é a 2026-10-07 — dentro de 12 dias · Sobreposição com trabalho avaliado: TP1 (todos os exemplos abaixo são analógicos, no domínio de uma loja online, não no domínio Sócios/Livros/Empréstimos do enunciado) · Fontes verificadas em: 2026-09-25

## Em resumo

`GROUP BY` agrupa as linhas de uma tabela (ou do resultado de um `JOIN`) em "baldes" segundo o valor de uma ou mais colunas, e as funções de agregação (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) calculam um único valor por balde. A dificuldade não está na sintaxe — está em pensar por grupos em vez de por linhas: depois do `GROUP BY`, cada linha do resultado já não representa um sócio, um produto ou uma venda individual, representa um grupo inteiro. Isso explica a maior parte dos erros: filtrar um grupo com `WHERE` (que ainda não sabe que grupos existem), pedir no `SELECT` uma coluna que não é igual para todas as linhas do grupo, ou esquecer que `HAVING` filtra depois de agregar e `WHERE` filtra antes.

## Três formas de ver isto

- **Formal**: dada uma consulta com `GROUP BY c1, c2, ...`, o motor forma um grupo por cada combinação distinta de valores de `c1, c2, ...` (depois de aplicar o `WHERE`), e qualquer coluna no `SELECT` tem de ser (a) uma das colunas de agrupamento, (b) o resultado de uma função de agregação, ou (c) funcionalmente dependente das colunas de agrupamento (o SQL Server não relaxa esta regra como o MySQL — se não estiver em (a) ou (b), dá erro). `HAVING` é o `WHERE` dos grupos: corre depois de os grupos existirem.
- **Imagem**:
  ```
  Vendas (linhas)                    depois de GROUP BY VendedorId
  ┌─────────┬────────┐               ┌────────────┬──────────┐
  │Vendedor │ Valor  │               │ Vendedor   │ SUM(Valor)│
  ├─────────┼────────┤   agrupar     ├────────────┼──────────┤
  │  Ana    │  120   │   ────────►   │   Ana      │   370    │
  │  Ana    │  250   │               │   Bruno    │   90     │
  │  Bruno  │   90   │               └────────────┴──────────┘
  │  Ana    │  ...   │    (baldes: um por vendedor, cada linha
  └─────────┴────────┘     de entrada cai num só balde)
  ```
- **Analogia**: é como separar um monte de recibos por gaveta (uma gaveta por vendedor) e depois somar o conteúdo de cada gaveta — o resultado é "um número por gaveta", já não "um número por recibo". A analogia deixa de funcionar quando queres, na mesma linha do resultado, um dado que varia dentro da gaveta (por exemplo, a data de cada venda individual): isso já não existe depois de fechar a gaveta, por isso o SQL Server recusa mostrá-lo sem agregação.

## Exemplos resolvidos (do fácil ao nível de exame)

### 1. Total vendido por vendedor, do maior para o menor (fácil)

**Problema**: mostrar, para cada vendedor, o nome e o valor total das vendas que fez, ordenado do total mais alto para o mais baixo.

```sql
-- Esquema de referência: Vendedores(VendedorId, Nome), Vendas(VendaId, VendedorId, ProdutoId, DataVenda, Valor, Estado)
SELECT
    ve.VendedorId,
    ve.Nome,
    SUM(v.Valor) AS TotalVendido
FROM Vendedores ve
JOIN Vendas v
    ON v.VendedorId = ve.VendedorId
GROUP BY
    ve.VendedorId,
    ve.Nome
ORDER BY
    TotalVendido DESC;
-- não executado (sem SQL Server disponível neste ambiente)
```

**Explicação passo a passo** (ordem lógica: `FROM`/`JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`):
1. `FROM Vendedores ve JOIN Vendas v ON ...` — junta cada venda ao seu vendedor; não há `WHERE`, por isso todas as vendas entram.
2. `GROUP BY ve.VendedorId, ve.Nome` — forma um grupo por vendedor. Agrupa-se por `VendedorId` (a chave) e não só por `Nome`, para não juntar por engano dois vendedores homónimos; `Nome` entra também no `GROUP BY` porque aparece no `SELECT` sem agregação.
3. `SUM(v.Valor)` — soma o `Valor` de todas as vendas dentro de cada grupo.
4. `ORDER BY TotalVendido DESC` — ordena o resultado já agregado; corre por último, por isso pode usar o alias `TotalVendido`.

**Erro típico**: escrever `SELECT ve.Nome, SUM(v.Valor) ... GROUP BY ve.Nome` (sem `VendedorId`). Funciona enquanto os nomes forem todos diferentes, mas junta silenciosamente dois vendedores com o mesmo nome num só grupo — o erro clássico de agrupar pela coluna "bonita" em vez da chave.

### 2. Categorias de produtos com vendas totais acima de um limiar (médio)

**Problema**: listar as categorias de produtos cujo valor total vendido (`SUM(Valor)`) no ano de 2026 é superior a 5000€, ordenadas do total mais alto para o mais baixo.

```sql
SELECT
    p.Categoria,
    SUM(v.Valor) AS TotalCategoria
FROM Produtos p
JOIN Vendas v
    ON v.ProdutoId = p.ProdutoId
WHERE v.DataVenda >= '2026-01-01'
    AND v.DataVenda < '2027-01-01'
GROUP BY p.Categoria
HAVING SUM(v.Valor) > 5000
ORDER BY TotalCategoria DESC;
-- não executado
```

**Explicação passo a passo**:
1. `WHERE v.DataVenda >= '2026-01-01' AND v.DataVenda < '2027-01-01'` — filtra as **linhas** (vendas individuais) antes de agrupar; note-se o `< '2027-01-01'` em vez de `<= '2026-12-31'`, para não perder vendas registadas às 23:59:59 do último dia do ano.
2. `GROUP BY p.Categoria` — só agora se formam os grupos, um por categoria, já só com as vendas de 2026.
3. `HAVING SUM(v.Valor) > 5000` — filtra **grupos**, depois de a soma já existir; teria de dar erro de sintaxe se estivesse em `WHERE`, porque uma soma agregada não existe ainda ao nível da linha.
4. `ORDER BY TotalCategoria DESC` — ordena o resultado final.

**Erro típico**: escrever a condição de valor em `WHERE SUM(v.Valor) > 5000` em vez de `HAVING`. O SQL Server recusa com "an aggregate may not appear in the WHERE clause" — o sintoma que revela que a condição é sobre o grupo, não sobre a linha.

### 3. Vendas pagas vs. pendentes por vendedor, numa só linha (nível de exame)

**Problema**: para cada vendedor, mostrar numa única linha o número de vendas com `Estado = 'Pago'` e o número de vendas com `Estado = 'Pendente'`, e o valor total apenas das vendas pagas.

```sql
SELECT
    ve.VendedorId,
    ve.Nome,
    COUNT(CASE WHEN v.Estado = 'Pago' THEN 1 END) AS NumVendasPagas,
    COUNT(CASE WHEN v.Estado = 'Pendente' THEN 1 END) AS NumVendasPendentes,
    SUM(CASE WHEN v.Estado = 'Pago' THEN v.Valor ELSE 0 END) AS ValorPago
FROM Vendedores ve
JOIN Vendas v
    ON v.VendedorId = ve.VendedorId
GROUP BY
    ve.VendedorId,
    ve.Nome
ORDER BY ve.Nome;
-- não executado
```

**Explicação passo a passo**:
1. `JOIN` e `GROUP BY` formam um grupo por vendedor, como no exemplo 1.
2. `COUNT(CASE WHEN v.Estado = 'Pago' THEN 1 END)` — dentro de cada grupo, o `CASE` transforma cada linha em `1` (se paga) ou `NULL` (senão, porque não há `ELSE`); `COUNT` **não conta `NULL`**, por isso só conta as vendas pagas daquele vendedor. É a técnica de "agregação condicional": um `CASE` dentro de uma função de agregação para contar/somar categorias diferentes na mesma linha do resultado (um "pivot" simples).
3. `SUM(CASE WHEN v.Estado = 'Pago' THEN v.Valor ELSE 0 END)` — aqui o `ELSE 0` é necessário: para somar, uma linha "não paga" tem de contribuir com `0`, não com `NULL` (embora `SUM` ignore `NULL`s, o `ELSE 0` torna a intenção explícita e evita confusão).
4. Nenhuma destas colunas precisa de estar no `GROUP BY`: são agregações, não valores diretos de coluna.

**Erro típico**: usar `COUNT(v.Estado = 'Pago')` (sem `CASE`) — em T-SQL isto não é uma expressão booleana utilizável assim (ao contrário de MySQL, onde `= ` devolve `0`/`1`); o SQL Server dá erro de sintaxe. O outro erro comum é esquecer o `ELSE 0` no `SUM` quando se quer mesmo garantir zero (por exemplo, se mais tarde alguém trocar `SUM` por `AVG`, o `NULL` implícito distorce a média porque `AVG` ignora as linhas `NULL`, não as conta como zero).

## Erros comuns

| Erro | Porque acontece | Como o detetar no teu trabalho |
|---|---|---|
| Coluna no `SELECT` que não está agregada nem no `GROUP BY` | Confundir "uma linha por grupo" com "uma linha por registo original" | Para cada coluna do `SELECT`, pergunta: está numa função de agregação, ou está no `GROUP BY`? Se não, o SQL Server vai recusar a query |
| Filtrar um grupo com `WHERE` em vez de `HAVING` | Esquecer que `WHERE` corre antes de os grupos existirem (ordem lógica: `WHERE` antes de `GROUP BY`) | Pergunta-te se a condição fala de uma linha ("`DataVenda` de 2026") ou de um grupo ("soma > 5000"); a segunda vai para `HAVING` |
| `COUNT(*)` quando se queria `COUNT(coluna)` (ou vice-versa) numa coluna com `NULL`s | Assumir que `COUNT(*)` e `COUNT(coluna)` dão sempre o mesmo número | Verifica se a coluna que estás a contar pode ter `NULL` (por exemplo, `Estado` antes de a venda ser confirmada); se puder, `COUNT(*)` conta a mais |
| Agrupar pela coluna "descritiva" (ex. `Nome`) em vez da chave (ex. `VendedorId`) | A coluna descritiva parece suficiente quando os dados de teste não têm duplicados | Pergunta: dois registos diferentes podiam ter o mesmo valor nesta coluna? Se sim, agrupa também pela chave |
| Esquecer o `ELSE` num `CASE` dentro de `SUM`/`AVG` quando se quer mesmo um zero | `CASE` sem `ELSE` devolve `NULL`, que `SUM` ignora silenciosamente (dá o resultado certo) mas `AVG` ignora a linha inteira (dá o resultado errado) | Se estás a calcular uma média condicional, confirma se queres "média só das linhas que contam" (sem `ELSE`) ou "média sobre todas as linhas, tratando as outras como zero" (com `ELSE 0`) |
| `GROUP BY` com colunas a mais ou a menos, mudando a granularidade sem se dar conta | Copiar um `GROUP BY` de outra query e ajustar só o `SELECT` | Conta quantos grupos esperavas (por exemplo, "uma linha por categoria") e compara com quantas linhas a query devolveu |

## Prática (respostas escondidas)

1. Escreve uma query que mostra, para cada categoria de produto, o número total de vendas registadas em `Vendas`, ordenado da categoria com mais vendas para a que tem menos.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       p.Categoria,
       COUNT(*) AS NumVendas
   FROM Produtos p
   JOIN Vendas v
       ON v.ProdutoId = p.ProdutoId
   GROUP BY p.Categoria
   ORDER BY NumVendas DESC;
   ```
   Porquê: `COUNT(*)` conta linhas dentro de cada grupo formado por `GROUP BY p.Categoria`, e `ORDER BY` corre depois de agregar, por isso pode usar o alias.
   </details>

2. A query seguinte dá erro no SQL Server. Explica porquê e corrige-a.
   ```sql
   SELECT
       v.VendedorId,
       ve.Nome,
       AVG(v.Valor) AS MediaVendas
   FROM Vendas v
   JOIN Vendedores ve
       ON ve.VendedorId = v.VendedorId
   GROUP BY v.VendedorId;
   ```
   <details><summary>Resposta</summary>
   `ve.Nome` aparece no `SELECT` mas não está agregado nem no `GROUP BY` — o SQL Server não sabe que valor de `Nome` mostrar para o grupo (mesmo sendo sempre o mesmo, na prática, o motor não infere isso). Correção: acrescentar `ve.Nome` ao `GROUP BY` (`GROUP BY v.VendedorId, ve.Nome`).
   </details>

3. Lista as categorias de produtos cujo valor total vendido (`SUM(Valor)`) é superior a 5000€, ordenadas do total mais alto para o mais baixo.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       p.Categoria,
       SUM(v.Valor) AS TotalCategoria
   FROM Produtos p
   JOIN Vendas v
       ON v.ProdutoId = p.ProdutoId
   GROUP BY p.Categoria
   HAVING SUM(v.Valor) > 5000
   ORDER BY TotalCategoria DESC;
   ```
   Porquê: o limiar de 5000€ é uma condição sobre o total do grupo, por isso vai em `HAVING`, não em `WHERE`.
   </details>

4. Queres o total vendido por vendedor, mas só considerando vendas com `DataVenda` em 2026, e só quer mostrar vendedores cujo total supere 1000€. Onde colocas cada condição, e porquê?
   <details><summary>Resposta</summary>
   O filtro de data (`v.DataVenda >= '2026-01-01' AND v.DataVenda < '2027-01-01'`) vai em `WHERE`, porque é uma propriedade de cada venda individual, avaliada antes de agrupar. O limiar de 1000€ (`SUM(v.Valor) > 1000`) vai em `HAVING`, porque só existe depois de somar dentro de cada grupo.
   </details>

5. Para cada vendedor, mostra numa única linha o número de vendas com `Estado = 'Pago'` e o número de vendas com `Estado = 'Pendente'`.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       ve.VendedorId,
       ve.Nome,
       COUNT(CASE WHEN v.Estado = 'Pago' THEN 1 END) AS NumPagas,
       COUNT(CASE WHEN v.Estado = 'Pendente' THEN 1 END) AS NumPendentes
   FROM Vendedores ve
   JOIN Vendas v
       ON v.VendedorId = ve.VendedorId
   GROUP BY
       ve.VendedorId,
       ve.Nome;
   ```
   Porquê: o `CASE` sem `ELSE` devolve `NULL` para as linhas que não interessam, e `COUNT` ignora `NULL`s, por isso cada `COUNT(CASE ...)` só conta o estado pedido.
   </details>

6. Para cada combinação de categoria de produto e estado da venda, mostra o número de vendas e o valor total, mas só as combinações com pelo menos 5 vendas **e** valor total superior a 2000€.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       p.Categoria,
       v.Estado,
       COUNT(*) AS NumVendas,
       SUM(v.Valor) AS ValorTotal
   FROM Produtos p
   JOIN Vendas v
       ON v.ProdutoId = p.ProdutoId
   GROUP BY
       p.Categoria,
       v.Estado
   HAVING COUNT(*) >= 5
       AND SUM(v.Valor) > 2000
   ORDER BY
       p.Categoria,
       v.Estado;
   ```
   Porquê: agrupar por duas colunas (`Categoria`, `Estado`) cria um grupo por cada combinação distinta das duas, e o `HAVING` pode combinar várias condições sobre agregações com `AND`, tal como um `WHERE` normal combina condições sobre linhas.
   </details>

## Fontes

| Fonte | Onde | Usado para | Verificado |
|---|---|---|---|
| Conhecimento do modelo sobre T-SQL (GROUP BY, HAVING, funções de agregação COUNT/SUM/AVG/MIN/MAX, ordem lógica de execução) | não aplicável (sem acesso à web hoje) | conceitos, regras de agrupamento e todos os exemplos | não verificado |
| SYLLABUS.md do workspace | pasta do curso | peso do tema, estado (seen), dependência do tema 1 | verificado no workspace |
| assignments/tp1/STATEMENT.md do workspace | pasta do curso | identificar a sobreposição a evitar e desenhar exemplos analógicos noutro domínio | verificado no workspace |
