#python中的魔法方法指的是python中类自带的内置语法
#如__init__(),__str__(self)
#包括用算符重载
#即通过自行实现__or__的方法即可

class People(object):#可以不写object会默认继承object
    def __init__(self, name):
        self.name = name
    def __or__(self, other):
        return Peoplelist(self,other)
    def __str__(self):
        return self.name#使print(People(a))==self.name


class Peoplelist(object):
    def __init__(self, *args):
        self.peoplelist = []
        for person in args:
            self.peoplelist.append(person)
    def __or__(self, other):
        self.peoplelist.append(other)
        return self
    def run(self):
        for person in self.peoplelist:
            print(person)

if __name__ == "__main__":
    a = People("张胜男")
    b = People("李斯")
    c = People("王麻子")
    d = a | b | c
    d.run()
    print(type(d))
