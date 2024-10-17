#!/bin/bash
source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
colcon build
source install/setup.bash
ros2 launch Indoor indoor_sim_env_launch.py
