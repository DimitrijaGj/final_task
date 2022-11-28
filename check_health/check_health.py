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


