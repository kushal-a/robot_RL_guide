# Isaac tools (and ROS)

This section will not cover core ROS but its only integrations with Isaac tools. The following will be discussed here.
1. [Isaac Sim](#isaac-sim), for simulation
2. [Isaac ROS](#isaac-ros), for tooling
3. [Isaac Lab](#isaac-lab), for learning

There are 3 compatibilites to check: 
| Interaction | Compatibility |
|--|--|
| Isaac Sim <-> Isaac Lab | Isaac Sim 4.5 and Isaac Lab 2.2 is currently supported, tested and [recommended](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html#local-installation) by NVIDIA |
| ROS <-> Isaac Sim | ROS humble on Ubuntu Jazzy for Isaac Sim 4.5.0 and 5.0 is [recommended](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/install_ros.html) by NVIDIA | 
| Isaac ROS <-> Isaac Sim | Isaac ROS 3.2.0 with Isaac Sim 4.5.0

For compatibility between the three tools, we will be using the following configuration.

    Isaac Sim 4.5.0
    Isaac Lab 2.2
    ROS Humble
    Ubuntu Jazzy 22.04

## Isaac Sim
Isaac Sim is a simulator, specializing in high end graphics rendering. 

You can either use native ROS, the barebone ROS built-in Isaac Sim for ROS integration. 

    Isaac Sim <-> Isaacsim.ros.bridge <-> Native ROS / built ROS of Isaac Sim


## Isaac ROS
Isaac ROS are a set of ROS packages. These are designed with NVIDIA-acceleration and for low latency.




## A few more terms

| Name | Description |
| -- | -- |
| [OpenUSD](https://docs.omniverse.nvidia.com/usd/latest) | NVIDIA's version of SDF, developed by PIXAR. Used for extremely [detailed scenes](https://docs.omniverse.nvidia.com/usd/latest/usd_content_samples/sample_content.html#) and robots |
| [OmniGraph](https://docs.omniverse.nvidia.com/extensions/latest/ext_omnigraph.html) | Visual Scripting Tool In Omniverse. Basically, it is like making a network of ROS nodes using drag and drop pulling the mouse to connect nodes with each other | 


```{toctree}
:maxdepth: 1
:hidden:

isaac/isaac-sim
isaac/isaac-ros
isaac/isaac-lab
```