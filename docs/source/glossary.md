# Glossary

:::{table}
:widths: grid


| Name | Description |
|--|--|
|**[Omniverse](https://www.nvidia.com/en-in/omniverse/)**| NVIDIA’s Industrial AI platform. Sort of like playstore for its applications. There is also an Omniverse SDK for you to make your own Omniverse applications. Some of these include digital twin, robot learning, synthetic data generation etc. This space is largely occupied by robotics and related fields.|
|**[Isaac](https://developer.nvidia.com/isaac/)**| Earlier being the name of a robotics application, this is being developed as a full fledged platform for robotics.|
|**[Isaac Sim](https://developer.nvidia.com/isaac/sim)**| A simulator like Gazebo. The speciality of Isaac Sim is that it provides highly photorealistic simulations, good for camera oriented development.|
|**[Isaac Ros](https://developer.nvidia.com/isaac/ros)**| A package to connect Isaac sim to Ros|
|**[Isaac Lab](https://developer.nvidia.com/isaac/lab)**| A package to use Isaac sim for robot learning. Here you can leverage other omniverse tools in integration.|
|**[OpenAI Gym](https://www.gymlibrary.dev/)**| OpenAI python library for RL. Due to its focus on RL development, the framework allowed excellent environment descriptions, as required by RL, and this feature is heavily used across platform, including AnyMal. However, It does not have a physics engine. This  package has been deprecated. Earlier Gym environments were used to run simulations in Isaac Sim.|
|**[Gymnasium](https://gymnasium.farama.org/index.html)**| Newly maintained version of OpenAI Gym by a non-profit|
|**[Pybullet](https://pybullet.org)**| Python library for physics simulation. Now you can combine Gym and Pybullet to make excellent environments with good physics simulations and use Gym or any other application to run your RL policy.|
|**[Tensorflow](https://tensorflow.org)**| Open source python library maintained by Google which leads in RL applications. However, it hosts a platter of ML tools.|
|CUDA| NVIDIA's software library/package to allow usage of GPU for tasks other than gaming. It optimizes how running scripts are implements to accelrate performance. |

:::