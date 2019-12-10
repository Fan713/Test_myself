#! usr/bin/env python
#coding=utf-8
# import os
path1=r'r.txt'
##############################################################################
#若路径下存在r.txt,则删除
# if os.path.exists(path1):
#     os.remove(path1)

###############################################################################
#case1:获取0-255的16进制，并去除0X，2位有效位
# for i in range(256):   
# #     print(hex(i),end=' ')  #数据输出在一行
# #     print(hex(i)[2:],end=' ')  #去掉0X
#     Hex_Data=hex(i)[2:]
#     print(Hex_Data.zfill(2),end=' ')  #2位有效位，不足自动补零
#     with open('r.txt','a') as f:
#         f.write(Hex_Data.zfill(2)+' ')
#     f.close()
################################################################################

################################################################################
#case2:将16进制转换成十进制，并存储在txt文本中
new_list=[]
with open(path1,'r+') as f0:
    lines=f0.read()
    elem_list=lines.split()               #按照空格将lines进行切片处理
    print('elem_list=',elem_list)    
    for elem in elem_list:
        elem=int(elem,16)                 #将16进制转换成十进制,如：int('0x0A',16)
        f0.write(str(elem)+' ')
        new_list.append(str(elem))
    print('new_list=',new_list)
f0.close()

################################################################################







