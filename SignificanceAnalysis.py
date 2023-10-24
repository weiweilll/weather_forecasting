import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# filepath = 'D:\！Dolinnn\\research\graduate two up\虚仿\显著性分析\显著性分析.xlsx'
# file = pd.read_excel(filepath, sheet_name='FMC')
#
# row = file.shape[0]
# FMC1 = np.zeros(row)
# FMC2 = np.zeros(row)
# for i in range(row):
#     FMC1[i] = file.loc[i,0]
#     FMC2[i] = file.loc[i][1]
# print(FMC1)
#
# # 计算显著性分析的P值，P值小于0.005，则有显著性
# res = ttest_ind(FMC1, FMC2).pvalue
# print(res)

# 各指标具体参数值
FMC_m1 = 150
FMC_s1 = 50
FMC_m2 = 270
FMC_s2 = 55

DFMC_m1 = 90
DFMC_s1 = 20
DFMC_m2 = 150
DFMC_s2 = 25

LAI_m1 = 3.2
LAI_s1 = 1
LAI_m2 = 5.5
LAI_s2 = 1.15

Ele_m1 = 2000
Ele_s1 = 500
Ele_m2 = 3000
Ele_s2 = 550

slope_m1 = 20
slope_s1 = 5
slope_m2 = 25
slope_s2 = 5

aspect_m1 = 140
aspect_s1 = 40
aspect_m2 = 220
aspect_s2 = 35

wind_m1 = 5
wind_s1 = 0.8
wind_m2 = 3
wind_s2 = 1

tem_m1 = 286
tem_s1 = 5
tem_m2 = 285
tem_s2 = 5

pre_m1 = 0.2
pre_s1 = 0.05
pre_m2 = 0.35
pre_s2 = 0.04

rh_m1 = 40
rh_s1 = 5
rh_m2 = 60
rh_s2 = 6

m1 = slope_m1
s1 = slope_s1
m2 = slope_m2
s2 = slope_s2
tap = '坡度'
unit = ' (°)'

# 绘制正态分布曲线
x1 = np.linspace(m1 - 3 * s1, m1 + 3 * s1, 100)
y1 = 10000 * (1 / (s1 * np.sqrt(2 * np.pi))) * np.exp(-(x1 - m1) ** 2 / (2 * s1 ** 2)) + 88
x2 = np.linspace(m2 - 3 * s2, m2 + 3 * s2, 100)
y2 = 10000 * (1 / (s2 * np.sqrt(2 * np.pi))) * np.exp(-(x2 - m2) ** 2 / (2 * s2 ** 2)) + 52

# plt.figure(figsize=(10,10))

# 用分幅进行曲线绘制
fig, ax = plt.subplots()
ax.plot(x1, y1, color='red', label='火点')
ax.plot(x2, y2, color='blue', label='非火点')
# ax.axis('equal') # 使X和Y间距相等
ax.tick_params(labelsize=20)
plt.text(0.03, 0.92, '显著性系数＝0.001', fontsize=15, transform=ax.transAxes)  # 以左下角为（0，0）坐标添加文字
leg = ax.legend()  # 绘制图例

# 定义横纵坐标范围
X2 = np.linspace(0, 50, 6)
Y2 = np.linspace(0, 1000, 6)
plt.xticks(X2)
plt.yticks(Y2)

# 定义横纵坐标内容及标题
plt.xlabel(tap + unit, fontsize=25)
plt.ylabel('数量', fontsize=25)
plt.title(tap + '显著性分析', fontsize=28)

# 保存图片
savefile = 'D:\！Dolinnn\\research\graduate two up\虚仿\显著性分析\\'
plt.savefig(savefile + tap + '显著性分析.png', bbox_inches='tight', dpi=300)
plt.show()
