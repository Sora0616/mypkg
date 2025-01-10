#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sora Hirano
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source /opt/ros/foxy/setup.bash  # ここで正しいパスを確認

# ノードを直接起動
timeout 60 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# ログファイルの内容を確認
cat /tmp/mypkg.log | grep -E '千葉|安房鴨川'

# 結果の表示
if grep -q "千葉" /tmp/mypkg.log && grep -q "安房鴨川" /tmp/mypkg.log; then
  echo "トピック stations に正しいデータが発信されています。成功です。"
else
  echo "トピック stations に正しいデータが発信されていません。エラーです。"
fi

