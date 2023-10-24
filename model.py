from itertools import *
import xlwt
import random

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = ['FMC  ', 'DFMC  ', 'LAI  ', 'Elevation  ', 'Slope  ', 'Aspect  ', 'WindSpeed  ', 'Temperature  ', 'Rainfall  ',
     'Humidity  ']
b1 = [''] * 210
b2 = [''] * 120
b3 = [''] * 10
i = 0
j = 0
k = 0

# 计算组合数
for element in combinations(s, 6):  # （C（6，10））
    # 生成随机小数
    q1 = random.random() / 10
    q2 = random.random() / 10
    q3 = random.random() / 10
    q4 = random.random() / 10
    q5 = random.random() / 10
    q6 = random.random() / 10
    q7 = random.random() * 100
    a = 'z = ' + str(q1) + c[element[0]] + '+  ' + str(q2) + c[element[1]] + '+  ' + str(q3) + c[element[2]] + '+  ' + str(q4) + \
        c[element[3]] + '+  ' + str(q5) + c[element[4]] + '+  ' + str(q6) + c[element[5]] + '+  ' + str(q7)
    b1[i] = a
    i = i + 1

for element in combinations(s, 3):
    w1 = random.random() / 10
    w2 = random.random() / 10
    w3 = random.random() / 10
    w4 = random.random() * 100
    a2 = 'z = ' + str(w1) + c[element[0]] + '+  ' + str(w2) + c[element[1]] + '+  ' + str(w3) + c[element[2]] + '+  ' + str(w4)
    b2[j] = a2
    j = j + 1

for element in combinations(s, 9):
    e1 = random.random() / 10
    e2 = random.random() / 10
    e3 = random.random() / 10
    e4 = random.random() / 10
    e5 = random.random() / 10
    e6 = random.random() / 10
    e7 = random.random() / 10
    e8 = random.random() / 10
    e9 = random.random() / 10
    e10 = random.random() * 100
    a3 = 'z = ' + str(e1) + c[element[0]] + '+  ' + str(e2) + c[element[1]] + '+  ' + str(e3) + c[element[2]] + '+  ' + \
         str(e4) + c[element[3]] + '+  ' + str(e5) + c[element[4]] + '+  ' + str(e6) + c[element[5]] + '+  ' + \
         str(e7) + c[element[6]] + '+  ' + str(e8) + c[element[7]] + '+  ' + str(e9) + c[element[8]] + '+  ' + str(e10)
    b3[k] = a3
    k = k + 1

filepath = 'D:\！Dolinnn\\research\graduate two up\虚仿\模型对应\模型2.xls'

# 新建excel和sheet并写入
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('model', cell_overwrite_ok=True)
for m in range(210):
    sheet.write(m, 0, b1[m])

for n in range(120):
    sheet.write(n, 1, b2[n])

for l in range(10):
    sheet.write(l, 2, b3[l])

book.save(filepath)
