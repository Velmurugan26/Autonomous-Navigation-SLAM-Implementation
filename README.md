#Autonomous Navigation & Real-Time SLAM using ROS

Building a robot that can explore, understand, and navigate an unknown environment autonomously

##Project Motivation

One of the biggest challenges in robotics is enabling a robot to move independently in an environment it has never seen before.

This project focuses on solving that problem by implementing Simultaneous Localization and Mapping (SLAM) and autonomous navigation using the ROS Navigation Stack.

The robot is able to:

Explore an unknown environment

Build a map in real time

Estimate its own position continuously

Plan safe paths to target locations

Navigate autonomously without human assistance

This project demonstrates my practical experience in building a complete end-to-end autonomous robotics system, similar to those used in real-world service robots and warehouse automation.

🎯 Project Objectives

The main goals of this project were:

Implement real-time SLAM for unknown environments

Integrate ROS Navigation Stack for autonomous movement

Deploy the system on embedded hardware (Raspberry Pi)

Enable manual control for environment exploration

Visualize mapping and navigation in RViz

🚀 Key Features
Real-Time Environment Mapping

Generates occupancy grid maps while the robot moves

Uses GMapping SLAM algorithm

No prior map required

Autonomous Navigation

Uses Move Base for global and local path planning

Avoids obstacles dynamically

Reaches target goals safely

Localization

Uses AMCL (Adaptive Monte Carlo Localization)

Continuously estimates robot position on the map

Manual Teleoperation

Keyboard-based control for exploration

Useful for initial map generation

Live Visualization

Real-time monitoring using RViz:

Map

Robot position

Sensor data

Navigation path

🛠️ Technologies & Tools
Robotics Framework

ROS (Robot Operating System)

ROS Navigation Stack

Algorithms

GMapping (SLAM)

AMCL (Localization)

DWA Local Planner

Global Path Planning

Hardware

TurtleBot platform

Raspberry Pi

LIDAR / depth sensor (simulation or hardware)

Software & Programming

Python

C++

Ubuntu Linux

RViz
