#!/usr/bin/env python
from sense_hat import SenseHat
import numpy as np
r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [255,255,255]
br = [165,42,42]
class Anzeige(object):
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.hintergrund()


    def regenbogen(self):
        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,r,r,e,e,e,
            e,r,r,o,o,r,r,e,
            r,o,o,y,y,o,o,r,
            o,y,y,g,g,y,y,o,
            y,g,g,b,b,g,g,y,
            b,b,b,i,i,b,b,b,
            b,i,i,v,v,i,i,b
        ]
        self.sense.set_pixels(image)



    def hintergrund(self):
        image =  [
            b,y,y,y,b,w,b,b,
            b,b,y,b,b,b,b,b,
            e,e,e,e,e,e,e,g,
            e,e,e,e,e,e,e,g,
            e,e,e,e,e,e,e,w,
            r,e,e,e,e,e,w,w,
            r,e,e,e,w,w,w,w,
            w,w,w,w,w,w,w,w
        ]
        self.sense.set_pixels(image)


    def baehnli(self,progress):
        start = np.array([1.,6.])
        end = np.array([7.,3.])
        interp = start + progress*(end - start)
        x = int(round(interp[0]))
        y = int(round(interp[1]))
        self.hintergrund()
        self.sense.set_pixel(x,y, o)
        self.sense.set_pixel(x-1,y, o)
        self.sense.set_pixel(x,y-1, o)
        self.sense.set_pixel(x-1,y-1, o)

        

if __name__ == "__main__":
    a = Anzeige()
    a.hintergrund()
    a.baehnli(0.5)
