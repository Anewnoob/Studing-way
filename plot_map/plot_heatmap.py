   
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
