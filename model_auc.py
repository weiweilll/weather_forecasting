from itertools import *
import xlwt

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = ['FMC  ', 'DFMC  ', 'LAI  ', '海拔  ', '坡度  ', '坡向  ', '风速  ', '温度  ', '降雨量  ', '空气湿度  ']
b1 = [''] * 210
b2 = [''] * 120
b3 = [''] * 10
i = 0
j = 0
k = 0

# 计算组合数
for element in combinations(s, 6):  # （C（6，10））
    a = c[element[0]] + c[element[1]] + c[element[2]] + c[element[3]] + c[element[4]] + c[element[5]]
    b1[i] = a
    i = i +1

for element in combinations(s, 3):
    a2 = c[element[0]] + c[element[1]] + c[element[2]]
    b2[j] = a2
    j = j +1

for element in combinations(s, 9):
    a3 = c[element[0]] + c[element[1]] + c[element[2]] + c[element[3]] + c[element[4]] + c[element[5]] + c[element[6]] + c[element[7]] + c[element[8]]
    b3[k] = a3
    k = k +1

filepath = 'D:\！Dolinnn\\research\graduate two up\虚仿\模型对应\模型.xls'

# 新建excel和sheet并写入
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('model',cell_overwrite_ok=True)
for m in range(210):
    sheet.write(m,0,b1[m])

for n in range(120):
    sheet.write(n,1,b2[n])

for l in range(10):
    sheet.write(l, 2, b3[l])

book.save(filepath)