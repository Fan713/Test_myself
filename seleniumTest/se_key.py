#!/usr/bin/env python
#coding:utf-8
# import csv
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import xlwt
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy 
import pandas as pd
def writeRes(row,res):
    workbook=xlwt.Workbook(encoding='ascii')
    report='case.xls'
    rb=open_workbook(report)
    wb=copy(rb)
    sheet=wb.get_sheet(0)
    sheet.write(row,4,res)
    wb.save(report)
    
class web(object):
    def __init__(self):
        self.browser = webdriver.Chrome()

    def pause(self,num):
        time.sleep(num)
    def open(self,url):
        self.browser.get(url)
    def verify(self):
        pass
    def input(self,xpath,value):
        input_=self.browser.find_element_by_id(xpath)
        
        element = WebDriverWait(self.browser,5,0.5).until(lambda browser : input_.is_displayed())
        input_.send_keys(value)
        self.browser.implicitly_wait(10)
        time.sleep(2)
    def click_by_id(self,xpath):
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id(xpath).click()
            
    def click_by_link(self,xpth):
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_link_text(xpath).click()
#             sel=self.browser.find_element_by_id('nr')
#             Select(sel).select_by_value('10')
#             right_click =self.browser.find_element_by_link_text("����")
#             ActionChains(self.browser).context_click(right_click).perform()
#             ActionChains(self.browser).move_to_element(right_click).perform()

#         finally:    
#             pass
#             self.browser.quit()
    def cookie(self,url):
        self.browser.get(url)
        cookies=self.browser.get_cookies()
        print(cookies)
    def quit(self):
        self.browser.quit()
if __name__=='__main__':
    df=pd.read_excel('case.xls')
    r=web()
    for i in range(len(df)):
        op=df.iloc[i][1]
        print('op:',op)
        if str(df.iloc[i][2]) != 'nan':
            xpath=df.iloc[i][2]
            if str(df.iloc[i][3]) !='nan':
                val=df.iloc[i][3]
                s="r.%s('%s','%s')"%(op,xpath,val)
            else:
                s="r.%s('%s')"%(op,xpath)
        else:
            if str(df.iloc[i][3]) != 'nan':
                val=df.iloc[i][3]
                s="r.%s('%s')"%(op,val)
            else:
                s="r.%s()"%op
        print(s)
        try:
            eval(s)
            writeRes(i+1,u'测试通过')
        except:
            pass
            writeRes(i+1, u'测试失败')
