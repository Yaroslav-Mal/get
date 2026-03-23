import RPi.GPIO as GPIO 
import pwm_dac as pwm_dac
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 100

try:
    dac = pwm_dac.PWM_DAC(12, 500, 3.290, True)
    start = time.time()
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time() - start)
            dac.set_voltage(voltage*amplitude)
            sg.wait_For_sampling_period(sampling_frequency)
        except ValueError:
            print("Не число")
finally:
    dac.deinit()