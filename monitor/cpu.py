import psutil #import for system checks

def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval=1) #Get CPU percentage through 1s.
    print(f"CPU Activity: {cpu_percent}%")