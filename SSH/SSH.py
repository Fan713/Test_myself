#! usr/bin/env python
#coding=GB18030

import paramiko

class SSHConnection(object):
    def __init__(self,host,username,port,pwd):
        self.host=host
        self.username=username
        self.port=port
        self.pwd=pwd

    #创建链接
    def connect(self):
        transprot=paramiko.Transport(self.host,self.port)
        transprot.connect(username=self.username, password=self.pwd)
        self._transport=transprot
    #从windows端下载linux服务器上的文件
    def downLoad(self,remotepath,localpath):
        sftp=paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remotepath,localpath)
        
    #从windows端上传文件到Linux服务器
    def upLoad(self,remotePath,localPath):
        sftp=paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(localPath,remotePath)
        
    #windows对Linux执行任意命令操作
    def cmd(self,order):
        #创建SSH对象
        ssh_=paramiko.SSHClient()
        #允许连接不在konw_hosts文件中的主机
        ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接服务器
        ssh_.connect(hostname=self.host, port=self.prot, username=self.usrname, password=self.pwd)
        #执行命令
        stdin,stdout,stderr=ssh_.exec_command(order,timeout=10)
        #读取执行结果
        result=stdout.read()
        print(result)
        return result
    
if __name__=='__main__':
    ssh=SSHConnection(host='192.168.223.128',username='ntuser',port='22',pwd='pwd')
    ssh.connect()
    ssh.cmd('su')
    ssh.close()
    
        