import xml.dom.minidom
import xlrd
# 安卓国际化脚本，xml里对应中文信息，excel里是翻译过的，包括英文和日文，调整配置运行后
# 可以生成对应的英文和日文xml;

zh,zh_x,en_x,ja_x = [],[],[],[]

def read_xml(path):
    global zh
    c = 1;
    dom = xml.dom.minidom.parse(path)
    x = dom.getElementsByTagName("string")
    read_excel()
    for s in x:
        for z in zh_x:
            if s.firstChild.data == z:
                i = zh_x.index(z)
                if c==1:
                    s.firstChild.data = en_x[i]
                if c==2:
                    s.firstChild.data = ja_x[i]
    if c == 1:
        f = open('../static/target_en.xml', 'w', encoding="utf-8")
        dom.writexml(f, addindent=' ', newl='', encoding='utf-8')
        f.close()
    if c == 2:
        f2 = open('../static/target_ja.xml', 'w', encoding="utf-8")
        dom.writexml(f2, addindent=' ', newl='', encoding='utf-8')
        f2.close()




def read_excel():
    global zh_x,en_x,ja_x
    workbook = xlrd.open_workbook('../static/inter.xls')
    sheet2 = workbook.sheet_by_name('Sheet1')
    zh_x = sheet2.col_values(0)  # 获取第1列内容
    en_x = sheet2.col_values(1)  # 获取第2列内容
    ja_x = sheet2.col_values(2)  # 获取第3列内容

if __name__ == '__main__':
    read_xml('../static/strings_zh.xml')
