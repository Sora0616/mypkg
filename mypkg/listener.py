# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TokyoTrafficInfoListener(Node):
    def __init__(self):
        super().__init__('tokyo_traffic_info_listener')
        self.subscription = self.create_subscription(
            String,
            'tokyo_traffic_info',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received traffic info: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = TokyoTrafficInfoListener()
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

