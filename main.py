import psutil #import for system checks
import monitor
import time
import datetime

def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval=1) #Get CPU percentage through 1s.
    print(f"CPU Activiy: {cpu_percent}%")

def get_ram_percent():
    raminfo = psutil.virtual_memory() #Sends all info about memory
    print(f"RAM Activiy: {raminfo.percent}%")

def get_disk_percent():
    diskinfo = psutil.disk_usage('/') #Sends all info about disk
    print(f"Disk Capacity: {diskinfo.percent}%") #Prints how full storage is in a %.

def checktime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

while True:
   
    get_cpu_percent()
    get_ram_percent()
    get_disk_percent()
    print(f"<{checktime()}>")
    print("----------Ctrl+C to close---------------") #divider for data
    time.sleep(2) #sleep 2 seconds to make more readable. CPU check is + 1 second.
