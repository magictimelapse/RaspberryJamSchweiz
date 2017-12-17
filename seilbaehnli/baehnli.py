#!/usr/bin/env python
import serialStepperControl
import time
from anzeige import Anzeige
class Baehnli(object):
    def __init__(self):
        self.ssc = serialStepperControl.SerialStepperControl()
        self.ssc.torque(200)
        self.anzeige = Anzeige()
        self.anzeige.baehnli(0.)
    def move(self,hoch=True):
        speeds = [40,60,80,100,100,100]
        steps =  [200,200,200,200,200,200]
        
        for ii,(speed,step) in enumerate(zip(speeds,steps)):
            print (speed,step)
            progress = (1.0+ii)/len(speeds)
            if not hoch:
                progress = 1.-progress
            print(progress)
            self.anzeige.baehnli(progress)
            self.ssc.setSpeed(speed)
            if not hoch:
                step = -step
            self.ssc.step(step)


    def button(self):
        return self.ssc.button()
            
    def hoch(self):
        self.move(hoch=True)
    

    def runter(self):
        self.move(hoch=False)

    def stop(self):
        self.ssc.stop()

if __name__ == "__main__":
    b = Baehnli()
    while True:
        if b.button():
            b.hoch()
            time.sleep(5)
            b.runter()
            time.sleep(5)
        else:
            time.sleep(1)
            b.stop()
    
