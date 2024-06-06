import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',   #/dev/ttyUSB0
                'serial_baudrate': 115200 ,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard',
                'queue_size':1000
            }]
        )
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='laser_broadcaster',
        #     arguments=['0.2', '0','0.1','0', '0','1.5708','base_link', 'laser_frame']

        # )
    ])
