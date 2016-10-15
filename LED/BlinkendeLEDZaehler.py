import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
zaehler = 0
while zaehler < 5:
    GPIO.output(3, GPIO.HIGH)
    print "an!"
    time.sleep(1)
    GPIO.output(3, GPIO.LOW)
    print "aus!"
    time.sleep(1)
    zaehler = zaehler + 1
