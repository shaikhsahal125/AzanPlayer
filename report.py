#!/usr/bin/python3

import smtplib
import calendar

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

# getting month
current_date = date.today()
month = current_date.month
prev_month = month-1 if month > 1 else 12 
prev_month_name = calendar.month_name[prev_month]



# longin credintials
sender = 'sahalshaikh217@gmail.com'
sender_pass = 'xxxxxxxxxxxxxxxx'
reciever = 'home.ew37@gmail.com'

# setting up email contents
message = MIMEMultipart()
message['From'] = sender
message['To'] = reciever
message['Subject'] = f'{prev_month_name}\'s Azan Player longs.'

body_content = """
Hello Dear,

This email includes the logs from last months Azans.
The file is attached to this email.

Thank you!

Auto generated email from RaspberryPI
"""

# the attachment
message.attach(MIMEText(body_content, 'plain'))
file = '/home/pi/AzanPlayer/logFile.log
'
attachFile = open(file, 'rb')

payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attachFile).read())
encoders.encode_base64(payload)
payload.add_header('LogsFile', 'attachment', filename="Report")
message.attach(payload)

# smtp session to send email
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(sender, sender_pass)
text = message.as_string()
session.sendmail(sender, reciever, text)
session.quit()

attachFile.close()

f = open(file, 'w')
f.truncate(0)
f.close()
