# Isaac Sim

The following things are covered for Isaac Sim here:

```{toctree}
:maxdepth: 2

isaac-sim/isaac-sim-standalone
isaac-sim/isaac-sim-with-ros

```
## Important links

[Documentation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/index.html) | [Website](https://developer.nvidia.com/isaac/sim) | [Reference Architecture](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/reference_architecture.html) (this is a must read)

> [!TIP]
> Unless you are simulating hundreds of rigid bodies and robots, it is more efficient to use the CPU solver instead of the GPU solver. Refer to the Environment Setup tutorial


## Choosing installation method, clash of the titans
Native installation of Isaac Sim is stable. Isaac Sim requires CUDA to run the simulation on GPU. Tensorflow, which is a part of the other workflow, also requires CUDA to run its training on NVIDIA's GPUs. Since we want to able to develop in both workflows on the same PCs, compatibility of drivers, CUDA, python and other dependencies is crucial. In addition to this, ROS has its own requirements and installation of python and its libraries. To prevent incompatibility among so many libraries and applications, we will be developing both these workflows and ROS in seperate docker containers. Hence, a containerized installation for Isaac Sim, and subsequently other applications/packages is chosen.

Irrespective of the installation method, you will receive an `isaac-sim` folder which contains key plugins and scripts to interact with Isaac Sim. The contents and uses of this folder is discussed in [Filesystem](./filesystem.md).

