   
    from matplotlib import pyplot as plt
  


    all_maps = list(plt.cm.datad.keys())
    plt.imshow(flow, cmap=all_maps[6])  # 4617-4625 #   4620 96   0 2 3  flow.shape = (32x32)
    plt.colorbar()
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    #plt.axis('off')  # 去掉坐标轴
    plt.show()

    plt.imshow(flow[20], cmap=all_maps[6])  # 4617-4625 #   4620 96   0 2 3
    plt.colorbar()
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    #plt.axis('off')  # 去掉坐标轴
    plt.show()

    #
    # for i in range(200):
    #     print(i)
    #     plt.imshow(inflow, cmap=all_maps[i])   #4617-4625 #   4620 96   0 2 3
    #     #plt.grid(True)
    #     plt.colorbar()
    #     plt.show()
      
      

"""plot the distribution map"""
coarse_flow_map = test_data[0][0].cpu().detach().numpy()      #32x32
fine_distribution = preds[0][0].cpu().detach().numpy()            #128x128
ext_distribution = ext_out[0][0].cpu().detach().numpy()

print(fine_distribution.shape,coarse_flow_map.shape)
superregion = coarse_flow_map* opt.scaler_X
subregion = fine_distribution[80:84]
print(subregion.shape)
subregion = subregion[:,[40,41,42,43]]
print(superregion)
print(subregion.shape)
#
#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')

#fine_distribution
#定义三维数据
x1 = [i for i in range(0,128)]
x1 = np.array(x1)
print(x1.shape)
y1 = [i for i in range(0,128)]
y1 = np.array(y1)
print(y1.shape)
x,y =np.meshgrid(x1,y1)

ax1.plot_surface(x,y,fine_distribution,rstride=4,cstride=4,cmap="rainbow")
plt.show()

#coarse-map
x1 = [i for i in range(0,128)]
x1 = np.array(x1)
print(x1.shape)
y1 = [i for i in range(0,128)]
y1 = np.array(y1)
print(y1.shape)
x,y =np.meshgrid(x1,y1)

ax1.plot_surface(x,y,coarse_flow_map,rstride=1,cstride=1,cmap="rainbow")
# ax1.contour(x,y,coarse_flow_map,zdir='z', offset=-3,cmap="rainbow")  #生成z方向投影，投到x-y平面
# ax1.contour(x,y,coarse_flow_map,zdir='x', offset=-6,cmap="rainbow")  #生成x方向投影，投到y-z平面
# ax1.contour(x,y,coarse_flow_map,zdir='y', offset=6,cmap="rainbow")   #生成y方向投影，投到x-z平面

plt.xticks([])  # 去掉x轴
plt.yticks([])  # 去掉y轴
plt.axis('off')  # 去掉坐标轴
plt.show()

