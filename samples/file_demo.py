# 普通文本读写
# with open('../static/hello', 'r', encoding='utf-8') as f:
#     print(f.read())
# with open('../static/hello', 'a', encoding='utf-8') as f:
#     for i in range(10):
#         f.write('\npython' + str(i))
#     f.flush()
# with open('../static/hello', 'r+', encoding='utf-8') as f:
#     f.seek(20)
#     print(f.read())

import csv;


# csv文件读写
# def readcsv1(filepath):
#     with open(filepath, newline='',encoding='utf-8') as f:
#         f_csv = csv.reader(f)
#         headers = next(f_csv)
#         print(headers)
#         for row in f_csv:
#             print(row)
#
#
# if __name__ == '__main__':
#     readcsv1('../static/scores.csv')

def writecsv(filepath):
    header = [' 学号', '姓名', '性别', '班级', '语文', '数学', '英语']
    rows = [(' 101531', '董永', '男', '三班', '55', '74', '79'),
            (' 101535', '朱玉萍', '女', '三班', '72', '76', '72')]
    with open(filepath, 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(rows)


# if __name__ == '__main__':
    # writecsv('../static/scores.csv')
