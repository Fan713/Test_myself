#! usr/bin/env python
#coding=GB18030

import paramiko

class SSHConnection(object):
    def __init__(self,host,username,port,pwd):
        self.host=host
        self.username=username
        self.port=port
        self.pwd=pwd

    #��������
    def connect(self):
        transprot=paramiko.Transport(self.host,self.port)
        transprot.connect(username=self.username, password=self.pwd)
        self._transport=transprot
    #��windows������linux�������ϵ��ļ�
    def downLoad(self,remotepath,localpath):
        sftp=paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remotepath,localpath)
        
    #��windows���ϴ��ļ���Linux������
    def upLoad(self,remotePath,localPath):
        sftp=paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(localPath,remotePath)
        
    #windows��Linuxִ�������������
    def cmd(self,order):
        #����SSH����
        ssh_=paramiko.SSHClient()
        #�������Ӳ���konw_hosts�ļ��е�����
        ssh_.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #���ӷ�����
        ssh_.connect(hostname=self.host, port=self.prot, username=self.usrname, password=self.pwd)
        #ִ������
        stdin,stdout,stderr=ssh_.exec_command(order,timeout=10)
        #��ȡִ�н��
        result=stdout.read()
        print(result)
        return result
    
if __name__=='__main__':
    ssh=SSHConnection(host='192.168.223.128',username='ntuser',port='22',pwd='pwd')
    ssh.connect()
    ssh.cmd('su')
    ssh.close()
    
        