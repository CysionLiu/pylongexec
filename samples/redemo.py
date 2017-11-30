import re

import time
from urllib import request

from samples.constants import DIV

t1 = re.findall("((\d{1,3}\.){3}\d{1,3})", 'ip地址为172.13.168.23')
print(t1)
m = re.search(r"(?P<Area>\d+)(?P<divd>-)(?P<No>\d+)", "tel is 021-89664546")
print(m.groupdict())
t2 = re.findall("\d+-\d+", "tel is 90-98788")
print(t2)
s1 = 'To be or not to be'
print(re.match('to', s1))
print(re.search('to', s1))
for s in re.findall('to', s1, re.IGNORECASE):
    print(s)
print(DIV)
# 正则表达式对象

re1 = re.compile("https?://www\..*\.{1}\w{2,8}")
print(re1.findall("http://www.baidu.com"))
print(re1.findall("http://www.basefsefom"))
print(re1.findall("https://www.basefsefom.net"))
print(re1.findall("ftp://sffe"))
print(DIV)

# 非普通字符分割
print(re.split('\W+', "good,better*best"))


# 字符串查找，url
def url_extract(homepage):
    re1 = re.compile(r'href="(.+?)"')
    print(time.ctime())
    result = request.urlopen(homepage)
    webcon = result.read().decode()
    print(time.ctime())
    re2 = re1.finditer(webcon)
    for r in re2:
        print(r.group(1))


if __name__ == "__main__":
    hp = "http://www.baidu.com"
    url_extract(hp)
