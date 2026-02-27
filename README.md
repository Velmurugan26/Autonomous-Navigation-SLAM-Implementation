# 📘 Technical Report: Autonomous Navigation & SLAM Implementation
**Author:** Anantharajan Vel Murugan  
**Project Type:** Robotics & AI Engineering Portfolio  
**Platform:** TurtleBot + Raspberry Pi + ROS 2  

---

## 1. Executive Summary
This project demonstrates a full-stack robotics implementation focusing on **Simultaneous Localization and Mapping (SLAM)**. [cite_start]As a final-year student at the **University of Hertfordshire (PSB Academy)**, I developed this system to solve the challenges of real-time mapping in unknown indoor environments[cite: 4, 27]. [cite_start]The project bridges the gap between low-level hardware control and high-level AI path planning[cite: 7, 15].

---

## 2. System Architecture & Hardware Specs
[cite_start]To achieve high-fidelity mapping, I integrated several hardware layers to ensure stable data flow between sensors and the central processing unit[cite: 11, 21].

### 2.1 Hardware Breakdown
| Component | Specification | Role |
| :--- | :--- | :--- |
| **SBC** | Raspberry Pi 4 | [cite_start]Central ROS 2 compute node [cite: 11, 15] |
| **Lidar** | 360° Laser Scanner | [cite_start]Environment perception and distance measuring [cite: 15] |
| **Microcontroller** | STM32 / Arduino | [cite_start]Low-level motor PWM and encoder feedback [cite: 11, 22] |
| **Chassis** | Custom 3D Printed | [cite_start]Designed in Fusion 360 for sensor stability [cite: 9, 21] |



---

## 3. Software Implementation & AI Logic
[cite_start]The "AI-First" mindset of this project relies on efficient data processing and algorithm selection[cite: 7].

### 3.1 SLAM Pipeline
I utilized **SLAM algorithms** to generate environment occupancy grids. This process involves:
* [cite_start]**Laser Scan Matching:** Comparing consecutive LiDAR frames to estimate movement.
* [cite_start]**Loop Closure:** Identifying previously visited areas to correct odometry drift.
* [cite_start]**Map Generation:** Exporting high-resolution `.pgm` and `.yaml` files for navigation.

### 3.2 Navigation & Path Planning
[cite_start]Once the map is generated, the **ROS Navigation Stack** handles movement[cite: 15]:
* **Global Planner:** Uses A* logic to find the shortest path on the static map.
* **Local Planner:** Uses Dynamic Window Approach (DWA) to avoid obstacles in real-time.

---

## 4. Engineering Challenges & Solutions
[cite_start]During development, I encountered several technical hurdles that required iterative debugging[cite: 6]:

1. **Odometry Drift:** Wheel slippage caused inaccurate mapping.  
   * [cite_start]**Solution:** Fused IMU data with encoder feedback to improve localization accuracy[cite: 15, 22].
2. **Computational Latency:** Running SLAM on a Raspberry Pi can be intensive.  
   * [cite_start]**Solution:** Optimized node execution and offloaded visualization to a remote workstation via ROS 2 Discovery Server[cite: 15].

---

## 5. Development Workflow (A-Z)
### 5.1 Prerequisites
* [cite_start]**OS:** Ubuntu Linux (ROS 2 Humble/Foxy) [cite: 15]
* [cite_start]**Languages:** Python (AI Logic) and C (Embedded Drivers) [cite: 10, 11]
* [cite_start]**Tools:** Visual Studio Code, GitHub, Webots [cite: 12, 17]

### 5.2 Deployment Steps
1. **Initialize Hardware:**
   ```bash
   ros2 launch turtlebot3_bringup robot.launch.py
