# mypkg
[![test](https://github.com/Sora0616/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Sora0616/mypkg/actions/workflows/test.yml)


## ノードの概要
このパッケージは次のファイルで構成されています：
- `__init__.py`: パッケージの初期化を行う。
- `chiba_weather_info.py`: 千葉市の明日、明後日の天気情報を１０秒ごと交互にパブリッシュする。
- `listener.py`: トピックからデータを受信する。

## 実行方法
実行は以下のコマンドで行う。

端末1
```
ros2 run mypkg chiba_weather_info
```
端末2
```
ros2 topic echo /weather
```
実行結果
```
data: '2025年01月21日、千葉市の天気は曇りです。

  最高気温は12度、最低気温は5度です。

  0時から6時までの降水確率は20%、6時から12時までの降水確率は10%、12時から18時までの降水確率は10%、18時から24時までの降水確率は10%です。'
---
data: '2025年01月22日、千葉市の天気は晴時々曇です。

  最高気温は12度、最低気温は6度です。

  0時から6時までの降水確率は20%、6時から12時までの降水確率は20%、12時から18時までの降水確率は20%、18時から24時までの降水確率は20%です。'
---
data: '2025年01月21日、千葉市の天気は曇りです。

  最高気温は12度、最低気温は5度です。

  0時から6時までの降水確率は20%、6時から12時までの降水確率は10%、12時から18時までの降水確率は10%、18時から24時までの降水確率は10%です。'
---
data: '2025年01月22日、千葉市の天気は晴時々曇です。

  最高気温は12度、最低気温は6度です。

  0時から6時までの降水確率は20%、6時から12時までの降水確率は20%、12時から18時までの降水確率は20%、18時から24時までの降水確率は20%です。'
---
```

## 注意点
listener.pyはテスト用。
talk_listen.launch.pyはノードを立ち上げるためのコード。

## 動作環境
このパッケージは以下の環境で動作確認済み

- ROS 2 humble
- Ubuntu 22.04 LTS
   
## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
    - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
#### © 2025 Sora Hirano
