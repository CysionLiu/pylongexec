class Person:
    count = 0

    def __init__(self, name, age):
        print('new one')
        Person.count += 1
        self.__name = name
        self.age = age

    def __del__(self):
        Person.count -= 1

    def say_hi(self):
        print('hello, i am ', self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod
    def get_count(cls):
        return Person.count


print('count-', Person.count)
p = Person('张三', 23)
p.say_hi()
print('count-', Person.count)
p2 = Person('李四', 19)
p2.say_hi()
print('count-', Person.get_count())
print(p2.age, p2.name)
p2.name = 'hello'
print(p2.name)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


po = Point(2, 3)
print('po({0},{1})'.format(po.x, po.y))
