import monitor.disk, monitor.cpu, monitor.memory, monitor.time_utils
import time

try: 
    print("Press Ctrl+C to exit")
    print("-------------------------")
    while True:
        monitor.cpu.get_cpu_percent()
        monitor.memory.get_ram_percent()
        monitor.disk.get_disk_percent()
        print(f"[{monitor.time_utils.checktime()}]")
        print("-------------------------") 
        time.sleep(2) #sleep 2 seconds to make more readable. CPU check is + 1 second. Therefore 3 second intervals.

except KeyboardInterrupt: #After Ctrl+C is pressed
    print("Session ended")
