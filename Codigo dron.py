# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bebop import Bebop
import time

drone = Bebop()
drone.takeoff()
drone.flyToAltitude(2.0)

time.sleep(3)
drone.takePicture()
time.sleep(3)
drone.land()