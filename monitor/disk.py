import psutil #import for system checks

def get_disk_percent():
    diskinfo = psutil.disk_usage('/') #Sends all info about disk
    print(f"Disk Capacity Used: {diskinfo.percent}%") #Prints how full storage is in a %.