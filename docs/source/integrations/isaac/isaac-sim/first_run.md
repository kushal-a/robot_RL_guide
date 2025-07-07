# Basics

Once in the bash of the docker container, we can start interacting with Isaac Sim. 

To start Isaac Sim, run,
```console
./runheadless.sh -v
```
Remember to use the streaming client to view the GUI.

Important concepts are covered [here](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/quickstart_index.html).

Isaac Sim has 3 [workflows](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/introduction/workflows.html). The first two workflows function the same as in native installation and docker installation. For the last workflow, we will have to make modifications.

The current set of of getting_started scripts and tutorials are designed for native installation. To run in streaming mode, the following modifications will have to be made.

