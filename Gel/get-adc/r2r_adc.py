import RPi.GPIO as GPIO 
import time
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time 

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11] 
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio,0)
        GPIO.cleanup()

    def number_to_dac(self,number):
        out =  [int(i) for i in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, out)
        return out
    
    def sequential_counting_adc(self):
        for value in range(256):

            signal = self.number_to_dac(value)
            voltage = (value / 255) * (self.dynamic_range)

            time.sleep(self.compare_time)
            comparator_value = GPIO.input(self.comp_gpio)

            if comparator_value == 1: 
                print("ADC value = {:^3} -> {}".format(value,signal))
                return (voltage)
        
        return self.dynamic_range

    def det_sc_voltage(self):
        for value in range(256):
            self.number_to_dac(value)
            voltage = (value / 255) * (self.dynamic_range)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return (voltage)
        
        return self.dynamic_range
    
    def successive_approximation_adc(self):
        low = 0
        high = 255
 
        while low < high : 
            mid =(low + high) //2
            self.number_to_dac(mid)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                high = mid
        
            else:
                low = mid + 1
        return low

    def get_sar_voltage(self):
        signal = self.successive_approximation_adc()
        voltage = (signal/255) * self.dynamic_range
        return voltage



if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.183,0.1,True)
        while True:

           # voltage = adc.sequential_counting_adc()
            #print(voltage)

            ADC_voltage = adc.get_sar_voltage()
            print("ADC voltage,",ADC_voltage )

    finally:
        adc.deinit()