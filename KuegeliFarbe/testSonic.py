from psonic import *
from time import sleep
import threading

from sense_hat import SenseHat
sense = SenseHat()
def spielMelodie():
    while True:
        for ii in range(2):
            play(C4)
            sleep(1)
            play(D4)
            sleep(1)
            play(E4)
            sleep(1)
            play(C4)
            sleep(1)
        for ii in range(2):
            play(E4)
            sleep(1)
            play(F4)
            sleep(1)
            play(G4)
            sleep(2)
        for ii in range(2):
            play(G4)
            sleep(0.5)
            play(A4)
            sleep(0.5)
            play(G4)
            sleep(0.5)
            play(F4)
            sleep(0.5)
            play(E4)
            sleep(1)
            play(C4)
            sleep(1)
        for ii in range(2):
            play(C4)
            sleep(1)
            play(G3)
            sleep(1)
            play(C4)
            sleep(2)
            
stimme1 = threading.Thread(target=spielMelodie)    
stimme2 = threading.Thread(target=spielMelodie)
stimme3 = threading.Thread(target=spielMelodie)
stimme4 = threading.Thread(target=spielMelodie)

stimme1.start()
sleep(8)
stimme2.start()
sleep(8)
stimme3.start()
sleep(8)
stimme4.start()



stimme1.join()
#stimme2.join()
"""    
try:
    while True:
        
        
        sense.clear((255,0,0))
        
        play (A4)
        sleep(1)
        sense.clear((0,255,0))
        play (A4)
        sleep(1)
        play(B4)
        sleep(1)
        play (C5)
        sleep(1)
        play(E5)
       
        play(D4)
        sleep(0.1)
        play(A4)
        sleep(2)
        play(G4)
        sleep(1)
        play(E4)
        sleep(1)
        play(F5)
        play(A5)
        
        sleep(1)
        play(G4)
        sleep(1)
        play(A5)      
        play(B4)
        sleep(1)
        play(C5)
        sleep(1)
        play(D5)
        sleep(1)
        play(C5)
        sleep(1)
        play(A4)
        play(C5)
        sleep(1)
        play(A4)

        sleep(1)
        play(C5)
        sleep(1)
        play(G4)
        sleep(1)
        play(E4)
        sleep(2)
        play(A4)
        play(C5)
        play(E5)
        spielMelodie()   
        
        
        

                 
        
             
 
        
except KeyboardInterrupt as e:
    pass
"""
