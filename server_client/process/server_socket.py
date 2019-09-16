#! /usr/bin/Python
#coding=utf-8
'''
Created on 2019年8月22日

@author: ZF
'''

import socket

s=socket.socket()                          #创建socket对象
# host=socket.gethostname()                  #获取本地主机名
# print(host)
host='172.20.4.47'
port=12345                                 #设置端口
s.bind((host,port))                        #绑定端口

s.listen(5)                                #等待客户端连接
while True:
    c,addr=s.accept()                      #建立客户连接
    print('连接地址:',addr)
#     print(addr)
    message=input('请输入返回内容:')
    c.send(message.encode())
c.close()