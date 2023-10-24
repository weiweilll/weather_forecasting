import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 读取Excel
filepath = 'D:\！Dolinnn\\research\graduate two up\虚仿\相关性分析\相关性分析.xlsx'
file = pd.read_excel(filepath, sheet_name='try_rh2')

# 画图正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel数据
row = file.shape[0]
FMC = np.zeros(row)
DFMC = np.zeros(row)
LAI = np.zeros(row)
dem = np.zeros(row)
slope = np.zeros(row)
aspect = np.zeros(row)
wind = np.zeros(row)
tem = np.zeros(row)
pre = np.zeros(row)
rh = np.zeros(row)
for i in range(row):
    FMC[i] = file.loc[i][0]
    DFMC[i] = file.loc[i][1]
    LAI[i] = file.loc[i][2]
    dem[i] = file.loc[i][3]
    slope[i] = file.loc[i][4]
    aspect[i] = file.loc[i][5]
    wind[i] = file.loc[i][6]
    tem[i] = file.loc[i][7]
    pre[i] = file.loc[i][8]
    rh[i] = file.loc[i][9]
x = rh
x1 = '空气湿度'
x11 = '空气湿度 (%)'
y = pre
y1 = '降雨'
y11 = '降雨 (mm)'
# plt.scatter(x,y)
#
# plt.show()


plt.figure(figsize=(10, 10))

# 获取数据范围
cxmax = max(x)
cxmin = min(x)
cymax = max(y)
cymin = min(y)

# 对散点数据进行线性拟合 获取斜率 截距 R2
slope2, intercept, r_value, p_value, std_err = stats.linregress(x, y)  # 斜率 截距 R2

# 画拟合线
X1 = np.arange(0, 360, 0.1)
Y1 = np.array([intercept + slope2 * x for x in X1])
plt.plot(X1, Y1, color='black')

# 统一 x y 轴范围
plt.xlim(cxmin, cxmax)
plt.ylim(cymin, cymax)

# 统一 x y 轴坐标
X2 = np.linspace(0, 100, 6)
Y2 = np.linspace(0, 0.02, 5)
plt.xticks(X2)
plt.yticks(Y2)

# #画建1：1 标                                                                                                                 准线
# plt.plot(range(int(cmax*1.1)),color='black')

# 画散点图
plt.scatter(x, y)

# 写入公式以及R2
plt.text(cxmax * 0.06, cymax * 1.19, 'R$^2$=%s' % (np.around(r_value ** 2, 2)), fontsize=32)
R2 = np.around(r_value ** 2, 2)
# plt.text(cmax*0.1,cmax*0.8,'y=%s*x+%s'%(np.around(slope,2),np.around(intercept,2)),fontsize=15)

# 写入坐标轴label
plt.xlabel(x11, fontproperties='KaiTi', fontsize=40)
plt.ylabel(y11, fontproperties='KaiTi', fontsize=40)

# 设置刻度大小
plt.tick_params(labelsize=35)

print(R2)
plt.title(x1 + '与' + y1 + '相关性分析', fontsize=45)

# #保存路径 格式 将边缘空白部分去除，设置分辨率为300
savefile = 'D:\！Dolinnn\\research\graduate two up\虚仿\相关性分析\\'
plt.savefig(savefile + x1 + '与' + y1 + '相关性分析.png', bbox_inches='tight', dpi=300)

plt.show()
