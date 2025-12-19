import psutil #import for system checks

def get_disk_percent():
    diskinfo = psutil.disk_usage('/') #Sends all info about disk
    return diskinfo.percent #Prints how full storage is in a %.

def get_disk_average(inc, added_disk):
    return (added_disk / inc)
