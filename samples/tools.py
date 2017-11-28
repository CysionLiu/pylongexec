import math


# 计算圆的面积
def calSquare(r):
    return math.pi * r * r;


# 计算一元二次方程的解
''' 
@ author cysionliu
'''


def calX(a, b, c):
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


# 比较大小
def compare(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return a, b, c


# 判断是否为闰年
def judge(y):
    print(y)
    if y % 400 == 0:
        return True
    if (y % 4 == 0) & (y % 100 != 0):
        return True
    else:
        return False


# 计算100以内奇数的和
def cal_odd_sum(is_odd):
    sum = 0
    for i in range(1, 101):
        if ((i % 2 != 0) & is_odd):
            sum += i
        elif ((i % 2 == 0) & (is_odd == False)):
            sum += i
    return sum


# 判断一个数是否为素数
def judgeSu(x):
    if type(x) is not int:
        return False
    k = int(math.sqrt(x))
    for i in range(2, k):
        if (x % i) == 0:
            return False
    return True
