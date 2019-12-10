#!/usr/bin/env python
#coding=utf-8

import os

root =os.path.abspath(os.path.join(os.getcwd(),'..'))
# print(root)
path = root+"\\photos\\"
# print(path)

f=os.listdir(path)
n=0
for i in f:
    s=str(n+1)
    s=s.zfill(3)
    oldname=path+f[n]
    newname=path+s+'.jpg'
    os.rename(oldname,newname)
    print(oldname,'---------->',newname)
    n+=1   