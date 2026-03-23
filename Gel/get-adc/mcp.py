import adc_plot as plt
import time
import mcp3021_driver as mcp

adc = mcp.MCP3021(3.183,False)

voltages = list()
times = list()
sampling_periods = list()
duration = 5
try:
    start = time.time()
    while (time.time()-start) < duration:
        sampling_start = time.time()
        voltage =adc.get_voltage()
        voltages.append(voltage)
        times.append(time.time()-start)
        sampling_periods.append(time.time() - sampling_start)
finally:
    adc.deinit()
plt.plot_sampling_preiod_hist(sampling_periods)
plt.plot_voltage_vs_time(times,voltages,3.18)