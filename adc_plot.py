import time
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO

# ===== Класс АЦП =====
class R2R_ADC:
    def __init__(self, dynamic_range=2.73, compare_time=0.01):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time

        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [(number >> i) & 1 for i in range(len(self.bits_gpio))]
        GPIO.output(self.bits_gpio, list(reversed(bits)))

    def sequential_counting_adc(self):
        max_code = (1 << len(self.bits_gpio)) - 1

        for code in range(max_code + 1):
            self.number_to_dac(code)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                return code

        return max_code

    def get_voltage(self):
        code = self.sequential_counting_adc()
        max_code = (1 << len(self.bits_gpio)) - 1
        return (code / max_code) * self.dynamic_range

# ===== График =====
def plot_voltage_vs_time(t, v, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(t, v)

    plt.title("Voltage vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")

    plt.xlim(min(t), max(t))
    plt.ylim(0, max_voltage)

    plt.grid()
    plt.show()

# ===== Основная программа =====
if __name__ == "__main__":

    adc = R2R_ADC(dynamic_range=2.73, compare_time=0.0001)

    voltage_values = []
    time_values = []

    duration = 3.0

    try:
        start = time.time()

        while time.time() - start < duration:
            voltage_values.append(adc.get_voltage())
            time_values.append(time.time() - start)

        plot_voltage_vs_time(
            time_values,
            voltage_values,
            adc.dynamic_range
        )

    finally:
        del adc
