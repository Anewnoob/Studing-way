"""plot gaussian distribution map--3D"""
all_mean = all_mean[0]
all_std = all_std[0]
print(all_std.shape)
from mpl_toolkits.mplot3d import Axes3D
all_mean = torch.mean(all_mean,1)
all_std = torch.mean(all_std,1)
all_mean = torch.mean(all_mean,0)
all_std = torch.mean(all_std,0)
print(all_mean.shape)
mean = all_mean.cpu().detach().numpy()
std = all_std.cpu().detach().numpy()


#plot gaussian
def build_gaussian_layer(mean=0,standard_deviation=1):
    x = np.arange(-0.1, 0.1, 0.02)
    y = np.arange(-0.1, 0.1, 0.02)
    x, y = np.meshgrid(x, y)
    z = np.exp(-((y-mean)**2 + (x - mean)**2)/(2*(standard_deviation**2)))
    z = z/(np.sqrt(2*np.pi)*standard_deviation)
    return (x, y, z)

fig = plt.figure()
ax = Axes3D(fig)
x3, y3, z3 = build_gaussian_layer(mean,std)#m8[0,:],s8[0,:]
ax.plot_surface(x3, y3, z3, rstride=1, cstride=1, cmap='coolwarm')
# plt.xticks([])  # 去掉x轴
# plt.yticks([])  # 去掉y轴
plt.axis('off')  # 去掉坐标轴
plt.show()
