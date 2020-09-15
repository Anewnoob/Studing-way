# Tensor

import torch

### create/filled/rand/add/zeros a tensor  

a = torch.Tensor([[1,2],[3,4],[5,6]])

torch.zeros((3,2))--->tensor([[0., 0.],[0., 0.],[0., 0.]])
 
torch.randn((3,2))--->random value

torch.ones((3,2))--->tensor([[1., 1.],[1., 1.],[1., 1.]])

torch.empty(5, 3 , dtype = torch.uint8)

torch.rand(5, 3 , dtype = torch.float32, requires_grad=True)

torch.view(3,-1) # reshape x to (3,x)

torch.unsqueeze(0) # 增加一维

torch.normal(mean, std, out=None) #正态分布

torch.arange(start, end, step=1, dtype=torch.int32)

torch.full(size, fill_value)

torch.randn_like(x, dtype = torch.float)

torch.ones_like(x, dtype = torch.float)


### change the value in tensor
c[0,1] = 1  --->tensor([[0., 1.],[0., 0.],[0., 0.]])
 
### numpy to tensor(指向同一地址)
e = np.array([[1,2],[3,4],[5,6]])
torch_e = torch.from_numpy(e)

### tensor to numpy
e = torch_e.numpy()



