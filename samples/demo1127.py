from collections import namedtuple

from samples import tools

# 类型和对象id

div = '--------------------------------------------'

print(type(25))
print(id(12))

print(div)
# 元组
t = tuple(range(2, 8))
print(t)
t2 = 1, 2, 3
print(t2)
print(div)
# 解包赋值
i, j, k = t2
print(i + j + k)
# 可变和不可变
x = y = [1, 2, 3]
print(id(x))
print(id(y))
x.append(4)
print(id(x))
print(y)
a, b = 3, 9
print(div)
# 命名元组，创建新类
Cat = namedtuple("Cat", ["name", "age"])
cat = Cat('MiMi', 6)
print(cat)
print(type(cat))
print(type(Cat))
print(div)
# 数字类型
# ba = float(input("请输入本金"))
# lv = float(input("请输入利率"))
# be = float(input('请输入年份'))
# amount = ba * (1 + lv / 100) ** be
# print(amount)
print(div)
# 格式化字符串
print(format('1', "^20"))
print(format('121', "^20"))
print(format('12321', '^20'))

# 集合
se = set({1, 2, 3, 11, 12, 23, 110})
print(se)
se.add(10)
print(se)

print(div)


# 函数，都是可调用对象
def f1():
    pass


print(type(f1))
print(id(f1))
print(f1.__name__)

# 导入模块，import是导入模块，通过模块调用方法
print(tools.calSquare(12))
x1, x2 = tools.calX(1, 5, 6)
print(x1, x2)

print(div)
# 选择结构
def remark(mark):
    if mark >= 90:
        return '优秀'
    if mark < 90 & mark >= 80:
        return '良好'
    if mark < 80 & mark > 60:
        return '及格'
    else:
        return '不及格'


print(remark(91))
print(remark(79))

print(div)
print(tools.compare(23,12,43))

print(div)
print(tools.judge(1500))