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
    bash:
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt

How to run:
    Streamlit Dashboard:
        bash:
            py -m streamlit run app.py

    Terminal: (Will need to uncomment this in app.py)
        bash:
            python main.py







