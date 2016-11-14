#!/usr/bin/env python

import pi2go
import time
pi2go.init()
speed = 50
print "vorwaerts!"
pi2go.forward(speed)
print "fuer 2 Sekunden..."
time.sleep(2)
print "drehe links!"
pi2go.spinLeft(speed)
print "fuer 3 Sekunden..."
time.sleep(3)
print "stop"
pi2go.stop()
linkerLinienSensor = pi2go.irLeftLine()
rechterLinienSensor = pi2go.irRightLine()
print "Linker Linien-Sensor: ", linkerLinienSensor
print "Rechter Linien-Sensor: ", rechterLinienSensor
pi2go.cleanup()
