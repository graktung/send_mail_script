import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "graktung@gmail.com"
password = "$password=$_REQUEST"

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
the_msg["To"] = input("[?] To: ")
file_html = input("[?] File HTML: ")
try:
	with open(file_html, 'r') as f:
		html_txt = f.read()
except:
	print('[-] No such file or directory: %r' %file_html)
	exit(0)

part = MIMEText(html_txt, 'html')
the_msg.attach(part)
body_mail = the_msg.as_string()

email_conn.sendmail(the_msg["From"], the_msg["To"], body_mail)
email_conn.quit()

print("[+] Email sent succesfully!")