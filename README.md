# ROS 2 Robot Communication
Objective
Create two ROS 2 packages and communicate robot name, robot ID and battery status using a custom message.

# Packages 1
robot_interfaces
         Contains RobotStatus.msg
# Package 2
robot_communication
        publisher_node (Sender node)
        subscriber_node (Receiver node)
        Launch file
# Custom Message
string robot_name 
int32 robot_id 
float32 battery_status

# source Terminal
source /opt/ros/humble/setup.bash 
source ~/pranav_ws/install/setup.bash
# launch file
ros2 launch robot_communication robot_communication.launch.py
