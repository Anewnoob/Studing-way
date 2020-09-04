"""plot ne-nfe  time-nfe scatter figure"""

from matplotlib import pyplot as plt
import warnings; warnings.filterwarnings(action='once')
from matplotlib.ticker import FuncFormatter
import numpy as np
import random
NE_path = '../saved_model/PDS/FlowODE-True/NE.txt'
nfe_path = '../saved_model/PDS/FlowODE-True/nfe.txt'
time_path = '../saved_model/PDS/FlowODE-True/time.txt'

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

with open(time_path, 'r') as f:
    content = f.read()
    all_time = content.split("\n")
    time_1 = all_time[0]
    time_1 = time_1.split("\t")
    print(len(time_1))

with open(NE_path, 'r') as f:
    content = f.read()
    all_NE = content.split("\n")
    NE_1 = all_NE[0]
    NE_1 = NE_1.split("\t")

    #print(content)

with open(nfe_path, 'r') as f:
    content = f.read()
    all_nfe = content.split("\n")
    nfe_1 = all_nfe[0]

    nfe_1 = nfe_1.split("\t")

    #print(content)

NE_1 = [ float(i) for i in NE_1[:-1]]
print(len(NE_1))

time_1 = [ float(i) for i in time_1[:-1]]
nfe_1 = [ float(i) for i in nfe_1[:-1]]
print(len(nfe_1))
print(len(time_1))


f,ax = plt.subplots(figsize=(10, 10),dpi=350)
ax2 = ax.twinx()
ax.scatter(nfe_1, NE_1, color='slateblue', label='Error (MSE)', rasterized=True, marker='d', s=12)
ax2.scatter(nfe_1, time_1, color='g', label='Time (s)', marker='.', rasterized=True, s=12)
#ax.set_ylim([0, 0.085])
ax.set_ylim([0, 0.006])
def formatnum(x, pos):
    if x == 0:
        return 0
    return '$%.0f$x$10^{-3}$' % (x * 1000)

formatter = FuncFormatter(formatnum)
ax.yaxis.set_major_formatter(formatter)
ax.set_xlabel(r'$\mathcal{N}$ (number of function evaluations)', fontsize=15, horizontalalignment='center')
ax.set_ylabel('MSE',fontdict={'fontweight': 300, 'size': 15})
#plt.yticks(fontsize=20, alpha=1.)

plt.tick_params(labelsize=10)
ax2.set_ylabel("Time (s)",fontdict={'fontweight': 300, 'size': 15})
#plt.legend(loc = 'best')
plt.show()


