import datetime

def checktime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")