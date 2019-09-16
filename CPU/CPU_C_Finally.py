#! usr/bin/env python
#coding=GB18030

import os
import time, re
import psutil

##########获取系统所有进程PID及进程名称###########
def processinfo(x):
    p=psutil.process_iter()
    tlp=0
    try:
        for r in p:
            aa = str(r)
#             print('aa=',aa)
            f=re.compile(x,re.I)    #正则表达式，匹配X,re.I不区分大小写
            if f.search(aa):
                tlp=int(aa.split('pid=')[1].split(',')[0])
#                 print('tlp=',tlp)
                #检索pid列表并获取传入值得pid
                return tlp
    except(psutil.NoSuchProcess):
        print('PID:%D'%aa.pid)

#############获取cpu及MEM##############
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
                            监控信息-Time: %s
            =========================================================================
            Name: %s,  PID: %s,  CPU使用率： %.2f %%,  MEM使用率: %.3f %%
            =========================================================================
            
            '''%(localtime,name,pid,cpu,Memory)
            with open(path,'a') as file0:
                file0.write(a)
        except IOError as e:
            print(e)
if __name__ == '__main__':      
        s=processinfo('MainApp.exe')
        getinfo(s)

    
    
    
    
    
    