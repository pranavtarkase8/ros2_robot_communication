from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher_node = Node(
        package='robot_communication',
        executable='robot_publisher',
        name='robot_publisher',
        output='screen'
    )

    subscriber_node = Node(
        package='robot_communication',
        executable='robot_subscriber',
        name='robot_subscriber',
        output='screen'
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
