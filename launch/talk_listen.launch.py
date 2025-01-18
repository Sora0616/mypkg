# SPDX-FileCopyrightText: 2025 Sora Hirano <s23c1115wh@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    weather_pub = launch_ros.actions.Node(
        package='mypkg',
        executable='chiba_weather_info',
        name='chiba_weather_info',
        output='screen'
    )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        name='listener',
        output='screen'
    )

    return launch.LaunchDescription([weather_pub, listener])

