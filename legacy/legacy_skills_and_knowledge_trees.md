# Legacy Skills and Knowledge Trees Summary

*This document consolidates the "Knowledge Tree" (mapping the fields of knowledge for the Robotic Arm with AI project) and the "Skills Tree" (mapping Cristopher's current profile against project requirements).*

## 1. Project Core: Robotic Arm with AI
The project sits at the intersection of Mechatronics and Intelligent Systems, requiring a fusion of mechanical design, automatic control, and artificial intelligence.

### Key Knowledge Areas & School Resources:
- **Robotics (Core):** Modeling, kinematics (DH, Jacobian), dynamics, and simulation (ROS, Gazebo). 
  - *Resources:* Centrale Nantes (LS2N, RoMaS), CentraleSupélec (L2S), Centrale Lyon (Ampère).
- **Automatic Control:** Classic control (PID), predictive control (MPC), robust control, and HIL (Hardware-In-the-Loop).
  - *Resources:* Centrale Lyon (Ampère dSPACE banks), CentraleSupélec (L2S).
- **Artificial Intelligence:** Reinforcement Learning (Gym, MuJoCo), Computer Vision (YOLO, Pose estimation), and Neural Networks for control.
  - *Resources:* CentraleSupélec (DataIA-Cluster), Centrale Nantes (LS2N).
- **Embedded Systems & Power Electronics:** Microcontrollers (STM32), FPGAs, GaN/SiC components for motor drivers.
  - *Resources:* Centrale Lyon (Ampère - unique GaN/SiC capacity in France).
- **Perception & Sensors:** Sensor fusion (Kalman filters), 3D Vision (LiDAR, RGBD, SLAM), force/torque sensors, and encoders.

## 2. Cristopher's Profile vs. Project Requirements

### ✅ Strengths (Ready to Apply)
- **AI & Multi-agent Orchestration:** Highly proficient from Oracle internship (LangGraph, A2A, RAG, OCI). Can build the decision architecture of the robot.
- **Computer Vision:** Strong base from FRC (OpenCV). Ready to extend to 3D pose estimation.
- **Software, APIs & Cloud:** Strong in Python, FastAPI, Docker, and CI/CD pipelines. Can build the robot's cloud backend and web dashboards.
- **Mechanical Design & 3D Scanning:** Professional level in Fusion360, 3D printing, and reverse engineering (Raptor IR scanner). Can build the physical arm.
- **C++ & Embedded (Base):** Good foundation from FRC and FLOW (ESP32).

### 🔴 Critical Gaps (To be addressed before/during the Double Degree)
1. **ROS2 (Priority 1):** The standard robotics middleware. Necessary to connect the AI logic (LangGraph) with physical control.
2. **Formal Automatic Control (Priority 2):** Lacks formal theoretical background in kinematics and PID/MPC. Essential for precise arm movement.
3. **Power Electronics & Motor Drivers (Priority 3):** Needs knowledge of BLDC drivers (like ODrive) and FOC (Field Oriented Control) to move the physical arm.
4. **Sensor Fusion (Priority 4):** Needs to learn Kalman filtering (EKF) to process noisy sensor data.

## 3. Strategic Argument for Eiffel Scholarship
*"My profile combines real-world experience in multi-agent AI systems (Oracle, LangGraph), computer vision for real-time robotics (FRC, OpenCV), and professional mechanical design/3D scanning. I have the software skills to build the high-level architecture of an AI-driven robotic arm, but I require the formal engineering resources of [Target School] — specifically [Target Lab/Equipment] — to develop the formal control layer (kinematics, MPC, HIL) that connects my AI foundation with physical hardware. This combination makes my project viable and is only possible at your institution."*
