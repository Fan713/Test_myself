#! /usr/bin/env python
#coding=utf-8

import xml.etree.ElementTree as ET
#     self.path=path
#     self.tree=ET.ElementTree(file=self.path)
#     self.root=self.tree.getroot()
strxml=r'C:\Users\KLJS151\QuiKLab3\config.xml'
updateTree=ET.ElementTree(file=strxml)
root=updateTree.getroot()
sub1=root.find('./mainTarget/port')
print(sub1.text)
for i in root.iter('item'):
    print(i.attrib)
# sub1.set('name','new Name')
# print(type(sub1))
    item_a='item'
    item='port'
    text='name'
    lab_text='woen'
    d=readXml(strxml)
    d.getTabValue(item,0)
    d.item_getAttribute(item_a,1,text)
    d.setTabValue(item,0,lab_text)
       
   # 增加标签
     newEle=ET.Element('newElement')
     newEle.attrib={'name':'newElement','age':'20'}
     newEle.text='This is a new elemnet'
     root.append(newEle)
    #修改标签属性
lists=[1,2,3]
print(type(lists))
print(type(root.iter('workpath')))
print(root.iter('workpath'))
for i in root.iter('item'):
    print(i.tag,i.attrib,i.text)
    for j in i.iter('item'):
        print('修改之前的属性值',j.attrib)
#         print('修改之前的内容',j.text)
        j.attrib={'newname':'25'}
#         j.text='1455451'
        print('修改之后的属性值:',j.attrib)
#         print('修改之后的文本',j.text)
updateTree.write(strxml)
 
#字典
# dc={'a':'we','b':'34'}
# print(dc['a'])
