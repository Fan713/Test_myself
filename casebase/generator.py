# gen=(x*x for x in range(5))
# print(gen.__next__())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(gen.__next__())
# print(next(gen))
# for n in gen:
#     print(n)
    
# def odd():
#     n=1
#     while True:
#         yield n
#         n+=2
# odd_num=odd()
# print(odd_num)
# count = 0
# for o in odd_num:
#     if count >=5:break
#     print(o)
#     count+=1

def g1():
    yield 'hello'
    yield 'nonono'
    return 'world'
g=g1()
print(next(g))
# g.close()
print(next(g))
    