import csv
import time
import datetime
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


if os.environ.get("client_password"):
    pwd = os.environ["client_password"]
    sender_qq = os.environ["sender"]
    receiver = os.environ["receiver"].split(';')

    host_server = 'smtp.qq.com' 
    sender_qq = '914966103@qq.com'
    
    mail_title = '定期邮件发送' 
    times = time.strftime('%Y-%m-%d %H:%M:%S')
    mail_content = f"当前时间：{times} \n"
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title,'utf-8')
    msg["From"] = sender_qq
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content,'plain','utf-8'))

    smtp = SMTP_SSL(host_server) 
    smtp.login(sender_qq,pwd)
    smtp.sendmail(sender_qq,receiver,msg.as_string())
    smtp.quit()