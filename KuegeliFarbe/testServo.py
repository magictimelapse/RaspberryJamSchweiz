import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x41)
servoStart = 0.6
servo = servoStart
servoEnd = 2.5

HOST = 'localhost'
PORT = 42001
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 # 1,000,000 us per second
    pulse_length /= 50 # 60 Hz
    pulse_length /= 4096 # 12 bits of resolution
    pulse *= 1000
    pulse /= pulse_length
    pulse = round(pulse)
    pulse = int(pulse)
    pwm.set_pwm(channel, 0, pulse)
    pwm.set_pwm_freq(50)

def auf():
    set_servo_pulse(0,1.8)

def zu():
    set_servo_pulse(0,1.0)

#if __name__ == "__main__":

