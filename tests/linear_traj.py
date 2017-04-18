import random, math
import json
import pypot.robot
import time
import sys
import pypot.dynamixel
from contextlib import closing
import logging
import logging.config
import matplotlib.pyplot as plt

def feedforward(dxl_io):
    print "Setting dt"
    # Please...
    dxl_io.set_dt({1:10000})
    dxl_io.set_dt({1:10000})
    dxl_io.set_dt({1:10000})
    dxl_io.set_dt({1:10000})
    print "Setting states"
    dxl_io.set_future_states({1:[20, 0, 0, 30, 0, 0, 40, 0, 0]})
    raw_input("Start cu")
    dxl_io.set_timestamp({1:0})
    time.sleep(0.1)
    print "Setting mode"
    dxl_io.set_mode_dynaban({1:3})
    print "Setting debug on"
    dxl_io.set_debug_mode_on({1:1})
    t0 = time.time()
    D0 = t0
    t = t0 + 1000
    while (time.time() - D0) < 3.3 :
        t = time.time() - t0
        if (t > 0.1) :
            #Fake call to get debug
            dxl_io.set_debug_mode_on({1:1})
            t0 = time.time()
        

if __name__ == '__main__' :
        ports = pypot.dynamixel.get_available_ports()
        if not ports:
            raise IOError('No port found!')
        print("Ports found", ports)
        print("Connecting on the first available port:", ports[0])
        dxl_io = pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)
        dxl_io.enable_torque([1])
        #dxl_io.set_goal_position({1:10})
        feedforward(dxl_io)