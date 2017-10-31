#!/usr/bin/python
#
# Author: Bryan Nguon
#
# Purpose:
# 
# Revision History:
#   + 10/21/17 (bsnguon): Initial file creation 
#
#
#

import Constants
from Simulation import Simulation
from device import Device
from device import CyclicDevice
from SimUtil import initialize_sim

def main():

    # Init simulation
    sim = Simulation()
    initialize_sim(sim)
    
    # Variable names to simplify device access
    devices = sim.dev_list
    LivingRoomLamp = devices[Constants.LIGHT_0_INDEX]
    DeskLamp       = devices[Constants.LIGHT_2_INDEX]
    Fridge         = devices[Constants.FRIDGE_INDEX]
    Dryer          = devices[Constants.DRYER_INDEX]
    Washer         = devices[Constants.WASHER_INDEX]
    TV             = devices[Constants.TV_INDEX]

    print "Living room lamp on for 60 seconds"
    LivingRoomLamp.turn_on()
    sim.wait(10)
    LivingRoomLamp.turn_off()
    sim.wait(5)

if __name__ == "__main__":
    main()
