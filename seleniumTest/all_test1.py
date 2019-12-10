#coding=utf-8

from seleniumTest import unittest_baidu,unittest_youdao
import unittest

def caseData():
    testunit=unittest.TestSuite()
    alltestnames=[unittest_baidu.MyTest,unittest_youdao.MyTest]
    print('success read case list')
    for test in alltestnames:
        testunit.addTest(unittest.makeSuite(test))
    runner=unittest.TextTestRunner()
    runner.run(testunit)   
if __name__=="__main__":
   caseData()
    
