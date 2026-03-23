import RPi.GPIO as GPIO 

class PWM_DAC:
    def __init__(self,gpio_pin,pwn_frequency,dynamic_range,verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwn_frequency = pwn_frequency

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin,GPIO.OUT,initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwn_frequency)
    
    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.gpio_pin,0)
        GPIO.cleanup()

    def set_voltage(self,voltage):
        voltage = voltage / self.dynamic_range * 100
        print(voltage)
        self.set_number(voltage)
    def set_number(self,number):
        self.pwm.start(number)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12,1800,3.290,True)

        while True:
            try:
                voltage = float (input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Не число")
    finally:
        dac.deinit()