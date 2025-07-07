# Standalone Python

Using the standalone python workflow is key to automating tasks and making detailed simulations. It provides the most amount of control over this simulation. To use standalone python effectively, one should be familiar with the workings of the contents of the Isaac Sim 

The Docker image provided in the 4.5.0 installation guide with the tag 4.5.0 also ships with `standalone_examples` folder. The documentation of this folder cannot be found in [4.5.0 documentation](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/py/index.html). It contains APIs and other example standalone python scripts to run Isaac Sim and its various functionalities. Luckily, its documentaiton can be found in the, currently under progress, [5.0(latest) documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/py/index.html). 

Or so I thought. That is just a list of python scripts. But it is still worthwile to go through to understand the examples we have at hand.

The `standalone_examples` folder contains several python scripts for interacting with Isaac Sim. These scripts import the extension libraries (`exts` etc) and call their methods and functions.

Unfortunately, most of the scripts in here have only been tested for native installation of Isaac Sim. So we will have to modify them to suit our needs.

```{toctree}
:maxdepth: 1

standalone_examples
```