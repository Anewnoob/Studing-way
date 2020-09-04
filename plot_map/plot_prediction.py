"""plt prediction and groundtruth"""
all_y_batch = np.array(all_y_batch[:-1])
all_x_res = np.array(all_x_res1[:-1])
all_x_res1 = np.array(all_x_res1[:-1])
all_x_res2 = np.array(all_x_res2[:-1])
all_x_res3 = np.array(all_x_res3[:-1])
all_x_res4 = np.array(all_x_res4[:-1])


print(all_y_batch.shape,all_x_res1.shape,all_x_res2.shape,all_x_res3.shape,all_x_res4.shape,)
print(len(all_x_res_HA),all_y_batch.shape)

#all_x_res_HA = np.array(all_x_res_HA[-all_x_res1.shape[0]*all_x_res1.shape[1]-1:-1])
all_x_res_HA = np.array(all_x_res_HA[168:all_x_res1.shape[0]*all_x_res1.shape[1]+168])
all_y_batch = np.sum(all_y_batch.reshape(all_y_batch.shape[0]*all_y_batch.shape[1], -1), axis=1)
all_x_res1 = np.sum(all_x_res1.reshape(all_x_res1.shape[0]*all_x_res1.shape[1], -1), axis=1)
all_x_res2 = np.sum(all_x_res2.reshape(all_x_res2.shape[0]*all_x_res2.shape[1], -1), axis=1)
all_x_res3 = np.sum(all_x_res3.reshape(all_x_res3.shape[0]*all_x_res3.shape[1], -1), axis=1)
all_x_res4 = np.sum(all_x_res4.reshape(all_x_res4.shape[0]*all_x_res4.shape[1], -1), axis=1)
print(all_y_batch.shape,all_x_res_HA.shape,all_x_res1.shape,all_x_res2.shape,all_x_res3.shape,all_x_res4.shape,)


"""折线图"""
#PDS
# start = 66*T  #+15
# end = 95*T #-1
start = 66*T  #+15
end = 67*T #-1


plt.figure(figsize=(15,10), dpi=300)
line = 1.5
markersize = 0
size  = 15
plt.plot(all_y_batch[-end-1:-start-1], color='r', lw=line,label="Ground Truth")
plt.plot(all_x_res_HA[-end:-start], color='silver', lw=line,label="HA",marker='x',markersize = markersize)
plt.plot(all_x_res1[-end:-start], color='slateblue', lw=line,label="Bi-GRU", marker='>',markersize = markersize) #12
plt.plot(all_x_res3[-end:-start], color='indigo', lw=line,label="GRU-VAE", marker='o',markersize = markersize) #12
plt.plot(all_x_res4[-end:-start], color='royalblue', lw=line,label="LatentODE", marker='*',markersize = markersize) #12
plt.plot(all_x_res2[-end:-start], color='gold', lw=line,label="FlowODE", marker='p',markersize = markersize) #12

plt.yticks(fontsize=size)
plt.tick_params(labelsize=size)
plt.ylabel('Water Inflow Volume',fontsize=size)
plt.xlabel("Hour (A Day)", fontsize=size, horizontalalignment='center')
plt.grid(linestyle=':')
#plt.gca().set_xticks([])
plt.legend(fontsize=10,loc='center',bbox_to_anchor=(0.5, 1.14),ncol=3)  #1.14
plt.show()
