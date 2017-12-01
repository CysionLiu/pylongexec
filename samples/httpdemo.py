import urllib.request

req = urllib.request
with req.urlopen("http://www.baidu.com") as f:
    print(f.read(2000).decode('utf-8'))