# coding=utf-8
import csv
import os

if __name__ == '__main__':
    s1 = 'python file'
    with open('text1', 'r') as f:
        print(f.read())
    s2='你好,python'
    # path2 = 'byte.dat'
    # if not os.path.isfile(path2):
    #     with open(path2,'xb') as f2:
    #         f2.write(s2.encode("utf8"))
    # else:
    #     with open(path2,'wb') as f2:
    #         f2.write(s2.encode("gbk"))
    # with open(path2,'rb') as f3:
    #     r=f3.read().decode("gbk")
    #     print(r)

    header=['学号','姓名','年龄']
    rows=[('100','Jack','12'),('101','Lily','16')]
    with open('te.csv','w') as fc:
        fcsv = csv.writer(fc)
        fcsv.writerow(header)
        fcsv.writerows(rows)

