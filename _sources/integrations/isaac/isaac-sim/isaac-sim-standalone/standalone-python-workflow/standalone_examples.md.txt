#  `standalone_examples` shippped with Isaac-Sim

[Source Code, I guess](https://github.com/isaac-sim/IsaacSim/tree/main/source/standalone_examples)

Each of the sub heading are folders in `standalone_examples`. All these files have to modified to run in docker as mentioned in the previous section.

## Tutorials

The two scripts `getting_started.py` and `getting_started_robot.py` starts Isaac Sim with scene and with a robot respectively.

Run as
```bash
./python.sh standalone_examples/tutorials/getting_started.py
```

## Testing
Directory for testing scripts. Kindly ignore.

## Data
Aasset Data (eg CAD files) references in other examples

## Benchmark
Used for benchmarking Isaac Sim. Not covered Here


## Notebooks
Contains files `hello_world.ipynb` and `scene_generation.ipynb`. Basically, standalone python scripts that can be run from jupyter. This will allow more dynamic control over the simulation than running standalone python scripts. At the same type, it more firendly compared to scripting. 

If you are starting for the first time, run
```bash
./jupyter_notebook.sh
```
If using docker, add `--allow-root`

From the next time, `jupyter` is available as CLI like full installation. If using docker, add `--allow-root` when starting jupyter server.

On running the server, a link will be provided to view jupyter client. This works in both standalone installation and docker.

If you are using docker, follow steps mentioned in the previous section in jupyter notebooks as well.


## API
Contains files whose content can be used to make our own simulation.


## Replicator
Contains files whose content can be used to run Omniverse Replicator.

```{toctree}
:maxdepth: 1

standalone_examples/api
standalone_examples/replicator
```