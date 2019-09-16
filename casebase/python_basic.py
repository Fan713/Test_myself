#! usr/bin/env python
#coding=utf-8
################################################################################
#while 循环
# num=1
# while num <=10:
#     print(num)
#     num+=1
################################################################################

#for 循环
# for i in range(1,12):
#     print(i)
    
################################################################################

#dictionary字典 同时输出多个元素
# dictionary_tk={'name':'leono','nicname':'lo','nationality':'CHINA','age':26}
# for key,value in dictionary_tk.items():
#     print('My %s is %s' %(key,value))

###############################################################################

#类、对象
class v:
    def __init__(self,number,type,name,age):
        self.number=number
        self.type=type
        self.name=name
        self.age=age
    def number(self):
#         return self.number
        print('yoyoyyo')

car=v(4,'cy','leo',4)
print(car)













