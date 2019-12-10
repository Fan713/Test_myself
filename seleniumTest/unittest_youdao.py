#coding=utf-8
import unittest, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTest(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"
    
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()       
        driver.find_element_by_id("translateContent").send_keys(u"词典")
        driver.find_element_by_id('translateContent').send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        title = driver.title
        print(title)
#         self.assertEqual(title,u"webdriver - 有道搜索")


    def tearDown(self):
        self.driver.close()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()