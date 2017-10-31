from device import Device

# Simulation
class Simulation:

    def __init__(self):
        self.time = 0;
        self.inst_power = 0;
        self.dev_list = []

    # Add device to device list
    def add_device(self, name, p_on, p_off, start_on):
        self.dev_list.append(Device(name, p_on, p_off, start_on))
            
    # Step function for simulation. Include any methods that should run
    # every time step here.
    def step(self):
        self.time += 1;
        self.report_power() 

    # Used in test cases to step through time_step
    def wait(self,time_step):
        for i in range(0,time_step):
            self.step()

    # report instantaneous power. Currently just prints...
    def report_power(self):
        #log_file = open("power_tracker.log", 'w');
        
        temp = 0
        for dev in self.dev_list:
            temp += dev.pwr()
        
        self.inst_power = temp

        print self.inst_power

