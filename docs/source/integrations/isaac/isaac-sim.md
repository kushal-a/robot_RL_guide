# Isaac Sim

The following things are covered for Isaac Sim here:

```{toctree}
:maxdepth: 2

isaac-sim/isaac-sim-standalone
isaac-sim/isaac-sim-with-ros
isaac-sim/isaac-sim-with-replicator
isaac-sim/isaac-sim-with-digital-twin

```
## Important links

[Documentation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/index.html) | [Website](https://developer.nvidia.com/isaac/sim) | [Reference Architecture](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/reference_architecture.html) (this is a must read)

:::{tip}
Unless you are simulating hundreds of rigid bodies and robots, it is more efficient to use the CPU solver instead of the GPU solver. Refer to the Environment Setup tutorial
:::

## Choosing installation method, clash of the titans
Native installation of Isaac Sim is stable. Isaac Sim requires CUDA to run the simulation on GPU. Tensorflow, which is a part of the other workflow, also requires CUDA to run its training on NVIDIA's GPUs. Since we want to able to develop in both workflows on the same PCs, compatibility of drivers, CUDA, python and other dependencies is crucial. In addition to this, ROS has its own requirements and installation of python and its libraries. To prevent incompatibility among so many libraries and applications, we will be developing both these workflows and ROS in seperate docker containers. Hence, a containerized installation for Isaac Sim, and subsequently other applications/packages is chosen.

Irrespective of the installation method, you will receive an `isaac-sim` folder which contains key plugins and scripts to interact with Isaac Sim. The contents and uses of this folder is discussed in [Filesystem](./isaac-sim/isaac-sim-standalone/understanding-filesystem.md).

## How ROS fits in

Since Isaac Sim is just a simulator, it has to be used for "something". NVIDIA calls this something as digital twin, fancy word for robot inside screen. But what can we do with having a digital twin.

Applications:
1. Synthetic Data Generation

    Usually simualators just take information, run some physics and spit some information back. But when using Isaac Sim for some larger ML application, sometimes the data might not be enough. 

    Example:

    > :Problem: Cannot get data of all possible lighting conditions for      street mapping
    > :Solution: Simulate in simulator to control lighting conditions.
    > :New Problem: Too many environments to configure
    > :Solution: NVIDIA uses Replicator to randomize lighting, generating data for Isaac Sim

    Replicator can randomize any variable for synthetic data generation
    
2. Software in Loop:   Run your robotics stack on PC for testing

3. Hardware in Loop: Run your robotics stack on hardware (eg.Jetson) for testing

4. CI/CD

For this we need Isaac Sim to communicate with bunch of other robotics software in the same PC/network. ROS is the perfect middleware for this. So we need Isaac Sim to talk to ROS. Isaac Sim does this by becoming a ROS node itself.
