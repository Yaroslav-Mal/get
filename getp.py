import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac_bits = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac_bits, GPIO.OUT)
GPIO.output(dac_bits, 0)
dynamic_range = 3.3


def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    if number < 0:
        number = 0
    if number > 255:
        number = 255

    binary = dec2bin(number)
    GPIO.output(dac_bits, binary)

    print(f"Число: {number}")
    print(f"Биты: {binary}\n")


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
