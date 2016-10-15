#!/usr/bin/env python
import pi2go
import time
pi2go.init()
speed = 50
while True:
    linkerSensor = pi2go.irLeft()
    rechterSensor = pi2go.irRight()
    distanz = pi2go.getDistance()
    # wenn die Distanz zur naechsten Wand zu kurz ist, musst der 
    # pi2go ausweichen:
    if distanz < 50:
       print "nahe an Wand!"
       # fahre z.B. ein paar Schritte rueckwaerts
    # mach etwas, wenn der linke Sensor eine Wand meldet:
    elif linkerSensor: 
        print "zu nahe an linker Wand!"
        # und reagier darauf!
    elif rechterSensor: 
        print "zu nahe an rechter Wand!"
        # und reagier darauf!
    else:
        print "Bahn frei!"
        # was soll jetzt der pi2go machen?
    time.sleep(0.1)

