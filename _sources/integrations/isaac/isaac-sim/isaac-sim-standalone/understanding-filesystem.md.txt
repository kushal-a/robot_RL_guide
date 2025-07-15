# Understanding Filesystem

Note

This page can be skipped if you are using inly GUI.

In the `/` folder, apart from standard ubuntu folder, there is the `isaac-sim` folder. Docker opens uses this folder as the initial working directory.

In the `isaac-sim` folder you have files to run Isaac Sim. There are mainly two kinds of files, `.sh` and Python libraries/packages. 

## .sh

The first three files are used to start Isaac Sim from terminal. Choose the one according to your use case.
1. `runapp.sh`
2. `runheadless.sh` - use to start Isaac Sim
3. `runoldstreaming.sh`

   To run any of there files, use,
   ```bash
   ./<file-name>
    ```
    ### Starting Isaac Sim from terminal
    Since we are running Docker, run
    ```bash
   ./runheadless.sh
    ```

    These files set some environment variables and arguments and calls the following files

1. `isaac-sim.sh`
2. `isaac-sim.streaming.sh`
3. `isaac-sim.old_streaming.sh`
    
    respectively.

    There are also
4. `isaac-sim.xr.vr.sh`
5. `isaac-sim.selector.sh`

    The selector is used in the normal GUI mode. Since we are running with docker, we will only be using the headless/streaming files.

    The `isaac-sim.<>.sh` files are not meant to be run directly.

6. `python.sh`

    To run a python script, we will use `python.sh`. Use the following command
    ```bash
    ./python.sh <py-file-name>

7. `clear_caches.sh`
8. `isaac-sim.docker.gui.sh`
9. `isaac-sim-docker.sh`
10. `isaac-sim.fabric.sh`
11. `license.sh`
12. `post_install.sh`
13. `privacy.sh`
14. `setup_conda_env.sh`
15. `setup_python_env.sh`
16. `warmup.sh`

## Python packages and libraries

The core functionality of Isaac Sim is written as various Isaac Sim extensions. These extensions, found in `exts` folder. Detailed documentation can be found [here](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/py/index.html) for the 4.5.0 version. We will be using these extensions, which are actually python libraries, in our scripts, automating and specifying our interactions with Isaac Sim.

There is also a folder called `standalone_examples`. Details of this will be discussed [later](./standalone-python-workflow/standalone_examples.md).

