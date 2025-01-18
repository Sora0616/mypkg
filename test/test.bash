#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier:BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

sudo apt -y install python3-pip
pip3 install requests

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source install/setup.bash && source install/local_setup.bash

# 新しいノードの起動とログの確認
timeout 45 ros2 launch mypkg talk_listen.launch.py &> /tmp/mypkg.log

# ログを表示
cat /tmp/mypkg.log

# ログから千葉市の天気情報を抽出
cat /tmp/mypkg.log |
grep '千葉市の天気は'

