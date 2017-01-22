import smtplib
from email.mime.text import MIMEText

username = input('Enter user name>')+'@gmail.com'
password = input('Enter password>')

sender = username
receiver = input('Enter receiver email address>')
subject = input('Enter Subject> ')
mail_content = '''Content: '''
msg = MIMEText(mail_content,'html','utf-8')
msg['Subject'] = subject

mail_server = 'smtp.gmail.com'
mail_server_port = 587
server = smtplib.SMTP('smtp.gmail.com', 587)

print('>connecting....')
server.ehlo()
server.starttls()
print('>connected....')
server.login(username, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()
