import time
import RPi.GPIO as GPIO

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self):
        try:
            GPIO.output(self.bits_gpio, [0] * len(self.bits_gpio))
            GPIO.cleanup()
        except:
            pass

    def number_to_dac(self, number):
        bits = [(number >> i) & 1 for i in range(len(self.bits_gpio))]

    
        gpio_values = list(reversed(bits))
        GPIO.output(self.bits_gpio, gpio_values)

        if self.verbose:
            print(f"DAC <= {number}")

    def sequential_counting_adc(self):
        max_code = (1 << len(self.bits_gpio)) - 1

        for number in range(max_code + 1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            comp_state = GPIO.input(self.comp_gpio)

        
            if comp_state == 1:
                return number

        return max_code

    def get_sc_voltage(self):
  
        code = self.sequential_counting_adc()
        max_code = (1 << len(self.bits_gpio)) - 1

        voltage = (code / max_code) * self.dynamic_range
        return voltage


if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range=3.3)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Measured voltage: {voltage:.3f} V")

    finally:
        del adc
