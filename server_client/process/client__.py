#!/usr/bin/env python
#

import socket
from time import sleep
from threading import Thread

host = "172.20.4.47"
port = 12345
num = 100

def sirec(s, n):
    s.sendall('sn:' + n)
    data = s.recv(1024).decode()
    s.close()


for i in range(1, 100):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    t = Thread(target=sirec, args=(s, 1))
    #t.setDaemon(True)
    t.start()


print('run over')