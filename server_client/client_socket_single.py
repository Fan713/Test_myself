#! /usr/bin/Python
#coding=utf-8

'''
Created on 2019年8月22日

@author: ZF
'''

import socket
s=socket.socket()             #创建对象
# host=socket.gethostname()     #获取本地地址
# print(host)
host='172.20.4.47'
port=12345                    #设置端口
s.connect((host,port))

while True: 
    data=s.recv(1024).decode()       
    print(data)            #指定接收TCP数据的最大数据量
    with open('1.txt','a') as file0:
        file0.write(data)
    file0.close()
s.close()