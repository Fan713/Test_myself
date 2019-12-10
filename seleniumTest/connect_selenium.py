# -*-encoding:utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import readCsv


class clickConnect(object):
    def __init__(self,url):
#         self.driver=webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver=webdriver.Chrome()
        self.url=url
    
    #建立连接，打开网址URL
    def connect(self):
#         self.driver=webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

#登录百度网盘        
    def login(self,username,password):
        self.driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').clear()
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').click()
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(username)
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').clear()
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').click()
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys(password)
        self.driver.find_element_by_id('TANGRAM__PSP_4__memberPass').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('TANGRAM__PSP_4__submit').submit()   #提交搜索框内容
        self.driver.implicitly_wait(30)

    #右击操作
    def right_click(self,textname):        
        right_click=self.driver.find_element_by_link_text(textname)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).context_click(right_click).perform()
    
    #键盘操作
    def keys_event(self,id_name,input_name):
        self.driver.find_element_by_id(id_name).send_keys(input_name)   #输入框输入内容
        self.driver.find_element_by_id(id_name).send_keys(Keys.BACK_SPACE)  #删除多输入的一个内容
        self.driver.find_element_by_id(id_name).send_keys(Keys.SPACE)   #输入空格键
        self.driver.find_element_by_id(id_name).send_keys(Keys.CONTROL,'a')  #全选输入框内容
        self.driver.find_element_by_id(id_name).send_keys(Keys.CONTROL,'x')  #剪切输入框内容
        self.driver.find_element_by_id(id_name).send_keys(Keys.CONTROL,'v')  #粘贴内容到输入框
        self.driver.find_element_by_id(id_name).send_keys(Keys.ENTER)    #通过回车键代替点击操作
        
        
    
    
    #关闭
    def close(self):
        self.close()
        self.quit()
        
if __name__=='__main__':
    URL='https://pan.baidu.com/'
    path=r'case.csv'
    usrname=readCsv.csvdata(path, 2, 2)
    password=readCsv.csvdata(path, 3, 2)
    print(usrname,password)
    connect=clickConnect(URL)
    connect.connect()
    connect.login(usrname,password)
    connect.right_click(u'自动化脚本Python___Linux')
    connect.close()