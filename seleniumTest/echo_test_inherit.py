import time
class A():
    def add(self,a,b):
        return a+b
    
class B(A):
    def sub(self,a,b):
        return a-b
count=B()
print(count.add(3,4))

print(time.ctime())