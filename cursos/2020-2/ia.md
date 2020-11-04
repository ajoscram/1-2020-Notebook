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
!> recordar esto

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

**Quiz:** Exposicion ejemplo grafico, pseudocodigo, codigo sobre el ejemplo grafico

### Algebra Lineal

Vectores

### Entorno

Los entornos de un agente son todo factor externo al agente que influencian su accionar y que son afectados por sus acciones. Estos pueden ser:

| Característica | Definición |
| :--- | :--- |
| **Observables** | tiene el acceso al entorno **completo** en cualquier momento dado |
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
| **Discreto** | | 
| **Contínuo** | |
|||
| **Conocidos** | |
| **Desconocidos** | |

Por ejemplo para los siguientes agentes se pueden analizar sus entornos:

| Característica | Solitario | Compra por Internet | Taxi Autónomo | Ajedrez con Reloj | Diagnóstico Médico | Controlador Refinería |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Observable** | No | Sí | No | Sí | No | No |
| **Determinista** | No | Sí | No | No | No | No |
| **Secuencial** | Sí | Sí | Sí | Sí | Sí | Sí |
| **Estático** | Sí | No | No | Sí | Sí | No |
| **Discreto** | Sí | Sí | No | Sí | Sí | No |
| **Mono-agente** | Sí | Sí | No | No | Sí | Sí |

### Agentes

La IA se define com el estudio de **agentes racionales**. Un agente racional es cualquier cosa que tome decisiones. Para tomar decisiones toman en cuenta percepciones pasadas y actuales.

Un sistema de IA está compuesto por un agente y su entorno. Los agentes **actúan** en su entorno.
Bajo su entorno, un agente es cualquier cosa que:
* percibe su entorno a partir de sensores
* actuar sobre su entorno a partir de actuadores

Los agentes tienen dos componentes primordiales:
* **Arquitectura:** La manifestación física de un agente que aloja un programa agente.
* **Programa Agente:** Es una implementación de una **función agente** (una secuencia de percepción a una acción).

![agente](https://imgur.com/zGmeBA5.png)

El agente percibe de su entorno mediante **sensores**, y dependiendo de lo percibido realiza acciones mediante **actuadores**.

Se debe tener una **medida de rendimiento** que define que tan efectiva es la racionalidad del agente. Se desea que el agente maximice dicha medida. Esa medida de rendimiento es una función del impacto que tenga el agente en el entorno que existe. Las acciones por parte del agente pueden incrementar o decrementar esa medida.

En general, para diseñar un agente se deben tomar en cuenta los **PEAS** (performance, environment, actuators, sensors). Por ejemplo en un servicio de taxi autónomo:

| Taxi Autónomo | Ejemplos |
| :--- | :--- |
| Performance | `+` llegar al destino, `+` uso eficiente de combustible, `+` velocidad, `+` respeta leyes de tránsito, `-` atropellar, `-` dañar propiedad |
| Environment | Las calles, semáforo, señales de tránsito, huecos, clima, personas |
| Actuators | Las ruedas que lo mueven por la calle, los frenos, las luces, bolsas de aire, puertas, interfaces de usuario |
| Sensors | Cámaras, sensores de proximidad, interfaces de usuario, sensores de humedad, acelerómetro, sensor de temperatura, sensor de cinturón |

---

leer seccion de agentes del libro de IA, task environments

1era clase----------------------------------------------------------

leer capitulo historia de la inteligencia artificial

hacer linea de tiempo con los avances y personajes importantes en portafolio

Disciplinas relacionadas a IA:
    Matemáticas (Computación, Probabilidad, Lógica)
    Economía (teoría de desición, teoría de juegos)
    Filosofía (Racionalismo, Dualismo)
    Neurociencia

AGENTES:   
    se busca que comporten 

INTELIGENCIA:
    habilidad para adquirir y aplicar conocimiento
    analizar el sentido que puede tomar una proposición, dicho o expresión

INTELIGENCIA ARTIFICIAL:
    Disciplina científica para crear programas informáticos que utilicen razonamiento lógico y se comporte como la mente humana. Se utiliza para:
        Tareas repetitivas
        Las tareas consumen muchos recursos si se delegan a humanos
        Tareas muy peligrosas, o con mucha precisión

Metodología del curso

Primera parte clase magistral, segunda ejercicios

Clases laboratorios investigaciones y tareas y proyecto grupal final quices exposiciones

proactividad es clave

hay actividades lúdicas

quices (pueden ser sorpresa)

Código de curso en el subject

entrega de proyecto:
    defensa
    bibliografía APA 6

entregables de evaluaciones:
    tecdigital
    Entrega por correo electrónico al profesor y asistente con copia a todos los integrantes del grupo antes de la fecha y hora límites.
    Se entrega en ZIP no RAR.

Evaluaciones:
    Laboratorios
            Colab - Jupiter y HTML para laboratorios
            Se pueden terminar extraclase
    Investigaciones
    Tareas
    Quices
    Exposiciones:
        Comunicación formal
        Faltar a una presentacion resta 30% de la nota al integrante del grupo
    Exámenes:
        15% después de redes neuronales
        10% final
    Portafolio de evidencias:
        Resumen gráfico de cada clase del semestre con material reciclado

Collab search:
    Jupiter y HTML para laboratorios

Libros:
    artificial intelligence a modern approach

Dudas de notas:
    5 días hábiles para apelar notas