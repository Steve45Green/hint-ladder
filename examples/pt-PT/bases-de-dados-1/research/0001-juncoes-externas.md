# Junções externas (LEFT, RIGHT, FULL JOIN)

Porquê agora: tens dois registos de aprendizagem em box 1 (repetição espaçada) sobre este tema exato — `0007-left-join-where` (condição no `WHERE` em vez do `ON`) e `0008-count-star-outer` (`COUNT(*)` a contar 1 em vez de 0) — o tema tem peso "alto" no SYLLABUS.md e está em estado "seen", não "mastered", e o Teste 1 (30%, mínimo 8,0) é em 2026-10-07, dentro de 12 dias · Sobreposição com trabalho avaliado: TP1 (todos os exemplos abaixo são analógicos, num domínio diferente — uma oficina automóvel, não a biblioteca do TP1) · Fontes verificadas em: 2026-09-25

## Em resumo

Um `INNER JOIN` só devolve as linhas em que as duas tabelas têm correspondência; qualquer linha sem par do outro lado desaparece. Uma junção externa existe precisamente para não deixar essas linhas desaparecer: `LEFT JOIN` garante que todas as linhas da tabela à esquerda ficam no resultado (com `NULL` nas colunas da direita quando não há correspondência); `RIGHT JOIN` faz o mesmo mas preservando a tabela à direita; `FULL JOIN` preserva as duas tabelas ao mesmo tempo. O ponto que mais gera erros — e que está na origem dos teus dois registos em box 1 — é que a decisão "esta linha fica ou não fica" é tomada pelo `FROM ... JOIN ... ON ...`, antes de o `WHERE` correr. Se puseres uma condição sobre a tabela do lado "opcional" no `WHERE`, estás a filtrar depois de a junção já ter decidido preservar as linhas sem correspondência — e como essas linhas têm `NULL` exatamente na coluna que estás a testar, o `WHERE` acaba por as eliminar, e o `LEFT JOIN` comporta-se como um `INNER JOIN`.

## Três formas de ver isto

- **Formal**: numa junção externa, o predicado de junção vive sempre no `ON`. `A LEFT JOIN B ON <condição>` devolve todas as linhas de `A`; para cada linha de `A`, se existir uma ou mais linhas de `B` que satisfaçam `<condição>`, essas linhas são combinadas com `A`; se não existir nenhuma, `A` aparece uma vez com todas as colunas de `B` a `NULL`. `RIGHT JOIN` é o mesmo com os papéis de `A` e `B` trocados (`A RIGHT JOIN B` ≡ `B LEFT JOIN A`, com as colunas por ordem diferente). `FULL JOIN` é a união das duas: linhas correspondidas, linhas só de `A` (com `B` a `NULL`) e linhas só de `B` (com `A` a `NULL`). Uma condição colocada no `WHERE` corre depois disto, sobre o resultado já combinado — e testa o valor real das colunas, incluindo os `NULL` que a própria junção acabou de introduzir.

- **Imagem**: pensa em duas tabelas pequenas e no que sobra de cada tipo de junção.

  ```
  Viaturas (v)              Reparacoes (r)
  ViaturaId  Matricula       ReparacaoId  ViaturaId  Custo
  1          AA-11-BB        10           1          150
  2          CC-22-DD        11           1          300
  3          EE-33-FF        (nenhuma reparação para a viatura 3)

  INNER JOIN v/r  ON r.ViaturaId = v.ViaturaId
  → só as viaturas 1 (duas linhas, uma por reparação). A viatura 3 não aparece.

  LEFT JOIN v/r  ON r.ViaturaId = v.ViaturaId
  → viatura 1 (duas linhas) + viatura 2 (r.* = NULL) + viatura 3 (r.* = NULL).
    Todas as viaturas ficam; é isto que "left" promete.

  FULL JOIN v/r  ON r.ViaturaId = v.ViaturaId
  → o mesmo que o LEFT JOIN acima, mais qualquer reparação cujo ViaturaId
    não exista em Viaturas (v.* = NULL nessas linhas).
  ```

- **Analogia**: pensa numa lista de convidados de um casamento (tabela da esquerda) e na lista de check-in feita à entrada (tabela da direita). Um `LEFT JOIN` dos convidados com o check-in mantém todos os convidados na lista, mesmo os que não apareceram — para esses, a "hora de chegada" fica em branco (`NULL`), mas o nome não desaparece. Um `RIGHT JOIN` seria o inverso: mantém toda a gente que fez check-in, incluindo alguém que apareceu sem estar convidado. Um `FULL JOIN` mantém as duas listas ao mesmo tempo: convidados que não vieram e pessoas que vieram sem convite. Onde a analogia deixa de ajudar: se quiseres "só os convidados que chegaram depois das 21h", na vida real filtras a lista já feita à mão; em SQL, se esse filtro for aplicado no `WHERE` depois do `LEFT JOIN`, ele também elimina os convidados que nunca chegaram (hora de chegada `NULL`, e `NULL` não é "depois das 21h") — exatamente as linhas que o `LEFT JOIN` prometeu manter. A analogia não avisa disto; só a regra formal (ON vs WHERE) o faz.

## Exemplos resolvidos (do fácil ao nível de exame)

Esquema usado em todos os exemplos (domínio: oficina automóvel, T-SQL / SQL Server):

```
Clientes   (ClienteId INT PK, Nome NVARCHAR(100))
Viaturas   (ViaturaId INT PK, ClienteId INT NULL FK -> Clientes, Matricula NVARCHAR(10))
Reparacoes (ReparacaoId INT PK, ViaturaId INT FK -> Viaturas, DataReparacao DATE, Custo DECIMAL(10,2))
```

`Viaturas.ClienteId` é anulável de propósito: nem todas as viaturas têm cliente já registado no sistema. Nenhuma destas queries foi executada (sem SQL Server disponível neste ambiente) — foram verificadas linha a linha, não com output real.

### 1. Todas as viaturas, com o nome do cliente quando existir (fácil)

**Problema**: a oficina quer uma lista de todas as viaturas registadas, com o nome do cliente proprietário quando esse cliente estiver associado. Algumas viaturas ainda não têm `ClienteId` preenchido e, mesmo assim, têm de aparecer na lista.

```sql
-- não executado
SELECT
    v.Matricula,
    c.Nome AS NomeCliente
FROM Viaturas AS v
LEFT JOIN Clientes AS c
    ON c.ClienteId = v.ClienteId
ORDER BY v.Matricula;
```

Passo a passo:
- `FROM Viaturas AS v`: esta é a tabela âncora. Tudo o que estiver aqui vai aparecer no resultado, aconteça o que acontecer no `JOIN`.
- `LEFT JOIN Clientes AS c ON c.ClienteId = v.ClienteId`: para as viaturas com `ClienteId` preenchido e correspondente a um cliente, traz `Nome`; para as viaturas com `ClienteId` a `NULL`, todas as colunas de `c` (incluindo `Nome`) ficam a `NULL`, mas a linha da viatura não é descartada.
- `SELECT v.Matricula, c.Nome`: `NomeCliente` a `NULL` é o sinal esperado de "sem cliente", não um erro nos dados.
- `ORDER BY v.Matricula`: só para uma listagem legível; não influencia quais linhas aparecem.

Erro típico neste passo: filtrar a seguir com `WHERE c.Nome IS NOT NULL` "para não mostrar linhas em branco" — isso transforma o `LEFT JOIN` num `INNER JOIN` e elimina exatamente as viaturas sem cliente que o enunciado pediu para manter (ver exemplo 3).

### 2. Reconciliação de clientes e viaturas nos dois sentidos (médio)

**Problema**: numa auditoria de dados, a oficina quer, numa única consulta, ver quantas viaturas não têm nenhum cliente associado e quantos clientes não têm nenhuma viatura associada — os dois lados ao mesmo tempo, para perceber a dimensão do problema de dados antes de o corrigir.

```sql
-- não executado
SELECT
    SUM(CASE WHEN c.ClienteId IS NULL THEN 1 ELSE 0 END) AS ViaturasSemCliente,
    SUM(CASE WHEN v.ViaturaId IS NULL THEN 1 ELSE 0 END) AS ClientesSemViatura
FROM Viaturas AS v
FULL JOIN Clientes AS c
    ON c.ClienteId = v.ClienteId;
```

Passo a passo:
- `FROM Viaturas AS v FULL JOIN Clientes AS c ON c.ClienteId = v.ClienteId`: o `FULL JOIN` devolve três tipos de linha: pares correspondidos, viaturas sem cliente (`c.*` a `NULL`) e clientes sem viatura (`v.*` a `NULL`). Nenhuma linha de nenhuma das duas tabelas é descartada.
- `SUM(CASE WHEN c.ClienteId IS NULL THEN 1 ELSE 0 END)`: conta as linhas do primeiro tipo de "buraco" — testar `IS NULL` na chave de junção é a forma correta de perguntar "esta linha não teve par", porque é exatamente essa coluna que o `FULL JOIN` deixa a `NULL` quando não há correspondência.
- A segunda soma faz o mesmo do lado dos clientes.
- Nenhuma condição destas está no `WHERE` a filtrar um atributo de negócio (como `Custo` ou `DataReparacao`) — está a testar a própria chave de junção, depois de a junção já ter decidido o que preservar. É por isso que este `WHERE` (se existisse, por exemplo `WHERE c.ClienteId IS NULL OR v.ViaturaId IS NULL` numa versão que lista as linhas em vez de as somar) não é o mesmo erro do exemplo 3: aqui estás a perguntar "houve correspondência?", não a aplicar um filtro de negócio que só faz sentido quando há correspondência.

Erro típico neste passo: esquecer que o SQL Server suporta `FULL JOIN` nativamente (ao contrário do MySQL, que obriga a simular com `UNION` de dois `LEFT JOIN`) — em T-SQL não precisas desse contorno.

### 3. Reparações caras por viatura, sem perder as viaturas sem reparações caras (nível de exame)

**Problema**: a oficina quer ver, para cada viatura, os dados de uma reparação com custo superior a 200€, mas sem perder da lista as viaturas que nunca tiveram uma reparação assim (ou nenhuma reparação). Estas viaturas devem aparecer com `DataReparacao` e `Custo` a `NULL`.

Versão errada (o erro do registo `0007-left-join-where`, aqui sobre `Custo` em vez de sobre o estado de uma encomenda):

```sql
-- não executado — ERRADO, incluído só para mostrar a falha
SELECT
    v.Matricula,
    r.DataReparacao,
    r.Custo
FROM Viaturas AS v
LEFT JOIN Reparacoes AS r
    ON r.ViaturaId = v.ViaturaId
WHERE r.Custo > 200.00
ORDER BY v.Matricula;
```

Porque falha: nas viaturas sem reparação (ou só com reparações baratas), `r.Custo` é `NULL`. A condição `r.Custo > 200.00` avaliada sobre `NULL` dá `UNKNOWN`, que o `WHERE` trata como "não incluir". O resultado perde precisamente as viaturas que o `LEFT JOIN` tinha preservado — a consulta comporta-se como um `INNER JOIN` com um filtro extra, apesar de estar escrita com `LEFT JOIN`.

Versão correta:

```sql
-- não executado
SELECT
    v.Matricula,
    r.DataReparacao,
    r.Custo
FROM Viaturas AS v
LEFT JOIN Reparacoes AS r
    ON r.ViaturaId = v.ViaturaId
    AND r.Custo > 200.00
ORDER BY v.Matricula;
```

Passo a passo:
- `FROM Viaturas AS v`: continuamos a garantir que toda e qualquer viatura fica no resultado.
- `LEFT JOIN Reparacoes AS r ON r.ViaturaId = v.ViaturaId AND r.Custo > 200.00`: a condição sobre `Custo` entra no `ON`, ao lado da condição de junção. Isto decide quais linhas de `Reparacoes` são candidatas a combinar com cada viatura — mas nunca decide se a viatura em si fica ou não fica. Se nenhuma reparação daquela viatura tiver `Custo > 200.00`, a viatura ainda aparece uma vez, com `r.*` a `NULL`.
- Não há `WHERE` nenhum a filtrar o lado direito depois da junção.
- Erro típico neste passo: exatamente o do registo `0007` — colocar a condição no `WHERE` em vez do `ON`, porque "funciona" num `INNER JOIN` e a diferença só aparece quando há linhas sem correspondência. Pergunta de defesa oral: "Que valor tem `r.Custo` nas linhas que o `LEFT JOIN` acrescentou para as viaturas sem reparação cara? O que dá `NULL > 200.00`?"

## Erros comuns

| Erro | Porque acontece | Como o detetar no teu trabalho |
|---|---|---|
| Condição sobre a tabela "opcional" no `WHERE` em vez do `ON` (liga ao registo `0007`) | Em `INNER JOIN` dá o mesmo resultado nos dois sítios, por isso o hábito não é corrigido até aparecer uma junção externa | Para cada condição no `WHERE`, pergunta: "esta coluna pode ser `NULL` numa linha que o `LEFT`/`RIGHT`/`FULL JOIN` acrescentou? Se sim, quero mesmo perder essa linha?" |
| `COUNT(*)` depois de uma junção externa conta 1 em vez de 0 para o lado sem correspondência (liga ao registo `0008`) | `LEFT JOIN` sem correspondência ainda produz uma linha (com `NULL`s); `COUNT(*)` conta linhas, não valores não-nulos | Troca `COUNT(*)` por `COUNT(<coluna da tabela do lado que pode faltar>)`; se os números mudarem, tinhas o erro |
| Confundir qual tabela `RIGHT JOIN` preserva | É a junção menos usada; a maioria reescreve como `LEFT JOIN` trocando a ordem das tabelas, e troca-se a ordem sem trocar o raciocínio | Reescreve o `RIGHT JOIN` como `LEFT JOIN` com as tabelas trocadas e confirma que o resultado esperado é o mesmo |
| `FULL JOIN` a duplicar linhas | A condição do `ON` não é exatamente a chave (por exemplo, comparar por `Matricula` em vez de `ViaturaId`, quando pode haver ambiguidade) | Confirma que a condição do `ON` usa a chave estrangeira e a chave primária correspondentes, não um atributo que possa repetir-se |
| `= NULL` em vez de `IS NULL` ao testar "esta linha não teve correspondência" | `NULL` não é um valor comparável com `=`; `x = NULL` dá sempre `UNKNOWN`, nunca `TRUE` | Predizer o resultado de `WHERE c.ClienteId = NULL` vs `WHERE c.ClienteId IS NULL` numa tabela com linhas sem correspondência |
| `NOT IN` contra uma subquery que pode devolver `NULL` | Se um só valor da lista for `NULL`, `x NOT IN (...)` deixa de conseguir provar `TRUE` para qualquer `x`, e o resultado fica vazio | Preferir `NOT EXISTS` ou um `LEFT JOIN ... WHERE <chave da direita> IS NULL`, e testar com um valor `NULL` na lista |

## Prática (respostas escondidas)

1. Escreve uma query que liste todas as reparações (`ReparacaoId`, `DataReparacao`) e a matrícula da viatura correspondente, usando `Reparacoes` como tabela âncora, de forma a que uma reparação cujo `ViaturaId` não exista em `Viaturas` (erro de importação) ainda apareça, com `Matricula` a `NULL`.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       r.ReparacaoId,
       r.DataReparacao,
       v.Matricula
   FROM Reparacoes AS r
   LEFT JOIN Viaturas AS v
       ON v.ViaturaId = r.ViaturaId
   ORDER BY r.ReparacaoId;
   ```
   Porquê: `Reparacoes` é a tabela âncora (`FROM`), por isso todas as suas linhas ficam; `Viaturas` é o lado opcional do `LEFT JOIN`.
   </details>

2. Reescreve a query do exercício 1 usando `RIGHT JOIN` em vez de `LEFT JOIN`, mantendo o mesmo resultado.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       r.ReparacaoId,
       r.DataReparacao,
       v.Matricula
   FROM Viaturas AS v
   RIGHT JOIN Reparacoes AS r
       ON v.ViaturaId = r.ViaturaId
   ORDER BY r.ReparacaoId;
   ```
   Porquê: `RIGHT JOIN` preserva a tabela à direita da palavra `JOIN`; pôr `Reparacoes` à direita tem o mesmo efeito que a tê-la como âncora de um `LEFT JOIN`.
   </details>

3. A oficina suspeita de dados inconsistentes entre `Clientes` e `Viaturas`. Escreve uma query com `FULL JOIN` que devolva o número de viaturas sem cliente associado e o número de clientes sem viatura associada, numa só linha de resultado.
   <details><summary>Resposta</summary>

   ```sql
   SELECT
       SUM(CASE WHEN c.ClienteId IS NULL THEN 1 ELSE 0 END) AS ViaturasSemCliente,
       SUM(CASE WHEN v.ViaturaId IS NULL THEN 1 ELSE 0 END) AS ClientesSemViatura
   FROM Viaturas AS v
   FULL JOIN Clientes AS c
       ON c.ClienteId = v.ClienteId;
   ```
   Porquê: o `FULL JOIN` traz os dois tipos de "buraco" ao mesmo tempo; testar `IS NULL` na chave de junção (não num atributo de negócio) identifica cada tipo sem arriscar eliminar linhas.
   </details>

4. Esta query devia listar todas as viaturas com a reparação mais recente feita depois de 2026-01-01, sem perder as viaturas sem nenhuma reparação depois dessa data. O que está mal, e como corrigir?

   ```sql
   SELECT
       v.Matricula,
       r.DataReparacao
   FROM Viaturas AS v
   LEFT JOIN Reparacoes AS r
       ON r.ViaturaId = v.ViaturaId
   WHERE r.DataReparacao > '2026-01-01'
   ORDER BY v.Matricula;
   ```
   <details><summary>Resposta</summary>
   Está mal: `WHERE r.DataReparacao > '2026-01-01'` corre depois do `LEFT JOIN`, e nas viaturas sem reparação recente `r.DataReparacao` é `NULL`; `NULL > '2026-01-01'` dá `UNKNOWN`, o `WHERE` descarta essas linhas, e a query passa a comportar-se como `INNER JOIN`. Correção: mover a condição para o `ON`.

   ```sql
   SELECT
       v.Matricula,
       r.DataReparacao
   FROM Viaturas AS v
   LEFT JOIN Reparacoes AS r
       ON r.ViaturaId = v.ViaturaId
       AND r.DataReparacao > '2026-01-01'
   ORDER BY v.Matricula;
   ```
   Este é o mesmo erro do registo `0007`, com `DataReparacao` em vez do estado de uma encomenda.
   </details>

5. Considera uma tabela `Viaturas` com 3 linhas (uma delas sem nenhuma reparação em `Reparacoes`) ligada por `LEFT JOIN` a `Reparacoes`, sem `GROUP BY` nenhum — só o resultado bruto da junção. Quantas linhas tem esse resultado? Que valor dá `COUNT(*)` sobre esse resultado completo, e que valor dá `COUNT(r.ReparacaoId)`? Porque são diferentes?
   <details><summary>Resposta</summary>
   O `LEFT JOIN` produz uma linha por cada reparação existente, mais uma linha extra (com `r.*` a `NULL`) para a viatura sem nenhuma reparação — essa linha "fantasma" existe no resultado, apesar de não haver reparação nenhuma nela. `COUNT(*)` conta essa linha porque conta linhas, sem olhar para o conteúdo; `COUNT(r.ReparacaoId)` não a conta, porque `COUNT(coluna)` ignora `NULL`s. É por isso que, ao agrupar por viatura, `COUNT(*)` dá 1 para uma viatura sem reparações em vez de 0 — o erro do registo `0008` — e `COUNT(r.ReparacaoId)` dá o valor correto.
   </details>

6. Num relatório com `FULL JOIN` entre `Clientes` e `Viaturas`, queres mostrar só os pares reais (cliente com viatura associada) cuja `Matricula` comece por `'AA'`, mas sem perder os clientes sem viatura nem as viaturas sem cliente do resultado. Onde deve ir o filtro de matrícula — `ON` ou `WHERE`? Porquê?
   <details><summary>Resposta</summary>
   No `ON`, junto à condição de junção (`AND v.Matricula LIKE 'AA%'`). Se fosse para o `WHERE`, um cliente sem viatura (onde `v.Matricula` é `NULL`) seria eliminado, porque `NULL LIKE 'AA%'` dá `UNKNOWN` — exatamente o mesmo mecanismo do exercício 4, aqui aplicado a um `FULL JOIN` em vez de um `LEFT JOIN`.
   </details>

## Fontes

| Fonte | Onde | Usado para | Verificado |
|---|---|---|---|
| SYLLABUS.md (workspace da cadeira) | tema 3 "Junções externas (LEFT, RIGHT, FULL)", peso alto, estado seen | justificar o "Porquê agora" e a data do Teste 1 | verificado no workspace |
| records/0007-left-join-where.md | box 1 (repetição espaçada) | escolher o exemplo 3 e os exercícios 4 e 6 | verificado no workspace |
| records/0008-count-star-outer.md | box 1 (repetição espaçada) | escolher o exercício 5 | verificado no workspace |
| assignments/tp1/STATEMENT.md | enunciado do TP1 (Socios/Livros/Emprestimos) | garantir que nenhum exemplo ou exercício acima reproduz as três tarefas pedidas no TP1 (usar domínio da oficina, não da biblioteca) | verificado no workspace |
| Conhecimento do modelo sobre T-SQL (LEFT/RIGHT/FULL JOIN, ON vs WHERE, COUNT(*) vs COUNT(coluna)) | não aplicável (sem acesso à web hoje) | conceitos, sintaxe e todos os exemplos e exercícios | não verificado |
