import base64
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

your_email = "youremail"
reciever_mail = "reciever's mail"

with open('app_password.txt', 'r') as app_password_file:
    app_password = app_password_file.read()

server.ehlo()

try:
    with open('password.txt', 'r') as file:
        content = file.read()
 
    password = base64.b64decode(content).decode("utf-8")
except UnicodeDecodeError as e:
    print("Decoding failed: It might not be UTF-8 encoded. Error:", e)
except base64.binascii.Error as e:
    print("The content is not valid base64. Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)


server.login(your_email,app_password)

msg = MIMEMultipart()
msg['From'] = 'Sender'
msg['To'] = 'reciever_mail'
msg['Subject'] = 'Python Email Message'

with open('message.txt', 'r') as message_file:
    message = message_file.read()

msg.attach(MIMEText(message, 'plain'))

file_name = 'bird.jpg'
attachment = open(file_name,'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={file_name}')
msg.attach(p)

text = msg.as_string()
server.sendmail(your_email, reciever_mail, text)