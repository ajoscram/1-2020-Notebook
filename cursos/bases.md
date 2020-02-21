### Joins

Cláusulas para conbimar dos o más tablas. Recordatorio de joins:

![tabla joins](https://ingenieriadesoftware.es/wp-content/uploads/2018/07/sqljoin.jpeg)

Ejemplo desarrollado en clase dónde settea una variable dentro de un `select`:

```sql
declare @earned float;

select @earned = @earned*percentage + commission
from tbSalesCommRange
where low <= @earned and @earned < high

insert into tbSalesTransactions values(@nickName, getDate(), @earned)
```

El operador [CUBE](https://www.sqlservertutorial.net/sql-server-basics/sql-server-cube/) genera un cubo multidimensional. [ROLLUP](https://www.sqltutorial.org/sql-rollup/) es una versión limitada de CUBE dónde se restrigen las combinaciones creadas.