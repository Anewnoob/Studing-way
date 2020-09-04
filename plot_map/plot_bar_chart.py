
"""Ablation Study"""
import matplotlib.pyplot as plt
name_list = ['RMSE','MAE','MAPE(%)']
#DGS-P1
DeepHydro = [144,106,41]
DeepHydro_NF = [149,109,43]
DeepHydro_RNN = [155,112,46]
DeepHydro_ne = [183,127,54]
LatentODE = [190,134,58.1]
#PDS-P1
# DeepHydro = [35,26,17]
# DeepHydro_ne = [46,31,19]
# DeepHydro_NF = [37,28,17.6]
# DeepHydro_RNN = [38,30,18]
# LatentODE = [49,33,20]
x = list(range(len(name_list)))
total_width, n =2, 10
#width = total_width / n
width = 0.15
plt.figure(figsize=(8,6), dpi=200)

plt.bar(x, LatentODE, width=width, label='LatentODE', fc = 'slateblue')
for a,b in zip(x, LatentODE):
 plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)
for i in range(len(x)):
    x[i] = x[i] + width

plt.bar(x, DeepHydro_ne, width=width, label='DeepHydro-NE', fc = 'b')
for a,b in zip(x, DeepHydro_ne):
 plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)
for i in range(len(x)):
    x[i] = x[i] + width
    
plt.bar(x, DeepHydro_RNN, width=width, label='DeepHydro-RNN', fc = 'r',tick_label = name_list)
for a,b in zip(x, DeepHydro_RNN):
 plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)
for i in range(len(x)):
    x[i] = x[i] + width
    
plt.bar(x, DeepHydro_NF, width=width, label='DeepHydro-NF',fc = 'k')
for a,b in zip(x, DeepHydro_NF):
 plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)
for i in range(len(x)):
    x[i] = x[i] + width

plt.bar(x, DeepHydro, width=width, label="DeepHydro", fc = 'y')
for a,b in zip(x, DeepHydro):
 plt.text(a, b, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)

ax = plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.yticks(fontsize=20)
plt.tick_params(labelsize=20)
# plt.xticks([])
#plt.yticks([])
import numpy as np
tick_label=['RMSE','MAE','MAPE(%)']
#plt.xticks(np.arange(len(name_list))+width/3,tick_label)#显示x坐标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置
plt.legend(fontsize=14,markerfirst = True)
plt.show()



"""Factor impact"""
import matplotlib.pyplot as plt

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
name_list = ['Outflow','Water level','Temporal','Precipitation','Temperature','Electricity price']
name_list2 = ['Water level','Temporal','Precipitation','Temperature','Electricity price']
#SXG-p1
value = [5.02,2.19,1.43,1.11,0.98,0.78]

#PBG- P2
value2 = [2.24,1.56,1.04,0.86,0.72]

# c = ["slateblue","b",'r','k','y',"g"]
c = ["navy",'royalblue','cornflowerblue','slateblue',"blueviolet","indigo"]
c2 = ['royalblue','cornflowerblue','slateblue',"blueviolet","indigo"]

# Plot Bars
plt.figure(figsize=(8, 6), dpi=300)
for i, val in enumerate(value2):
    plt.bar(i + 1, val, color=c2[i], width=0.5, label=name_list2[i])  # label=xticklabels[i]
    plt.text(i + 1, val, round(val, 1), horizontalalignment='center', verticalalignment='bottom', ha='center',
             fontdict={'fontweight': 300, 'size': 20})
# Decoration
plt.gca().set_xticks(range(1, len(name_list) + 1))
#plt.gca().set_xticklabels(xticklabels, rotation=20, horizontalalignment='center', fontsize=20)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.ylabel('Improvement (%)', fontdict={'fontweight': 300, 'size': 20}, )
#plt.ylim(0, 6)
plt.ylim(0, 3)
plt.legend(fontsize=14,markerfirst = True)
plt.show()


"""Horizon_error_comparison"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

import matplotlib
import random
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False

baselines = ['SVR', 'Bi-GRU', 'GRU-VAE', 'LatentODE', 'FlowODE']
baselines.reverse()

# 装载随机数据。
RMSE_hour = [232.8,200.6,197.8,195.1,184.7]
RMSE_day = [293.6,249.4,245.8,244.1,235.9]
RMSE_week = [335.3,285.9,278.6,275.4,267.1]

MAPE_hour = [63.6,51.0,50.1,49.8,46.6]
MAPE_day = [67.7,54.9,53.7,53.1,49.2]
MAPE_week = [77.5,68.2,66.8,66.1,59.4]
RMSE_hour.reverse()
RMSE_day.reverse()
RMSE_week.reverse()
MAPE_hour.reverse()
MAPE_day.reverse()
MAPE_week.reverse()

# 绘图。
# plt.figure(figsize=(8,6), dpi=200)
fig, ax = plt.subplots(figsize=(8,8), dpi=300)
b = ax.barh(range(len(baselines)), MAPE_hour, color='slateblue')  #slateblue  royalblue
#plt.xlim(150,250)
#plt.xlim(200,300)
#plt.xlim(250,350)
plt.xlim(40,65)
#plt.xlim(45,70)
#plt.xlim(55,80)
# 为横向水平的柱图右侧添加数据标签。
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
            w+"%", ha='left', va='center',fontsize='20')  #TODO  %

# 设置Y轴纵坐标上的刻度线标签。
ax.set_yticks(range(len(baselines)))
ax.set_yticklabels(baselines,fontsize='20')

#plt.title('RMSE (After an hour)', loc='center', fontsize='20')
#plt.title('RMSE (After a day)', loc='center', fontsize='20')
#plt.title('RMSE (After a week)', loc='center', fontsize='20')

plt.title('MAPE (After an hour)', loc='center', fontsize='20')
#plt.title('MAPE (After a day)', loc='center', fontsize='20')
#plt.title('MAPE (After a week)', loc='center', fontsize='20')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)


# 不要X横坐标上的label标签。
plt.xticks(())
plt.show()

