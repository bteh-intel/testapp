import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
filename = 'Accounts.txt'
SourcePathName  = './' + filename

msg = MIMEMultipart()
msg['From'] = 'sherifmagdy.barakat@hotmail.com'
msg['To'] = 'boon.hoe.teh@intel.com'
msg['Subject'] = 'Python Test Mail'
body = 'This is an email to test sending from python code 999'
msg.attach(MIMEText(body, 'plain'))

## ATTACHMENT PART OF THE CODE IS HERE
##attachment = open(SourcePathName, 'rb')
##part = MIMEBase('application', "octet-stream")
##part.set_payload((attachment).read())
##encoders.encode_base64(part)
##part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
##msg.attach(part)

s = smtplib.SMTP("outlook.com",587)
s.ehlo()
s.starttls()
s.ehlo()
s.login('sherifmagdy.barakat@hotmail.com', 'Smagdy$28121977')
s.send_message(msg)
print ("Successfully sent email")

s.quit()
