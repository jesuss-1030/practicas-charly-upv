# Sensores y Actuadores en Sistemas Mecatrónicos

**Archivo:** 2630129_CarrizalesUrbina.md  

---

## 1. Conceptos básicos

### ¿Qué es un sensor?
Un sensor es un dispositivo que detecta o mide una variable física del entorno (como temperatura, luz, distancia o presión) y la convierte en una señal eléctrica o digital que un sistema de control puede interpretar. Es como los “ojos” o “oídos” del sistema: observa lo que ocurre sin realizar acciones físicas por sí mismo.

### ¿Qué es un actuador?
Un actuador es el elemento que recibe una señal de control y la transforma en una acción física real. Puede generar movimiento, fuerza, desplazamiento o cambio de posición. Es la “mano” o el “músculo” del sistema: ejecuta la orden que el controlador le envía.

### Diferencia entre sensor y actuador
La diferencia fundamental es la dirección de la información:
- El **sensor** convierte una magnitud física en una señal eléctrica (entrada de información).
- El **actuador** convierte una señal eléctrica en una magnitud física o movimiento (salida de acción).

Mientras el sensor “observa”, el actuador “actúa”.

### Función dentro de un sistema mecatrónico
En un sistema mecatrónico (que combina mecánica, electrónica, control e informática) los sensores alimentan de datos al controlador, y los actuadores ejecutan las decisiones del controlador. Juntos cierran el lazo de control: medir → decidir → actuar → volver a medir.

### Ejemplo sencillo: puerta automática de un edificio
- **Sensor:** un sensor de proximidad infrarrojo o ultrasónico detecta si hay una persona cerca de la puerta.
- **Actuador:** un motor eléctrico (o un cilindro neumático) abre o cierra la puerta según la señal recibida.

Cuando el sensor detecta presencia, el controlador ordena al actuador que abra la puerta; cuando ya no hay nadie, la cierra.

---

## 2. Investigación de sensores

| Tipo de sensor | Variable que mide | Principio de funcionamiento | Tipo de señal | Ejemplo comercial | Aplicación |
|----------------|-------------------|-----------------------------|---------------|-------------------|------------|
| Temperatura | Temperatura | Cambio de resistencia (termistor), generación de voltaje (termopar) o variación de semiconductores | Analógica o digital | LM35, DS18B20, DHT22 | Termostatos, control de procesos industriales, aires acondicionados |
| Luz | Intensidad luminosa | Variación de resistencia de un material fotosensible (LDR) o corriente generada por fotodiodo | Analógica o digital | LDR, BH1750 | Control de iluminación automática, detección día/noche |
| Proximidad | Presencia de un objeto cercano | Campo electromagnético (inductivo), cambio de capacitancia o reflexión de luz/ultrasonido | Digital (on/off) o analógica | Sensor inductivo Omron, HC-SR04 (ultrasónico) | Detección de piezas en líneas de montaje, puertas automáticas |
| Distancia | Distancia a un objeto | Tiempo de vuelo de ultrasonido, infrarrojo o láser (ToF) | Analógica o digital | HC-SR04, VL53L0X (ToF láser) | Robots móviles, medición de nivel, estacionamiento asistido |
| Presión | Fuerza por unidad de área | Deformación de un diafragma que cambia resistencia o capacitancia | Analógica (0-10 V, 4-20 mA) | BMP280, sensores de presión industriales | Sistemas hidráulicos, control de neumáticos, HVAC |
| Humedad | Cantidad de vapor de agua en el aire | Cambio de capacitancia o resistencia de un material higroscópico | Digital o analógica | DHT22, BME280 | Invernaderos, control climático, almacenamiento de productos |
| Posición | Ubicación angular o lineal | Codificadores ópticos o magnéticos, potenciómetros, sensores Hall | Digital (pulsos) o analógica | Encoder incremental, potenciómetro | Control de ejes en robots, posicionamiento de válvulas |
| Velocidad o movimiento | Velocidad angular/lineal o detección de movimiento | Efecto Doppler, conteo de pulsos de encoder, o detección de infrarrojos pasivos (PIR) | Digital o analógica | Encoder, sensor PIR HC-SR501 | Control de velocidad de motores, sistemas de seguridad |
| Fuerza o peso | Fuerza aplicada o masa | Deformación de una galga extensométrica (strain gauge) | Analógica | Celda de carga, sensor de fuerza | Básculas, robots de agarre, prensas industriales |

---

## 3. Clasificación de sensores

### Sensores analógicos y digitales
- **Analógicos:** entregan una señal continua (voltaje o corriente) que varía proporcionalmente con la magnitud medida. La característica clave es que la salida puede tomar **infinitos valores** dentro de un rango. Ejemplo: un LM35 entrega 10 mV por cada grado Celsius.
- **Digitales:** entregan valores discretos (bits o palabras digitales). La característica principal es que la información ya está cuantificada y codificada. Ejemplo: el DS18B20 envía la temperatura como un número digital por el bus 1-Wire.

### Sensores de contacto y sin contacto
- **De contacto:** requieren tocar físicamente el objeto o medio medido. La característica que los define es la **interacción mecánica directa**. Ejemplo: un termopar en contacto con una superficie, o un final de carrera mecánico.
- **Sin contacto:** detectan a distancia. La característica es que **no hay contacto físico**. Ejemplo: sensores ultrasónicos, inductivos o de infrarrojos.

### Sensores activos y pasivos
- **Activos:** necesitan una fuente de energía externa y, en muchos casos, emiten una señal (luz, ultrasonido, campo electromagnético) para luego medir la respuesta. La característica clave es que **generan su propia energía de exploración**. Ejemplo: sensor ultrasónico HC-SR04, radar.
- **Pasivos:** no emiten energía; solo capturan la que ya existe en el entorno (radiación térmica, luz ambiente, vibraciones). La característica es que **no requieren emisión propia**. Ejemplo: termopar, LDR, sensor PIR de movimiento.

---

## 4. Investigación de actuadores

| Actuador | Energía utilizada | Movimiento | Cómo funciona | Ventaja | Limitación | Aplicación real |
|----------|-------------------|------------|---------------|---------|------------|-----------------|
| Motor de corriente directa (DC) | Eléctrica | Rotatorio continuo | Una corriente genera un campo magnético que hace girar el rotor | Bajo costo, fácil control de velocidad | Desgaste de escobillas (en tipos con escobillas), precisión limitada | Ruedas de robots móviles, ventiladores, juguetes |
| Servomotor | Eléctrica | Rotatorio controlado (normalmente ±90° o 180°) | Motor DC + caja reductora + potenciómetro de realimentación + circuito de control | Alta precisión de posición angular | Carrera angular limitada, costo mayor que un motor DC simple | Articulaciones de brazos robóticos, direcciones de modelos RC |
| Motor paso a paso | Eléctrica | Rotatorio discreto (pasos angulares) | Bobinas se energizan en secuencia, avanzando el rotor en pasos fijos | Posicionamiento preciso sin realimentación (lazo abierto) | Puede perder pasos si se sobrecarga, torque disminuye a altas velocidades | Impresoras 3D, máquinas CNC, posicionadores |
| Solenoide | Eléctrica | Lineal de corto recorrido | Una bobina genera un campo magnético que atrae un núcleo metálico | Respuesta muy rápida, simple | Carrera muy corta, fuerza limitada | Cerraduras eléctricas, válvulas, impulsadores de piezas |
| Cilindro neumático | Aire comprimido | Lineal | El aire a presión empuja un pistón dentro de un cilindro | Rápido, limpio, seguro en ambientes explosivos | Fuerza limitada por la presión de aire, requiere compresor | Líneas de ensamble, sujeción de piezas, apertura de puertas |
| Cilindro hidráulico | Aceite a presión | Lineal | El fluido hidráulico empuja un pistón | Fuerzas muy elevadas en tamaño reducido | Más lento, riesgo de fugas, instalación costosa | Excavadoras, prensas industriales, elevadores de gran carga |

---

## 5. Comparación de actuadores

### Motor DC vs. Servomotor
El motor DC gira de forma continua y se controla principalmente por velocidad. El servomotor incluye realimentación de posición y se controla por ángulo.  
**Cuándo elegir uno:**  
- Motor DC cuando se necesita rotación continua y bajo costo (ruedas de un robot móvil).  
- Servomotor cuando se requiere detenerse en un ángulo exacto (articulación de un brazo robótico).

### Servomotor vs. Motor paso a paso
El servomotor usa realimentación cerrada y es más suave a altas velocidades. El motor paso a paso avanza en pasos discretos y puede mantener posición sin energía adicional en algunos casos.  
**Cuándo elegir uno:**  
- Servomotor para movimientos suaves y rápidos con realimentación (cámaras pan-tilt).  
- Paso a paso cuando se necesita precisión angular económica y lazo abierto es suficiente (impresora 3D).

### Actuador neumático vs. Actuador hidráulico
El neumático usa aire comprimido (rápido y limpio). El hidráulico usa aceite a alta presión (fuerzas mucho mayores).  
**Cuándo elegir uno:**  
- Neumático en líneas de producción rápidas y ambientes limpios (sujeción de piezas ligeras).  
- Hidráulico cuando se necesitan fuerzas muy grandes (prensas, maquinaria pesada de construcción).

---

## 6. Sensores y actuadores en un sistema real

**Sistema seleccionado: Puerta automática de un edificio**

### Elementos identificados
- **Sensor de proximidad / distancia (ultrasónico o infrarrojo):** detecta si una persona se acerca a la puerta.
- **Sensor de posición (final de carrera o encoder):** verifica si la puerta está completamente abierta o cerrada.
- **Actuador (motor DC o cilindro neumático):** genera el movimiento de apertura y cierre de la puerta.
- **Controlador (PLC o microcontrolador):** procesa las señales y ordena al actuador.

### Diagrama sencillo de la relación

```
                    ┌─────────────────────┐
                    │   Controlador       │
                    │  (PLC / MCU)        │
                    └──────────┬──────────┘
           Señal de            │           Señal de
           detección           │           control
               ▲               │               │
               │               │               ▼
    ┌──────────┴──────────┐    │    ┌──────────────────┐
    │ Sensor de           │    │    │ Actuador         │
    │ proximidad /        │    │    │ (Motor o         │
    │ distancia           │    │    │  cilindro)       │
    └─────────────────────┘    │    └────────┬─────────┘
                               │             │
                               │             ▼
                               │    Movimiento de la puerta
                               │
                    ┌──────────┴──────────┐
                    │ Sensor de posición  │
                    │ (final de carrera)  │
                    └─────────────────────┘
```

El sensor de proximidad informa al controlador que hay una persona. El controlador ordena al actuador abrir la puerta. El sensor de posición confirma que la puerta llegó al final de carrera y detiene el movimiento. Cuando ya no hay presencia, el proceso se invierte para cerrar.

---

## 7. Selección de componentes

| Situación | Sensor o actuador recomendado | Razón de la selección |
|-----------|-------------------------------|-----------------------|
| Detectar si una persona se encuentra frente a una puerta automática | Sensor de proximidad ultrasónico o infrarrojo | Detecta presencia a distancia sin contacto físico, ideal para seguridad y higiene |
| Medir la temperatura dentro de un salón | Sensor de temperatura digital (DHT22 o DS18B20) | Entrega lectura precisa y fácil de procesar por un microcontrolador |
| Detectar el nivel de agua de un depósito | Sensor de distancia ultrasónico o de presión | Mide el nivel sin contacto (ultrasónico) o por la presión hidrostática |
| Mover una rueda de un robot móvil | Motor de corriente directa (DC) con reductora | Proporciona rotación continua y par suficiente a bajo costo |
| Controlar con precisión el ángulo de una pequeña articulación robótica | Servomotor | Ofrece control de posición angular con realimentación interna |
| Empujar una pieza en una línea de producción | Cilindro neumático o solenoide | Movimiento lineal rápido y repetitivo, adecuado para producción |
| Medir la distancia entre un robot y una pared | Sensor de distancia láser ToF o ultrasónico | Mide distancia con buena precisión y sin contacto |
| Detectar si una habitación está iluminada | Sensor de luz (LDR o BH1750) | Responde directamente a la intensidad luminosa ambiente |

---

## Reflexión final

Medir una variable es solo observar y convertir información del mundo físico en datos que un sistema puede entender. Realizar una acción física es transformar una orden eléctrica en movimiento, fuerza o cambio real en el entorno.  

Un sistema mecatrónico necesita sensores y actuadores porque sin sensores no sabe qué está ocurriendo, y sin actuadores no puede modificar la realidad. Ambos cierran el ciclo de control: percibir → decidir → actuar → volver a percibir.  

De todos los dispositivos investigados, el que más me interesó fue el **servomotor**. Me parece fascinante cómo combina un motor simple con realimentación de posición para lograr movimientos tan precisos y suaves. Es como darle “conciencia” de su propia posición a un actuador, lo cual abre un mundo de posibilidades en robótica y automatización.

---

## Referencias

1. Tecneu. (2025). *Todo sobre Sensores de Temperatura y Humedad*. https://www.tecneu.com/blogs/noticias/todo-sobre-sensores-de-temperatura-y-humedad-tipos-usos-y-aplicaciones  

2. VIOX Electric. (2024). *La guía definitiva de los sensores de proximidad: principios de funcionamiento, tipos y aplicaciones*. https://viox.com/es/the-ultimate-guide-to-proximity-sensors-working-principles-types-and-applications/  

3. Dacpol. (2021). *Sensores de presión industriales: principio de funcionamiento, tipos y aplicaciones*. https://www.dacpol.eu/es/blog/post/sensores-de-presion-industriales-principio-de-funcionamiento-tipos-y-aplicaciones.html  

4. Brunete, A. (2025). *2.1 Sensores industriales*. Introducción a la Automatización Industrial. https://bookdown.org/alberto_brunete/intro_automatica/sensores-industriales.html  

5. Dombor. (2022). *Actuador neumático frente a actuador hidráulico*. https://www.dombor.com/es/actuador-neumatico-frente-a-actuador-hidraulico/  

6. RoboticsBiz. (2025). *How to choose and use DC motors, servos, steppers and solenoids*. https://roboticsbiz.com/how-to-choose-and-use-dc-motors-servos-steppers-and-solenoids/  

7. Universidad de Alicante. (2016). *Tema 4-5 Accionamientos*. https://rua.ua.es/bitstream/10045/18435/1/Tema%204-5_Accionamientos.pdf  

8. Meskernel. (2025). *Principio de funcionamiento del sensor láser de distancia*. https://meskernel.net/es/principio-de-funcionamiento-del-sensor-laser-de-distancia/  

9. A2N Automation Systems. (2026). *Sensórica industrial: tipos de sensores industriales*. https://a2nautomation.com/sensorica-industrial-tipos-de-sensores/  

10. SuperAuto. (2023). *Sensores Activos vs. Pasivos en tu Auto*. https://superauto.com.ar/sensores-activos-y-pasivos-del-automovil/  
