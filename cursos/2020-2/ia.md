```
Clase 13/11/2020

Funciones de activación
Se utilizan para determnar la salida de la red neuronal, mappeando los valores resultantes entre 0 y 1, -1 y 1, etc.

Dos tipos:
    Lineales
```

```
Clase 06/11/2020

Redes Neuronales

Un perceptrón es una red neuronal de una sola capa

Se pueden encadenar varias capas juntas para crear una red neuronal.
Las capas que no interactúan con su entorno (o sea, que están en el medio) se llaman capas ocultas.
Bias
Forward propagation
Backward propagation
    Atribuir el valor de error a cada neurona
    Las neuronas más activas son las que se culpan más
Cost function
Gradient descent
funcion de activación

```

```
Clase 30/10/2020

perceptrón
    se usan para resolver poblemas de clasificación binaria
    sinápsis es una aproximación neuronal
    recibe caracteristicas (X)
    pesos

    bias: regresión lineal
    
    función de activación
    
    pasan por algo que excita o inhibe a neuronas
    saco la sumatoria de esos valores
    y dependiendo del bias se mappea bi

    angulo entre dos vectores

Algoritmo de aprendizaje de perceptrón
    (perceptron algorithm.png)


desviación estándar
```

```
Clase 23/10/2020

desviación estándar

descenso del gradiente
    (pasos_decenso_gradiente.png)

Regresión Logística Multinomial

Regresión Logística Ordinal

Sigmoide

```

---

### Algoritmos de búsqueda

**Búsquedas no informadas o ciegas:**
* **Búsqueda en profundidad:** Dado un nodo visitado, se selecciona uno de sus hijos y se visita hasta topar la solución o recorrer todo el árbol. Se debe mantener una lista de los nodos visitados para evitar ciclos. 
    * Debe recordar todos los nodos visitados
    * Se asume que cualquier ruta es tan buena como las demás
* **Búsqueda en anchura:** Se visitan los nodos de un árbol por cada nivel desde la raíz.

**Búsquedas informadas o heurísticas:**
* **Escalada simple (Hill Climbing):**
    * **Maximo local:** Es un estado que es mejor que sus vecinos.
    * **Máximo global:** Es el mejor estado posible de todos.
    * **Shoulder:** 
* Steepest Ascend Hill climbing
* Stochastic Hill Climbing
* Búsqueda en haz
* Búsqueda en mejor primero

Las estrategias se evalúan mediante:
* Completitud
* Complejidad temporal
* Complejidad espacial
* Optimaalidad

---

### Álgebra Lineal

##### Vectores

Un **vector** es una cantidad que tiene dirección y magnitud, usualmente denotado como su nombre con una flecha arriba, así: $\vec{v}$. Un vector existe en un espacio vectorial, y guarda el punto de desplazamiento desde el origen en un arreglo de una dimensión. Por tanto el dominio de todos los vectores será $\R^{n}$, donde $n$ es el total de dimensiones del espacio vectorial.

Los vectores se pueden **sumar** y **restar**. Siendo $\vec{a}, \vec{v} \in \R^n$ dos vectores cualquiera, estas operaciones están definidas así:

?> $ 
\vec{a} \pm \vec{v} =
    \begin{pmatrix}
        \vec{a}_1 \pm \vec{v}_1 \\
        \vec{a}_2 \pm \vec{v}_2 \\
        ...\\
        \vec{a}_n \pm \vec{v}_n \\
    \end{pmatrix} 
$

Los vectores también se pueden **multiplicar** (o escalar) mediante **escalares**, en otras palabras un número. Siendo $\alpha \in \R$ un número, entonces esa multiplicación sería:

?> $ 
\alpha \cdot \vec{a} =
    \begin{pmatrix}
        \alpha \cdot \vec{a}_1\\
        \alpha \cdot \vec{a}_2\\
        ...\\
        \alpha \cdot \vec{a}_n\\
    \end{pmatrix} 
$

También está definido el **producto punto**. Su resultado es un **escalar**. La operación es así:

?> $ \vec{a} \cdot \vec{v} = \sum\limits_{i = 1}^n \vec{a}_i \cdot \vec{v}_i = \vec{a}_1 \cdot \vec{v}_1 + \vec{a}_2 \cdot \vec{v}_2 + ... + \vec{a}_n \cdot \vec{v}_n$

Cabe recalcar que si se piensa en los vectores como matrices, esta operación es equivalente a la multiplicación matricial:

?> $\vec{a} \cdot \vec{v}^T$

##### Matrices

Las matrices son arreglos $n$-dimensionales de números, usualmente denotadas con una letra mayúscula. Por ejemplo, sea una matriz $A \in \R^{n \times m}$, entonces esa matriz serán $n$ filas por $m$ columnas de números.

Las matrices se pueden **sumar** y **restar** igual que los vectores. Sean $A,B  \in \R^{n \times m}$ dos matrices cualquiera, entonces estas operaciones serían:

?> $ 
A \pm B =
    \begin{pmatrix}
        A_{1,1} \pm B_{1,1} & A_{1,2} \pm B_{1,2} & ... & A_{1,m} \pm B_{1,m}\\
        A_{2,1} \pm B_{2,1} & A_{2,2} \pm B_{2,2} & ... & A_{2,m} \pm B_{2,m}\\
        ... & ... & ... & ...\\
        A_{n,1} \pm B_{n,1} & A_{n,2} \pm B_{n,2} & ... & A_{n,m} \pm B_{n,m}\\
    \end{pmatrix} 
$

Las matrices también se pueden escalar igual que los vectores:

?> $ 
\alpha \cdot A =
    \begin{pmatrix}
        \alpha \cdot A_{1,1} & \alpha \cdot A_{1,2} & ... & \alpha \cdot A_{1,m}\\
        \alpha \cdot A_{2,1} & \alpha \cdot A_{2,2} & ... & \alpha \cdot A_{2,m}\\
        ... & ... & ... & ...\\
        \alpha \cdot A_{n,1} & \alpha \cdot A_{n,2} & ... & \alpha \cdot A_{n,m}\\
    \end{pmatrix} 
$



---

### Entorno

##### ¿Qué es un entorno?

Los entornos de un agente son todo factor externo al agente que influencian su accionar y que son afectados por sus acciones. Estos pueden clasificados según sus características de las siguientes formas:

| Característica | Definición |
| :--- | :--- |
| **Observable** | tiene el acceso al entorno **completo** en cualquier momento dado |
| **Parcialmente observable** | tiene acceso limitado al entorno por recursos o ruido en el entorno |
|||
| **Monoagente** | hay un único agente a la vez en el entorno |
| **Multiagente** | hay múltiples agentes a la vez |
|||
| **Competitivo** | hay varios agente compitiendo |
| **Colaborativo** | hay varios agentes trabajando por un objetivo común |
|||
| **Determinístico** | el siguiente estado del ambiente es determinado por el estado actual y la acción del agente |
| **Estocástico** | asociado a probabilidades |
|||
| **Episódico** | la siguiente acción del agente no depende del anterior |
| **Secuencial** | la siguiente acción del agente depende de acciones previas |
|||
| **Dinámico** | el entorno cambia mientras el agente está deliberando |
| **Estático** | el entorno no cambia mientras el agente delibera |
|||
| **Discreto** | el entorno tiene una cantidad de estados no contínua, usualmente finita |
| **Contínuo** | el entorno cuenta con domínios contínuos, por ejemplo tiempo |
|||
| **Conocidos** | los resultados de todas las posibles acciones del agente en el entorno son conocidas |
| **Desconocidos** | los resultados de todas las posibles acciones del agente son desconocidas |

---

### Agente

##### ¿Qué es un agente?

Un agente racional es cualquier cosa que tome decisiones. Para tomar decisiones toman en cuenta percepciones pasadas y actuales. Un sistema de IA está compuesto por un agente y su entorno. Los agentes **actúan** en su entorno. Bajo su entorno, un agente es cualquier cosa que:

* Percibe su entorno a partir de sensores
* Actua sobre su entorno a partir de actuadores

Los agentes tienen dos componentes primordiales:
* **Arquitectura:** La manifestación física de un agente que aloja un programa agente.
* **Programa Agente:** Es una implementación de una **función agente** (una secuencia de percepción a una acción).

![agente](https://imgur.com/zGmeBA5.png)

##### PEAS
Para diseñar un agente se deben tomar en cuenta sus **PEAS**. Corresponden con sus siglas en inglés:

| Aspecto | Descripción |
| :---: | :--- |
| **Performance** | Una medida de rendimiento que define que tan efectiva es la racionalidad del agente. El agente debe minimizar o maximizar esta medida. Mide el impacto que tenga el agente en su entorno. Las acciones por parte del agente pueden incrementar o decrementarla. |
| **Environment** | El entorno en el que vive el agente. Esto será abordado a más detalle en la siguiente sección de este cuaderno. |
| **Actuators** | Medios que utiliza el agente para realizar acciones en su entorno. |
| **Sensors** | Medios que utiliza el agente para percibir su entorno. |

Por ejemplo en un servicio de taxi autónomo:

| Taxi Autónomo | Ejemplos |
| :--- | :--- |
| Performance | `+` llegar al destino, `+` uso eficiente de combustible, `+` velocidad, `+` respeta leyes de tránsito, `-` atropellar, `-` dañar propiedad |
| Environment | Las calles, semáforo, señales de tránsito, huecos, clima, personas |
| Actuators | Las ruedas que lo mueven por la calle, los frenos, las luces, bolsas de aire, puertas, interfaces de usuario |
| Sensors | Cámaras, sensores de proximidad, interfaces de usuario, sensores de humedad, acelerómetro, sensor de temperatura, sensor de cinturón |

---

### Inteligencia

##### ¿Qué es inteligencia?

Es la habilidad para adquirir y aplicar conocimiento, analizando el sentido que puede tomar una proposición, dicho o expresión.

##### ¿Qué es inteligencia artificial?

Disciplina científica para crear programas informáticos que utilicen razonamiento lógico y se comporte como la mente humana. Se utiliza para tareas que:
* Son repetitivas
* Consumen muchos recursos si se delegan a humanos
* Son muy peligrosas, o requieren mucha precisión

##### Disciplinas relacionadas a IA:

* Matemáticas (Computación, Probabilidad, Lógica)
* Economía (teoría de desición, teoría de juegos)
* Filosofía (Racionalismo, Dualismo)
* Neurociencia    

!> agregar linea de tiempo con los avances y personajes importantes

---

### Información General

[Carta del curso](recursos/ia/IC_6200_Inteligencia_Artificial_-_2020_-_02.pdf ':ignore')

| | |
| :--- | :--- |
| Profesora | Adriana Álvarez |
| Correo | aalvarez@itcr.ac.cr |
| Horario de consulta | Viernes de 3:30p.m. a 5:30p.m. |

El curso sera evaluado así:

| Evaluación  | Peso |
| :--- | :---: |
| Examen 1 | 15% |
| Examen 2 | 10% |
| Laboratorio y otros | 50 % |
| Quices, otros | 20% |
| Portafolio | 5% |

##### Notas Importantes:

* 5 días hábiles para apelar notas
* El portafolio es un resumen gráfico de cada clase del semestre con material reciclado
* Se envía un archivo de HTML y el Jupyter fuente en el TEC Digital
* Se entrega en ZIP, no RAR
* Las bibliografías deben ser APA 6
* Respecto a exposiciones:
    * Comunicación formal
    * Faltar a una presentacion resta 30% de la nota al integrante del grupo
* El asunto de todo correo enviado a la profesora debe incluir el código de curso:
```
IC-6200 Resto del subject
```
* Todo nombre de archivo enviado en el TEC Digital debe tener el siguiente formato:
```
IC-6200_nombre#n.ext
```