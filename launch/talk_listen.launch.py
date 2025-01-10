from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='station_publisher',
            name='station_publisher',
            output='screen',
        ),
    ])

