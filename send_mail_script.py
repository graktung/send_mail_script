import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "null"
password = "null"

try:
	email_conn = smtplib.SMTP(host, port)
except ConnectionRefusedError:
	print('[-] Connection Refused.')
	exit(0)
email_conn.ehlo()
email_conn.starttls()
try:
	email_conn.login(username, password)
except:
	print('[-] Could not login.')
	exit(0)

the_msg = MIMEMultipart("alternative")

the_msg["Subject"] = input("[?] Subject: ")
the_msg["From"] = input("[?] From: ")
to_list = input("[?] To: ")
try:
	with open(to_list) as f:
		to_list =  f.readlines()
		for i in range(len(to_list)):
			to_list[i] = to_list[i].rstrip()
file_html = input("[?] File HTML: ")
try:
	with open(file_html) as f:
		html_txt = f.read()
except:
	print('[-] No such file or directory: %r' %file_html)
	exit(0)

part = MIMEText(html_txt, 'html')
the_msg.attach(part)
body_mail = the_msg.as_string()

for to in to_list:
	the_msg["To"] = to
	email_conn.sendmail(the_msg["From"], the_msg["To"], body_mail)

email_conn.quit()

print("[+] Email sent succesfully!")
