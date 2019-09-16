#!/usr/bin/env python
#coding:utf-8

import os
import socket
import threading

host='172.20.4.47'
port=12345
hostname=socket.gethostname()                      #获取本机计算机名称
localhost=socket.gethostbyname(hostname)           #获取本地IP
path='1.txt'

def sendMsg(clientSocket):                              #发送消息至server
    while True:
        msg = input('\n'+'%s sendmsg……>>>'%localhost)
        if msg=='q' or msg == 'Q':
            os._exit(0)
        clientSocket.sendall(msg.encode('utf-8'))

def recvMsg(clientSocket):                              #接收server返回的消息
    while True:
        msg = clientSocket.recv(2048)
        print('\n'+'%s recvmsg……>>>%s'%(host,msg.decode('utf-8')))    #/r换行，光标在上一行；/n换行，光标在下一行
        with open(path,'a') as file0:
            file0.write(msg.decode('utf-8')+'\n')  
        file0.close()

def check_alive(t_send,t_recv):
    while True:
        dir={'send':t_send.is_alive(),'recv':t_recv.is_alive()}  
        for i in dir:
            if dir[i]==False:
                print('dir[%s]='%i,dir[i])
                os._exit(0)

def check_file():
    with open(path,'r+') as file1:
#        print(file1.readlines())
       for line in file1:
           print(line)
       position=file1.tell()
       print('当前文件位置:',position)
    print(len(path))   
    file1.close()
    fsize=os.path.getsize(path)
    fsize=fsize/float(1024*1024)
    print(fsize)
    
def main():   
    clientSocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((host,port))
    threads=[]
#     t_send = threading.Thread(target=sendMsg,args=(clientSocket,))
#     t_send.setName('sendMSG')
#     threads.append(t_send)
    t_recv = threading.Thread(target=recvMsg,args=(clientSocket,)) #将套接字作为参数传给新线程，各自的线程中分别执行收，发数据
    t_recv.setName('recvMsg')
    threads.append(t_recv)   
    t_send = threading.Thread(target=sendMsg,args=(clientSocket,))
    t_send.setName('sendMSG')
    threads.append(t_send) 
#     tr.start()                #可直接启动两个线程，不用下面for循环
#     ts.start()
    for t in threads:                       
        t.setDaemon(True)        #设置为守护线程，Thread中setDaemon把线程的daemon标志设为daemonic(在调用start()函数前调用)
        t.start()
    check_alive(t_send, t_recv)
#     for j in threads:            #遍历所有线程,程序挂起，直到线程结束
#         j.join() 
#     print(threading.enumerate())     #获取所有线程
    check_file()
if __name__ == '__main__':
    main()
#     check_file()
    
        