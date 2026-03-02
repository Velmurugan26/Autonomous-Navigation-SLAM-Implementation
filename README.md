# Autonomous Navigation & SLAM using ROS2 | TurtleBot3

## Project Summary

This project demonstrates a complete autonomous mobile robot system built using ROS2 and the Navigation2 (Nav2) stack. The robot is capable of mapping unknown environments, localizing itself within the generated map, and navigating autonomously to user-defined goals while avoiding obstacles.

The objective of this project was to gain hands-on experience with real-world autonomous robotics systems, focusing on the integration of perception, localization, planning, and control on a physical robot platform.

This work reflects practical implementation experience in autonomous navigation using industry-standard robotics tools.

---

## Key Highlights

- Real-time environment mapping using SLAM  
- Occupancy grid map generation and reuse  
- Localization using AMCL (particle filter)  
- Autonomous goal-based navigation  
- Global path planning and local trajectory control  
- Dynamic obstacle avoidance using costmaps  
- System visualization and debugging in RViz  
- Deployment on TurtleBot3 with Raspberry Pi  

---

## System Architecture

The navigation pipeline follows a complete robotics workflow:

**LiDAR Sensor → SLAM → Map Server → AMCL Localization → Nav2 Stack → Velocity Commands → Robot Motion**

Nav2 Components:
- Global Planner (A*-based)
- Local Controller
- Global and Local Costmaps
- Recovery Behaviors

All system states and robot behavior are monitored in RViz.

---

## Hardware Platform

- TurtleBot3 (Burger)
- Raspberry Pi (Onboard computation)
- 2D LiDAR sensor
- Ubuntu-based remote workstation
- WiFi communication

---

## Software Stack

- Ubuntu 22.04
- ROS2 Humble
- Navigation2 (Nav2)
- SLAM Toolbox / Cartographer
- AMCL
- RViz2
- TurtleBot3 ROS2 packages

---

## Project Workflow

### 1. Environment Mapping (SLAM)

The robot is manually controlled using keyboard teleoperation while SLAM runs in real time.  
During this phase, LiDAR data is processed to generate an occupancy grid map of the environment.

The generated map is saved for future navigation tasks.

---

### 2. Localization

When the saved map is loaded, the robot uses **Adaptive Monte Carlo Localization (AMCL)** to estimate its pose using a particle filter and sensor observations.

---

### 3. Autonomous Navigation

Once localized, navigation goals are provided through RViz using the **2D Goal Pose** tool.

The Nav2 stack performs:
- Global path planning
- Local motion control
- Obstacle avoidance
- Recovery behaviors when necessary



