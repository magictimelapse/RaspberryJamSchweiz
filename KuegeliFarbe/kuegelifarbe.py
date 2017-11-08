from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep
import closest_colour
import numpy as np
import math
class KuegeliFarbe(object):
    port = 1
    colorReferences = [
                    {"color": "rot", "vector": (190,72,88)},
                    {"color": "gruen", "vector": (70,140,80)},
                    {"color": "blau", "vector": (0,0,255)},
                    {"color": "weiss2", "vector": (255,255,255)},
                    {"color": "orange", "vector": (160,60,60)},
                    {"color": "gelb", "vector": (140,103,66)}
                    ]
    def __init__(self):
        self._bus = smbus.SMBus(self.port)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.IN)
        self._apds = APDS9960(self._bus)
        self._apds.enableLightSensor()
        self._apds.enableProximitySensor()
        self._apds.setAmbientLightGain(APDS9960_AGAIN_64X)
        self._apds.setLEDBoost(APDS9960_LED_BOOST_300)
        
    def distance(self,P,b):
    # see https://de.serlo.org/mathe/geometrie/analytische-geometrie/abstaende-winkel/abstaende/abstand-punktes-einer-geraden-berechnen-analytische-geometrie
        return np.linalg.norm(np.cross(P, b))/np.linalg.norm(b)


    def rgba(self):
        val = self._apds.readProximity()
        color = (-1,-1,-1,-1)
        if val>254:
            ambient = self._apds.readAmbientLight()
            if ambient > 0:
                r = self._apds.readRedLight()
                g = self._apds.readGreenLight()
                b = self._apds.readBlueLight()
                color = (r,g,b,ambient) 
        return color
    
    def rgb(self):
        val = self._apds.readProximity()
        color = (-1,-1,-1)
        if val>254:
            ambient = self._apds.readAmbientLight()
            if ambient > 0:
                r = float(255.*self._apds.readRedLight()/ambient)
                g = float(255.*self._apds.readGreenLight()/ambient)
                b = float(255.*self._apds.readBlueLight()/ambient)
                color = (r,g,b) 
        return color

    
    def farbe(self):
        val = self._apds.readProximity()
        if val>254:
            ambient = self._apds.readAmbientLight()
            if ambient > 0:
                r = float(255.*self._apds.readRedLight()/ambient)
                g = float(255.*self._apds.readGreenLight()/ambient)
                b = float(255.*self._apds.readBlueLight()/ambient)
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

        return "weiss"
                #threshold= 1.5
                #if red/green > threshold and red/blue >threshold:
                #    print ("red !", red/green, red/blue)
        
           
