from email.mime.text import MIMEText

msg=MIMEText('hello,send by Python...','plain','utf-8')

#from_addr=input('From:')
#password=input('password:')
#to_addr=input('T0:')
#smtp_server=input('SMTP server:')

from_addr=('1606675254@qq.com')
password=('syc19900015')
to_addr=('1606675254@qq.com')
smtp_server=('smtp.qq.com')

import smtplib
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()