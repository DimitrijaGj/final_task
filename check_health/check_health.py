#!/usr/bin/env python3
import psutil
import os
import shutil
import datetime
import time
import smtplib
import getpass
from email.message import EmailMessage

#Variables
cpu_alert = 80
mem_alert = 20


#CPU Alert!!!
print(psutil.cpu_percent())
if psutil.cpu_percent() > cpu_alert:
    print(time.strftime("%c") + ' - CPU ALERT!!! - CPU Usage is currently above %s percent' % cpu_alert)
    message = EmailMessage()
    sender = 'mail@example.com'
    recipient = ' exm@mail.com'
    message['From']= sender
    message['To']=recipient
    message['Subject'] = 'Error - CPU usage is over 80%'
    body = '''Please check your system and  resolve the issue as soon as posible'''