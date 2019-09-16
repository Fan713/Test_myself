#! /usr/bin/env python
#coding=utf-8

from xml.etree.ElementTree import ElementTree,Element
import lxml.html
etree=lxml.html.etree

class lxmlReaderModify(object):
    def __init__(self,strxml):
        parser = etree.HTMLParser()
        if type(strxml)==str:
            self.xml=etree.XML(strxml,parser)    #将string转化为python对象
        else:
            self.xml=etree.parse(strxml,parser)   #导入并解析xml文件
    
#         self.xml=ElementTree()
#         self.xml.parse(strxml)
    #获取标签对之间的文本及标签的属性的值
    def getTabNobeVaule(self,xpathName):
        value=self.xml.xpath(xpathName)
        return value
    
    #修改标签对之间的文本
    def modifNodeText(self,xpathDir,value,fileUrl):
        node=self.xml.find(xpathDir)  #定位元素
        node.text=value               #修改节点的文本内容
        self.xml.write(open(fileUrl,'w'),pretty_print=True)    #将修改之后的内容写入文件中
        
        
    #修改标签属性的值
    def modifyTabQualityValue(self,xpathDir,quality,value,fileUrl):
        node=self.xml.find(xpathDir)    #定位元素
        node.set(quality,value)
        self.xml.write(open(fileUrl,'w'),pretty_print=True)    #将修改之后的内容写入文件中

if __name__=='__main__':
    
#读取字符串方式，python2、python3都适用
    strl='''
            <?xml version="1.0" encoding="utf-8"?>
            <catalog>
            <maxid>4</maxid>
            <login username="pytest" passwd="123456">
            <caption>Python</caption>
            <item id="4">
            <caption>test</caption>
            </item>
            </login>
            <item id="2">
            <caption>Zope</caption>
            </item>
            </catalog>
        '''
    print(type(strl))
    strl=strl.replace('GBK', 'utf-8')
    dom=lxmlReaderModify(strl)
    print(dom.getTabNobeVaule('//login/@username'))    #获取标签中属性的值
    print(dom.getTabNobeVaule('//maxid/text()'))       #获取标签对中间的文本

#读取xml文件，以下方式不适合python3,适用于python2
    file=open(r'C:\Users\KLJS151\QuiKLab3\config.xml','r',encoding='utf-8')
    dom=lxmlReaderModify(file)
    fileUrl = r"C:\Users\KLJS151\QuiKLab3\config.xml"    
    dom.modifNodeText("//config/useDatabase", '7', fileUrl)
    dom.modifyTabQualityValue("//config/useDatabase", 'useDatabase', '7', fileUrl)
    print(dom.getTabNobeVaule('//config/targetMode/text()'))
    
    