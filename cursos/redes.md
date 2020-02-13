# Redes

### Acceso al Medio

Hay dos tipos de equipo en toda red:

* **Pasivos:** Son "estúpidos" y pertenecen a la capa 1 de OSI. Ejemplos: *repetidor, hub, puente*.
* **Activos:** Son "inteligentes" y perteneces a las capas 2 o superior del OSI. Ejemplos: *switch*.

Hay tres maneras mediante las cuales se puede transportar información a través de una red:

* **Semi-Duplex:** Solo se puede enviar o recibir información por el medio físico, pero no los dos.
* **Half-Duplex:** Se puede enviar o recibir información, pero no al mismo tiempo.
* **Full-Duplex:** Se puede enviar y recibir información al mismo tiempo.

Todas las máquinas en una red cuentan con una [NIC (Network Interface Card)](https://es.wikipedia.org/wiki/Tarjeta_de_red). Estas tienen grabado una **dirección MAC**, que tiene este formato:

![direccion mac](https://networkencyclopedia.com/wp-content/uploads/2019/08/mac-address.jpg)

### Topologías de Red

![topologias](https://sites.google.com/site/redesbasico150/_/rsrc/1323230015750/topologias-de-red/topologias-fisicas/topologias4.JPG)

### Modelo TCP/IP

A diferencia del de OSI este es un modelo implementado en la realidad. Se separa en las siguientes capas:

| # | Nombre | Ejemplos |
| :---: | :--- | :--- |
| **3** | Aplicación | `FTP`, `HTTP`, `SMTP`, `DNS`, `TFTP` |
| **2** | Transporte | `TCP`, `UDP` |
| **1** | Internet | `IP` |
| **0** | Acceso a Red | Una `LAN` o `WAN` |

### Modelo OSI

Modelo teórico usado para comparar una red con otra red. Se separa en las siguientes capas:

| # | Nombre | Unidad |
| :---: | :--- | :--- |
| **7** | Aplicación | Datos |
| **6** | Presentación | Datos |
| **5** | Sesión | Datos |
| **4** | Transporte | Segmentos |
| **3** | Red | Paquetes |
| **2** | Enlace de Datos | Tramas |
| **1** | Física | Bits |

### Baudios

Toda red puede ser medida mediante su **ancho de banda**. Se mide en **bps (bits por segundo)**. Originalmente, esa **b** significaba baudios en su lugar.

Un [baudio](https://es.wikipedia.org/wiki/Baudio) es una unidad de medida que representa el número de símbolos por segundo en un medio de transmición digital mediante un esquema de codificación de bits (cuyo proceso se conoce como **modulación**).

El esquema de [modulación](https://es.wikipedia.org/wiki/Modulaci%C3%B3n_(telecomunicaci%C3%B3n)) determina cómo y cuánta información digital viaja sobre una **onda portadora**. Pequeño recordatorio sobre ondas:

![ondas](https://lh3.googleusercontent.com/proxy/6WRAOqJr0f56Wwm0P5EpOraNgmMDpofGK9QtA2QppN5bQCYFpQVqIJbvam2VC1-6Sp2NlASnEQAURRHnYn8cmpdeEBb0jrXJKBEWLVyq-nxemWj_t22k-WIu40WiOzc)

### Definición de Red

Una **red** es un conjunto de dos o más nodos con **información a transmitir** entre ellos.

En la práctica, tiene un **medio físico y un protocolo** de transmición. Un protocolo de transmición son reglas que deben seguir los nodos para comunicarse.

La red también debe contar con un **sistema operativo** que administre la red.

Hay dos tipos básicos:

* **WAN:** Wide Area Network
* **LAN:** Local Area Network

### Información General

**Profesor:** Carlos Benavides

| Evaluación  | Peso |
| :--- | :---: |
| Tareas | % |
| Laboratorios | % |
| Exámenes | % |
| Videos | % |
| Proyectos | % |

El curso se pasa con solo ir a clases y entregar los laboratorios y asignaciones. Los exámenes son solo necesarios si se pierden puntos fáciles en eso.