from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Path to the standard TurtleBot3 SLAM launch
    tb3_slam_dir = FindPackageShare('turtlebot3_slam')
    
    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        
        # Includes the SLAM Toolbox or Cartographer logic
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([tb3_slam_dir, '/launch/slam.launch.py']),
            launch_arguments={'use_sim_time': LaunchConfiguration('use_sim_time')}.items(),
        ),
    ])
