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
disk_alert = 80


def send_report(subject):
    message = EmailMessage()
    sender = 'sender@mail.com'
    recipient = 'recipient@example.com'
    message['From']= sender
    message['To']=recipient 
    message['Subject']= subject
    body = '''Please check your System and resolve the issue as soon as possible'''

#CPU Alert!!!
print(psutil.cpu_percent())
if psutil.cpu_percent() > cpu_alert:
    print(time.strftime("%c") + ' - CPU ALERT!!! - CPU Usage is currently above %s percent' % cpu_alert)
    subject = 'Error - CPU usage is over 80%'
    send_report(subject)
print(psutil.)

#Memeory check
print(psutil.virtual_memory().percent)
if psutil.virtual_memory().percent > disk_alert:
    print('time.strftime("%c'+ ' - MEMORY ALERT !!! - Memory is currently above %S percent' % mem_alert)
    subject = 'Error -Memory usage is over 20'

#Disk space check
if psutil.disk_usage('/').percent > disk_alert:
    print(psutil.disk_usage())
    print(time.strftime('%c') + ' - DISK SPACE ALERT - Disk usage is over 20%')
    Subject ='Error -Avaliable Disk Space is below 20%'
    send_report(subject)
    