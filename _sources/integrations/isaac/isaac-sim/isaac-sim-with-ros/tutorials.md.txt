# Examples from documentation

[Tutorial Documentation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/ros2_tutorials/index.html)

## Tutorial Workflow Compatibility

The following are the compatibility of these examples with different Isaac Sim workflow.

:::{list-table}
:widths: 30% 20% 25% 25%
:header_rows: 1
✅ | ❌ | ❌ |
| Example | GUI | Scripting | Standalone Python |
|---------|------|----------|------------------|
| URDF Import: Turtlebot | ✅ | ❌ | ❌ |
| Driving TurtleBot via ROS2 messages |✅ | ❌ | ❌ |
| ROS2 Clock | ✅ | ❌ | ❌ |
| ROS 2 Publish Real Time Factor (RTF) |✅ | ❌ | ❌ |
| ROS2 Cameras | ✅ | ❌ | ❌ |
| Publishing Camera’s Data - same as ROS2 Cameras | ❌ | ✅ | ✅ |
| RTX Lidar Sensors |  ✅ | ✅ | ✅ |
| ROS2 Transform Trees and Odometry | ✅ | ❌ | ❌ |
| ROS2 Setting Publish Rates | | |
| ROS 2 Quality of Service (QoS) |✅ | ❌ | ❌ |
| ROS2 Joint Control: Extension Python Scripting |✅ | ✅ | ✅ |
| NameOverride Attribute | ✅ | ❌ | ❌ |
| ROS 2 Ackermann Controller |✅ | ❌ | ❌ |
| Automatic ROS 2 Namespace Generation |✅ | ✅ | ✅ |
| ROS 2 Bridge in Standalone Workflow |❌ | ✅ | ✅ [here](../isaac-sim-standalone/standalone-python-workflow/standalone_examples/api.md/#ros-bridge) |
| ROS2 Navigation |❌ | ✅ | ✅ [here](../isaac-sim-standalone/standalone-python-workflow/standalone_examples/api.md/#ros-bridge) |
| Multiple Robot ROS2 Navigation |❌ | ✅ | ✅ |
| ROS 2 Navigation with Block World Generator |✅ | ❌ | ❌ |
| MoveIt 2 |✅ | ❌ | ❌ |
| ROS 2 Generic Publisher and Subscriber |✅ | ❌ | ❌ but available [here](../isaac-sim-standalone/standalone-python-workflow/standalone_examples/api.md/#ros-bridge) |
| ROS 2 Generic Server and Client | ✅ | ❌ | ❌
| ROS 2 Service for Manipulating Prims Attributes |✅ | ❌ | ❌
| ROS 2 Python Custom Messages |❌ | ✅ | ✅ |
| ROS 2 Python Custom OmniGraph Node | | |
| ROS 2 Custom C++ OmniGraph Node | | |
| ROS 2 Launch | | | command line|


:::

A lot of the tasks are performed as a mixture of GUI Omnigraph creation and python scripting. 