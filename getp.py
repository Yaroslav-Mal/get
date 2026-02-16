import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

        self.pwm.start(0)

        if self.verbose:
            print("PWM DAC инициализирован")

    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()

        if self.verbose:
            print("PWM DAC остановлен, GPIO очищены")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение {voltage:.3f} В вне диапазона (0 - {self.dynamic_range:.3f} В). Устанавливаем 0 В.")
            duty_cycle = 0
        else:
            duty_cycle = voltage / self.dynamic_range * 100

        self.pwm.ChangeDutyCycle(duty_cycle)

        if self.verbose:
            print(f"Напряжение: {voltage:.3f} В → Duty cycle: {duty_cycle:.2f}%")
