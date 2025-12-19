import monitor.disk, monitor.cpu, monitor.memory, monitor.time_utils
import time

inc = 0
last_cpu = 0 
last_ram = 0 
last_disk = 0 #Still need to find average if disk size is changing

starttime = time.time()
try: 
    print("Press Ctrl+C to exit")
    print("-------------------------")
    while True:
        cpu_percent = monitor.cpu.get_cpu_percent()
        print(f"CPU Activity: {cpu_percent}%")
        last_cpu += cpu_percent     #Adding for average

        ram_percent = monitor.memory.get_ram_percent() 
        print(f"RAM Activity: {ram_percent}%")
        last_ram += ram_percent     #Adding for average

        disk_percent = monitor.disk.get_disk_percent()
        print(f"Disk Capacity Used: {disk_percent}%")
        last_disk += disk_percent   #Adding for average

        print(f"[{monitor.time_utils.checktime()}]")
        inc+=1     #inc for amount of times loop has run
        print("-------------------------") 
        time.sleep(2)  #sleep 2 seconds to make more readable. CPU check is + 1 second. Therefore 3 second intervals.

except KeyboardInterrupt: #After Ctrl+C is pressed
    endtime = time.time()
    print(f"Session ended -- Length: {(endtime-starttime):.1f}s") #Outputs session length in seconds

    print(f"Average CPU Activity of Session: {monitor.cpu.get_cpu_average(inc, last_cpu):.1f}%")
    print(f"Average RAM Activity of Session: {monitor.memory.get_ram_average(inc, last_ram):.1f}%")
    print(f"Average used DISK Capacity of Session: {monitor.disk.get_disk_average(inc, last_disk):.1f}%")

