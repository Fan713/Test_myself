#! usr/bin/env python
#coding=utf-8
from _operator import itemgetter

# list=[1,3,34,5,6,7,100,-3]
# list2=['aa','BB','zz','CC']

# list.sort(reverse=True)
# print(list)

# print(sorted(list2))
# print(sorted('aa BB cc ZZ'.split(),key=str.lower))

#利用sort排序，第二个元素排序
# random=[(2,3),(4,-8),(23,100)]
# def takeSecond(elem):
#     return elem[1]
# random.sort(key=takeSecond,reverse=True)
# print(random)


#对多维列表排序
student=[('john','A',15),('jane','B',12),('dave','B',10)]
print(sorted(student,key=lambda student:student[2]))     #按照年龄排序
print(student)

print(sorted(student,key=itemgetter(2)))         #按照年龄排序







