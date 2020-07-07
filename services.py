#!/usr/bin/env python


import smtplib
import time
import os
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import commands


def sendmail(service):
    #Preparando Email
    mail_content = '''Ola
    O servico ''' + service + ''' esta inativo no servidor ''' + commands.getoutput('hostname') + ''';
    Sera necessario reiniciar o mesmo.
    Favor nao responder este email.

    Atte.
    '''
    sender_address = 'email-for-monitoro@gmail.com'
    sender_pass = 'xxxxxxxxx'
    receiver_address='client@seudominio.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'O Servico '+ service +' parado no servidor ' + commands.getoutput('hostname')
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("Send Alert to service " + service )



output = commands.getoutput('ps -A')
if 'cups' not in output:
    sendmail('cups')
    os.system("sudo /etc/init.d/cups restart")

if 'apache2' not in output:
    sendmail('Apache2')
    os.system("sudo /etc/init.d/apache2 restart")

if 'mysql' not in output:
    sendmail('Mysql')
    os.system("sudo /etc/init.d/mysql restart")
