import Adafruit_PCA9685
import time
pwm = Adafruit_PCA9685.PCA9685(address=0x40)
oben=[440]
unten = [390]
def initialisiere(servos):
    for servo in servos:
        pwm.set_pwm(servo,0,oben[servo])

def spiel_ton(servo=0):
    pwm.set_pwm(servo,0,unten[servo])
    time.sleep(0.1)
    pwm.set_pwm(servo,0,oben[servo])
    time.sleep(0.1)

if __name__ == "__main__":
    initialisiere([0])
    time.sleep(0.5)
    
    spiel_ton(0)
    spiel_ton(1)
