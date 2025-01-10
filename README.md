# 外房線駅名ノード
[![test](https://github.com/Sora0616/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Sora0616/mypkg/actions/workflows/test.yml)

## 概要
- ROS2のパッケージ

- 外房線の駅名を毎秒トピックにパブリッシュする。

## 実行方法
実行は以下のコマンドで行う。
端末1
```
ros2 run mypkg station_publisher
```
端末2
```
ros2 topic echo /stations
```
実行結果(1部抜粋)
```
data: 千葉
---
data: 本千葉
---
data: 蘇我
---
data: 鎌取
---
data: 誉田
---
data: 土気
---
data: 大網
---
data: 永田
---
data: 本納
---
data: 新茂原
---
data: 茂原
---
data: 八積
---
data: 上総一ノ宮
---
```

## 注意点
talk_listen.launch.pyはテスト用。

## 必要なソフトウェア
- python
- ROS 2 humble
## テスト済み環境
- Ubuntu 22.04 LTS
   
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
© 2025 Sora Hirano
