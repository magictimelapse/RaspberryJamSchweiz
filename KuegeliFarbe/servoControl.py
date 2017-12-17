import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x41)
servoStart = 0.6
servo = servoStart
servoEnd = 2.5

HOST = 'localhost'
PORT = 42001
ServoPositions= {
    0:{"auf":2.5, "zu":1.4},
    1:{"auf":1.8, "zu":0.75},
      2:{"auf":1.8, "zu":0.6},
         3:{"auf":1.8, "zu":0.75}
                 }
                 

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 # 1,000,000 us per second
    pulse_length /= 60 # 60 Hz
    pulse_length /= 4096 # 12 bits of resolution
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)
    pwm.set_pwm_freq(60)

def auf(servoNummer=0):
    set_servo_pulse(servoNummer,ServoPositions[servoNummer]["auf"])

def zu(servoNummer=0):
    set_servo_pulse(servoNummer,ServoPositions[servoNummer]["zu"])


#if __name__ == "__main__":

