# Configuraciones Mecánicas de Robots Móviles

**Archivo:** 2630129_CarrizalesUrbina.md  

---

## 1. Conceptos básicos

### ¿Qué es un robot móvil?
Un robot móvil es una máquina que puede desplazarse de un lugar a otro de forma autónoma o semiautónoma. A diferencia de las máquinas fijas, su cuerpo completo se mueve en el entorno para cumplir una tarea.

### Diferencia entre robot móvil y robot manipulador fijo
El robot manipulador fijo (como un brazo industrial) permanece anclado a un punto y solo mueve sus articulaciones. El robot móvil, en cambio, cambia de posición en el espacio. Puede llevar un brazo encima, pero su característica principal es la locomoción.

### Función del sistema de locomoción
El sistema de locomoción es el conjunto de ruedas, motores y mecanismos que permiten al robot avanzar, retroceder, girar o desplazarse lateralmente. Determina cómo el robot interactúa con el suelo y qué movimientos puede realizar.

### Movilidad omnidireccional
Significa que el robot puede moverse en cualquier dirección del plano (adelante, atrás, izquierda, derecha o diagonal) sin necesidad de girar primero su cuerpo. Es la máxima libertad de movimiento en dos dimensiones.

### Relación entre disposición de ruedas y movimientos
La forma en que se colocan y orientan las ruedas define los grados de libertad del robot. Dos ruedas fijas permiten solo avance y giro; ruedas con rodillos permiten movimiento lateral; la geometría Ackermann limita el movimiento lateral directo.

### Aplicaciones de robots móviles
- Almacenes y logística (AGV/AMR)
- Limpieza de pisos
- Exploración y rescate
- Educación y prototipado
- Vehículos autónomos y delivery
- Inspección industrial

---

## 2. Robot diferencial con rueda de castor

### Descripción de la configuración
Se utilizan dos ruedas motrices alineadas en el mismo eje (izquierda y derecha) y una o más ruedas de castor (locas) que solo soportan peso y giran libremente.

### Colocación de las ruedas motrices
Las dos ruedas de tracción están en los lados del robot, normalmente en el centro o ligeramente hacia atrás. Cada una es impulsada por su propio motor.

### Función de la rueda de castor
Sirve de apoyo pasivo. No transmite fuerza de tracción; solo mantiene el equilibrio y permite que el robot no se vuelque. Puede orientarse libremente según el movimiento.

### Movimientos básicos
- **Línea recta:** ambas ruedas giran a la misma velocidad y en el mismo sentido.
- **Giro izquierda/derecha:** una rueda gira más rápido (o en sentido contrario) que la otra.
- **Giro sobre su eje:** las dos ruedas giran a la misma velocidad pero en sentidos opuestos. El centro de rotación queda entre las dos ruedas.
- Si una rueda avanza y la otra se detiene, el robot gira alrededor de la rueda detenida.

### Tabla de movimientos

| Rueda izquierda | Rueda derecha | Movimiento del robot          |
|-----------------|---------------|-------------------------------|
| Avanza          | Avanza        | Avance en línea recta         |
| Detenida        | Avanza        | Giro hacia la izquierda       |
| Avanza          | Detenida      | Giro hacia la derecha         |
| Avanza          | Retrocede     | Giro sobre su propio eje      |
| Retrocede       | Avanza        | Giro sobre su propio eje (sentido contrario) |
| Retrocede       | Retrocede     | Retroceso en línea recta      |

### Diagrama (vista superior)

```
          [Castor]
             ○
             
    ●───────────●
   Izq.        Der.
   (motriz)   (motriz)
   
   ←── Eje de giro aproximado ──→
```

### Ventajas
- Muy simple mecánicamente (solo dos motores).
- Fácil de controlar y programar.
- Puede girar en el sitio.
- Bajo costo.

### Limitaciones
- No se desplaza lateralmente.
- Sensible a deslizamiento y diferencias de fricción.
- La rueda de castor puede generar arrastre en suelos irregulares.

### Aplicaciones
Robots educativos (TurtleBot, mBot), robots de servicio ligeros, prototipos de laboratorio.

---

## 3. Robots omnidireccionales con ruedas Omni

### Funcionamiento de una rueda Omni
Una rueda Omni tiene un disco principal que gira sobre su eje y, alrededor de su perímetro, pequeños rodillos orientados a 90° respecto al plano de la rueda.  
La rueda genera fuerza solo en la dirección de su eje de rotación principal. Los rodillos permiten que se deslice libremente en la dirección perpendicular, sin oponer resistencia.

Esta característica permite movimientos que una rueda convencional no puede hacer, porque el robot no queda “bloqueado” lateralmente.

### Configuración de tres ruedas
Las ruedas se colocan normalmente a 120° entre sí, formando un triángulo equilátero.  
- Avance/retroceso: combinación de velocidades de las tres ruedas.  
- Movimiento lateral: las fuerzas se cancelan en una dirección y se suman en la perpendicular.  
- Diagonal: mezcla de componentes.  
- Giro sobre su eje: las tres ruedas giran en el mismo sentido relativo al centro.

Cuando las tres ruedas giran a velocidades diferentes, el robot puede realizar cualquier combinación de traslación y rotación simultáneas.

### Diagrama (vista superior – 3 ruedas)

```
          Rueda 1
             ●
            / \
           /   \
          /     \
    Rueda 3 ●─────● Rueda 2
```

### Configuración de cuatro ruedas
Las ruedas se colocan en las esquinas de un rectángulo, orientadas a 90° o en pares.  
Ofrece mayor estabilidad y capacidad de carga que el sistema de tres ruedas.  
La complejidad de control aumenta porque hay un grado de libertad redundante.

**Ventajas de 4 ruedas:** más estabilidad y carga.  
**Limitaciones:** más motores, control más complejo y mayor costo.

---

## 4. Robot omnidireccional con ruedas Mecanum

### Construcción y diferencia con Omni
Las ruedas Mecanum también tienen rodillos, pero estos están inclinados a 45° respecto al eje de la rueda.  
Una rueda Omni tiene rodillos a 90°; la Mecanum genera una fuerza diagonal.  
Por eso normalmente se usan cuatro ruedas con orientaciones espejo (izquierda y derecha invertidas).

### Orientación típica
Las dos ruedas delanteras y traseras se orientan de forma que los rodillos formen una “X” o “O” vista desde arriba.

### Combinaciones de movimiento

| Movimiento              | Delantera izq. | Delantera der. | Trasera izq. | Trasera der. |
|-------------------------|----------------|----------------|--------------|--------------|
| Avanzar                 | →              | →              | →            | →            |
| Retroceder              | ←              | ←              | ←            | ←            |
| Desplazarse a la izquierda | ←           | →              | →            | ←            |
| Desplazarse a la derecha   | →           | ←              | ←            | →            |
| Girar a la izquierda    | ←              | →              | ←            | →            |
| Girar a la derecha      | →              | ←              | →            | ←            |

(→ = gira hacia adelante, ← = gira hacia atrás)

### Diagrama (vista superior – Mecanum)

```
   ●───45°───●
   |         |
   |         |
   ●───45°───●
```
(Las flechas de los rodillos se orientan en “X”)

### Ventajas
Movimiento omnidireccional completo con cuatro motores.  
Buena capacidad de carga y estabilidad.

### Limitaciones
Más costoso y complejo de controlar.  
Los rodillos se desgastan y son sensibles a pisos irregulares o sucios.

---

## 5. Robot con dirección Ackermann

### Distribución de ruedas
Cuatro ruedas: normalmente las traseras proporcionan la tracción y las delanteras la dirección (o ambas).  
Las ruedas delanteras están unidas por un mecanismo de dirección que hace que la rueda interior gire un ángulo mayor que la exterior durante una curva.

### Por qué ángulos diferentes
Para que todas las ruedas giren alrededor del mismo centro instantáneo de rotación y no haya deslizamiento lateral de los neumáticos.  
El radio de giro es la distancia desde ese centro hasta el eje del vehículo.

### Limitaciones
No puede desplazarse directamente hacia un costado. Debe avanzar o retroceder mientras gira (como un automóvil convencional).

### Diagrama de curva

```
          Centro de giro
               ○
              /
             /
    ●───────●  ← rueda exterior (ángulo menor)
    |       |
    ●───────●  ← rueda interior (ángulo mayor)
```

### Ejemplos
Vehículos autónomos tipo coche, robots de delivery de exterior, plataformas agrícolas y algunos AGV de gran tamaño.

---

## 6. Comparación de configuraciones

| Configuración       | Nº típico de ruedas | Movimiento lateral | Giro sobre su eje | Complejidad mecánica | Complejidad de control | Aplicaciones típicas          |
|---------------------|---------------------|--------------------|-------------------|----------------------|------------------------|-------------------------------|
| Diferencial + castor| 2 + 1               | No                 | Sí                | Baja                 | Baja                   | Educación, robots ligeros     |
| Omni de 3 ruedas    | 3                   | Sí                 | Sí                | Media                | Media                  | Service robots, indoor        |
| Omni de 4 ruedas    | 4                   | Sí                 | Sí                | Media-Alta           | Alta                   | Plataformas de carga          |
| Mecanum             | 4                   | Sí                 | Sí                | Alta                 | Alta                   | AMR, almacenes, investigación |
| Ackermann           | 4                   | No                 | No (radio mínimo) | Media                | Media                  | Vehículos autónomos, outdoor  |

### Elección según caso
- **Robot pequeño para aprender:** Diferencial + castor (simple y barato).
- **Almacén con espacios reducidos:** Omni o Mecanum (movimiento lateral).
- **Moverse lateralmente sin girar:** Omni de 3/4 o Mecanum.
- **Circular como automóvil:** Ackermann.
- **Cambio rápido de dirección:** Mecanum u Omni.
- **Solo dos motores:** Diferencial + castor.

---

## 7. Análisis del movimiento

### Diferencial
Para girar sobre su propio eje, una rueda debe girar hacia adelante y la otra hacia atrás a la misma velocidad. El punto medio entre ambas se convierte en el centro de rotación.

### Omni
Los rodillos permiten que la rueda se deslice libremente en la dirección perpendicular a su eje de tracción. Al combinar las fuerzas de varias ruedas orientadas de forma distinta, se genera una fuerza neta en cualquier dirección del plano.

### Mecanum
Aunque ninguna rueda apunta directamente hacia el costado, los rodillos a 45° descomponen la fuerza de cada rueda en componentes longitudinal y transversal. La suma vectorial de las cuatro ruedas produce el movimiento lateral deseado.

### Ackermann
El vehículo está sujeto a una restricción no holonómica: las ruedas no pueden deslizar lateralmente. Por eso solo puede cambiar de posición lateral avanzando o retrocediendo mientras gira (como un coche al estacionar).

---

## 8. Aplicación en un robot real

**Robot:** TurtleBot 3 (Burger / Waffle)  
**Fabricante:** ROBOTIS  
**Tipo de locomoción:** Diferencial con ruedas de castor de apoyo  
**Número y tipo de ruedas:** 2 ruedas motrices + 1 o 2 ruedas de castor  
**Sensores principales:** LiDAR, IMU, sensores de contacto, cámara (según modelo)  
**Actuadores:** Motores Dynamixel para las ruedas  
**Aplicación:** Educación, investigación de navegación y ROS  

Esta configuración es adecuada porque es sencilla, económica, permite girar en el sitio y es ideal para aprender control y algoritmos de navegación en espacios interiores.

---

## Reflexión final

La configuración diferencial con castor me pareció la más sencilla de comprender: solo dos motores y un comportamiento intuitivo.  

La que ofrece mayor libertad de movimiento es la Mecanum o la Omni de tres/cuatro ruedas, porque permiten traslación y rotación simultáneas en cualquier dirección.  

Para construir mi primer robot móvil elegiría el diferencial + castor: es barato, fácil de controlar y suficiente para la mayoría de experimentos iniciales.  

No existe una sola configuración ideal porque cada una equilibra de forma distinta costo, complejidad, capacidad de carga, terreno y tipo de movimiento requerido. El entorno y la tarea determinan la mejor elección.

---

## Referencias

1. Robohub. (2016). *Pros and cons for different types of drive selection*. https://robohub.org/pros-and-cons-for-different-types-of-drive-selection/  
2. Tagliavini, L. et al. (2022). *Wheeled Mobile Robots: State of the Art Overview and Kinematic Comparison*. Journal of Intelligent & Robotic Systems.  
3. SECURE Caster. (2026). *Omni Wheels vs Mecanum Wheels for AMR and Service Robots*.  
4. FDataBot. (2026). *Differential Drive vs Mecanum vs Omni Wheel: Complete Robot Chassis Comparison*.  
5. Duckietown. (2024). *Development of an Ackermann steering autonomous vehicle*.  
6. Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). *Introduction to Autonomous Mobile Robots* (2nd ed.). MIT Press.  
7. ROBOTIS. Documentación técnica TurtleBot 3.  
