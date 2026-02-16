import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac_bits = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac_bits, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    if not (0 <= number <= 255):
        print("Число должно быть в диапазоне 0–255")
        return

    binary = format(number, "08b")
    for pin, bit in zip(dac_bits, binary):
        GPIO.output(pin, int(bit))

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
