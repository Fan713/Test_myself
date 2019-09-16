#!/usr/bin/env python
#coding:utf-8
from socketserver import BaseRequestHandler,ThreadingTCPServer
import threading

BUF_SIZE=4096

class Handler(BaseRequestHandler):
    def handle(self):
        address,pid = self.client_address
        print('%s connected!'%address)
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)>0:
                print('receive=',data.decode('utf-8'))
                Replydata=input('Reply msssage:')
                cur_thread = threading.current_thread()
                #response = '{}:{}'.format(cur_thread.ident,data)
#                 self.request.sendall(data)
                self.request.sendall(Replydata.encode('utf-8'))
#                 self.request.sendall(address.encode())
                print('send:',Replydata.decode('utf-8'))
            else:
                print('close')
                break

if __name__ == '__main__':
    HOST = '172.20.4.47'
    PORT = 12345
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler) 
    print('listening')
    server.serve_forever() 
    print(server)
