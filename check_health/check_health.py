#!/usr/bin/env python3
import psutil
import os
import shutil
import datetime
import time

#Variables
cpu_alert = 80
mem_alert = 20


#CPU Alert!!!
print(psutil.cpu_percent())
if psutil.cpu_percent() > cpu_alert:
    print(time.strftime("%c") + ' - CPU ALERT!!! - CPU Usage is currently above %s percent' % cpu_alert)