#!/usr/bin/env python
#coding:utf-8

import socket,sys
host='172.20.4.50'
port=12345
BUFSIZE=1024
ADDR=(host,port)

sock=socket.socket()
try:
    sock.connect(ADDR)
    print('have connected with server')
    
    while True:
        data=input('lockey#')
        if len(data)>0:
            print('send:',data)
            sock.sendall(data.encode('utf-8'))
            recv_data=sock.recv(BUFSIZE)
            print('receive:',recv_data.deconde('utf-8'))
        else:
            sock.close()
            break
except Exception:
    print('error')
    sock.close()
    sys.exit()