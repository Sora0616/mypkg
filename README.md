# 外房線駅名ノード
[![test](https://github.com/Sora0616/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Sora0616/mypkg/actions/workflows/test.yml)

## 概要
- ROS2のパッケージ

- 外房線の駅名を毎秒トピックにパブリッシュする。

## 実行方法
実行は以下のコマンドで行う。
```
ros2 run mypkg station_publisher
```
トピックの確認は以下のコマンドで確認する。
```
ros2 topic echo /stations
```
```


## 注意点
talk_listen.launch.pyはテスト用。
