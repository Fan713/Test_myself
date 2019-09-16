#!/usr/bin/env python
#coding:utf-8

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data=self.request.recv(1024)
                print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                self.request.sendall(self.data)
        except Exception as e:
            print(self.client_address,"连接断开")
        finally:
            self.request.close()
    def setup(self):
        print("before handle,连接建立：",self.client_address)
    def finish(self):
        print("finish run  after handle")

if __name__=="__main__":
    HOST,PORT = "172.20.4.47",12345
    server=socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()