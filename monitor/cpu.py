import psutil #import for system checks

def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval=0.1) #Get CPU percentage through 0.1 second.
    return cpu_percent
     
def get_cpu_average(inc, added_cpu):
    return (added_cpu / inc)

def did_spike(last, new):
    if new >= last + 15 and last != 0:
        return True
    else:
        return False

