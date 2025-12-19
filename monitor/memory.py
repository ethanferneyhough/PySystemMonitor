import psutil #import for system checks

def get_ram_percent():
    raminfo = psutil.virtual_memory() #Sends all info about memory
    print(f"RAM Activity: {raminfo.percent}%")