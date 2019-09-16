#! usr/bin/env python
#conding=GB18030

import os
import sys
import time

import psutil

import pandas as pd


##########获取系统所有进程PID及进程名称###########
List=[]
pids=psutil.pids()
for pid in pids:
    p=psutil.Process(pid)
    list1='%d'%pid,'%s'%p.name()
    List.append(list1)
print('List =',List)
print(len(List))

###############添加################################
def get_cpu_percent(ids,interval=1):
    processes=[psutil.Process(pid=i) for i in ids]
    for p in processes:
        p.cpu_percent(interval=None)
    time.sleep(interval)
    percents=[p.cpu_percent(interval=None) for p in processes]
    return percents
# #获取进程名称为MainApp.exe的PID
# for i in range(len(List)):
#     if 'MainApp.exe' in List[i][1]:
#         PID = List[i][0]
#         print('MainApp.exe进程PID=',PID)
# #         PID.cpu_percent(interval=None)
# def getProcessInfo(p): 
#     """取出指定进程占用的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
#     """
#     try:
#         cpu = int(p.get_cpu_percent(interval=0)) 
#         rss, vms = p.get_memory_info() 
#         name = p.name 
#         pid = p.pid 
#     except psutil.error.NoSuchProcess,e:
#         name = "Closed_Process"
#         pid = 0
#         rss = 0
#         vms = 0
#         cpu = 0
#     return [name.upper(), pid, rss, vms, cpu]







#         
# ##################获取report路径#####################
# def get_path():
#     path=sys.path[0]+r'\report'
#     if not os.path.exists(path):
#         path=os.path.abspath('..')+r'\report'
#         print(path)
# #         
# # ##################获取进程CPU与MEM占用率###############
# def get_usage():
#     path1=get_path()+'\Usage.txt'   #设定生成Usage.txt的路径
#     print(path1)
#     if os.path.exists(path1):
#         os.remove(path1)
#     c=[]
#     m=[]
#     t=[]
#     try:
#         def get_cpu_info():
#             i=0
#             print("getting Usage……")
#             while True:
# #                 if check_exist('MainApp.exe')==0:
# #                     break
#                 i=i+1
#                 text=open(path1,'a')
#                 cpucount=psutil.cpu_count(logical=True)   #CPU核个数
#                 process=psutil.Process(int(PID))          #获取PID监视进程
#                 cpupercent=process.cpu_percent(interval=1)  #设置获取cpu的间隔时间为1s
#                 cpu=int(cpupercent/cpucount)    
#                 mem=process.memory_percent()
#                 now=time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime())
#                 c.append(cpu)
#                 m.append(mem)
#                 t.append(now)
#                 if cpu<=50:
#                     print >>text,now+'               '+str(cpu)+'                  '+str(mem)
#                     text.close()
#                 else:
#                     print >>text,now+'               '+str(cpu)+'                  '+str(mem)
#                     text.close()
#                     Log_file=get_path()+'log.txt'
#                     with open(Log_file,'r') as tf:
#                         lines=tf.readlines()
#                         fun_name=lines[-1].split(' ')[1]
#                     over_file=get_path()+'\overusage.txt'
#                     over=open(over_file,'a')
#                     over.write(fun_name)
#                     over.write('\n')
#                     over.close()
#         print('进程%s的'%PID +'cpu监控已经运行，结果在result.txt生成')
#         print('---------------------------------------------')
#         text=open(path1,'a')
#         print >> text,'测试时间'+'              '+'cpu使用率'+'                   '+'MEM占用率'
#         text.close()
#         get_cpu_info()
#     except:
#         pass
#     finally:
#         print(u'进程%s'%PID + u'已经结束')
#         info={u'记录时间':t,
#               u'CPU使用率':c,
#               u'MEM使用率':m
#             }
#         df=pd.DataFrame(info)
#         ex=get_path()+r'\usage.xls'
#         df.to_excel(ex)
# if __name__=='__main__':
#     get_path()
#     get_usage()

# def getAllProcessInfo():
#     """取出全部进程的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
#     """
#     instances = []
#     all_processes = list(psutil.process_iter()) 
#     for proc in all_processes: 
#         proc.get_cpu_percent(interval=0) 
#     #此处sleep1秒是取正确取出CPU使用率的重点
#     time.sleep(1) 
#     for proc in all_processes: 
#         instances.append(getProcessInfo(proc))
#     return instances
# getAllProcessInfo()