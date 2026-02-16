import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds,0)
up = 20
down = 21
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0
def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]
sleep_time = 0.2
Max_NUM = 255
while True:
    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)
        