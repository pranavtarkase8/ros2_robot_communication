import rclpy
from rclpy.node import Node

from robot_interfaces.msg import RobotStatus


class RobotSubscriber(Node):

    def __init__(self):
        super().__init__('robot_subscriber')

        self.subscription = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.robot_status_callback,
            10
        )

    def robot_status_callback(self, msg):

        self.get_logger().info(
            f'Received -> Name: {msg.robot_name}, '
            f'ID: {msg.robot_id}, '
            f'Battery: {msg.battery_percentage}%'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotSubscriber()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
