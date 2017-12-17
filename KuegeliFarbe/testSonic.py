from psonic import *
from time import sleep
from MLAnwenden import gibFarbe
from servoControl import auf,zu
sleepTime = 0.3

try:
    while True:
        farbe = gibFarbe()
        print (farbe)
        if farbe == "rot":
            play (A4,attack=1, sustain=6*sleepTime)
            play (A4,attack=1, sustain=6*sleepTime)
        elif farbe == "gruen":
            play(B4,attack=1, sustain=6*sleepTime)
        elif farbe == "orange":
            play (C5,attack=1, sustain=6*sleepTime)
        elif farbe == "gelb":
            play(E5,attack=1, sustain=6*sleepTime)
        elif farbe == "blau":
            play(D4,attack=1, sustain=6*sleepTime)

 
      
        time.sleep(sleepTime)
        auf(0)
        time.sleep(sleepTime*2)
        zu(0)
        time.sleep(sleepTime)
        auf(2)
        time.sleep(sleepTime)
        zu(2)       
        time.sleep(sleepTime)
        auf(3)
        time.sleep(sleepTime)
        zu(3)
        time.sleep(sleepTime)
        
except KeyboardInterrupt as e:
    for ii in range(4):
        zu(ii)
