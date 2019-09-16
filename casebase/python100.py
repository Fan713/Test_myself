#! /usr/bin/env python
#coding=utf-8

# a = 25
# b = 3
# print (a/b)
# print(a // b)
# print(a % b)
# print(a ** b)
# 
# e = '123'
# f = int(e)
# g = '123.456'
# h = float(g)
# print (type(e),type(g)) 

from random import randint
import math
import getpass

# face = randint(2,9)
# if face == 1 :
#     result ='唱首歌'
# elif face ==2:
#     result = 'TT'
# elif face == 3 or 4 or 5 or 6 or 7 or 8 or 9:
#     result ='123木头人，不许动'
# print(result)

# print("math.sqrt(100) : ", math.sqrt(100))  #平方根

# usr=getpass.getuser()   #获取用户名
# password = getpass.getpass()   #获取密码
# print(usr)
# print(password)


#####################################
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value >100:
#             raise ValueError('score must between 0~100!')
#         self._score=value
# if __name__== '__main__':
#     s=Student()
#     s.score=60
#     print(s.score)
#     s.score=999



import json
import re
import sys
import os
s="愿你合上笔盖的刹那，有着侠客收剑入鞘的骄傲"
s=re.sub(r"(.{16})","\\1\n",s)
print(s)








