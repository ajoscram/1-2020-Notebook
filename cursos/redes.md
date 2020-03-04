# Redes

### Seguridad de Puertos

Hay tres modos de seguridad de capa 2 en los puertos de todo switch:

| Modo | Descripción |
| :---: | :--- |
| `protect` | No permite transmisión |
| `restrict` | Registra una estadística con la cantidad de direcciones MAC erróneas |
| `shutdown` | El puerto se apaga por completo en violación |

En alguna puerto del switch, esto se registra de la siguiente manera:

```
switchport mode access
switchport port-security
switchport port-security mac-address sticky
switchport port-security violation [protect | restrict | shutdown]
```

`switchport port-security mac-address sticky` escucha la primera dirección MAC y lo registra como la única permitida.

### DHCP

[DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) es un protocolo para automáticamente asignar una dirección IP a hosts desde un servidor de red local. El servidor encargado de DHCP debe tener una dirección IP estática.

En caso de que un host no consiga una dirección IP cuando lo pide mediante ARP, entonces se autoasigna una dirección [APIPA](https://es.wikipedia.org/wiki/Automatic_Private_Internet_Protocol_Addressing).

Cada red debería tener un solo servicio DHCP en general. Para asegurar esto, en los switches de red se puede configurar de la siguiente manera:

```
enable
conf t
ip dhcp snooping vlan 1
int faX/X
switchport mode access
ip dhcp snooping trust
```

### Bloques Privados

Estas no pueden ser usadas en internet, únicamente en redes locales.

| Inicio  | Final |
| :---: | :---: |
| `10.0.0.0` | `10.255.255.255` |
| `172.16.0.0` | `172.31.255.255` |
| `192.168.0.0` | `192.168.255.255`|

### Sub-redes y súper-redes

Las sub-redes y súper-redes se determinan mediante la **máscara de red**. En la máscara de red no se pueden mezclar `0`s y `1`s, todos deben de estar a un lado o al otro. Entre más subredes, más direcciones se pierden 

### Router

Es un dispositivo de capa 3 que redirecciona paquetes entre redes y los lleva a su destino. Cada vez que se conecta algo al enrutador **se necesitan IDs de red distintos.** Para saber por dónde redireccionar los paquetes, tiene una tabla de enrutamiento que mappea una **red** con un **puerto** en el router. El router mata todos los paquetes de broadcasts de `255.255.255.255`.

### Direccionamiento IP

Para transmitir información entre redes es necesario tener información tanto para reconocer la red y la máquina dónde se debe llevar la información. Para esto existe la capa 3 del modelo OSI, dónde el protocolo utilizado en la práctica es el * [**Internet Protocol**](https://en.wikipedia.org/wiki/Internet_Protocol):

![Imágen IP](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Ipv4_address.svg/300px-Ipv4_address.svg.png)

Tienen asociados una clase para ordenarlas, así:

![Clases IP](https://labs.ripe.net/Members/olafur_gudmundsson/pre-1993-ip-addresses-1.png)

* Para ser de clase A, la dirección debe comenzar con `0`. La máscara de red por defecto es `255.0.0.0`
* Para ser de clase B, la dirección debe comenzar con `1 0`. La máscara de red por defecto es `255.255.0.0`
* Para ser de clase C, la dirección debe comenzar con `1 1 0`. La máscara de red por defecto es `255.255.255.0`

**Dirección de Red:** Cuando los campos de hosts están todos en `0`, ese es el identificador de red.

**Broadcast:** Dirección general reservada utilizada para comunicarse a todas las máquinas dentro de la misma red local dónde todos los campos de host están en `1`. Ningún host puede tener dirección igual a la dirección de red o broadcast.

### Colisiones

Protocolo [**ALOHA**](https://en.wikipedia.org/wiki/ALOHAnet) es el predecesor de otros protocolos usados en redes de área local actualmente.

* **Dominio de colisión:** En una red directamente conectada el dominio de colisión es igual a la cantidad de equipos en la red. Cada red indirectamente conectada tiene su propio dominio de colisión. A vece es necesario segregar una red en varias para evitar colisiones. Los equipos de capa 3 segmentan los dominios de colisión.

### Protocolos de Red

* [**Spanning Tree Protocol**](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol)
* [**Address Resolution Protocol**](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)
* [**CSMA/CD:**](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection) Método MAC usado en Ethernet (nombrada así en honor a [Einstein](https://en.wikipedia.org/wiki/Einstein_aether_theory). Carrier sense media access with collision detection. Funciona así:
    * Sensar la onda portadora
    * Se accede al medio físico
    * Se detecta la colisión al tiempo RTT/4 por el transmisor si existe.
    * El transmisor espera escuchar la información del paquete que envió. Si no escucha eso, entonces asume que existió una colisión y se envía un paquete JAM que ignora lo que le llega hasta un total de **16** veces.

### Cables

* **UTP:** Par trenzado sin blindaje
* **STP:** Par trenzado blindado (cada hilo está encerrado en una jaula de Faraday)

En general, existen dos tipos de cable, que son de particular interés para trabajar en Packet Tracer:
* **Cable Plano (Straight Through):** Cable donde los pines se conectan con la hembra en el orden 1 - 8. Se usan solo los pines 1, 2, 3, y 6. Se usan cuando se tienen equipos distintos.
![Cable Straight Through](http://www.cables-solutions.com/wp-content/uploads/2016/12/Straight-Through-Cable.png)

* **Cable Trenzado (Crossover):** Cable dónde se cruzan el pin 1 con el 3, 2 con el, 5 con el  Necesario cuando se emite una transmición entre dos máquinas con la misma frecuencia.
![Cable Crossover](http://www.cables-solutions.com/wp-content/uploads/2016/12/crossover-cable-.png)

* [**RJ-45:**](https://en.wikipedia.org/wiki/Registered_jack) El estándar de interfaz de comunicación universal.

Si se conecta el pin A con el B entonces es un cable trenzado. 

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

Dependiendo del direccionamiento, las redes pueden ser:

* **Directamente conectadas:** Redes en las que todos los hosts comparten la capa 1 y la comunicación no se conmuta del todo.
* **Indirectamente conectadas:** Cuando se tienen equipos en cada capa y se hace alguna de las siguientes conmutaciones de rutas:
  * Conmutación de circuitos: El circuito físico se crea cuando se necesita (capa 2).
  * Conmutación por paquetes: Se cambia la ruta dependiendo de la información en un paquete (capa 3).
  * Conmutación por celdas: agrupa muchos paquetes y se cambia la ruta con respecto (capa 4).

### Información General

**Profesor:** Carlos Benavides

**Correo:**  tec.benavides.profesor@gmail.com

**Correo Asistente:** asistente.redes@outlook.com

[**Link del Drive**](https://drive.google.com/drive/folders/1s_ocyGvy4Yoxszav7TibZhTzir_xlSDG)

| Evaluación  | Peso |
| :--- | :---: |
| Tareas | % |
| Laboratorios | % |
| Exámenes | 30 % |
| Videos | % |
| Proyectos | % |

El curso se pasa con solo ir a clases y entregar los laboratorios y asignaciones. Los exámenes son solo necesarios si se pierden puntos fáciles en eso.