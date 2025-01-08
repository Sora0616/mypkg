# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
from bs4 import BeautifulSoup

class TokyoStationDelayInfoPublisher(Node):
    def __init__(self):
        super().__init__('tokyo_station_delay_info_publisher')
        self.publisher_ = self.create_publisher(String, 'traffic', 10)
        self.create_timer(5.0, self.publish_delay_info)

    def publish_delay_info(self):
        msg = String()
        msg.data = self.get_delay_info()
        self.publisher_.publish(msg)

    def get_delay_info(self):
        url = "https://traininfo.jreast.co.jp/train_info/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            delay_info = soup.find('div', class_='delay-info')
            if delay_info:
                return "現在の遅延状況: 東京駅での遅延があります。"
            else:
                return "現在の遅延状況: 東京駅での遅延はありません。"
        else:
            return "現在の遅延状況: 遅延情報を取得できませんでした。"

def main(args=None):
    rclpy.init(args=args)
    node = TokyoStationDelayInfoPublisher()
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

