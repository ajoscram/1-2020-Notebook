# Bases de Datos II
[Link de Zoom](https://zoom.us/j/99815087244)
[Link de Zoom Alicia](https://us02web.zoom.us/j/83150481023)

### Bases de Datos Distribuidas

Administra el almacenamiento y procesamiento de dato relacionados de forma lógica, interconectados por varios sistemas de computación. Pueden ser de dos tipos:
* **Homogéneas:** Toda máquina en el entorno utiliza la misma tecnología, tanto software ccomo hardware.
* **Heterogéneas:** Se mezclan tecnologías DBMS de software y/o máquinas.

**Características:**

* Interface de aplicaciones para interactuar con el usuario, aplicaciones, etc.
* Transparencia de distribución, transacciones, fallas, peformance y heterogeneidad. El usuario debe sentir que existe una única base de datos.

**Ventajas:**
* Los datos se encuentran cerca del sitio de demanda
* Mejora las comunicaciones
* Interfaces user-friendly
* Reduce el costo de operación
* No tiene un punto de falla único
* Independencia de procesador

**Desventajas:**
* Dificultad tecnológica
* Es bastante más caro
* Seguridad
* Backups
* Recuperación
* Complejidad de administración y control
* Requerimientos de almacenamiento intrementados

**Procesamiento Distribuido:** La base de datos está en un solo sitio, pero cada otro sitio puede acceder a los datos y hacer algo con ellos.

### Administración de Usuarios

* Cada base de datos tiene una lista de usuarios.
* Se puede realizar autenticación por: *base de datos* ó *sistema operativo*.

##### Usuarios SQLServer
* Enforce password expiration
* Enforce passwoord policy
* Must change password
* Quitar acceso a la cuenta `GUEST`
* Permiso `CONTROL SERVER`
* Un **login** es una cuenta individual de usuario para ingresar a una base de datos. El usuario se mapea a un login del servidor. Se pueden crear usuarios dependientes o no del login
* Se borran mediante `DROP USER`

### Bases de Datos Multimedia

La importancia de las bases de datos multimedia (MM-DBMS) se debe a los cambios de las tecnologías. **Datos multimedia** se refieren a un rango de diferentes tipos de datos: **documentos, imágenes, audio, o video**. Hay varios retos a cumplir para manejar una de estas bases de datos:
  * **Tiempo:** El tiempo no puede correr hacia atrás 
  * **Requerimientos Básicos:** Integración, independencia de datos, control de concurrencia, consultas, almacenamiento eficiente.
  * **Presentación y entrega:** 

### Arquitectura Oracle

Se divide en general en 
Procesos de base

**System Global Area**

**Program Global Area**

**Shared Global Area**

1. **Shared SQL:** 
2. **Database Buffer Cache:**
3. **Redo Buffer Log:**

**Archivos de base**

**Archive**

**Data files** Los archivos físicos escritos en disco dónde se guardan los datos.

**Tablespace** 
    
  * Son una unidad lógica de almacenamiento que se encarga de ligar entre la lógica de SQL y los archivos físicos de la BD.
  * Cada base de datos tiene al menos uno llamado `SYSTEM`. 
  * Un tablespace puede pertenecer a solo una BD.
  * Puede estar online o offline.

**Segmentos**

Todos los datos de la BD están almacenadas en segmentos. Hay 5 tipos de segmentos: **

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