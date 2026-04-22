<img width="1280" height="680" alt="pythonpic" src="https://github.com/user-attachments/assets/8925ecf3-a3aa-4141-bfec-531f38cadb9a" /><img width="1280" height="740" alt="1769916446445" src="https://github.com/user-attachments/assets/3d6c3d96-f2d9-4008-8326-6bcc55a0455e" />

PySystemMonitor is a lightweight Python system monitoring tool that tracks CPU, RAM, and Disk usage and displays a
live output to the user in a streamlit dashboard and/or the terminal.

-Live CPU/RAM/Disk metrics
-Trackable history over time
-Optional Streamlit and/or terminal output
-Graphing of history of output over time.
-Warning messages if metrics spike.
-Terminal averages for metrics after session
-Session length timer

Installation:

        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt

How to run:

Streamlit Dashboard:
      
        py -m streamlit run app.py

or

Terminal: (Will need to uncomment this in app.py)
       
         python app.py







