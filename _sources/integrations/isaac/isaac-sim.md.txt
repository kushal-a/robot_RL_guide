# Isaac Sim

[Documentation](https://isaac-sim.github.io/IsaacLab/main/index.html) | [Website](https://developer.nvidia.com/isaac/sim)

## Choosing installation method, clash of the titans
Native installation of Isaac Sim is stable. Isaac Sim requires CUDA to run the simulation on GPU. Tensorflow, which is a part of the other workflow, also requires CUDA to run its training on NVIDIA's GPUs. Since we want to able to develop in both workflows on the same PCs, compatibility of drivers, CUDA, python and other dependencies is crucial. In addition to this, ROS has its own requirements and installation of python and its libraries. To prevent incompatibility among so many libraries and applications, we will be developing both these workflows and ROS in seperate docker containers. Hence, a containerized installation for Isaac Sim, and subsequently other applications/packages is chosen.

Isaac Sim has been installed as a [docker image](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/install_container.html). 

The image I used is:

    Repository: nvcr.io/nvidia/isaac-sim
    Tag: 4.5.0

To run a container, use the following command.
```bash
sudo docker run --name isaac-sim --entrypoint bash -it --runtime=NVIDIA --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
    -e "PRIVACY_CONSENT=Y" \
    -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
    -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
    -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
    -v ~/docker/isaac-sim/cache/glcache:/root/.cache/NVIDIA/GLCache:rw \
    -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
    -v ~/docker/isaac-sim/logs:/root/.NVIDIA-omniverse/logs:rw \
    -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
    -v ~/docker/isaac-sim/documents:/root/Documents:rw \
    nvcr.io/NVIDIA/isaac-sim:4.5.0
```
To open a new terminal in existing running container of Isaac Sim, use the following command.
```bash
sudo docker exec -ti <container-name> bash
```

To save the container in its existing state,
```bash
sudo docker commit -m <message> <container-name> nvcr.io/nvidia/isaac-sim:<new/old-tag>
```

The drawback of of docker container installation is unavailability of direct GUI support. However, Isaac Sim has built in feature where the GUI is published/streamed. Docker installation of Isaac Sim has been designed for running on servers. Hence, one can connect remotely via NVIDIA's Omniverse Streaming Client to view the GUI. Here we will be running the server (docker container) and the streaming client on the same PC. The installation of the streaming client is included in the container installation steps of Isaac Sim.

## Inside the docker container

Once in the bash of the docker container, we can start interacting with Isaac Sim. 

To start Isaac Sim, run,
```bash
./runheadless.sh -v
```
Remember to use the streaming client to view the GUI.

Important concepts are covered [here](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/quickstart_index.html).

Isaac Sim has 3 [workflows](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/workflows.html). The first two workflows function the same as in native installation and docker installation. For the last workflow, we will have to make modifications.

The current set of of getting_started scripts and tutorials are designed for native installation. To run in streaming mode, the following modifications will ahve to be made.

## Standalone Python for docker installation (enabling streaming)





