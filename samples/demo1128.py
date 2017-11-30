import os
from fractions import Fraction

import math

from samples import tools
from samples.constants import DIV

print(DIV)

print('100以内的奇数的和为', tools.cal_odd_sum(True))
print('100以内的偶数的和为', tools.cal_odd_sum(False))
# 另一种实现方式
amount = 0
for x in [i for i in range(1, 101) if i % 2 == 0]:
    amount += x
print('100以内的偶数的和为', amount)

amount_odd = 0
for x in range(1, 101, 2):
    amount_odd += x
print('100以内的奇数的和为', amount_odd)

print(DIV, '素数校验')

print(tools.judgeSu(13))
print(tools.judgeSu(123))
print(tools.judgeSu(113))

print(DIV, '进制转换')
# 进制转换
print(bin(72))
tbin = bin(23)
print(tbin)
to = int(tbin, 2)
print(to)
print(DIV, '分数练习')
# 分数
ftemp = Fraction('1/3') * Fraction('1/4')
print(ftemp)
print(round(3.1415925))
print(round(3.1415925, 5))
print(sum((1, 2, 3, 4), 90))

print(DIV, 'math函数练习')
print(math.e)
print(math.pi)
te = round(math.e, 3)
tpi = round(math.pi, 3)
print(te)
print(tpi)

print(DIV, '序列')
s = 'abcdefghi'
print(s[0], s[7], s[-1], s[-3])
print(s[1:3], s[:8:2], s[:-3:3])
slice1 = slice(1, len(s) - 1, 2)
print(slice1)
print(s[slice1])
print('abc' + 'xyz' * 3)
print(b'abc')
print(sorted(s[slice1], reverse=True))

print(DIV, '序列拆封')
# 序列拆封
print(list(range(10)))
first, second, *last = range(10)
print(last)
*first, second, third, last = range(10)
print(first)

print(DIV, '元组')
# 元组
t = (1)
print(t)
t = (1,)
print(t)
print(list(range(10)))  # 列表
t = tuple(range(10))  # 元组
print(t)

# 列表解析表达式
print(DIV, '# 列表解析表达式')
print([i ** 3 for i in range(10)])
print([(x, y, x * y) for x in range(1, 4) for y in range(2, 6) if x >= y])
L = list(range(1, 5))
L.pop()
print(L)
L.pop()
print(L)
# 字符串
print(DIV, '字符串')
print(str.isalnum('op90'))
print(str.isdigit('9090'))
s1 = 'hello'
print(s1.isdigit())
print(s1.upper())
print(s1.startswith('h'))
print(s1.partition(','))
s2 = 'hello*world'
print(s2.partition('*'))

print(DIV, '字符串格式化')
print('姓名：%s,年龄:%d' % ('张三', 20))
print(DIV, '字典dict')
d1 = {'a': 'hello', 'b': 'world'}
d2 = dict(c='hello', d='world')
print(d1)
print(d2)
d1['c'] = 'HaHa'
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
print('d' in d1)
print('d' in d2)

print(os.listdir('../static/'))
