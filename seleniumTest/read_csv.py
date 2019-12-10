#!/usr/bin/env python
#coding:utf-8

# import csv
# 
# 
# stu1 = ['marry',26]
# stu2 = ['bob',23]
# 
# out = open('1.csv','a', newline='')
# 
# csv_write = csv.writer(out,dialect='excel')
# 
# csv_write.writerow(stu1)
# csv_write.writerow(stu2)
# print ("write over")

import pandas as pd

df=pd.read_excel('case.xls',header = 0)
print(df)
print('len=',len(df))
# df_new = df.set_index(["country"])
# print(df.iloc[0][1])













