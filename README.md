# home_power_management

home_power_management is an AI-based simulation of a home with smart devices that can be controlled to regulate total power usage

## Setup

Before running the main program, run the setup script:

```
$./setup.py
```

This script will generate a Constants.py and SimUtils.py file based off of device.xml. 

### Device.xml

This xml file allows the user to simplify the process of adding a new type of device to the simulated environment.
Example of adding a device is shown below:


```
    <device name="FRIDGE">
        <enabled>True</enabled>
        <p_on>800</p_on>
        <p_off>80</p_off>
        <start_on>True</start_on>
        <cyclic>False</cyclic>
        <desc>Temp placeholder for Fridge</desc>
    </device>
```

For the current implementation we use the following fields:

* name - The name of the device
* p_on - The amount of power consumed by the device when on
    * p_off - The amount of power consumbed by the device when off
    * (phantom power)
* start_on - The initial state of the device (True/False)
    * cyclic - If the device is cyclic (True/False)    *Note*:
    * Currently don't support this

### Constants.py

The Constants.py file contains a list of constants (surprise) that could be useful when testing our simulated
environment. In the setup script, you can specify fields from device.xml you want generated as constants. In the below
example, constants will be generated for the devices p_on, p_off, and start_on value.

```python
TAG_LIST = ['p_on', 'p_off', 'start_on'] # setup.y
```

```python
# Constants.py
...

FRIDGE_INDEX =               3
FRIDGE_P_ON =              800
FRIDGE_P_OFF =              80
FRIDGE_START_ON =         True
```

*Note*: The simulation class has a dev_list member with a list of devices. By generating a constant for the device
index, the user can simply use the constant to specify what device to use in test cases. 

```python
sim.dev_list[FRIDGE_INDEX]
```

### SimUtil.py

Currently, SimUtil is an auto-generated file used to include helper methods for the simulation. Currently, it only contains a function for populating the device list for the simulation class based on the device.xml file:

 ```python
 # SimUtil.py
 def initialize_sim(sim):
     sim.add_device("LIGHT_0", 500, 25, False)
     sim.add_device("LIGHT_1", 200, 25, False)
     sim.add_device("LIGHT_2", 300, 25, False)
     sim.add_device("FRIDGE", 800, 80, True)
     sim.add_device("DRYER", 1000, 10, False)
     sim.add_device("WASHER", 400, 10, False)
     sim.add_device("TV", 200, 50, False)

```

