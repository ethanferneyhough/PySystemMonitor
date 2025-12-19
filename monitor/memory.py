import psutil #import for system checks

def get_ram_percent():
    raminfo = psutil.virtual_memory() #Sends all info about memory
    return raminfo.percent

def get_ram_average(inc, added_ram):
    return (added_ram / inc)
