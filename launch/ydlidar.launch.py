import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ydlidar_ros2_driver',
            executable='ydlidar_ros2_driver_node',
            name='ydlidar_x3',
            output='screen',
            parameters=[{
                'port': '/dev/ttyUSB0',        # Kiểm tra lại port đúng với thiết bị
                'frame_id': 'laser',           # Đổi sang 'laser' cho nhất quán
                'ignore_array': '',
                'baudrate': 115200,
                'low_exposure': False,
                'reversion': True,
                'resolution_fixed': True,
                'auto_reconnect': True,
                'isSingleChannel': False,
                'angle_max': 179.5,
                'angle_min': -179.5,
                'range_max': 12.0,
                'range_min': 0.1,
                'frequency': 10.0,
                'sample_rate': 4,
                'scan_frequency': 6.0
            }],
            remappings=[
                ('/scan', '/scan')  # đảm bảo /scan tồn tại
            ]
        )
    ])
