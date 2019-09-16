#! usr/bin/env python
#coding=utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
sender = 'fan.zhou@keliangtek.com'
receiver = 'fan.zhou@keliangtek.com'
smtpserver = 'smtp.exmail.qq.com'
username = 'fan.zhou@keliangtek.com'
password = 'ZHOUFANabc123'
mail_title = '主题：这是带附件的邮件'
 
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')
 
# 邮件正文内容
message.attach(MIMEText('来来来，这是邮件的正文', 'plain', 'utf-8'))
 
# 构造附件1（附件为TXT格式的文本）
pdfFile = r'C:\Users\KLJS151\Desktop\address.txt'
att1 = MIMEText(open(pdfFile, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="address.txt"'
message.attach(att1)
 
# # 构造附件2（附件为JPG格式的图片）
# att2 = MIMEText(open('123.jpg', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="123.jpg"'
# message.attach(att2)
#  
# # 构造附件3（附件为HTML格式的网页）
# att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')
# att3["Content-Type"] = 'application/octet-stream'
# att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
# message.attach(att3)
 
 
smtpObj = smtplib.SMTP_SSL(smtpserver,465)   # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
smtpObj.login(username, password)
print('login sucessful!')
smtpObj.sendmail(sender, receiver, message.as_string())
print("邮件发送成功！！！")
smtpObj.quit()
