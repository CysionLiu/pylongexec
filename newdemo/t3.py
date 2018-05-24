from itertools import count


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def ge():
    for i in (x **3 for x in range(12) if x%3==0):
        print(i,end='&')
    pass
def m(n):
    return n*3

if __name__ == '__main__':
    for i in fib():
        if i < 1000:
            print(i, end=',')
        else:
            break
    print()
    ge()
    print()
    print(list(map(m,list(range(1,30,3)))))
    print(list(filter(lambda x:x%3==0,list(range(3,50,2)))))
    for i in count(1,3):
        if i<100:
            print(i,end=';')
        else:break


