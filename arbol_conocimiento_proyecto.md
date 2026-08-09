# Árbol de conocimiento: Brazo robótico con IA
## Guía de campos, recursos y universidades para la Beca Eiffel

> **Propósito:** Mapa de todos los campos de conocimiento relevantes, organizados desde el núcleo del proyecto (brazo robótico con IA) hacia afuera. Cada campo incluye distancia relativa al proyecto, descripción breve, y recursos disponibles en las Top 3 escuelas.
>
> **Cómo leer este árbol:** Navega desde el núcleo (distancia 0) hacia afuera. Cuanto mayor la distancia, más esfuerzo requiere integrar ese campo sin perder coherencia con el proyecto central.

---

## Escala de distancia

| Etiqueta | Significado práctico |
|---|---|
| 🟢 **Núcleo** (0) | Es el proyecto mismo. Todo fluye desde aquí. |
| 🔵 **Muy cercano** (1) | Se integra directamente sin cambiar el eje del proyecto. |
| 🟣 **Cercano** (2) | Requiere un módulo adicional pero es coherente con el proyecto. |
| 🟡 **Relacionado** (3) | Posible extensión futura. Requiere trabajo paralelo. |
| 🔴 **Lejano** (4) | Campo distinto; integrable solo con un cambio de contexto significativo. |
| ⚫ **Referencia** (5) | Fuera del alcance razonable del proyecto. Solo para conocimiento del ecosistema. |

---

## RAÍZ — Mecatrónica · Sistemas Inteligentes

Campo de confluencia entre ingeniería mecánica, electrónica, informática y control automático. Todo el árbol emana desde aquí.

---

## 1. 🤖 Robótica — 🟢 Núcleo

Diseño, modelado, control y percepción de sistemas robóticos físicos. Es el campo central del proyecto.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N (RoMaS, ARMEN, ReV): CORO IMARO, UAVs, robot CRAFT cable-driven, arena de vuelo, plataforma cobots médicos.
- **CentraleSupélec** — L2S (equipo SYCOMORE): control robusto, guía de UAVs, M2 Autonomous Systems.
- **Centrale Lyon** — Ampère (dept. MIS): bancos dSPACE, HIL, robótica médica.

---

### 1.1 ★ Brazo robótico con IA — 🟢 Núcleo — **TU PUNTO DE PARTIDA**

Un brazo robótico inteligente integra mecánica, control, percepción e IA en un sistema capaz de tomar decisiones autónomas en tiempo real.

> **Nota estratégica:** Este nodo es tu "ancla". Cualquier campo que explores puede conectarse de vuelta aquí: visión para el agarre, RL para aprender movimientos, embebidos para ejecutar el control.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N · RoMaS: manipuladores industriales, cable-driven robot, MSc CORO IMARO.
- **CentraleSupélec** — L2S · SYCOMORE: M2 MMVAI, control adaptativo de brazos, visión artificial.
- **Centrale Lyon** — Ampère · MIS: HIL real para brazos, dSPACE, cobots con socios Safran/Valeo.

---

### 1.2 Modelado & dinámica de robots — 🟢 Núcleo

Base matemática: cinemática directa/inversa, Jacobiano, ecuaciones de Lagrange y Newton-Euler. Es el lenguaje fundamental para cualquier proyecto de robótica.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N · ARMEN: ROS / MATLAB-Simulink, simulación multibody.
- **CentraleSupélec** — L2S: modelado de sistemas complejos, control en espacio de estados.
- **Centrale Lyon** — Ampère · MIS: AMESim, SimulationX, modelado multifísico.

#### 1.2.1 Cinemática directa e inversa — 🟢 Núcleo
Transformaciones homogéneas, ángulos de Euler, parámetros DH. Fundamento de todo brazo robótico.

#### 1.2.2 Dinámica de manipuladores — 🟢 Núcleo
Ecuaciones de movimiento, torques, compensación de gravedad e inercia en tiempo real.

#### 1.2.3 Simulación (ROS, MATLAB, Gazebo) — 🟢 Núcleo
ROS/ROS2 como middleware estándar; MATLAB/Simulink para modelado; Gazebo/MuJoCo como simuladores físicos.

---

### 1.3 Robótica colaborativa (cobots) — 🔵 Muy cercano

Robots diseñados para trabajar junto a humanos de forma segura. Áreas clave: detección de colisiones, control de impedancia, certificaciones de seguridad (ISO TS 15066).

**Universidades y recursos:**
- **Centrale Nantes** — LS2N · RoMaS: plataforma cobots médicos 2024, HRC research.
- **CentraleSupélec** — L2S: control físico HRC, M2 Autonomous Systems.

---

### 1.4 Robótica médica — 🟣 Cercano

Brazos robóticos para cirugía (Da Vinci-like), rehabilitación o procedimientos de precisión. Requiere dominar HRI + control de fuerza + validación clínica.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N · NExT Talent (PercuCob): macro-mini robot, control admitancia/impedancia, ultrasonido guiado.
- **Centrale Lyon** — Ampère · MIS: robótica médica, diagnóstico operacional.

---

## 2. ⚙️ Control automático — 🔵 Muy cercano

Disciplina que estudia cómo hacer que un sistema siga una referencia deseada de forma estable y eficiente. Es la columna vertebral técnica de cualquier robot.

**Universidades y recursos:**
- **CentraleSupélec** — L2S · SYCOMORE: MPC robusto, control de UAVs, control no-lineal.
- **Centrale Nantes** — LS2N: MSc Control Systems (CORO CSYS), control dinámico.
- **Centrale Lyon** — Ampère / M2 EEEA: dSPACE HIL, LabVIEW, track Automatics.

### 2.1 Control clásico (PID, lazo cerrado) — 🔵 Muy cercano
Controladores proporcional-integral-derivativo. Punto de partida inevitable.

### 2.2 Control predictivo (MPC) — 🔵 Muy cercano
Optimiza la acción de control prediciendo el futuro. Ideal para brazos con restricciones de velocidad y torque.
- **CentraleSupélec** — L2S · SYCOMORE: MPC robusto no-lineal, evasión de obstáculos.

### 2.3 Control robusto (H∞, LMI) — 🔵 Muy cercano
Diseño de controladores funcionales ante incertidumbres. Clave para brazos con cargas variables.
- **CentraleSupélec** — L2S: H∞ synthesis, LMI design tools.

### 2.4 Control en tiempo real & HIL — 🔵 Muy cercano
Implementación de leyes de control en hardware real. dSPACE permite validar el controlador antes del robot real.
- **Centrale Lyon** — Ampère · MIS: bancos dSPACE, prototipado rápido Microchip, LabVIEW FPGA.

### 2.5 Control adaptativo — 🟣 Cercano
El controlador aprende y ajusta sus parámetros en tiempo real. Natural para un brazo que maneja cargas distintas.
- **Centrale Nantes** — LS2N: CORO CSYS, control adaptativo robusto.

---

## 3. 🧠 Inteligencia artificial aplicada — 🔵 Muy cercano

Algoritmos de aprendizaje que permiten a los robots mejorar su comportamiento con experiencia o datos. Complementa al control clásico.

**Universidades y recursos:**
- **CentraleSupélec** — DataIA-Cluster + L2S: DataIA France 2030, 800+ investigadores en IA, 47 laboratorios.
- **Centrale Nantes** — LS2N: CORO IMARO + DASSIP, redes neuronales para control.

### 3.1 Aprendizaje por refuerzo (RL) — 🔵 Muy cercano
El robot aprende por prueba y error en entornos simulados (Gym, MuJoCo). Algoritmos: PPO, SAC, TD3. Directamente aplicable a brazos que aprenden a agarrar objetos.
- **CentraleSupélec** — DataIA-Cluster: Deep RL research, INRIA Saclay.
- **Centrale Nantes** — LS2N · ARMEN: RL para locomoción robótica.

### 3.2 Visión artificial — 🔵 Muy cercano
Cámaras + algoritmos para "ver": detección de objetos (YOLO), estimación de pose 3D (6-DoF), segmentación. Permite al brazo saber qué agarrar y cómo.
- **CentraleSupélec** — L2S + M2 MMVAI: machine vision AI, cámaras SAR 3D, tomografía 3D.
- **Centrale Nantes** — LS2N · DASSIP: MSc Signal & Image Processing, percepción exteroceptiva.

### 3.3 Redes neuronales para control — 🔵 Muy cercano
Uso de redes neuronales como controladores o como modelos del sistema. Permite control cuando la dinámica es desconocida o compleja.
- **CentraleSupélec** — L2S: neural control synthesis, DataIA.
- **Centrale Nantes** — LS2N: cómputo dedicado para robótica.

### 3.4 Planificación de movimiento con IA — 🔵 Muy cercano
Algoritmos para trazar trayectorias evitando obstáculos: RRT*, PRM, motion planning con RL. Esencial para entornos dinámicos.
- **Centrale Nantes** — LS2N · ARMEN / RoMaS: motion planning, CORO IMARO.

---

## 4. 🔌 Sistemas embebidos — 🔵 Muy cercano

Hardware y firmware que ejecuta el control en tiempo real: microcontroladores, FPGA, drivers de motores, buses industriales.

**Universidades y recursos:**
- **Centrale Lyon** — Ampère (MIS + M2 EEEA): dSPACE, LabVIEW, GaN/SiC, Microchip Tech, EtherCAT.
- **Centrale Nantes** — LS2N: MSc Embedded Real-time Systems (CORO ERTS).

### 4.1 Electrónica de potencia & actuadores — 🔵 Muy cercano
Drivers para motores DC, BLDC, servos. Componentes GaN/SiC para alta eficiencia. **Centrale Lyon es uno de los únicos laboratorios en Francia con capacidad completa en GaN/SiC.**
- **Centrale Lyon** — Ampère: GaN/SiC únicos en Francia, sala 1MV, bancos de carga 500A.

### 4.2 Microcontroladores & FPGA — 🔵 Muy cercano
STM32, ARM Cortex-M para control de tiempo real. FPGA (Xilinx, Intel Altera) para control ultrarrápido de múltiples ejes.
- **Centrale Lyon** — Ampère: prototipado rápido Microchip, Control/Motion Desk.

### 4.3 Buses industriales (EtherCAT, CANbus) — 🟣 Cercano
EtherCAT para tiempo real duro, CANbus para sensores, ROS2 DDS para arquitecturas distribuidas.

### 4.4 Diseño de PCBs & hardware propio — 🟣 Cercano
KiCad, Altium Designer. Permite integrar sensores y actuadores a medida en el robot.

---

## 5. 📡 Percepción & sensores — 🔵 Muy cercano

El "sistema nervioso" del robot: cómo siente su entorno y su propio estado.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N (ReV + IMARO): LiDAR, cámaras estéreo, drones multi-sensor, bio-sensores eléctricos.
- **CentraleSupélec** — L2S: cámaras anecoicas, cámaras microondas, fusión de sensores.

### 5.1 Fusión de sensores — 🔵 Muy cercano
IMU + encoders + cámaras + LiDAR → estimación precisa de posición. Filtro de Kalman Extendido (EKF).
- **Centrale Nantes** — LS2N · IMARO: percepción exteroceptiva, fusión multi-sensor V2X.

### 5.2 Sensores de fuerza & torque — 🔵 Muy cercano
ATI, JR3 — miden fuerza ejercida por el brazo. Habilitan control de impedancia/admitancia para HRI segura.
- **Centrale Nantes** — LS2N · RoMaS (PercuCob): control híbrido posición-fuerza.

### 5.3 Visión 3D (LiDAR, RGBD, SLAM) — 🔵 Muy cercano
Intel RealSense, Azure Kinect para profundidad. SLAM para navegación. Permite ver objetos en 3D.
- **Centrale Nantes** — LS2N · Autonomous vehicles facility: LiDAR + V2X, SLAM, drones con cámaras.

### 5.4 Sensores propioceptivos (encoders) — 🟢 Núcleo
Encoders ópticos, resolvers. Miden el ángulo de cada articulación. El mínimo indispensable de cualquier brazo robótico.

---

## 6. 📊 Ciencia de datos & señales — 🟣 Cercano

Análisis de datos generados por el robot y sus sensores. Puente hacia mantenimiento predictivo o gemelos digitales.

**Universidades y recursos:**
- **CentraleSupélec** — L2S + DataIA-Cluster: Data Science M2, SAR imaging, 47 labs de IA.
- **Centrale Nantes** — LS2N: MSc DASSIP (Data Science Signal Image).

### 6.1 Procesamiento de señales (DSP) — 🟣 Cercano
FFT, filtrado digital, análisis espectral. Detecta vibraciones anómalas o extrae información de sensores de fuerza.
- **Centrale Nantes** — LS2N · DASSIP: MSc SIP.
- **CentraleSupélec** — L2S: signal processing research.

### 6.2 Mantenimiento predictivo — 🟣 Cercano
Datos históricos del brazo para predecir fallos. ML sobre series de tiempo. Muy valorado en la industria automotriz.
- **Centrale Lyon** — Ampère · socios Safran, Valeo: diagnóstico y seguridad operacional.

### 6.3 Big data industrial (IIoT) — 🟡 Relacionado
El brazo como nodo de una fábrica conectada. Edge computing, gemelos digitales, AWS IoT.
- **CentraleSupélec** — DataIA-Cluster: DataIku partners, industria del futuro.
- **Centrale Nantes** — LS2N: tema transversal "Industria del Futuro".

---

## 7. 🏭 Manufactura avanzada — 🟣 Cercano

Aplicación de robots y automatización en la producción industrial.

**Universidades y recursos:**
- **Centrale Nantes** — LS2N (RoMaS + ARMEN): CRAFT cable-driven robot, fábrica del futuro.
- **Centrale Lyon** — Ampère · socios Siemens, Schneider, Alstom: automatización industrial.

### 7.1 Industria 4.0 & fábrica del futuro — 🟣 Cercano
Automatización flexible, cobots en líneas de producción, gemelos digitales de procesos.
- **Centrale Nantes** — LS2N: tema transversal "Industria del Futuro".
- **CentraleSupélec** — Saclay industrial cluster: Airbus, Renault, Dassault partners.

### 7.2 Manufactura aditiva (impresión 3D) — 🟡 Relacionado
El robot CRAFT de Nantes se usa para manufactura aditiva de piezas grandes. Conexión con prototipado de piezas del brazo.
- **Centrale Nantes** — LS2N · CRAFT robot: manufactura aditiva de gran escala, composites.

### 7.3 Materiales compuestos — 🟡 Relacionado
Fibra de carbono, CFRP. Relevante si el brazo debe ser ligero y rígido. Plataforma específica en Nantes.
- **Centrale Nantes** — research platforms: composites experimental platform.

---

## 8. ⚫ Campos de referencia (distantes)

Presentes en el ecosistema de las universidades seleccionadas, pero fuera del eje brazo robótico + IA.

### 8.1 Energías renovables & marina — 🔴 Lejano
SEM-REV en Nantes: sitio offshore europeo único para energía marina. Comparte sistemas embebidos y control eléctrico, pero el contexto es completamente distinto.
- **Centrale Nantes** — SEM-REV offshore site.

### 8.2 Ingeniería naval / marítima — ⚫ Referencia
Los robots submarinos y offshore existen pero requieren un cambio completo de contexto.

### 8.3 Bioingeniería ambiental — ⚫ Referencia
Microbiología ambiental (Ampère), metagenómica de suelos (LS2N). Muy distante de robótica a menos que sea robótica médica.
- **Centrale Lyon** — Ampère · Bioengineering dept.: microbiología ambiental.

---

## Guía de decisiones futuras

Usa esta tabla para evaluar si integrar un nuevo campo al proyecto es viable:

| Si el brazo ya funciona y quieres agregar... | Distancia | Esfuerzo de integración | Recomendación |
|---|---|---|---|
| Visión artificial para agarre inteligente | 🔵 Muy cercano | Bajo | ✅ Integrar |
| Aprendizaje por refuerzo para movimientos | 🔵 Muy cercano | Bajo-Medio | ✅ Integrar |
| Sistema embebido en tiempo real (dSPACE) | 🔵 Muy cercano | Medio | ✅ Integrar |
| Control predictivo (MPC) | 🔵 Muy cercano | Medio | ✅ Integrar |
| Fusión de sensores (fuerza + visión + encoders) | 🔵 Muy cercano | Medio | ✅ Integrar |
| Mantenimiento predictivo sobre datos del brazo | 🟣 Cercano | Medio | 🟡 Viable como extensión |
| Gemelo digital (IIoT / edge computing) | 🟡 Relacionado | Alto | 🟡 Para proyectos más largos |
| Big data industrial | 🟡 Relacionado | Alto | ⚠️ Requiere justificación clara |
| Manufactura aditiva con el brazo | 🟣 Cercano | Medio-Alto | 🟡 Viable como caso de uso |
| Energías renovables | 🔴 Lejano | Muy alto | ❌ Cambio de contexto |
| Ingeniería naval | ⚫ Referencia | — | ❌ Campo distinto |

---

*Documento generado como parte del proyecto `notre_constellation` — Candidatura Beca France Excellence Eiffel 2026.*  
*Fecha de generación: Abril 2026.*
