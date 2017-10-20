#
# device.py
#
# Defines a basic class for representing a device in a power management sim
#
#==========================================================================


class device:
    
    # Constructor for a device: name, power used when on, power used when off
    def __init__(self, device_name, pwr_on, pwr_off):
        self.name = device_name
        self.on = False
        self.p_on = pwr_on # The constant power drawn by the device while it is on
        self.p_off = pwr_off # The "ghost" power drawn by the device while it is off

    # Returns the name of the device object as a string
    def getName():
        return self.name

    # Returns a boolean indicating whether or not the device is turned on
    def is_on():
        return self.on

    # Turns on the device
    def turn_on(self):
        self.on = True

    # Turns off the device
    def turn_off(self):
        self.on = False

    # Returns the instantaneous power drawn by the device
    def pwr(self, time_point):
        if self.is_on():
            return self.p_on
        else:
            return self.p_off
 
#==============================================================================
# Class cyclicDevice:
# 
# Useful for representing a device that has an inherently cyclic pattern to its
# operation. Many household devices are like this. A prime example is a 
# refrigerator. It uses a lot of power while its compressor is on and actively
# cooling the inside, and very little power while it is idle.   
    
class cyclicDevice(device):
    
    #Constructor for a cyclicDevice: name, power when on and idle, power when off
    # power when in high-draw on state, period in simulation timesteps, 
    # and duty cycle between 0 and 1.
    def __init__(self, device_name, pwr_on, pwr_off, pwr_high, period, duty_cycle):
        device.__init__(device_name, pwr_on, pwr_off)
        self.p_high = pwr_high # The power the device uses when in its high-power state
        self.period = period # The period of the cyclic action of the device
        self.dc = duty_cycle # The duty cycle of the cyclic action of the device. Value between 0 and 1
    
    # Returns the instantaneous power drawn by the device
    def pwr(self, time_point):
        if self.is_on():
            # Here's where my implementation question applies
        else:
            return self.p_off
        

