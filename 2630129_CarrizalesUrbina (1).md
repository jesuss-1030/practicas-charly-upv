# Agilidad: Principios, Scrum, Kanban y Design Thinking

**Archivo:** 2630129_CarrizalesUrbina.md  

---

## Resumen ejecutivo

La **agilidad** es un enfoque de trabajo que prioriza la adaptación al cambio, la entrega continua de valor y la colaboración estrecha entre personas, en lugar de seguir planes rígidos y documentación exhaustiva. Surgió a principios de la década de 2000 como respuesta a los problemas de los métodos tradicionales (cascada), que resultaban demasiado lentos e inflexibles ante entornos complejos e inciertos.

Este documento explica:
- Los valores y principios del Manifiesto Ágil.
- Tres marcos ampliamente usados: **Scrum**, **Kanban** y **Design Thinking**.
- Sus conceptos clave, roles, artefactos, eventos, métricas y cuándo aplicar cada uno.
- Ventajas, riesgos y una reflexión sobre su uso en contextos académicos y profesionales.

---

## Principios ágiles

### Valores del Manifiesto Ágil (2001)

Se valora más:

1. **Individuos e interacciones** sobre procesos y herramientas.
2. **Software funcionando** sobre documentación exhaustiva.
3. **Colaboración con el cliente** sobre negociación contractual.
4. **Respuesta ante el cambio** sobre seguir un plan.

Esto no significa que lo de la derecha no tenga valor, sino que se prioriza lo de la izquierda.

### Doce principios clave (impacto en la gestión)

- Entregar valor de forma temprana y continua.
- Acoger el cambio incluso en etapas tardías.
- Entregar software funcionando con frecuencia (semanas o meses).
- Trabajo diario conjunto entre negocio y desarrollo.
- Construir proyectos alrededor de personas motivadas y confiar en ellas.
- Comunicación cara a cara como método más efectivo.
- El software funcionando es la principal medida de progreso.
- Ritmo sostenible de trabajo.
- Atención continua a la excelencia técnica y al buen diseño.
- Simplicidad (maximizar el trabajo no realizado).
- Los mejores resultados emergen de equipos auto-organizados.
- Reflexión regular del equipo para mejorar su efectividad.

**Impacto:** estos principios cambian la gestión del trabajo hacia ciclos cortos de feedback, autonomía del equipo, foco en valor real y mejora continua, reduciendo el riesgo de construir algo que nadie necesita.

---

## Panorama de marcos ágiles

| Marco              | Enfoque principal                          | Cuándo elegirlo                                                                 |
|--------------------|--------------------------------------------|---------------------------------------------------------------------------------|
| **Scrum**          | Iteraciones fijas (Sprints) con roles y eventos definidos | Proyectos con objetivos claros de producto, necesidad de ritmo predecible y equipos multidisciplinarios |
| **Kanban**         | Flujo continuo, visualización y limitación de trabajo en progreso (WIP) | Trabajo de soporte, mantenimiento, alta variabilidad o cuando se quiere mejorar un proceso existente sin cambiar roles |
| **Design Thinking**| Enfoque centrado en el usuario para descubrir e innovar soluciones | Fase de descubrimiento de problemas, ideación de productos nuevos o cuando hay alto riesgo de construir “lo incorrecto” |

---

## Ventajas y riesgos

| Aspecto              | Beneficios                                      | Limitaciones / Trade-offs                                      |
|----------------------|-------------------------------------------------|----------------------------------------------------------------|
| Adaptabilidad        | Responde rápido al cambio                       | Puede generar incertidumbre si no hay disciplina               |
| Entrega de valor     | Incrementos frecuentes y usable                 | Requiere disciplina en la Definition of Done                   |
| Colaboración         | Mejora comunicación y alineación                | Depende fuertemente de la madurez del equipo                   |
| Transparencia        | Trabajo visible (tableros, backlogs)            | Exige honestidad y apertura (puede generar resistencia)        |
| Mejora continua      | Retrospectivas y métricas de flujo              | Riesgo de “métricas vanidosas” si se usan mal                  |
| Escalabilidad        | Funciona bien en equipos pequeños               | Más complejo de escalar sin frameworks adicionales (SAFe, LeSS)|

---

## Scrum

### Conceptos base
Scrum es un framework ligero para desarrollar, entregar y sostener productos complejos. Se basa en empirismo (transparencia, inspección y adaptación) y en valores como compromiso, coraje, foco, apertura y respeto.  
**Cuándo usarlo:** cuando el producto necesita entregas incrementales, hay incertidumbre y se desea un ritmo predecible de trabajo.

### Roles

| Rol                | Responsabilidades principales                                      | Errores frecuentes                                      |
|--------------------|--------------------------------------------------------------------|---------------------------------------------------------|
| **Product Owner**  | Maximizar el valor del producto; gestionar y priorizar el Product Backlog | Convertirse en “gestor de tareas” o no estar disponible |
| **Scrum Master**   | Facilitar Scrum, eliminar impedimentos, ayudar al equipo y a la organización a mejorar | Actuar como jefe o secretario del equipo                |
| **Developers**     | Crear el Incremento usable cada Sprint; auto-organizarse           | Esperar que les asignen tareas o no colaborar entre sí  |

### Artefactos

- **Product Backlog**: lista ordenada y emergente de todo lo que se necesita para mejorar el producto. Compromiso: Product Goal.
- **Sprint Backlog**: conjunto de elementos del Product Backlog seleccionados para el Sprint + plan para entregarlos. Compromiso: Sprint Goal.
- **Increment**: suma de todos los elementos completados durante el Sprint y los anteriores. Debe cumplir la **Definition of Done**.

**Definition of Done vs Criterios de aceptación**  
- *Definition of Done*: estándar de calidad del equipo (código revisado, pruebas pasadas, documentación mínima, etc.). Aplica a todo el Incremento.  
- *Criterios de aceptación*: condiciones específicas de cada historia de usuario para considerarla completa desde el punto de vista del negocio.

### Eventos

| Evento              | Objetivo                                      | Duración sugerida (Sprint de 2 semanas) | Antipatrones típicos                          |
|---------------------|-----------------------------------------------|-----------------------------------------|-----------------------------------------------|
| **Sprint**          | Contenedor de todo el trabajo                 | 1–4 semanas (fijo)                      | Extender el Sprint o cancelarlo sin motivo    |
| **Sprint Planning** | Definir qué se hará y cómo                    | Máx. 4 h                                | Planificar demasiado detalle o sin Sprint Goal|
| **Daily Scrum**     | Inspeccionar progreso hacia el Sprint Goal    | 15 min                                  | Convertirlo en reunión de status para el jefe |
| **Sprint Review**  | Inspeccionar el Incremento y adaptar el Backlog | Máx. 2 h                              | Solo demo técnica sin feedback de stakeholders|
| **Sprint Retrospective** | Mejorar la efectividad del equipo         | Máx. 1,5 h                              | Quejarse sin acciones concretas               |

### Métricas
- **Velocity**: cantidad de trabajo completado por Sprint (en puntos o historias). Sirve para predecir capacidad futura. **No usar** para comparar equipos ni como objetivo de rendimiento.
- **Burndown**: gráfico que muestra trabajo restante vs tiempo. Ayuda a ver si el equipo va en camino.
- **Work in Progress (WIP)**: cantidad de trabajo iniciado pero no terminado. Alto WIP suele indicar problemas de flujo.

**Cómo interpretarlas:** como señales de salud del sistema, no como metas absolutas. El foco debe estar en el valor entregado y en la mejora del flujo.

---

## Kanban

### Fundamentos
Kanban es un método para optimizar el flujo de valor. Se basa en:
1. Visualizar el trabajo.
2. Limitar el trabajo en progreso (WIP).
3. Gestionar el flujo.
4. Hacer explícitas las políticas.
5. Implementar bucles de feedback.
6. Mejorar de forma evolutiva (kaizen).

### Tablero Kanban propuesto (equipo de desarrollo)

| Columna              | Descripción                              | Límite WIP sugerido |
|----------------------|------------------------------------------|---------------------|
| Backlog / To Do      | Trabajo priorizado listo para empezar    | Sin límite (o 10–15)|
| En análisis / Ready  | Historias refinadas y listas             | 3–5                 |
| En desarrollo        | Trabajo activo de coding                 | 3–4 (por persona)   |
| En revisión / Code Review | Revisión de código                    | 2–3                 |
| En pruebas           | Testing y validación                     | 2–3                 |
| Done                 | Completado y desplegable                 | —                   |

Los límites WIP se ajustan según la capacidad real del equipo para evitar sobrecarga y cuellos de botella.

### Métricas de flujo
- **Lead Time**: tiempo total desde que se solicita hasta que se entrega al cliente.
- **Cycle Time**: tiempo desde que se empieza a trabajar en un ítem hasta que se termina.
- **Throughput**: cantidad de ítems completados por unidad de tiempo.
- **Diagrama de Flujo Acumulado (CFD)**: muestra cómo se acumulan los ítems en cada estado a lo largo del tiempo. Una pendiente pronunciada en “Done” indica buen throughput; áreas planas en columnas intermedias señalan cuellos de botella.

### Políticas y clases de servicio
Ejemplos de clases de servicio:
- **Estándar**: trabajo normal, FIFO.
- **Expedite**: urgencias (bugs críticos). Se salta la cola pero con límite estricto.
- **Fixed Date**: fechas fijas (releases legales).
- **Intangible**: mejoras técnicas o deuda técnica.

Se aplican según el impacto y el costo de demora (Cost of Delay).

### Cuándo usar Kanban
Ideal cuando hay alta variabilidad de trabajo (soporte, mantenimiento, tickets), se quiere mejorar un proceso existente sin cambiar roles o cuando el equipo necesita flexibilidad continua más que sprints fijos.

---

## Design Thinking

### Visión general
Design Thinking es un enfoque centrado en el ser humano para resolver problemas complejos. Combina empatía, creatividad y experimentación. Se articula muy bien con el desarrollo de software porque reduce el riesgo de construir algo que no resuelve una necesidad real.

### Fases (modelo Stanford d.school)

| Fase          | Objetivo                                      | Técnicas sugeridas                          | Entregables mínimos                     |
|---------------|-----------------------------------------------|---------------------------------------------|-----------------------------------------|
| **Empatizar** | Entender profundamente a los usuarios         | Entrevistas, observación, shadowing, mapas de empatía | Insights y hallazgos de usuarios        |
| **Definir**   | Enmarcar el problema correcto                 | Affinity mapping, Point of View (POV), “How Might We” | Declaración de problema clara           |
| **Idear**     | Generar muchas posibles soluciones            | Brainstorming, Crazy 8s, SCAMPER            | Lista amplia de ideas                   |
| **Prototipar**| Hacer tangible una idea para aprender         | Bocetos, wireframes, mockups de baja fidelidad | Prototipo de baja fidelidad             |
| **Probar**    | Validar con usuarios reales                   | Pruebas de usabilidad, entrevistas de feedback | Aprendizajes y próximos pasos           |

El proceso es no lineal: se puede volver a fases anteriores según los aprendizajes.

### Mini-caso hipotético
**Problema:** Estudiantes universitarios olvidan entregar tareas a tiempo y pierden puntos.

- **Empatizar:** Entrevistas a 8 estudiantes → descubren que olvidan porque las notificaciones de la plataforma no son claras y las fechas se pierden entre otros avisos.
- **Definir:** “¿Cómo podríamos ayudar a los estudiantes a recordar las fechas de entrega de forma no intrusiva?”
- **Idear:** Ideas: widget de calendario, recordatorios inteligentes, integración con WhatsApp, gamificación.
- **Prototipar:** Boceto en papel de una app sencilla con un calendario visual y recordatorios 48 h y 24 h antes.
- **Probar:** Mostrar el boceto a 5 estudiantes → feedback: “me gusta el calendario, pero prefiero notificaciones solo por la mañana”.

### Relación con SDLC / Ágil
Design Thinking se usa principalmente en la fase de descubrimiento (antes o al inicio de un producto). Reduce el riesgo de construir “lo incorrecto”. Luego se puede pasar a Scrum o Kanban para construir e iterar la solución validada. DT aporta el “qué y por qué”, mientras Scrum/Kanban aportan el “cómo y cuándo”.

---

## Conclusiones

En un contexto académico, Scrum es excelente para trabajos en equipo con entregas parciales (proyectos de software, tesis por capítulos). Kanban resulta útil para gestionar tareas personales o de laboratorio con alta variabilidad. Design Thinking ayuda a no empezar a “programar” sin haber entendido realmente el problema del usuario.

En el ámbito profesional, combinar estos enfoques permite entregar valor más rápido, adaptarse al cambio y reducir el desperdicio de construir soluciones que nadie necesita. La clave está en no aplicar los marcos de forma dogmática, sino adaptar las prácticas a la realidad del equipo y del problema.

---

## Referencias

1. Beck, K. et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org/  
2. Schwaber, K. & Sutherland, J. (2020). *The Scrum Guide*. https://scrumguides.org/  
3. Kanban Guides. (2025). *The Kanban Guide*. https://kanbanguides.org/the-kanban-guide/  
4. Hasso Plattner Institute of Design at Stanford (d.school). *An Introduction to Design Thinking Process Guide*.  
5. Atlassian. (n.d.). *Agile Manifesto*. https://www.atlassian.com/agile/manifesto  
6. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.  
7. Brown, T. (2009). *Change by Design*. HarperBusiness.  
