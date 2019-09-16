#! usr/bin/env python
#coding=utf-8


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.header import Header


mailto_list=['fan.zhou@keliangtek.com']     #多个用户用,隔开
# mailto_list='fan.zhou@keliangtek.com'
mail_host='smtp.exmail.qq.com'             #服务器地址
mail_user="fan.zhou@keliangtek.com"
mail_pass="ZHOUFANabc123"          

def send_mail(receivers,sub,content):
    sender="python_Test"+"<"+mail_user+">"
    print(sender)
    msg=MIMEMultipart()                    #创建邮件体
#     msg['subject']=sub
    msg['Subject'] = Header(sub, 'utf-8')  
    msg['From']=sender
    msg['To']=','.join(receivers)
#     msg['To']=receivers
    msg.attach(MIMEText(content,'plain','utf-8'))

    #附件为文件
    pdfFile = [r'E:\eclipse\workspace\ZF_myself\Automatically_send_a_mailbox.py',r'E:\eclipse\workspace\ZF_myself\Auto_send_email.py']
    for filename in pdfFile:
        att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=Automatically_send_a_mailbox.py"'
        att1["Content-Disposition"] = 'attachment; filename='+filename
        msg.attach(att1)
    
    try:
        server=smtplib.SMTP_SSL(mail_host,465)    #连接服务器
        server.login(mail_user,mail_pass)
        print('login Successful')
        server.sendmail(sender,receivers,msg.as_string())
        print('send Successful')
        server.quit()
    except Exception:
        print('error')

content='hello,this is a python_test email, not reply' 
send_mail(mailto_list, "Python_email_test", content)


