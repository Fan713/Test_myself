#! usr/bin/env python
#coding=GB18030

import os
import time, re
import psutil

##########��ȡϵͳ���н���PID����������###########
def processinfo(x):
    p=psutil.process_iter()
    tlp=0
    try:
        for r in p:
            aa = str(r)
#             print('aa=',aa)
            f=re.compile(x,re.I)    #������ʽ��ƥ��X,re.I�����ִ�Сд
            if f.search(aa):
                tlp=int(aa.split('pid=')[1].split(',')[0])
#                 print('tlp=',tlp)
                #����pid�б���ȡ����ֵ��pid
                return tlp
    except(psutil.NoSuchProcess):
        print('PID:%D'%aa.pid)

#############��ȡcpu��MEM##############
def getinfo(tlp):
    p=psutil.Process(tlp)
    path=r'txt.txt'
    if os.path.exists(path):
        os.remove(path)
    while True:
        p_cpu=p.cpu_percent(interval=1)
        cpucount=psutil.cpu_count(logical=True)
        cpu=int(p_cpu/cpucount)
        try:
            pid=p.pid
            name=p.name()
            Memory=p.memory_percent(memtype='rss')
            localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            a='''
                            �����Ϣ-Time: %s
            =========================================================================
            Name: %s,  PID: %s,  CPUʹ���ʣ� %.2f %%,  MEMʹ����: %.3f %%
            =========================================================================
            
            '''%(localtime,name,pid,cpu,Memory)
            with open(path,'a') as file0:
                file0.write(a)
        except IOError as e:
            print(e)
if __name__ == '__main__':      
        s=processinfo('MainApp.exe')
        getinfo(s)

    
    
    
    
    
    