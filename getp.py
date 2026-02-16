import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(bit) for bit in bin(value)[2:].zfill(8)]

    def set_number(self, number):
        if number < 0:
            number = 0
        if number > 255:
            number = 255

        binary = self.dec2bin(number)
        GPIO.output(self.gpio_bits, binary)

        if self.verbose:
            print(f"Число: {number}, Биты: {binary}")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение {voltage:.2f} В вне диапазона (0 - {self.dynamic_range:.3f} В). Устанавливаем 0 В.")
            number = 0
        else:
            number = round(voltage / self.dynamic_range * 255)

        self.set_number(number)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
