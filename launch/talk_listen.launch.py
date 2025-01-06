# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    tokyo_traffic_info_publisher = launch_ros.actions.Node(
        package='mypkg',
        executable='tokyo_traffic_info',
    )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([
        tokyo_traffic_info_publisher,
        listener
    ])

