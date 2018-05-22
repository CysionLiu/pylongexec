import os
import random
print('t1执行开始------')
i=9
print(i)
def plus(a,b,c):
    return a+b+c;
def a():
    for i in range(10):
        print(i,end=",")

print(random.choice(range(19)))
print(random.Random().choice(range(129)))
def b(f):
    f()
print(bin(100))
print(bin(0x8))
print(hex(100))

print(pow(3,5))
print(random.randint(3,10))

s=['v','p','s','e','o']
print(s[2])
print(s[1:3])
print(s[1:-1])
print(s[1:4])
print('---------')
ss='helloworld'
print(sorted(ss))


for i in [x **2 for x in range(10) if x%2==0]:
    print(i,end=",")
print(os.linesep)
stack = list()
stack.append('java')
stack.append('android')
stack.append('php')
stack.append('javascript')
stack.append('c#')
stack.append('python')
print(stack,end=', ')
print(os.linesep)
stack.pop()
stack.pop()
stack.pop()
print(stack,end=", ")
print('\n')
print(str.upper(ss))

s1 = 'Python语言'
b1 = s1.encode('utf8')
b2 = s1.encode('gbk')
print(b1)
print(b2)
s11 = b1.decode('utf8')
s12 = b2.decode('gbk')
print(s11)
print(s12)
print(os.linesep)
d1={'name':'Jack','age':12}
d1['address']='Beijing'
del d1['age']
print(d1)
for k,v in d1.items():
    print(k+'='+v)
print('address' in d1)
d2=dict(name='Lily',age=13)
print(d2)

ll=[1,2,3]
sc={1,2,3,4}
print(type(ll))
print(type(sc))
print(type(d1))

print('\nt1执行结束###------')
