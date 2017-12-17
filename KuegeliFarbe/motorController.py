import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x41)
import RPi.GPIO as GPIO
from time import sleep

class MotorController(object):
    def __init__(self,address=0x41):
        self._pwm =  Adafruit_PCA9685.PCA9685(address=address)
        self._pwm.set_pwm_freq(400)
        GPIO.setmode(GPIO.BOARD)
        self._dir0Pin = 40
        self._dir1Pin = 38
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._dir0Pin,GPIO.OUT)
        GPIO.setup(self._dir1Pin,GPIO.OUT)
        GPIO.output(self._dir0Pin,GPIO.LOW)
        GPIO.output(self._dir1Pin,GPIO.LOW)
        self.set_servo_pulse(0,0.)
    def __del__(self):
        GPIO.output(self._dir1Pin,GPIO.LOW)
        GPIO.output(self._dir0Pin,GPIO.LOW)
        self.set_servo_pulse(0,0.)
        
    def set_servo_pulse(self,channel, pulse):
        pulse_length = 1000000 # 1,000,000 us per second
        pulse_length /= 400 # 400 Hz
        pulse_length /= 4096 # 12 bits of resolution
        pulse *= 1000
        print (pulse_length)
        pulse /= pulse_length
        print(pulse)
        pulse = round(pulse)
        pulse = int(pulse)
        print(pulse)
        self._pwm.set_pwm(channel, 0, pulse)

    
        
    def vorwaerts(self,speed):
        GPIO.output(self._dir1Pin,GPIO.LOW)
        sleep(0.1)
        GPIO.output(self._dir0Pin,GPIO.HIGH)
        self.set_servo_pulse(0,speed)

    def rueckwaerts(self,speed):
        GPIO.output(self._dir0Pin,GPIO.LOW)
        sleep(0.1)
        GPIO.output(self._dir1Pin,GPIO.HIGH)
        self.set_servo_pulse(0,speed)


    def stop(self):
        GPIO.output(self._dir1Pin,GPIO.LOW)
        GPIO.output(self._dir0Pin,GPIO.LOW)
        self.set_servo_pulse(0,0.)
        
