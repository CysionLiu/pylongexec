import re


def f1():
    s='<book>Python</book>'
    ll=re.findall('<.+?>', s)
    print(ll)

def f2():
    s="jglsjr049u0fw3rw3^j4#%#$%^#%rjwflsf0-203i4rwlf!jw2#$@#$@4"
    r=re.compile(r"j\w{1,8}\d")
    print(r.findall(s))
if __name__ == '__main__':
    f1()
    f2()
    pass