from servoControl import auf,zu
from gibPfeilTaste import gibPfeilTaste
import time
states =[False,False,False,False]
def setServos(states):
    for i,state in enumerate(states):
        if state:
            auf(i)
        else:
            zu(i)
        time.sleep(0.25)
setServos(states)
while True:
    pfeil = gibPfeilTaste()
    print (pfeil)
    
    #states[number] = not states[number]
    #setServos(states)
        
