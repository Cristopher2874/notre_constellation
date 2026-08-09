# Árbol de habilidades → Proyecto de brazo robótico con IA
## Mapa desde el perfil técnico de Cristopher hacia el proyecto Eiffel

> **Propósito:** A diferencia del `arbol_conocimiento_proyecto.md` (que parte del campo/proyecto), este documento parte de las **habilidades actuales** para trazar rutas concretas y naturales hacia el brazo robótico con IA. Incluye qué ya está listo para usar, qué es el siguiente paso inmediato, y cuáles son los gaps críticos a cubrir antes o durante la beca.
>
> **Fecha:** Abril 2026 | **Perfil base:** CV + LEAD 3D + Oracle (experiencia extendida)

---

## Escala de dominio actual

| Etiqueta | Significado |
|---|---|
| ✅ **Ya lo dominas** | Habilidad aplicable hoy directamente al proyecto |
| 🔵 **Fácil extensión** | Un paso desde lo que ya sabes. Curva baja. |
| 🟣 **Aprendizaje moderado** | Requiere estudio, pero la base ya está |
| 🟡 **Esfuerzo considerable** | Nuevo territorio con algo de base aplicable |
| 🔴 **Gap — necesario aprender** | No lo tienes y el proyecto lo requiere. Prioridad alta. |

---

## Resumen ejecutivo del perfil

| Cluster | Nivel actual | Listo para el proyecto |
|---|---|---|
| IA & orquestación de agentes | ✅ Muy fuerte | Sí — arquitectura de decisión del brazo |
| Visión artificial (OpenCV) | ✅ Fuerte | Sí — detección de objetos, con extensión a 3D |
| C++ & sistemas embebidos | ✅ Moderado-Fuerte | Sí — firmware, pero falta ROS2 |
| Diseño mecánico & 3D | ✅ Fuerte | Sí — diseño físico del brazo desde hoy |
| Escaneado 3D (Raptor IR) | ✅ Aplicado real | Sí — reverse engineering de entorno |
| Software, APIs & cloud | ✅ Muy fuerte | Sí — arquitectura software del robot |
| Algoritmos & optimización | ✅ Fuerte | Sí — motion planning (con paso adicional) |
| Control automático formal | 🔴 Gap #2 | No — indispensable para precisión del brazo |
| ROS2 | 🔴 Gap #1 | No — middleware estándar de robótica |
| Drivers de motores & potencia | 🔴 Gap #3 | No — necesario para mover el brazo físico |
| Fusión de sensores & Kalman | 🔴 Gap #4 | No — para estimación robusta de estado |

---

## 1. ✅ IA & Orquestación de agentes — YA LO DOMINAS

**Fuente:** Oracle ML Intern (LangGraph, A2A, AG-UI, RAG, MCP) + Scale AI (modelos ML) + Hackathons

**Habilidades actuales:**
- LangChain / LangGraph (orquestación de agentes)
- A2A protocol + AG-UI (interfaces generativas)
- RAG — Retrieval-Augmented Generation
- Semantic cache para eficiencia computacional
- Graph DB models (grafos de conocimiento)
- MCP (Model Context Protocol)
- OCI Gen AI + OpenAI APIs
- Multi-model orchestration
- Integración con bases de datos y flujos de trabajo

**Qué habilita para el brazo robótico:**
- Arquitectura de decisión inteligente del brazo con agentes especializados
- Agente perceptor → ve con cámara y procesa
- Agente planificador → decide qué movimiento hacer
- Agente ejecutor → envía comandos al hardware
- Memoria semántica del robot (RAG) para recordar objetos y tareas previas
- Interfaz generativa (AG-UI) para operar el robot en lenguaje natural
- Graph DB como base de conocimiento del entorno físico

**Siguientes pasos concretos:**
1. Conectar LangGraph a ROS2 como middleware del robot (ROS2 como "tool" del grafo)
2. Implementar agente de visión: tool call → OpenCV → decisión
3. Implementar agente de control: tool call → driver motor → acción física
4. Graph DB como mapa semántico del entorno del brazo

**Gap restante:** ROS2 como middleware estándar (ver Gap #1). Entrenamiento en simuladores físicos (Gymnasium, MuJoCo).

**Recursos universitarios:**
- **CentraleSupélec** — DataIA-Cluster (France 2030) + L2S: 47 laboratorios de IA, 800+ investigadores, ML para sistemas autónomos.
- **Centrale Nantes** — LS2N · CORO IMARO + DASSIP: redes neuronales para control, cómputo dedicado robótica.

---

### 1.1 ✅ Multi-agent AI (LangGraph + A2A) — aplicación directa

Ya construyes sistemas multi-agente en producción real (Oracle). La arquitectura de agentes de un robot (perceptor + planificador + ejecutor) es exactamente el mismo paradigma.

**Próximo paso:** Crear un grafo LangGraph donde los nodos son módulos del robot y los edges son el flujo de información sensores → decisión → acción.

---

### 1.2 ✅ RAG + Graph DB + semantic cache — aplicación directa

Para el robot: base de datos vectorial de objetos del entorno, historial de tareas, recuperación de experiencias previas. Semantic cache para no repetir inferencias costosas.

**Próximo paso:** Embeddings de estados del robot para búsqueda semántica de situaciones similares. Graph DB como mapa relacional del entorno físico.

---

### 1.3 🟡 Aprendizaje por refuerzo (RL) — por desarrollar

No tienes RL formal, pero tu base en ML (Scale AI, hackathons) y Python da una rampa rápida. RL es el puente entre tus agentes de software y un brazo que aprende solo.

**Siguientes pasos:**
- Gymnasium (entornos de simulación de robots)
- Stable-Baselines3 / RLlib (algoritmos RL en Python)
- MuJoCo / Isaac Sim (simulación física del brazo)
- Algoritmos objetivo: PPO, SAC, TD3

**Recursos universitarios:**
- **CentraleSupélec** — DataIA + INRIA Saclay: Deep RL research, sim-to-real transfer.
- **Centrale Nantes** — LS2N · ARMEN: RL para locomoción robótica.

---

## 2. ✅ Visión artificial — YA LO DOMINAS (con extensión necesaria)

**Fuente:** FIRST FRC (2 modelos de detección en tiempo real) + Scale AI (image recognition, NN) + hackathons

**Habilidades actuales:**
- OpenCV (producción real en robots FRC)
- Detección con haar cascade
- Redes neuronales para imagen (entrenadas en Scale AI)
- Python para procesamiento de imágenes

**Qué habilita para el brazo:**
- Detección de objetos a agarrar en tiempo real
- Control visual del brazo (visual servoing)
- Pick & place inteligente basado en visión
- Integración como tool del agente LangGraph

**Siguientes pasos concretos:**
1. YOLOv8 / YOLOv11 para detección rápida y robusta
2. Estimación de pose 6-DoF: MediaPipe (rápido) → FoundationPose (preciso)
3. Intel RealSense D435 (cámara RGBD, ~$200) para visión 3D
4. Calibración cámara-robot (eye-in-hand con OpenCV)
5. Integrar como tool en LangGraph: agent ve → decide → actúa

**Gap:** Visión 3D con RGBD/LiDAR (solo tienes 2D actualmente). Estimación de pose 6-DoF. SLAM para mapeo.

**Recursos universitarios:**
- **CentraleSupélec** — L2S + M2 MMVAI: machine vision AI, tomografía 3D, MSc vision & AI.
- **Centrale Nantes** — LS2N · DASSIP + IMARO: MSc Signal & Image Processing, percepción exteroceptiva, cámaras estéreo.

---

### 2.1 ✅ OpenCV & detección de objetos — aplicable hoy

Ya usas OpenCV en producción (FRC: aiming autónomo + recolección de piezas). Transferencia directa al brazo.

---

### 2.2 🟣 Estimación de pose 3D — extensión natural

El paso desde OpenCV 2D: detectar posición y orientación 3D de objetos para que el brazo sepa cómo aproximarse. Herramientas: MediaPipe → FoundationPose → calibración eye-in-hand.

---

### 2.3 🟡 SLAM (cartografía + localización) — más adelante

Permite al robot construir un mapa del entorno. Más avanzado. Útil si el brazo opera en espacios cambiantes. Herramientas: ORB-SLAM3, ROS2 Nav2.

---

## 3. ✅ C++ & Sistemas embebidos — FUERTE BASE

**Fuente:** FIRST FRC (2 robots de competencia, WPILib, control algorithms) + FLOW (ESP32, PCB, C++ dinámico) + ICPC (C++ avanzado)

**Habilidades actuales:**
- C++ proficient (algoritmos, OOP, control)
- Arduino + Raspberry Pi (producción real)
- ESP32 (FLOW: dispositivo comercial premiado)
- PCB design (FLOW project)
- Algoritmos de control en FRC

**Qué habilita para el brazo:**
- Firmware del controlador de articulaciones
- Control de servomotores / BLDC en tiempo real
- Lectura de encoders y sensores
- Comunicación entre módulos del robot

**Siguientes pasos concretos:**
1. **ROS2 en C++** (ver Gap #1 — este es el paso más urgente)
2. Implementar PID formal para control de articulaciones (ver Gap #2)
3. Estudio de drivers de motores BLDC con FOC (ver Gap #3)
4. Librería de cinemática directa/inversa en Python/C++ (Robotics Toolbox — Peter Corke, gratuito)

**Recursos universitarios:**
- **Centrale Lyon** — Ampère · MIS + M2 EEEA: dSPACE HIL, prototipado rápido Microchip, LabVIEW FPGA, EtherCAT.
- **Centrale Nantes** — LS2N: MSc Embedded Real-time Systems (CORO ERTS).

---

### 🔴 GAP #1 — ROS2 (prioridad máxima)

**Por qué es crítico:** ROS2 es el middleware estándar de toda la robótica moderna. Sin él, el brazo no tiene arquitectura estándar ni compatibilidad con ninguna herramienta (MoveIt2, Nav2, Gazebo). Es el eslabón que conecta tu IA (LangGraph) con el hardware físico.

**Por qué tienes buena base:** C++ proficient + Python proficient = las dos únicas dependencias de ROS2.

**Ruta de aprendizaje:**
1. Instalar ROS2 Humble (Ubuntu 22.04 o WSL2 en Windows)
2. Tutorial oficial: `ros2 run`, topics, services, actions
3. Primer nodo: publicar estado simulado de encoders del brazo
4. Segundo nodo: suscribir comandos desde Python (LangGraph tool)
5. Gazebo: simular el brazo URDF antes de tener hardware real

**Tiempo estimado para nivel funcional:** 3-4 semanas de práctica diaria.

---

### 🔴 GAP #2 — Control automático formal (PID, cinemática, MPC)

**Por qué es crítico:** Haces control empírico (FRC) pero sin la teoría matemática formal. Sin esto, el brazo no es preciso ni predecible.

**Lo que necesitas:**
- Cinemática directa e inversa (parámetros DH, Jacobiano)
- PID tuning formal (Ziegler-Nichols, frequency response)
- Espacio de estados y estabilidad
- Introducción a MPC (a nivel de las escuelas francesas, esto se da de forma intensiva)

**Ruta de aprendizaje:**
1. Robotics Toolbox Python — Peter Corke (gratuito, excelente)
2. Libro: "Modern Control Engineering" — Ogata (base sólida)
3. MATLAB/Simulink (disponible en UASLP) para simulación de lazo cerrado
4. CoppeliaSim / Gazebo para validar cinemática antes del hardware

---

## 4. ✅ Diseño mecánico & manufactura aditiva — MUY FUERTE

**Fuente:** LEAD 3D (profesional: Fusion360, Bambu Lab, filamentos, escáner Raptor IR/azul, point cloud) + FLOW (SolidWorks, Fusion360, 3D printing) + FRC (ensambles mecánicos)

**Habilidades actuales:**
- Fusion360 a nivel profesional (diseño de piezas, ensambles, planos)
- SolidWorks (familiar — válido para análisis estructural)
- 3D printing end-to-end: diseño → selección de filamento → impresión Bambu Lab → supervisión → entrega
- Escáner 3D Raptor (luz IR + luz azul, marcadores reflectantes, optimización de nube de puntos)
- Reverse engineering: escanear → limpiar modelo → imprimir a escala

**Qué habilita para el brazo:**
- Diseñar y fabricar el brazo físico completo desde cero
- Prototipado rápido iterativo de eslabones y gripper
- Reverse engineering de componentes para integración
- Gripper a medida para los objetos del entorno específico

**Siguientes pasos concretos:**
1. Análisis FEM en Fusion360 (Simulation workspace — ya tienes el software)
2. Cálculo de torques requeridos por articulación (para selección de motores)
3. Diseño de gripper adaptado a la tarea objetivo del brazo
4. Integración CAD + electrónica en Fusion360 (Electronics workspace)

**Recursos universitarios:**
- **Centrale Nantes** — Platforms: manufactura aditiva gran escala, CRAFT cable-driven robot, materiales compuestos.
- **Centrale Lyon** — Ampère + socios Safran: diseño de sistemas mecatrónicos en contexto aeronáutico.

---

### ✅ Escaneado 3D & reverse engineering (Raptor IR/azul)

Experiencia real y directa: escáner con luz IR y azul, marcadores reflectantes, optimización de nube de puntos, impresión a escala (caso: silla escaneada e impresa).

**Conexión con el proyecto:** Escanear objetos del entorno del brazo para construir modelos 3D precisos para pick & place. Integrar con ROS2 (sensor_msgs/PointCloud2). Procesar con Open3D en Python.

---

### 🔴 GAP #3 — Electrónica de potencia & drivers de motores

**Por qué es crítico:** Tienes PCB design y ESP32, pero un brazo robótico requiere drivers especializados (BLDC, servos industriales) con control de par y velocidad preciso.

**Ruta de aprendizaje:**
1. Estudio de tipos de motores para robótica: DC, BLDC, servo, stepper
2. ODrive (driver BLDC open-source) — comunidad amplia, bien documentado
3. Cálculo de torques del brazo diseñado en Fusion360
4. Simulación de circuito en LTspice antes de fabricar

**Recurso universitario clave:** Centrale Lyon (Ampère) — único laboratorio en Francia con capacidad completa en GaN/SiC, bancos dSPACE, prototipado rápido Microchip.

---

## 5. ✅ Software, APIs & cloud — MUY FUERTE

**Fuente:** Oracle (Docker, VMs, pipelines, cloud deploy) + VR Intern (React, HTML) + hackathons (FastAPI, Python)

**Habilidades actuales:**
- Python proficient (ML, APIs, scripting, data)
- FastAPI (REST APIs)
- Docker (containerización)
- VMs y cloud deploy (Oracle Cloud)
- CI/CD pipelines
- React + HTML/CSS + JavaScript
- GitHub (control de versiones, colaboración)

**Qué habilita para el brazo:**
- API REST para recibir comandos del robot desde cualquier cliente
- Dashboard web React con estado en tiempo real del brazo
- Docker: containerizar toda la IA del robot (portable, reproducible)
- Deploy de agentes en servidor remoto (cloud robotics)
- GitHub Actions como CI/CD del software del robot

**Siguientes pasos concretos:**
1. WebSocket (FastAPI + asyncio) para control de baja latencia (vs REST que es más lento)
2. ROS2 en Docker (`ros:humble` como imagen base)
3. rosbridge_suite: exponer ROS2 topics sobre WebSocket → React puede controlar el brazo
4. Three.js o Babylon.js para visualizar el URDF del brazo en 3D en el dashboard

**Recursos universitarios:**
- **CentraleSupélec** — DataIA + Saclay (Dassault Systèmes): cloud robotics, digital twins, gemelos digitales.
- **Centrale Nantes** — LS2N: Industry 4.0, sistemas conectados en nube.

---

## 6. ✅ Algoritmos & optimización — FUERTE

**Fuente:** ICPC 3° lugar estatal C++ + hackathons ML multi-parámetro + ROOT (olimpiadas de matemáticas)

**Habilidades actuales:**
- C++ algorithms: grafos, búsqueda, data structures
- BFS / DFS / A* / Dijkstra (ICPC)
- ML con múltiples parámetros y análisis de resultados
- Pensamiento matemático formal (olimpiadas)

**Qué habilita para el brazo:**
- Motion planning eficiente (A* ya lo conoces → RRT* es extensión natural)
- Optimización de trayectorias del brazo
- Implementación eficiente de cinemática inversa
- Algoritmos de planificación de tareas

**Siguientes pasos concretos:**
1. OMPL Python bindings (Open Motion Planning Library)
2. MoveIt2 sobre ROS2 (motion planning estándar de la industria)
3. Configuración del URDF del brazo y joint limits para el planner
4. scipy.optimize para IK numérica

**Recursos universitarios:**
- **Centrale Nantes** — LS2N · ARMEN + OGRE: motion planning, optimización no-lineal garantizada.
- **CentraleSupélec** — L2S · SYCOMORE: control predictivo bajo restricciones.

---

## 7. 🔴 Gaps críticos — Resumen y ruta de acción

### Gap #1 — ROS2 ⬅ Cubrir primero
**Tiempo:** 3-4 semanas · **Recursos:** Tutorial oficial + The Construct + docs.ros.org
**Por qué primero:** Todo lo demás (MoveIt2, Gazebo, drivers, sensores) depende de ROS2.

### Gap #2 — Control automático formal (PID, cinemática)
**Tiempo:** 2-3 meses de estudio paralelo · **Recursos:** Robotics Toolbox Python (Peter Corke, gratuito), Ogata, MATLAB UASLP
**Por qué segundo:** Sin cinemática inversa y PID formal, el brazo no llega a donde debe.

### Gap #3 — Electrónica de potencia & drivers de motores
**Tiempo:** 1-2 meses · **Recursos:** ODrive (open-source), YouTube "SimpleFOC", LTspice
**Por qué tercero:** Necesario para mover el brazo físico real. Puedes simularlo antes.

### Gap #4 — Fusión de sensores & filtro de Kalman
**Tiempo:** 1 mes · **Recursos:** filterpy (Python), robot_localization (ROS2), "Probabilistic Robotics" — Thrun
**Por qué cuarto:** Para estimación precisa del estado del brazo y compensación de ruido.

---

## Tabla de priorización: qué hacer antes de la beca

| Prioridad | Tarea | Tiempo est. | Qué desbloquea |
|---|---|---|---|
| 1 🔴 | Aprender ROS2 (Humble, nodos, topics) | 3-4 sem. | Todo lo demás del proyecto |
| 2 🔴 | Cinemática básica (DH + IK en Python) | 2-3 sem. | Precisión del brazo |
| 3 🔵 | YOLOv8 + estimación de pose 2.5D | 1-2 sem. | Mejora tu ya fuerte visión |
| 4 🔵 | LangGraph → ROS2 tool (integrar agente) | 1 sem. | Brazo controlado por agente IA |
| 5 🟣 | PID formal en simulador | 2-3 sem. | Control estable del brazo |
| 6 🟣 | ODrive + motor BLDC básico | 2-3 sem. | Primer movimiento real |
| 7 🟣 | Gymnasium + RL básico (PPO) | 3-4 sem. | Brazo que aprende |
| 8 🟡 | Filtro de Kalman en Python | 1-2 sem. | Estimación robusta del estado |

---

## Argumento Eiffel basado en perfil

Con este árbol de habilidades, el argumento más sólido para la carta de motivación es:

> *"Mi perfil combina experiencia real en sistemas multi-agente con IA (Oracle, LangGraph, RAG), visión artificial aplicada a robots en tiempo real (FRC, OpenCV) y diseño mecánico + manufactura aditiva de nivel profesional (LEAD 3D, Fusion360, escaneado 3D). Cuento con las habilidades de software para construir la arquitectura de alto nivel del brazo, y requiero los recursos formales de [escuela] — específicamente [laboratorio X con equipo Y] — para desarrollar la capa de control formal (cinemática, MPC, HIL) que conecte mi base en IA con el hardware físico. Esta combinación, posible únicamente en su institución, es lo que hace viable mi proyecto de brazo robótico con inteligencia artificial distribuida."*

---

*Documento generado como parte del proyecto `notre_constellation` — Candidatura Beca France Excellence Eiffel 2026.*  
*Fecha de generación: Abril 2026.*
