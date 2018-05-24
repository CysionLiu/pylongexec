import ret
import pandas

# coding=utf-8
import xml.dom.minidom

L = []
for i in range(3):
    path = '../static/string' + str(i) + '.xml'
    # 打开xml文档
    dom = xml.dom.minidom.parse(path)
    # 得到文档元素对象
    root = dom.documentElement
    cc = dom.getElementsByTagName('string')
    for c in cc:
        L.append(c.firstChild.data)

        # print(len(L))
        # for l in L:
        # print(l)
# print("div---")
s = set(L)
# print(len(s))
# for tmp in s:
#     print(tmp)


with open('../static/keywords', encoding='utf-8') as f:
    result = f.read()
    Lios = result.split('\n')
s_ios = set(Lios)

s = s | s_ios

L = list(s)
L2 = []
for i in range(len(L)):
    L2.append(str(i))
Lios = []
df = pandas.DataFrame(L, index=L2, columns=['中文'])
print(df)
df.to_excel('e:/tmp.xlsx')
