import mcp4715_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 100
try:
    MCP = mcp.MCP4725(5, True)
    start = time.time()
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time() - start)
            MCP.set_voltage(voltage*amplitude)
            sg.wait_For_sampling_period(sampling_frequency)
        except ValueError:
            print("Вы не ввели число.Попробуйте езе раз")
finally:
    MCP.deinit()