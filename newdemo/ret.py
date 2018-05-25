import re,urllib
from urllib import request


def f1():
    s='<book>Python</book>'
    ll=re.findall('<.+?>', s)
    print(ll)

def f2():
    s="jglsjr049u0fw3rw3^j4#%#$%^#%rjwflsf0-203i4rwlf!jw2#$@#$@4"
    r=re.compile(r"j\w{1,8}\d")
    print(r.findall(s))

def f3(url):
    reg=re.compile(r"http\w?://.*\"")
    with request.urlopen(url) as req:
        result=req.read().decode()
        print(result)
        for u in reg.findall(result):
            print(u)
        pass
if __name__ == '__main__':
    f1()
    f2()
    f3("https://github.com/features")
    pass