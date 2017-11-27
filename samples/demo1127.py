from collections import namedtuple

# 类型和对象id
print(type(25))
print(id(12))

# 元组
t = tuple(range(2, 8))
print(t)
t2 = 1, 2, 3
print(t2)
# 可变和不可变
x = y = [1, 2, 3]
print(id(x))
print(id(y))
x.append(4)
print(id(x))
print(y)
a, b = 3, 9
# 命名元组，创建新类
Cat = namedtuple("Cat", ["name", "age"])
cat = Cat('MiMi', 6)
print(cat)
print(type(cat))
print(type(Cat))
