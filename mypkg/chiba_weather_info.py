# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

import requests
from datetime import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("chiba_weather_info")  
pub = node.create_publisher(String, "weather", 10)
toggle = False  

def cb():
    global toggle
    msg = String()
    if toggle:
        msg.data = get_weather(next_day=True)
    else:
        msg.data = get_weather(next_day=False)
    toggle = not toggle
    pub.publish(msg)

def main():
    node.create_timer(10, cb)  
    rclpy.spin(node)

def get_weather(next_day):
    url = "https://weather.tsukumijima.net/api/forecast?city=120010"  
    response = requests.get(url)
    response.raise_for_status()

    data_json = response.json()

    if next_day:
        date_str = data_json["forecasts"][1]["date"]
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y年%m月%d日")
        city = "千葉市"
        weather = data_json["forecasts"][1]["telop"]
        max_temp = data_json["forecasts"][1]["temperature"]["max"]["celsius"] or "不明"
        min_temp = data_json["forecasts"][1]["temperature"]["min"]["celsius"] or "不明"
        chance_of_rain = data_json["forecasts"][1]["chanceOfRain"]
    else:
        date_str = data_json["forecasts"][2]["date"]
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y年%m月%d日")
        city = "千葉市"
        weather = data_json["forecasts"][2]["telop"]
        max_temp = data_json["forecasts"][2]["temperature"]["max"]["celsius"] or "不明"
        min_temp = data_json["forecasts"][2]["temperature"]["min"]["celsius"] or "不明"
        chance_of_rain = data_json["forecasts"][2]["chanceOfRain"]

    chance_of_rain_str = (f"0時から6時までの降水確率は{chance_of_rain.get('T00_06', '不明')}、"
                          f"6時から12時までの降水確率は{chance_of_rain.get('T06_12', '不明')}、"
                          f"12時から18時までの降水確率は{chance_of_rain.get('T12_18', '不明')}、"
                          f"18時から24時までの降水確率は{chance_of_rain.get('T18_24', '不明')}です。")

    results = (f"{date}、{city}の天気は{weather}です。\n"
               f"最高気温は{max_temp}度、最低気温は{min_temp}度です。\n"
               f"{chance_of_rain_str}")

    return results

if __name__ == "__main__":
    main()

