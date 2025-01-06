# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

from rclpy.node import Node
import rclpy
from std_msgs.msg import String
import requests
import time

class TokyoTrafficInfoPublisher(Node):
    def __init__(self):
        super().__init__('tokyo_traffic_info_publisher')
        self.publisher_ = self.create_publisher(String, 'tokyo_traffic_info', 10)
        self.timer = self.create_timer(1.0, self.publish_traffic_info)

    def publish_traffic_info(self):
        try:
            # 交通情報APIから東京駅周辺の交通情報を取得
            response = requests.get('https://api.example.com/traffic_info?location=tokyo_station')
            response.raise_for_status()
            data = response.json()

            # 交通情報をフォーマット
            traffic_info = data['traffic']
            message = f"Latest Tokyo Station Traffic Info: {traffic_info}"

            # メッセージをパブリッシュ
            msg = String()
            msg.data = message
            if rclpy.ok():
                self.publisher_.publish(msg)

        except requests.exceptions.RequestException as e: 
            if rclpy.ok(): 
                self.get_logger().error(f"HTTP error: {e}")
        except Exception as e:
            if rclpy.ok():
                self.get_logger().error(f"Error publishing traffic info: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = TokyoTrafficInfoPublisher()
    print("TokyoTrafficInfoPublisher node started. Publishing traffic info to 'tokyo_traffic_info' topic.")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error during spin: {e}")
    finally:
        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()

