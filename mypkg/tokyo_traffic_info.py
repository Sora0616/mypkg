# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TokyoTrafficInfoPublisher(Node):
    def __init__(self):
        super().__init__('tokyo_traffic_info_publisher')
        self.publisher_ = self.create_publisher(String, 'tokyo_traffic_info', 10)
        self.publisher_position = self.create_publisher(String, 'now_position', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Current traffic status: Smooth traffic on all major roads.'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing traffic info: "%s"' % msg.data)

        position_msg = String()  
        position_msg.data = 'Current position: Tokyo Station'
        self.publisher_position.publish(position_msg)
        self.get_logger().info('Publishing position info: "%s"' % position_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = TokyoTrafficInfoPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()

