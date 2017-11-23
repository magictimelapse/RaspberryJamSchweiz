from servoControl import auf,zu
from gibPfeilTaste import gibPfeilTaste
import time
servos = {
    "rechts": {"number": 0, "state":False},
    "links": {"number": 1, "state":False},
    "unten": {"number": 2, "state":False},
    "oben": {"number": 3, "state":False}
    }
    
  
def setServos(servos):
    for servo in servos:
        if servos[servo]["state"]:
            auf(servos[servo]["number"])
        else:
            zu(servos[servo]["number"])
        time.sleep(0.25)
setServos(servos)
while True:
    pfeil = gibPfeilTaste()
    print (pfeil)
    servos[pfeil]["state"] = not servos[pfeil]["state"]
    #states[number] = not states[number]
    setServos(servos)
        
