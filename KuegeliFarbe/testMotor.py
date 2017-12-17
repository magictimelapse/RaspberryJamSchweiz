import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x41)
import RPi.GPIO as GPIO
from time import sleep
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 # 1,000,000 us per second
    pulse_length /= 400 # 60 Hz
    pulse_length /= 4096 # 12 bits of resolution
    pulse *= 1000
    print (pulse_length)
    pulse /= pulse_length
    print(pulse)
    pulse = round(pulse)
    pulse = int(pulse)
    print(pulse)
    pwm.set_pwm(channel, 0, pulse)
    
pwm.set_pwm_freq(400)
if __name__== "__main__":
    dir0Pin = 40
    dir1Pin = 38
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dir0Pin,GPIO.OUT)
    GPIO.setup(dir1Pin,GPIO.OUT)
    GPIO.output(dir0Pin,GPIO.LOW)
    GPIO.output(dir1Pin,GPIO.LOW)
    set_servo_pulse(0,0.)
    sleep(1)
    print("start")
    set_servo_pulse(0,0.5)
    GPIO.output(dir0Pin,GPIO.HIGH)
    sleep(3)
    print("faster")
    set_servo_pulse(0,2)
    sleep(3)
    print("PWM off")
    set_servo_pulse(0,0.)
    GPIO.output(dir0Pin,GPIO.LOW)
    sleep(0.5)
    GPIO.output(dir1Pin,GPIO.HIGH)
    sleep(1)
    print("Rueckwaerts")
    set_servo_pulse(0,1)
    sleep(3)
    print("Disable")
    GPIO.output(dir0Pin,GPIO.LOW)
    GPIO.output(dir1Pin,GPIO.LOW)
    set_servo_pulse(0,0.)
