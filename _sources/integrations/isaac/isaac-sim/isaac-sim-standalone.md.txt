# Isaac Sim 
...understaing it solo first



```{toctree}
:maxdepth: 2

isaac-sim-standalone/docker-installation
isaac-sim-standalone/understanding-filesystem
isaac-sim-standalone/basics
isaac-sim-standalone/standalone-python-workflow


```

## How ROS fits in

Since Isaac Sim is just a simulator, it has to be used for "something". NVIDIA calls this something as digital twin, fancy word for robot inside screen. But what can we do with having a digital twin.

Applications:
1. Synthetic Data Generation

    Usually simualators just take information, run some physics and spit some information back. But when using Isaac Sim for some larger ML application, sometimes the data might not be enough. 

    Example:

       Problem - Cannot get data of all possible lighting conditions for      street mapping
       Solution - Simulate in simulator to control lighting conditions.
       New Problem - Too many environments to configure
       Solution - NVIDIA uses Replicator to randomize lighting, generating data for Isaac Sim

    Replicator can randomize any variable for synthetic data generation
    
2. Software in Loop:   Run your robotics stack on PC for testing

3. Hardware in Loop: Run your robotics stack on hardware (eg.Jetson) for testing

4. CI/CD

For this we need Isaac Sim to communicate with bunch of other robotics software in the same PC/network. ROS is the perfect middleware for this. So we need Isaac Sim to talk to ROS. Isaac Sim does this by becoming a ROS node itself.