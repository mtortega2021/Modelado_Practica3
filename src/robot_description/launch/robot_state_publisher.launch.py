from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import launch_ros.descriptions

def generate_launch_description():
    # Declare arguments
    description_file = LaunchConfiguration("description_file", default="robot.urdf.xacro")
    prefix = LaunchConfiguration("prefix", default="")
    use_sim_time = LaunchConfiguration('use_sim_time' , default='true')

    robot_description_content = Command([
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        PathJoinSubstitution([
            FindPackageShare("rover_description"), 
            "robots",
            description_file
        ]),
    ])

    robot_description_param = launch_ros.descriptions.ParameterValue(robot_description_content, value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': robot_description_param,
        }],
    )


    joint_state_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', PathJoinSubstitution([FindPackageShare("rover_description"), "rviz", "robot.rviz"])]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_gui_node
    ])
