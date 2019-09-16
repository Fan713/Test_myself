
import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse(r'C:\Users\KLJS151\Desktop\abc.xml')

#得到文档元素对象
root = dom.documentElement
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)
# bb = root.getElementsByTagName('caption')
# b= bb[2]
# print(b.nodeName)
# 
# bb = root.getElementsByTagName('item')
# b= bb[1]
# print(b.nodeName)


# itemlist=root.getElementsByTagName('login')
# print(itemlist)
# item =itemlist[0]
# print(item)
# un=item.getAttribute('username')
# print(un)
# pd =item.getAttribute('passwd')
# print(pd)
# 
# ii=root.getElementsByTagName('item')
# i1=ii[0]
# i=i1.getAttribute('id')
# print(i)
# 
# i2=ii[1]
# i=i2.getAttribute('id')
# print(i)

#firstChild 属性返回被选节点的第一个节点
#.data表示获取该节点人数据
cc=dom.getElementsByTagName('caption')
c1=cc[0]
print(c1.firstChild.data)

c2=cc[1]
print(c2.firstChild.data)  

c3=cc[2]
print(c3.firstChild.data)











