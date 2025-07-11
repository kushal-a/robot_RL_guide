# Standalone examples for Docker

To run standalone python `.py` scripts available from NVIDIA in a container installation of Isaac Sim whilst using streaming client, the following change has to be made.

Replace 
```python
simulation_app = SimulationApp({"headless": False})
```

with

```python
# This sample enables a livestream server to connect to when running headless
CONFIG = {
    "width": 1280,
    "height": 720,
    "window_width": 1920,
    "window_height": 1080,
    "headless": True,
    "hide_ui": False,  # Show the GUI
    "renderer": "RaytracedLighting",
    "display_options": 3286,  # Set display options to show default grid
}


# Start the omniverse application
simulation_app = SimulationApp(launch_config=CONFIG)

from isaacsim.core.utils.extensions import enable_extension

# Default Livestream settings
simulation_app.set_setting("/app/window/drawMouse", True)

# Enable Livestream extension
enable_extension("omni.kit.livestream.webrtc")
```

Whereever there is 
```python
my_world.step(render=True)
```

add below it
```python
simulation_app.update()
```

For details, refer to `standalone_examples/api/isaac-sim.simulation_app/livestream.py`


:::{tip}
To check is streaming app is still working, use
```python
while simulation_app._app.is_running() and not simulation_app.is_exiting():
```
:::