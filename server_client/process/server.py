#!/usr/bin/env python
#encoding=utf-8

import socket
import queue
import threading
from time import sleep

host = "172.20.4.47"
port = 12345
timeWait = 3           #定义每个线程处理任务时需要的时间，模拟处理任务
ThreadNum = 10         #定义创建的线程

cache = queue.Queue(maxsize=1000)         #定义一个队列

# 处理任务的类
class Server(threading.Thread):
    def __init__(self, cache, ThreadName):
        threading.Thread.__init__(self)
        self.name = ThreadName
        self.cache = cache

    def run(self):
       while True:
           if not cache.empty():     #判断队列是否为空
               conn, addr = cache.get()
               data = conn.recv(1024).decode()
               message='success'
               conn.sendall(message.encode())
               print('cacheData: ' + data + '; ThreadName: ' + self.name + '; cacheSize: ' +  str(self.cache.qsize()))
               sleep(timeWait)


for i in range(ThreadNum):
    s = Server(cache, str(i))
    s.setDaemon(True)       #设置为守护模式，当主线程退出时，子线程立即退出
    s.start()

# 创建Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定socket
s.bind((host, port))
# 设置系统最大等待队列，当连接过多时，系统缓存中可以缓存多少连接，不宜设置过大，消耗内存和cpu
s.listen(5)

while True:
    # 循环接受，当接受到连接时，把连接放入队列中，由线程获取后执行
    conn, addr = s.accept()
    cache.put((conn, addr))

conn.close()
