import time

from samples.constants import DIV


def find_max(a, b, *c, **d):
    max = a
    if max < b:
        max = b
    for i in c:
        if max < i:
            max = i;
    print('最大值为:', max)
    print('关键词参数为:', d)


find_max(12, 45, 76, 234, 45, 1234, 7532, tname='oop', tage=25)


def out_fun():
    rate = 0.13
    print('outrate is :', rate)

    def inner_fun():
        nonlocal rate
        rate = 0.09
        print('innner rate:', rate)

    inner_fun()
    print('new out fun:', rate)


out_fun()

# 装饰器
print(DIV, '装饰器')


def timeit(f):
    def wrapper(*s):
        print(time.perf_counter())
        f(*s)
        print(time.perf_counter())

    return wrapper


@timeit
def foo(n):
    if type(n) is not int:
        return
    total = 0
    for i in range(n):
        total += i
    print('total:', total)


foo(1000)

print(DIV, '递归')


def jiecheng(n):
    if n == 0:
        return 1
    if n >= 1:
        return jiecheng(n - 1) * n


print(jiecheng(7))

print(DIV, 'lambda')
tf = lambda x, y: x * y
print(tf(2, 6))
