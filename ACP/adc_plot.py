from matplotlib import pyplot as plt
def plot_voltage_vs_time(time , voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage, marker ='o', linestyle='-', markersize = 3)
    plt.xlabel("Время(С)")
    plt.ylabel("Напряжение(В)")

    plt.xlim(0,max(time) if time else 10)
    plt.ylim(0,max_voltage*1.05)

    plt.grid(True, linestyle='--', alpha=0.7)
    
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    ax.plot(0,0,'ko',markersize = 5)

    plt.show()

def plot_sampling_preiod_hist(sampling_period):
    plt.figure(figsize=(10,6))
    plt.xlabel("Время(С)")
    plt.ylabel("Замеры")

    plt.xlim(0,max(sampling_period) if sampling_period else 10)
    plt.ylim(0,len(sampling_period)*1.05)

    plt.grid(True, linestyle='--', alpha=0.7)
    
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    ax.hist(sampling_period)

    plt.show()
