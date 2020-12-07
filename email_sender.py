#In this project we are trying to send email using python
# Do not use "email.py" for the name of this python file 
import smtplib
from email.message import EmailMessage
from string import Template #if we use html
from pathlib import Path   #if we use html

html = Template(Path('index.html').read_text())	#for using html and read it as a sting(text)
email = EmailMessage()
email['Subject'] = 'You are doing a great project'
email['From'] = 'sam'
email['To'] = 'receiverexample@gmail.com'	#this email address will receive your email
# email.set_content('I am a python master!')	#while using text instead of html
email.set_content(html.substitute({'name':'sam','age':30}),'html')	#Don't forget to use html
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo() #hello part
	smtp.starttls()	#encryption part
	#give the email and password so python code can login and send email
	smtp.login('senderexample@gmail.com','emailpassword')
	smtp.send_message(email)
	print('done!')

