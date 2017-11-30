from itertools import count, accumulate

from samples.constants import DIV

t = range(10)
t_iter = iter(t)
while True:
    try:
        i = next(t_iter)
        print(i)
    except:
        print('迭代完成')
        break
print(DIV, '迭代器')


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fib()
for f in fib:
    if f < 100:
        print(f, end=',')
    else:
        break

print('')
print(DIV, '生成器')


def fib_g(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


for i in fib_g(12):
    print(i, end=',')
print()
print(DIV, '生成器表达式')
for j in (i * 3 for i in range(10)):
    print(j, end=',')
print('')
print(DIV)


def double(n):
    return n * 2


for i in map(double, range(0, 10, 2)):
    print(i, end=',')
print()
for i in map(lambda x: x * 2, range(6)):
    print(i, end='*')

print()
for i in count(0, 2):
    if i > 30:
        break
    print(i, end=',')
print()

print(list(accumulate(range(11))))


class SubDict(dict):
    def __getitem__(self, item):
        return item
d = SubDict(name='python',age=28)
print(d)
print(d.get('name'))
print(d['name'])
