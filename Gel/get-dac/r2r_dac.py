import RPi.GPIO as GPIO 
class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial = 0)
    

    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()
    
    def set_number(self,number):
        return [int(i) for i in bin(number)[2:].zfill(8)]
    
    def set_voltage(self,voltage):
        if not ( 0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за данимический диапозон ЦАП (0.00 - {self.dynamic_range: .2f} 2B)")
            print("устанавливаем 0.0В")
            return 0
        return int((voltage / self.dynamic_range) * 255)
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16,20,21,25,2,17,27,22],3.183,True)
        dac_b = [16,20,21,25,2,17,27,22]
        while True:
            try:
                voltage = float (input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                print(dac.set_number(dac.set_voltage(voltage)))
                for i in range(8):
                    GPIO.output(dac_b[i],((dac.set_number(dac.set_voltage(voltage))))[i])
            except ValueError:
                print("Вы не ввели число.Попробуйте езе раз")
    finally:
        dac.deinit()