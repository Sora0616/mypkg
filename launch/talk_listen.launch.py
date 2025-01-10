# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='sotobo_tation_publisher',
            name='sotobo_station_publisher',
            output='screen',
        ),
    ])

