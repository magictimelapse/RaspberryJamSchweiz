from time import sleep
from MLAnwenden import gibFarbe
from servoControl import auf,zu
from psonic import *

### Musik spielen mit:
# play(C5)
### Spielt ein C in 5. Lage

## Servo Motoren
# auf(0)
## oeffnet servo 0
# zu(3)
## schliesst servo 3

## farbe erkennen
# gibFarbe()
## gibt die Farbe des Kuegelchens am Sensor 

while True:
    print("Start")
    auf(0)
    sleep(1)
    zu(0)
    sleep(1)
    farbe == gibFarbe()
    if farbe == "rot":
        print ("das war rot!")

    ## mache dasselbe fuer gruen, orange und gelb!




    ## Wenn eine rote Kugel kommt, dann spiel ein C5!


    ## Programmiere:
    ## Schliesse Servo 2 und 3
    ## schlafe 0.5 Sekunden
    ## Oeffne Servo 2
    ## Schlafe 0.5 Sekunden
    ## Schliesse Servo 2
    ## Schlafe 0.5 Sekunden
    ## Oeffne Servo 3
    ## Schlafe 0.5 Sekunden
    ## Schliesse Servo 3
    ## Schlafe 0.5 Sekunden
