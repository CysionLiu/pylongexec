import os
import shutil

# os.makedirs(r'e:\PythonTest\test2')
# 创建10个文件
# for i in range(10):
#     os.make
# dirs(r'e:\PythonTest\test\temp%d' % i)
# open('e:\\PythonTest\\test\\ahah3.txt','w')
import time

div = '+'
divf = '-'


def getdirs(path):
    global div, divf
    for (tdir, tsubdir, files) in os.walk(path):
        print(div, '%s' % tdir)
        div += '+'
        for f in files:
            print(divf, os.path.join(tdir, f))
        divf += '-'


def getdirs2(path, level=0):
    div = ''
    divf = ''
    for i in range(level):
        div += '++'
        divf += '---'
    if os.path.isdir(path):
        print(div, path)
        level += 1
        files = os.listdir(path)
        for f in files:
            getdirs2(path + '\\' + f, level)
            # print(time.ctime(os.path.getatime(path)))
    else:
        print(divf, path)

getdirs2('e:\\PythonTest\\test')

# 把目录树拷贝到另一个目录底下，自动创建新目录
# shutil.copytree('e:\\PythonTest\\test','e:\\PythonTest\\test2')