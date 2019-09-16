class car(object):
    def __init__(self,name,size):
        self.name=name
        self.size=size
    def value(self):
#         list=['study','working']           
        name=self.name
        size=self.size
        print(name,size)
class person(car):
    def v(self):
        print('234')
            
if __name__=='__main__':
    name='we'
    size='23'
#     d=car(name,size)
#     d.value()
    t=person(name,size)
    t.value()