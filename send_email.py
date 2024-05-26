import ssl, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
msg['From'] = 'sunny990931@gmail.com'
msg['To'] = 'n11071130@ntub.edu.tw'
msg['Subject'] = Header('Test send email','utf-8').encode()

body = 'this is email from python'
msg_content = MIMEText(body)
msg.attach(msg_content)
c = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=c) as server:
    server.login('sunny990931@gmail.com','ilmk xjgb edjg mmlc')
    print(msg.as_string())
    server.sendmail('sunny990931@gmail.com','n11071130@ntub.edu.tw',msg.as_string())
    print('end')