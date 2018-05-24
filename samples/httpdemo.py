import ret
import urllib.request

req = urllib.request
# with req.urlopen("http://www.baidu.com") as f:
#     print(f.read(2000).decode('utf-8'))
reg = ret.compile('(href="http.*?")')
with req.urlopen("https://github.com/CysionLiu") as f:
    content = f.read().decode('utf-8')
    for s in reg.findall(content):
        print(s)

