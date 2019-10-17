import smtplib
from email.mime.text import MIMEText
from email.header import Header

address = input('Gmailアドレスを入力 : ')
pw = input('パスワードを入力 : ')
# connect with SMTP Server
smtp_o = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtp_o))

# submit message 'Hello' to SMTP 
smtp_o.ehlo()

# start TLS encryption
smtp_o.starttls()

# login SMTP Server
smtp_o.login(address, pw)

# create email-text
# Japanese support
charset = 'iso-2022-jp'
subject = '日報の'
text = 'お疲れ様です。AAです。日報の更新が完了しましたので、報告いたします。'
msg = MIMEText(text, 'plain', charset)
msg['Subject'] = Header(subject.encode(charset), charset)

# submit email-text
smtp_o.sendmail(address, address, msg.as_string())
