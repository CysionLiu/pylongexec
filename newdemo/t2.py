# coding=utf-8
import functools
import time


def fuli(base, n, num):
    if n == 1:
        return base * (1 + 4.0 / 100 / 12) + num;
    return int(fuli(base, n - 1, num) * (4.0 / 100 / 12 + 1) + num)


def ar(a, b, *c, **d):
    total = a + b
    for i in c:
        total = total + i
    for k, v in d.items():
        print(k + '=' + str(v))
    print(total)


def w(f):
    @functools.wraps(f)
    def wrapper(*a):
        start = time.perf_counter()
        f(*a)
        end = time.perf_counter()
        print('运行时间:', end - start)

    return wrapper


def total(n):
    t = 0
    for i in range(n):
        t += i
    print(t)


def fi(n):
    li = []
    i, c = 1, 2
    f1 = f2 = 1
    li.append(f1)
    while i < n:
        f1, f2 = f2, f1 + f2
        li.append(f1)
        i += 1
    return li


def jie(n):
    if n == 0:
        return 1
    return n * jie(n - 1)


def jie2(n):
    i = 1
    m = 1
    while i < n:
        m = m*i
        i += 1
    return m

g='hello'
if __name__ == '__main__':
    s = fuli(0, 90, 22000)
    print(s)
    print(90 * 22000 + 0)
    print('------')
    ar(1, 5, 6, 7, name='Jack', age=12, address='Beijing')
    total(100000)
    print(total.__name__)
    print(fi(10))
    start = time.perf_counter()
    print(jie(100))
    print(time.perf_counter() - start)
    print(globals()['g'])
