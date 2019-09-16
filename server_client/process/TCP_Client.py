#! /usr/bin/Python
#coding=utf-8

import socket
# import errno
# from errno import EINTR
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='172.20.4.50'
port=12345
s.connect((host,port))
while True:
#     data=s.recv(1024).decode()
#     print(data)
    message=input('请输入发送内容:')
    if message=='Q' or message == 'q':
        break            
    s.sendall(message.encode('utf-8'))
    data=s.recv(1024).decode()
    print(data)

    print('the dat received is',data) 
    with open('1.txt','a') as file0:
        file0.write(data+'\n')   
    file0.close()
#     if len(data)<=0 and errno!=EINTR:
#         break
s.close()