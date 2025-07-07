# Installation and Management of Isaac Sim Container in Docker

Isaac Sim has been installed as a [docker image](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/install_container.html). 

The image I used is:

    Repository: nvcr.io/nvidia/isaac-sim
    Tag: 4.5.0

To run a container, use the following command.
```console
$ sudo docker run --name isaac-sim --entrypoint bash -it --runtime=NVIDIA --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
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
```console
$ sudo docker exec -ti <container-name> bash
```

To save the container in its existing state,
```console
$ sudo docker commit -m <message> <container-name> nvcr.io/nvidia/isaac-sim:<new/old-tag>
```

The drawback of of docker container installation is unavailability of direct GUI support. However, Isaac Sim has built in feature where the GUI is published/streamed. Docker installation of Isaac Sim has been designed for running on servers. Hence, one can connect remotely via NVIDIA's Omniverse Streaming Client to view the GUI. Here we will be running the server (docker container) and the streaming client on the same PC. The installation of the streaming client is included in the container installation steps of Isaac Sim.
