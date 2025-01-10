# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StationPublisher(Node):
    def __init__(self):
        super().__init__('station_publisher')
        self.publisher_ = self.create_publisher(String, 'stations', 10)
        timer_period = 1  # タイマーの周期を1秒に設定
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.stations = [
            "千葉", "本千葉", "蘇我", "鎌取", "誉田", "土気",
            "大網", "永田", "本納", "新茂原", "茂原", "八積",
            "上総一ノ宮", "東浪見", "太東", "長者町", "三門",
            "大原", "浪花", "御宿", "勝浦", "鵜原", "上総興津",
            "行川アイランド", "安房小湊", "安房天津", "安房鴨川"
        ]
        self.index = self.stations.index("千葉")  # インデックスを「千葉」に初期化

    def timer_callback(self):
        try:
            msg = String()
            msg.data = self.stations[self.index]  # 現在の駅名をメッセージに設定
            self.publisher_.publish(msg)  # メッセージをパブリッシュ
            self.index = (self.index + 1) % len(self.stations)  # インデックスを更新
        except Exception as e:
            print(f'Error in timer_callback: {e}')  # エラーメッセージを出力

def main(args=None):
    rclpy.init(args=args)
    station_publisher = StationPublisher()
    try:
        rclpy.spin(station_publisher)  # ノードをスピン
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            station_publisher.destroy_node()  # ノードを破棄
            rclpy.shutdown()  # rclpyをシャットダウン

if __name__ == '__main__':
    main()

