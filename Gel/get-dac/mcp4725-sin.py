import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 100

MCP = None

try:
    MCP = mcp.MCP4725(5, 0x61, True)
    start = time.time()

    while True:
        t = time.time() - start
        sin_val = sg.get_sin_wave_amplitude(signal_frequency, t)   # ожидается диапазон -1..1
        voltage = (sin_val + 1) / 2 * amplitude                    # теперь диапазон 0..3.2 В

        MCP.set_voltage(voltage)
        sg.wait_For_sampling_period(sampling_frequency)

finally:
    if MCP is not None:
        MCP.deinit()
