import smbus
import RPi.GPIO as GPIO
import smbus
from time import sleep
import numpy as np
import math
import Adafruit_TCS34725
class KuegeliFarbe(object):
    port = 1
   
    def __init__(self):
        self._tcs = Adafruit_TCS34725.TCS34725()
        self._tcs.set_interrupt(False)
        
    def __del__(self):
        self._tcs.set_interrupt(True)
        self._tcs.disable()
        #tcs = Adafruit_TCS34725.TCS34725(integration_time=Adafruit_TCS34725.TCS34725_INTEGRATIONTIME_700MS,
#                                 gain=Adafruit_TCS34725.TCS34725_GAIN_60X)
# Possible integration time values:
#  - TCS34725_INTEGRATIONTIME_2_4MS  (2.4ms, default)
#  - TCS34725_INTEGRATIONTIME_24MS
#  - TCS34725_INTEGRATIONTIME_50MS
#  - TCS34725_INTEGRATIONTIME_101MS
#  - TCS34725_INTEGRATIONTIME_154MS
#  - TCS34725_INTEGRATIONTIME_700MS
# Possible gain values:
#  - TCS34725_GAIN_1X
#  - TCS34725_GAIN_4X
#  - TCS34725_GAIN_16X
#  - TCS34725_GAIN_60X



    def distance(self,P,b):
    # see https://de.serlo.org/mathe/geometrie/analytische-geometrie/abstaende-winkel/abstaende/abstand-punktes-einer-geraden-berechnen-analytische-geometrie
        return np.linalg.norm(np.cross(P, b))/np.linalg.norm(b)


    def rgba(self):
       r,g,b,a = self._tcs.get_raw_data()
       return (r,g,b,a)
    
    def rgb(self):
        r,g,b,a = self.rgba()
        return (r,g,b)

    
    def farbe(self):
        r,g,b,a = self.rgba()
        color = (r,g,b)
                
                #print (ambient, math.sqrt(r*r + g*g + b*b))
        minDistance = 1000
        fitColor = "black"
        print (color)
        for ref in self.colorReferences:
            ### Find the closest distance betweeen our color
            dist = self.distance(color, ref["vector"])
            #print (dist,ref["color"])
            if dist < minDistance:
                minDistance = dist
                fitColor = ref["color"]
                        
        return fitColor

        
        
        
           
