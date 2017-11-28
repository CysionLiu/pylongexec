from samples import tools
from samples.constants import DIV

print(DIV)

print('100以内的奇数的和为', tools.cal_odd_sum(True))
print('100以内的偶数的和为', tools.cal_odd_sum(False))
# 另一种实现方式
amount = 0
for x in [i for i in range(1, 101) if i % 2 == 0]:
    amount += x
print('100以内的偶数的和为',amount)

amount_odd = 0
for x in range(1, 101, 2):
    amount_odd += x
print('100以内的奇数的和为',amount_odd)

print(DIV)

print(tools.judgeSu(13))
print(tools.judgeSu(123))
print(tools.judgeSu(113))