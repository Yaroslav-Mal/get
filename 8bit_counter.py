import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0) 


up = 5       
down = 6     
GPIO.setup([up, down], GPIO.IN, pull_up_down=GPIO.PUD_UP)


num = 0


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


sleep_time = 0.2

try:
    while True:
        if not GPIO.input(up):  
            num += 1
            if num > 255:       
                num = 255
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)

        if not GPIO.input(down):
            num -= 1
            if num < 0:         
                num = 0
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)

        if not GPIO.input(up) and not GPIO.input(down):
            num = 255
            print(num, dec2bin(num))
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()