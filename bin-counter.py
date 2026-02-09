import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds,0)
up = 20
down = 21
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0
def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfile(8)]
sleep_time = 0.2
while Tbinrue:
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)
    for led in reversed(leds):
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)