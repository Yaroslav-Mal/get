import adc_plot as plot
import r2r_adc as adc
import time

r2r = adc.R2R_ADC(3.183,0.0001,True)
voltages = list()
times = list()
sampling_periods = list()
duration = 5

try:
    start = time.time()
    while (time.time()-start) < duration:
        sampling_start = time.time()
        voltage =r2r.get_sar_voltage()
        voltages.append(voltage)
        times.append(time.time()-start)
        sampling_periods.append(time.time() - sampling_start)
finally:
    r2r.deinit()
plot.plot_sampling_preiod_hist(sampling_periods)
plot.plot_voltage_vs_time(times,voltages,3.18)
