#!/usr/bin/env python
#coding:utf-8
import csv
import xlrd
from selenium import webdriver
import unittest
import pandas as pd
import time
path=r'case.csv'

def csvdata(path,a,b):    
    with open(path) as csvfile:
        rows=csv.reader(csvfile)           
        return(list(rows)[a][b])
            
def writecsv(path,list):
    out=open(path,'w',newline='')
    csv_writer = csv.writer(out, dialect='excel')
    csv_writer.writerow(list)
   
        

class web(object):
    def __init__(self,url) :
        self.driver = webdriver.Chrome()
#         self.url=url
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
        
    def connect(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def test_input(self,text):        
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(text)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
#         title = driver.title
#         self.assertEqual(title,u"unittest_百度搜索")
    
    def test_close(self):
        self.close()
        self.quit()
        
if __name__=="__main__":
#     print(csvdata(path,1,1))   
#     url=csvdata(path, 1, 2)
#     print(url)
    li=[]
    totalrows = len(open(path).readlines())     
# #     print(totalrows)
    for a in range(totalrows):
        ur=csvdata(path, a, 2)
        print(type(ur))
        li.append(ur)
    print(li)
#     for i in len(li):
        
#         text=csvdata(path,a+1,2)
#         print(url,text)
#         baidu=web(url)
#         baidu.connect()
#         baidu.test_input(text)
#     data=pd.read_csv(path)
#     print(data)    
