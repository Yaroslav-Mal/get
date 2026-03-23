import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)
led = 26
state = 1 
GPIO.setup(led, GPIO.OUT)
button = 6
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button):
        GPIO.output(led,0)
    else:
        GPIO.output(led,1)