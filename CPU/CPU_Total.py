#! usr/bin/env python
#coding=GB18030

import time,re

import psutil

##########��ȡϵͳ���н���PID����������###########
def processinfo(x):
    p=psutil.process_iter()
    tlp=0
    try:
        for r in p:
            aa = str(r)
            f=re.compile(x,re.I)
            if f.search(aa):
                tlp=int(aa.split('pid=')[1].split(',')[0])
                #����pid�б���ȡ����ֵ��pid
                return tlp
    except(psutil.NoSuchProcess):
        print('PID:%D'%aa.pid)

#############��ȡcpu��MEM##############
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
         

#���CPU��Ϣ
def cpu():
    cpu_per=int(psutil.cpu_percent(1))
    return cpu_per

#����ڴ���Ϣ
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
                            �����Ϣ
        ===================
        CPUʹ���ʣ� %s %%,
        ===================
                    �ڴ��ܴ�С(MB): %s,
                    �ڴ�ʹ�ô�С(MB): %s,
                    �ڴ�ʹ����: %s %%
        '''%(cpu_info,mem_info['mem_total'],mem_info['mem_used'],mem_info['mem_per'])
    print(info)
main()

