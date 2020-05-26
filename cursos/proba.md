# Probabilidades

<!--
### Tercer Parcial:

#### Teorema del límite central
##### [Video](https://youtu.be/1_xwjki12cs)



#### Ley de grandes números
##### [Video](https://youtu.be/SD24edQpQO0)



#### Generalidades
##### [Video](https://youtu.be/exJiuy_hLms)



#### Distribución Gamma
##### [Video](https://youtu.be/qTafWIKAOV8)



#### Distribución exponencial
##### [Video](https://youtu.be/p6eqD8NrNrw)



-->
### Segundo Parcial:
<!--
#### Variables continuas
##### [Video](https://youtu.be/al2dE0bv9PA)



#### Distribución normal
##### [Video](https://youtu.be/1D-DSh22Fpg)



#### Distribución hipergeométrica
##### [Video](https://youtu.be/IdfvSBP_KO0)



#### Distribución geométrica
##### [Video](https://youtu.be/8zUM8j6Pbck)



#### Distribución binomial
##### [Video I](https://youtu.be/8_c6_FNen3o), [Video II](https://youtu.be/K4TdphFhagE)



#### Distribución de probabilidad
##### [Video](https://youtu.be/SPr5mc7vbBc)



#### Variables aleatorias
##### [Video](https://youtu.be/D6q5rn-tEeI)



-->
### Primer Parcial:

#### Objetos distinguibles
##### [Video](https://youtu.be/eW-1u9FxB4Y)

Un conjunto de **objetos distinguibles** son aquellos cuyas diferencias son importantes para el análisis probabilístico, y por ende el orden en que se escogen importa. Cada objeto es único.

#### Objetos indistinguibles
##### [Video](https://youtu.be/bsZNypnKza0)

Un conjunto de **objetos indistinguibles** son aquellos cuyas diferencias no son relevantes para el análisis probabilístico, y por ende su orden es indistinto (se cuentan como el mismo objeto). Si se tienen cinco bolas rojas estas no son iguales en todo sentido, pero todas son indistinguibles por su color.

Si se quieren acomodar *n* objetos indistinguibles en *k* celdas, una manera de pensarlo es que cada celda es separada por *k* − 1 objetos de otro tipo. Se agregan los objetos al conjunto inicial y se tienen un total de *n* + *k* − 1 objetos, de los cuales se seleccionan *k* − 1. Esto se puede expresar mediante un coeficiente binomial para encontrar todas las formas de acomodarlas, así:

![coeficiente binomial indistinguible](https://imgur.com/K2ehXYZ.png)

O *n* + *k* − 1 escoge *k* − 1.

#### Coeficiente Binomial

Se utiliza para encontrar el número total de subconjuntos posibles de tamaño *k* hecho a partir de los elementos de cualquier conjunto de tamaño *n*, y se escribe así:

![coeficiente binomial](https://www.gstatic.com/education/formulas/images_long_sheet/en/binomial_coefficient.svg)

Esto se lee ***n* escoge *k***.

#### Conteo
##### [Video](https://youtu.be/raum73br0kA)

El **principio de la suma** dicta que si *A* y *B* son conjuntos finitos disjuntos (que no tienen elementos repetidos) entonces:

| *A* ∪ *B* | = | *A* | + | *B* |

El **principio del producto** dicta que si *A* y *B* son conjuntos finitos entonces la cardinalidad de su producto cartesiano es:

| *A* × *B* | = | *A* | · | *B* |

Por ejemplo:

>*Suponga A = {1,2,3,4} y se quieren formar números de dos dígitos distintos. Cuántos números hay?*

Hay cuatro posibilidades para el primero y tres para el segundo, entonces la respuesta es (por el principio del producto):

4 · 3 = **12**

>*Cuántos de estos son pares?*

Primero se seleccionan las unidades. Se tienen sólamente dos posibles valores para números pares: dos y cuatro. Entonces serían dos posiblidades para el valor de las unidades y los tres números restantes para el de las decenas. Se cuentan mediante el principio del producto, así:

2 · 3 = **6**

---

>*Suponga A = {0,1,2,...,9}. Cuántos números de tres dígitos distintos hay?*

Primero se seleccionan las centenas, pues no pueden incluir un cero. Se tienen entonces nueve posibilidades. Luego hay nueve más para las decenas porque se incluye el cero, y ocho restantes para las unidades. Se cuentan mediante el principio del producto, sí:

9 · 9 · 8 = 81 · 8 = **648**

>*Cuántos de estos son pares?*

Cómo hay dos condiciones es más fácil dividir el problema en dos casos primero:
* El número termina en cero: Si el número termina de fijo en cero, entonces hay nueve posibilidades para las centenas y ocho para las decenas. Las unidades sólo pueden incluir al cero.
* El número no termina en cero: en ese caso se tienen 2,4,6,8 como posibles valores para las unidades. En las centenas no se puede incluir el cero, entonces hay ocho posibles valores. En las decenas se ponen los ocho valore restantes.

Los resultados de ambos casos se cuentan mediante el principio del producto, y se suman para contar todos los posibles números por el principio de suma, así:

(9 · 8 · 1) + (4 · 8 · 8) = 72 + 256 = **328**

---

#### Permutación y combinación
##### [Video](https://youtu.be/3jW3g7jfQuc), [Ejemplos I](https://youtu.be/4fy9u6l_-Ok), [Ejemplos II](https://youtu.be/seDovNqsjv4)

Una **permutación** de un conjunto de elementos es un ordenamiento de dichos elementos. El conjunto de permutaciones son todos los posibles ordenamientos de ese conjunto.

Suponga un conjunto *A* tal que | *A* | = n. El total de maneras de permutar ese conjunto es **n!**.

Se pueden aplicar restricciones al momento de permutar, por ejemplo:

>*Se tiene 5 personas y se acomodan en una fila. Se desea obtener el conjunto de permutaciones, con la restricción de las personas Andrés y Santiago queden juntas.*

Se considera a Andrés y Santiago como una sola unidad, y luego se permutan entre sí por aparte. Entonces la respuesta sería:

4! · 2! = 4 · 3 · 2 + 2 = **26**

---

>*Se tiene 5 personas y se acomodan en una fila. Se desea obtener el conjunto de permutaciones, con la restricción de que Andrés y Santiago queden **separados**.*

Tomando cómo base el ejemplo anterior, se considera el total del acomodos sin restricciones y se le resta la cantidad que queden juntos, así:

5! − (4! · 2!) = 120 − 26 = **94**

---

Suponga un conjunto *A* tal que | *A* | = n. Si se desea permutar *A* de forma que las permutaciones resultantes sean un subconjunto *B* de *A* tal que | *B* | = k, entonces el total de permutaciones es:

![formula permutaciones](https://i1.wp.com/www.fairlynerdy.com/wp-content/uploads/2016/02/permutations-1.png?resize=768%2C313)

Las permutaciones son usadas cuando el orden de los elementos resultantes importa, dado a que este se toma en cuenta en los cálculos. **Si el orden no importa**, se usan combinaciones.

Una **combinación** se calcula igual que una permutación, pero al final se eliminan todos los conteos extra de orden que conlleva el cálculo de la permutación, así:

![formula conbinaciones](https://i2.wp.com/www.fairlynerdy.com/wp-content/uploads/2016/02/combinations.png?resize=768%2C297)


Por ejemplo:

>*Se tiene una clase con 10 personas y se desea elegir 3 de estas personas para entregarles 3 premios, sin ningún orden.*

Simplemente aplicando la fórmula anterior:

10! / ( ( 10 - 3 )! · 3! )

= ( 10 · 9 · 8 · 7 · 6 · 5 · 4 · 3 · 2 ) / ( 7 · 6 · 5 · 4 · 3 · 2 ) · ( 3 · 2 )

= ( 10 · 9 · 8 ) / ( 3 · 2 )

= 10 · 3 · 4

= **120**

---

**En resumen:**

* Para encontrar las permutaciones de un conjunto completo:
    1. Saque factorial a su cardinalidad.

* Para encontrar las permutaciones de un conjunto parcial:
    1. Encuentre las permutaciones del conjunto completo.
    2. Divida por la cantidad de permutaciones de los elementos no contados.

* Para encontrar las combinaciones de un conjunto parcial:
    1. Encuentre las permutaciones del conjunto completo
    2. Divida por la cantidad de permutaciones de los elementos no contados.
    3. Divida por la cantidad de permutaciones de los elementos contados.

#### Probabilidad total
##### [Video](https://youtu.be/cwr9WcLG7bI)

Sea *Ω* un conjunto, y *Ω1*, *Ω2*, ..., *Ωn* subconjuntos de *Ω* tales que:

* *Ω1* ∪ *Ω2* ∪ ... ∪ *Ωn* = *Ω*
* *Ωi* ∩ *Ωj* = ∅, ∀ *i* ≠ *j*

Entonces *Ω1*, *Ω2*, ..., *Ωn* son **particiones** de *Ω*.

En otras palabras, una partición es un subconjunto que no tiene elementos repetidos con otras particiones del mismo superconjunto. Gráficamente se puede apreciar así:

![particion](https://upload.wikimedia.org/wikipedia/commons/8/8c/Partition_of_a_set.png)

Si *A* es un evento, se puede descomponer como una unión de eventos disjuntos *A1*, *A2*, *A3*, ..., *An*, así:

*A* = ( *A* ∩ *A1* ) ∪ ( *A* ∩ *A2* ) ∪ ... ∪ ( *A* ∩ *An* )

Y luego, por propiedades de probabilidades:

P [ *A* ]

= P [ *A* ∩ *A1* ] + P [ *A* ∩ *A2* ] + ... + P [ *A* ∩ *An* ]

= P [ *A* | *A1* ] · P [ *A1* ] + P [ *A* | *A2* ] · P [ *A2* ] + ... + P [ *A* | *An* ] · P [ *An* ]

Esto se conoce como la **regla de las probabilidades totales**.

#### Regla de Bayes

![teorema de bayes](https://i.imgur.com/FaKcbJr.png)

Esta regla es una consecuencia directa de la fórmula de probabilidad condicional, porque la operación de intersección es conmutativa, así:

P [ *A* ∩ *B* ]

= P [ *B* ∩ *A* ]

= P [ *B* | *A* ] ⋅ P [ *A* ]

El teorema de Bayes es muy importante para determinar la probabilidad de eventos previos dado que ya se conoce su resultado.

#### Probabilidad condicional
##### [Video](https://youtu.be/IfH7GdEZ9R4)

La **probabilidad condicional** es la probabilidad de que un evento ocurra dado que otro evento ocurrió de fijo. Si se sabe que un evento *B* ocurrió, la probabilidad de que un evento *A* ocurra dado *B* se escribe así:


P [ *A* | *B* ]


En caso de que el resultado de *A* dependa del resultado de *B* entonces se dice que **A depende de B**. Se puede calcular el resultado mediante la siguiente fórmula:

![formula condicional](https://i0.wp.com/www.profesor10demates.com/wp-content/uploads/2013/09/Probabilidadcondicionada.png?fit=240%2C89&ssl=1)

Si P [ *A* | *B* ] = P [ *A* ] entonces *A* y *B* son **eventos independientes**. Esto implica por la fórmula anterior que:

P [ *A* ∩ *B* ] = P [ *A* ] ⋅ P [ *B* ]

En otras palabras, la probabilidad de que ocurran dos eventos independientes es igual a multiplicar sus probabilidades.

#### Enfoques de probabilidad
##### [Video](https://youtu.be/YXg1514bO_c)

Hay dos enfoques:

* **Estadístico:** Si se tiene un experimento aleatorio *X* y un evento *A*, se repite *X* una cantidad *n* de veces y se hace un estudio de la cantidad de veces que ocurrió *A*.
* **Teórico:** Se hace cuando se conoce las características del espacio muestral y el evento en estudio. Esto permite hacer un análisis teórico de la probabilidad del evento.

#### Probabilidad básica
##### [Video](https://youtu.be/xjZGYEMU7Ls)

Teniendo en cuenta un experimento aleatorio cualquiera, un **evento** es un subconjunto del espacio muestral.

**Regla de Laplace:** Si todos los elementos del espacio muestral tienen la misma probabilidad, entonces se cumple que:

![regla laplace](http://2.bp.blogspot.com/-OOg-lzA4Ids/TpyqzfmKj7I/AAAAAAAAAxQ/OoUOGUQf-zw/s400/ecuacion4.jpg)

Con *A* siendo un evento cualquiera del espacio muestral total y *P(A)* la probabilidad de que ocurra. Los *casos favorables* corresponden al total de elementos del evento, y los *casos posibles* al total de elementos del espacio muestral.

#### Espacio muestral
##### [Video](https://youtu.be/bjLnFE_CbFg)

El **espacio muestral** se refiere a todos los posibles resultados de un experimento aleatorio.

Por ejemplo:

>*Se posee una urna con 4 bolitas negras y 3 bolitas blancas. Se extrae una muestra de 4 bolitas; ¿Cuántas bolitas negras se han sacado?*

En este caso el espacio muestral sería el conjunto **{1,2,3,4}** .

---

#### Inclusión y exclusión
##### [Video](https://youtu.be/NLdtPc0guFA)

La **cardinalidad** la cantidad de elementos en un conjunto. Siempre será un número entero mayor o igual a cero. Sea *A* un conjunto, su cardinalidad se denota con | *A* |. 

Suponiendo dos conjuntos *A* y *B* cualesquiera, si *A* ∩ *B* ≠ ∅, entonces *A* ∪ *B* puede escribirse así:

* *A* ∪ *B* = ( *A* − *B* ) ∪ ( *B* − *A* ) ∪ ( *A* ∩ *B* )
* *A* ∪ *B* = ( *A* − *B* ) ∪ *B*
* *A* ∪ *B* = ( *B* − *A* ) ∪ *A*

El **principio de inclusión y exclusión** dicta que la cardinalidad de *A* ∪ *B* se puede calcular sumando las cardinalidades de *A* y *B* y quitando la cardinalidad de la intersección (que son los repetidos); de la siguiente forma:
* | *A* ∪ *B* | = | *A* | + | *B* | - | *A* ∩ *B* |

El principio se puede extender a cualquier cantidad de conjuntos. En general:

![inclusion exclusion](https://1.bp.blogspot.com/-oD4oa8jVeDQ/T_adITg4sRI/AAAAAAAAA_4/qjgEhlUdpd4/s1600/image007.png)

#### Teoría de conjuntos
##### [Video](https://www.youtube.com/watch?v=vCd9oIlu5Tk)

**Conjunto:** Objeto al cual pertenecen elementos. Si *x* es un elemento y *A* es un conjunto, entonces:

* Si *x* ∈ *A* entonces se dice que *x* **pertenece** a *A*.
* Si *x* ∉ *A* entonces se dice que *x* **no pertenece** a *A*.

Se pueden describir de dos maneras:

* **Por extensión:** Se listan todos los elementos del conjunto.
* **Por comprensión:** Se especifica un criterio de inclusión y todo elemento del universo que lo cumpla está en él.

Si un conjunto no tiene elementos se dice que es **vacío** y se representa con ∅.

Suponiendo dos conjuntos *A* y *B* cualesquiera, se tienen las siguientes operaciones sobre conjuntos:
* **Unión:** Incluye todos los elementos de *A* y *B*. Se representa como *A* ∪ *B*.

![union](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/SetUnion.svg/280px-SetUnion.svg.png)

* **Intersección:** Incluye los elementos que se encuentran tanto en *A* como en *B*. Se representa como *A* ∩ *B*.

![interseccion](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/SetIntersection.svg/280px-SetIntersection.svg.png)

* **Diferencia:** Incluye los elementos que se encuentran en *A* pero no en *B*. Se representa como *A* − *B*.

![diferencia](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/SetDifferenceA.svg/280px-SetDifferenceA.svg.png)

### Información General

**Profesor:** Mario Marin

**Correo:**  mmarin@itcr.ac.cr

**Link del aula:** [https://us02web.zoom.us/j/6251207225](https://us02web.zoom.us/j/6251207225)

**ID de Reunión:** 625 120 7225

| Evaluación  | Peso |
| :--- | :---: |
| Tareas y Quices | 40% |
| Parcial 1 | 20 % |
| Parcial 2 | 20 % |
| Parcial 3 | 20 % |