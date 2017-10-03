#!/usr/bin/python3

import getpass
import smtplib
from email.mime.text import MIMEText

smtp_srvr   = 'smtp.gmail.com'
smtp_user   = 'nardos.tessema@gmail.com'
smtp_pass   = getpass.getpass('Authenticating <%s> to use <%s> as a relay.\nEnter Password: ' % (smtp_user, smtp_srvr))

textfile    = 'email.txt'
sender      = input('From: ')
recepient   = input('To: ').split()

server = smtplib.SMTP(smtp_srvr, 587)
server.ehlo()
server.starttls()
server.login(smtp_user, smtp_pass)

fp = open(textfile, 'r')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = sender
msg['To'] = ', '.join(recepient)
server.sendmail(sender, recepient, msg.as_string())
server.quit()
