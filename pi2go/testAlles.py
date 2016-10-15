#!/usr/bin/env python

import pi2go
import time
pi2go.init()
speed = 50

pi2go.stepForward(speed,15)
time.sleep(1)
pi2go.stepSpinL(speed, 12)
time.sleep(1)
linkerSensor = pi2go.irLeft()
rechterSensor = pi2go.irRight()
distanz = pi2go.getDistance()
knopf = pi2go.getSwitch()
pi2go.cleanup()
print "Linker Sensor: ", linkerSensor
print "Rechter Sensor: ", rechterSensor
print "Distanz: ", distanz
print "Knopf: ", knopf
