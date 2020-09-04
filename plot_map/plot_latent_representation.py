 #description: Visualizing latent variables using T-SNE
 
 
        import matplotlib.pyplot as plt
        from matplotlib.ticker import NullFormatter
        from sklearn.manifold import TSNE
        z = z.cpu().detach().numpy()
        fig = plt.figure(figsize=(8, 8), dpi=300)
        '''t-SNE'''
        Y = TSNE(n_components=2).fit_transform(z0)
        ax = fig.add_subplot(2, 1, 2)
        plt.scatter(Y[:, 0], Y[:, 1], c='slateblue', cmap='coolwarm')  # PuOr_r #plt.cm.Spectral  
        ax.xaxis.set_major_formatter(NullFormatter())  # 设置标签显示格式为空
        ax.yaxis.set_major_formatter(NullFormatter())
        plt.axis('tight')
        plt.axis('off')
        plt.show()
