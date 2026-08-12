import rclpy
from rclpy.node import Node

from robot_interfaces.msg import RobotStatus


class RobotPublisher(Node):

    def __init__(self):
        super().__init__('robot_publisher')

        self.publisher = self.create_publisher(
            RobotStatus,
            'robot_status',
            10
        )

        self.timer = self.create_timer(2.0, self.publish_robot_status)

    def publish_robot_status(self):

        msg = RobotStatus()

        msg.robot_name = 'Pranav_bot'
        msg.robot_id = 101
        msg.battery_percentage = 85.5

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Sent -> Name: {msg.robot_name}, '
            f'ID: {msg.robot_id}, '
            f'Battery: {msg.battery_percentage}%'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
