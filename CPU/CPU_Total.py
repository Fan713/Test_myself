#! usr/bin/env python
#coding=GB18030

import time,re

import psutil

##########获取系统所有进程PID及进程名称###########
def processinfo(x):
    p=psutil.process_iter()
    tlp=0
    try:
        for r in p:
            aa = str(r)
            f=re.compile(x,re.I)
            if f.search(aa):
                tlp=int(aa.split('pid=')[1].split(',')[0])
                #检索pid列表并获取传入值得pid
                return tlp
    except(psutil.NoSuchProcess):
        print('PID:%D'%aa.pid)

#############获取cpu及MEM##############
def getinfo(tlp):
    p=psutil.Process(tlp)
    cpu_list=[]
    while True:
        p_cpu=p.cpu_percent(interval=1)
        cpucount=psutil.cpu_count(logical=True)
        cpu=int(p_cpu/cpucount)
        cpu_list.append(p_cpu)
        cpu=0.00
        cpu=float(sum(cpu_list))/len(cpu_list)
        print(cpu)
        try:
            pid=p.pid
            name=p.name()
            Memory=p.memory_percent(memtype='rss')/2
            localtime=time.strftime('%H:%M:%S',time.localtime(time.time()))
        except IOError as e:
            print(e)
    else:
        print('Time:%s'%(localtime), "PID:%s" % (pid), "Name:%s" % (name),
            "Memory=%.3f%%" % (Memory), "CPU=%.2f%%" % (cpu * 2))
         

#监控CPU信息
def cpu():
    cpu_per=int(psutil.cpu_percent(1))
    return cpu_per

#监控内存信息
def mem():
    mem_total = int(psutil.virtual_memory()[0]/1024/1024)
    mem_used = int(psutil.virtual_memory()[3]/1024/1024)
    mem_per = int(psutil.virtual_memory()[2])
    mem_info={
        'mem_total':mem_total,
        'mem_used':mem_used,
        'mem_per':mem_per
        }
    return mem_info


def main():
    cpu_info=cpu()
    mem_info=mem()
    info='''
                            监控信息
        ===================
        CPU使用率： %s %%,
        ===================
                    内存总大小(MB): %s,
                    内存使用大小(MB): %s,
                    内存使用率: %s %%
        '''%(cpu_info,mem_info['mem_total'],mem_info['mem_used'],mem_info['mem_per'])
    print(info)
main()

