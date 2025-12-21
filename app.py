import monitor.disk, monitor.cpu, monitor.memory, monitor.time_utils
import time
import streamlit as st
import pandas as pd

st.title("System Monitor Dashboard")
st.write("Press Ctrl+C in terminal to end session")

cpu_percent = monitor.cpu.get_cpu_percent()
ram_percent = monitor.memory.get_ram_percent()
disk_percent = monitor.disk.get_disk_percent()

cpuCol, ramCol, diskCol = st.columns(3)

cpuCol.metric("CPU Activity (%)", f"{cpu_percent:.1f}")
ramCol.metric("RAM Activity (%)", f"{ram_percent:.1f}")
diskCol.metric("Disk Space Used (%)", f"{disk_percent:.1f}")

if "history" not in st.session_state:
    st.session_state.history = []  #On startup conditions
    st.session_state.cpu_last = 0
    st.session_state.ram_last = 0  #Data is only remebered by Streamlit if it is defined it st.session_state
    st.session_state.disk_last = 0

st.session_state.history.append({
    "time": time.strftime("%H:%M:%S"), #Put info into history
    "cpu": cpu_percent,
    "ram": ram_percent,
    "disk": disk_percent
})  

st.session_state.history = st.session_state.history[-20:] #Only last 20 seconds

df = pd.DataFrame(st.session_state.history).set_index("time") #Organize data into a dataframe

st.line_chart(df[["cpu", "ram", "disk"]])
            #Send DataFrame - then names from dataframe

if monitor.cpu.did_spike(st.session_state.cpu_last, cpu_percent):                       #WARNINGS FOR SPIKES
    st.warning(f"CPU Usage SPIKE: [{monitor.time_utils.checktime()}]")
if monitor.memory.did_spike(st.session_state.ram_last, ram_percent):                           
    st.warning(f"RAM Usage SPIKE: [{monitor.time_utils.checktime()}]")
if monitor.disk.did_spike(st.session_state.disk_last, disk_percent) == True:
    st.warning(f"Disk Space is low: [{monitor.time_utils.checktime()}]")


st.session_state.cpu_last = cpu_percent
st.session_state.ram_last = ram_percent
st.session_state.disk_last = disk_percent

time.sleep(1)
st.rerun()


 ## RUN CODE BELOW FOR JUST TERMINAL DATA (No Need for STREAMLIT OR PANDAS DOWNLOAD)

# inc = 0
# last_cpu = 0 
# last_ram = 0 
# last_disk = 0 #Still need to find average if disk size is changing

# starttime = time.time()
# try: 
#     print("Press Ctrl+C to exit")
#     print("-------------------------")
#     while True:
#         cpu_percent = monitor.cpu.get_cpu_percent()
#         print(f"CPU Activity: {cpu_percent}%")
#         last_cpu += cpu_percent     #Adding for average

#         ram_percent = monitor.memory.get_ram_percent() 
#         print(f"RAM Activity: {ram_percent}%")
#         last_ram += ram_percent     #Adding for average

#         disk_percent = monitor.disk.get_disk_percent()
#         print(f"Disk Capacity Used: {disk_percent}%")
#         last_disk += disk_percent   #Adding for average

#         print(f"[{monitor.time_utils.checktime()}]")
#         inc+=1     #inc for amount of times loop has run
#         print("-------------------------") 
#         time.sleep(2)  #sleep 2 seconds to make more readable. CPU check is + 0.1 second. Therefore 2.1 second intervals.

# except KeyboardInterrupt: #After Ctrl+C is pressed
#     endtime = time.time()
#     print(f"Session ended -- Length: {(endtime-starttime):.1f}s") #Outputs session length in seconds

#     print(f"Average CPU Activity of Session: {monitor.cpu.get_cpu_average(inc, last_cpu):.1f}%")
#     print(f"Average RAM Activity of Session: {monitor.memory.get_ram_average(inc, last_ram):.1f}%")
#     print(f"Average used DISK Capacity of Session: {monitor.disk.get_disk_average(inc, last_disk):.1f}%")


