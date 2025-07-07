# robot_RL_guide
The package explore various tools available for Reinforcement learning for robotics applications

# Context
Nvidia is the creator of GPU, specialized physical devices meant for gaming. Turns out it is good at bunch of other stuff. One among several new applications is Industrial AI of which Robotics is a part (according to Nvidia). Over years, Nvidia has developed specialized tools and created platforms for these applications. OpenAI, Google are other big players.

# Glossary

|**Omniverse**| Nvidia’s Industrial AI platform. Sort of like playstore for its applications. There is also an Omniverse SDK for you to make your own Omniverse applications. Some of these include digital twin, robot learning, synthetic data generation etc. This space is largely occupied by robotics and related fields.|
|**Isaac**| Earlier being the name of a robotics application, this is being developed as a full fledged platform for robotics.|
|**Isaac Sim**| A simulator like Gazebo. The speciality of Isaac Sim is that it provides highly photorealistic simulations, good for camera oriented development.|
|**Isaac Sim Ros**| A package to connect Isaac sim to Ros|
|**Isaac Lab**| A package to use Isaac sim for robot learning. Here you can leverage other omniverse tools in integration.|
|**OpenAI Gym**| OpenAI python library for RL. Due to its focus on RL development, the framework allowed excellent environment descriptions, as required by RL, and this feature is heavily used across platform, including AnyMal. However, It does not have a physics engine. This  package has been deprecated. Earlier Gym environments were used to run simulations in Isaac Sim.|
|**Gymnasium**| Newly maintained version of OpenAI Gym by a non-profit|
|**Pybullet**| Python library for physics simulation. Now you can combine Gym and Pybullet to make excellent environments with good physics simulations and use Gym or any other application to run your RL policy.|
|**Tensorflow**| Open source python library maintained by Google which leads in RL applications. However, it hosts a platter of ML tools.|

# News and Updates
1. Isaac Sim had been close sourced for a long time. In June 2025, Nvidia made Isaac Sim 5.0 opensource.
2. Pybullet has not been well maintained in since 2023 (to 2025). It has since got one update in 2025. Although Pybullet does not have other dependencies, examples problems, tutorials and documentation still refers old and deprecated libraries. Pybullet RL examples still use the old Gym library. Hence, using pybullet for RL is problematic as of now (2025)
3. Although Isaac SIm 5.0 is open-source, it is still very new with several bugs. Isaac Lab 2.2 is compatible with Isaac Sim 4.5 and is the recommended compatibility.
4. There are updates coming in all these libraries very actively.

# Integrations

Docker images are made for software that was developed in close proximity with each other.

Clearly there are 2 workflows: Isaac tools (and ROS) and Pybullet with TF & Gym.
Isaac tools (and ROS)
This section will not cover ROS core and only integrations with Isaac tools. First we familiarize ourselves with the simulator, Isaac Sim. Then we will integrate with ROS using the Isaac Sim ROS. Then we will use Isaac Lab for our RL training.

There are 2 compatibilites to check: Sim <-> Lab and ROS <-> Sim.
For the first one, the current recommended implementation is Sim 4.5 and Lab 2.2
ROS <-> Sim can work on 
## Isaac Sim
Isaac Sim has been installed as a docker image. To run a container, use the following command.
```bash
docker run --name isaac-sim --entrypoint bash -it --runtime=nvidia --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
    -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
    -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
    -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
    -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/documents:/root/Documents:rw \
    nvcr.io/nvidia/isaac-sim:4.5.0
```



