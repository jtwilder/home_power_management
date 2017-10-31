#!/usr/bin/python

import xml.etree.ElementTree as ET

MAX_LENGTH = 30
TAG_LIST = ['p_on', 'p_off', 'start_on']

#==============================================================================
# generate_constants_file(name):
#   name - name of file to write constants to
#
def generate_constants_file(name):
    const_file = open(name, 'w')

    const_file.write("#!/usr/bin/python\n")
    const_file.write("#\n")
    const_file.write("# WARNING: DO NOT EDIT! THIS FILE IS AUTOGENERATED!!! (setup.py)\n")
    const_file.write("#\n")
    const_file.write("# THIS FILE CONTAINS CONSTANTS USED TO ACCESS DEVICES FROM SIMULATION\n")
    const_file.write("#\n\n")

    generate_constants(const_file)

    const_file.close

    print "Constants generated in Constants.py."

#==============================================================================
# generate_constants(logfile):
#   logfile - file handler to write constants to
#

def generate_constants(logfile):
    tree = ET.parse('device.xml')
    root = tree.getroot()

    index = 0
    for dev in root:
        if dev.tag == "device":
            # Check if device is enabled
            if dev[0].text != "True":
                continue

            temp_string = dev.get('name') + "_INDEX =" 
            line_length = len(temp_string) + len(str(index))
            num_spaces  = MAX_LENGTH - line_length

            temp_string += ' ' * num_spaces
            temp_string += str(index)

            #print temp_string
            logfile.write(temp_string + '\n')
            
            index += 1

            for child in dev:
                if child.tag in TAG_LIST:
                    attr_string= child.text
                    temp_string = dev.get('name') + "_" + child.tag.upper() + " ="
                    line_length = len(temp_string) + len(attr_string)
                    num_spaces = MAX_LENGTH - line_length
                    
                    temp_string += ' ' * num_spaces
                    temp_string += attr_string

                    #print temp_string
                    logfile.write(temp_string + '\n')
        #print '\n'
        logfile.write('\n')

#==============================================================================
# add_devices(outfile):
#    outfile - file object to write to
#    
#    This function populates the add_device calls to the sim enviornment
#
def add_devices(outfile):
    tree = ET.parse('device.xml')
    root = tree.getroot()

    for dev in root:
        if dev.tag == "device":
            dev_name = dev.get('name')
            dev_p_on = dev_p_off = dev_start_on = ""
            print (dev_name, dev[0].tag, dev[0].text)
            if dev[0].text != "True":
                continue
            for child in dev:
                if child.tag == 'p_on':
                    dev_p_on = child.text
                elif child.tag == 'p_off':
                    dev_p_off = child.text
                elif child.tag == "start_on":
                    dev_start_on = (child.text == "True")
            
            dev_args = "\"" + dev_name + "\", "  + dev_p_on + ", " + dev_p_off + ", " + str(dev_start_on)
            dev_init_string = "\tsim.add_device(" + dev_args + ")\n"

            outfile.write(dev_init_string)

#==============================================================================
# generate_sim_util():
#   Generates SimUtil.py. This file contains autogenerated setup for adding 
#   devices to simulation class
#
def generate_sim_util():
    util_file = open("SimUtil.py", 'w')
    util_file.write("#!/usr/bin/python\n")
    util_file.write("import Simulation\n")
    util_file.write("\n")
    util_file.write("def initialize_sim(sim):\n")
    add_devices(util_file)
    
    util_file.close()

def main():
    generate_constants_file("Constants.py")
    generate_sim_util()
 
if __name__ == "__main__":
    main()