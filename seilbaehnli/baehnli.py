#!/usr/bin/env python
import serialStepperControl
import time
from datetime import datetime
from anzeige import Anzeige
msleep = lambda x: time.sleep(x / 1000.0)

class Baehnli(object):
    def __init__(self):
        self.ssc = serialStepperControl.SerialStepperControl()
        self.ssc.torque(280)
        self.anzeige = Anzeige()
        self.anzeige.baehnli(0.)
    def __del__(self):
        self.ssc.stop()
    def move(self,hoch=True):
        speeds = [15,15,15,15,15,15]
        ds = 140
        steps =  [ds,ds,ds,ds,ds,ds]
        
        for ii,(speed,step) in enumerate(zip(speeds,steps)):
            print (speed,step)
            progress = (1.0+ii)/len(speeds)
            if not hoch:
                progress = 1.-progress
            print(progress)
            self.anzeige.baehnli(progress)
            self.ssc.setSpeed(speed)
            if hoch:
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
    #time.sleep(4*60*60+30*60)
    start = datetime.now()
    time.sleep(5)
    stop = datetime.now()
    diff = (stop - start).total_seconds()
    while diff < 6*60*60:
        stop = datetime.now()
        diff = (stop - start).total_seconds()
        if b.button():
            b.hoch()
            time.sleep(5)
            b.runter()
            time.sleep(5)
        else:
            b.stop()
            msleep(1)
            b.anzeige.off()
            
    
