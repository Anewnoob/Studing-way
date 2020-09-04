from matplotlib import pyplot as plt
import pickle
import numpy as np
import os

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42


DATAPATH = os.path.dirname(os.path.abspath(__file__))
target_year = 2017
# Load Data
preprocess_file = DATAPATH+ f'/PDP_{target_year}_data.pkl'
print(preprocess_file)
# DGS_data = {"data": DGS_DG_norm, "LL_data": DGS_flow_norm, "temp": temperature, "date": DGS_DG_T,
#             "E_min": mmn._min, "E_max": mmn._max, "LL_min": ll_mmn._min, "LL_max": ll_mmn._max}
fpkl = open(preprocess_file, 'rb')
data = pickle.load(fpkl)
fpkl.close()

DGS_DG = data['data']
DGS_flow = data['LL_data']
DGS_DG_T = data['date']
LL_mmn = data['LL_mmn']
mmn = data['E_mmn']
temperature  = np.array(data['temp'])
print(temperature.shape,temperature.min(),temperature.max())

start = 24*0
end = 24*7

print(DGS_flow[:,0].shape,DGS_flow[:,0].min(),DGS_flow[:,0].max())
print(DGS_flow[:,2].shape,DGS_flow[:,2].min(),DGS_flow[:,2].max())
print(DGS_flow[:,1].shape,DGS_flow[:,1].min(),DGS_flow[:,1].max())
#one-month:
temperature = temperature[start:end]
HG_1 = DGS_DG[:,0][start:end]
HG_2 = DGS_DG[:,1][start:end]
HG_3 = DGS_DG[:,2][start:end]

print(len(DGS_flow[:,0]))
WF_1 = DGS_flow[:,0][start:end]
WF_2 = DGS_flow[:,1][start:end]
WF_3 = DGS_flow[:,2][start:end]
#print(DGS_flow.shape)

WF_1 = LL_mmn.inverse_transform(WF_1)
WF_2 = LL_mmn.inverse_transform(WF_2)
#print(WF_1)
HG_1 = mmn.inverse_transform(HG_1)


plt.figure(figsize=(10,1), dpi=300)
plt.plot(WF_1, color='g', lw=1,rasterized=True)  # #dc6243  #355A24  #orangered


plt.xticks([])  #去掉x轴
plt.yticks([])  #去掉y轴
plt.axis('off')  #去掉坐标轴
#plt.ylabel('temperature', fontdict={'fontweight': 300, 'size': 8}, )
# plt.xlabel("Time Interval (an hour)", fontsize=20, horizontalalignment='center')
plt.yticks(fontsize=10)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
#plt.legend(fontsize=15,markerfirst = True)
plt.show()
