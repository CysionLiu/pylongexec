import math

from samples.constants import DIV


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

print(DIV, '衍生类')


class derived(Person):
    def __init__(self, name, age, sid):
        Person.__init__(self, name, age)
        self.sid = sid

    def say_hi(self):
        Person.say_hi(self)
        print('my sid is :', self.sid)


de = derived('Hanmei', 13, 10123)

de.say_hi()
print(DIV)


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self, *p):
        pass


class Circle(Shape):
    def __init__(self, name):
        Shape.__init__(self, name)

    def area(self, *p):
        return p[0] ** 2 * math.pi


class Rect(Shape):
    def __init__(self, name):
        Shape.__init__(self, name)

    def area(self, *p):
        return p[0] * p[1]


cir = Circle('圆')
print(cir.name, '()的面积为', cir.area(1))
re = Rect('矩形')
print(re.name, '的面积为', re.area(3, 4))
print(dir())