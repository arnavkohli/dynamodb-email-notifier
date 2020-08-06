import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 

def send_email(sender_address: str, sender_password: str, receiver_address: str, body: str, subject: str):
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = subject
	message.attach(MIMEText(body, 'html')) 
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.starttls()
	session.login(sender_address, sender_password)
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('[INFO] Mail Sent')