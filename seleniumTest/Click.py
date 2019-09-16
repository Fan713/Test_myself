# -*-encoding:utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import readCsv
class clickConnect(object):
    def __init__(self,url):
#         self.driver=webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver=webdriver.Chrome()
        self.url=url
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
        self.driver.find_element_by_id('TANGRAM__PSP_4__submit').submit()
        self.driver.implicitly_wait(30)

    def right_click(self,textname):        
        right_click=self.driver.find_element_by_link_text(textname)
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).context_click(right_click).perform()
    
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