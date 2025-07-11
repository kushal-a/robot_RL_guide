# API in `standalone_examples`

API is divided in the following groups
## Asset
script for URDF import
## Core
There are two types of core functions covered.
### API
There are scripts that perform standard actions. This includes:
1. Adding Cubes
2. adding Franka Robot
3. Adding a cloth
4. Controlling a robot: Joint position controller for a manipulator
5. Logging Data
6. Derfmable objects
7. Viewing Contact data
8. Making omnigraph triggers
9. rigit contact viewing
10. simulating a robot
11. simulation callbacks
12. time stepping
13. Visualizing materials
### Cloner
A script that creates clones of ants. This can be used to spawn a large number of robots and managee its articulation.
## Cortex
TODO
### Replicator
### Behaviour
### Domain Randomization## Examples
## Robot
TODO
### Manipulator
### Policy
### Wheeled Robots
## ROS bridge

Making ROS nodes to publish or subscribe to data from Isaac Sim. The following examples are available.

Manual Camera Publishing, Periodic Camera Publishing, Clock, MoveIt, RTX LIDAR, Standard Subscriber, Carter's Stereo and Carter's Multi Robot Navigation.

Carter is like turtlebot
## Sensor
Contains standalone scripts for the following sensors:

:**Camera**: camera, camera with openCV, fisheye camera with openCV, Camera with ROS, Camera with viewing

:**Physics**: Contact, Effort and IMU

:**PhysX**: Rotating LIDAR

:**RTX**: Rotating LIDAR

## Simulation App
Run scipts to get empty world. There are scripts for default world, livestreaming (used in docker installation), contant fps, changing resolution and loading sample stage.
## Util

Contains a script to detech clash in Carter and to draw points seen by Lidar/Radar as debug draw.
## XR
Script for hand tracking in XR.
## Omni
Contains files that use Omni API for asset conversion and to run simulation in async. This way simulation can be started and then script can be run to execute commands. This is used in a manipulation examples. There is also a file called `app_framework.py` which I am not sure what it does.


