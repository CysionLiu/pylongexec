class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, na):
        self.__name = na
if __name__ == '__main__':
    p=Person('Jack',13)
    print(p.name)
    p.address='Beijing'
    print(p.address)
    for k,v in p.__dict__.items():
        print(k,'=',v)