import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac_bits = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac_bits, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за диапазон (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    if not (0 <= number <= 255):
        number = 0

    binary_str = format(number, '08b')
    binary_list = [int(bit) for bit in binary_str]

    GPIO.output(dac_bits, binary_list)

    # 👇 ВЫВОД В КОНСОЛЬ
    print(f"Число для ЦАП: {number}")
    print(f"Биты: {binary_str}\n")


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)

            print(f"Введено: {voltage:.3f} В")
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()

