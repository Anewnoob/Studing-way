# Tensor

import torch

### create a tensor

a = torch.Tensor([[1,2],[3,4],[5,6]])--->tensor([[1., 2.],[3., 4.],[5., 6.]])


### create a tensor filled with zero or random values  or ones

c = torch.zeros((3,2))--->shape(3,2) --->tensor([[0., 0.],[0., 0.],[0., 0.]])
 
d = torch.randn((3,2))--->random value

torch.ones((3,2))--->tensor([[1., 1.],[1., 1.],[1., 1.]])

### change the value in tensor
c[0,1] = 1  --->tensor([[0., 1.],[0., 0.],[0., 0.]])
 
### numpy to tensor(指向同一地址)
e = np.array([[1,2],[3,4],[5,6]])
torch_e = torch.from_numpy(e)

### tensor to numpy
e = torch_e.numpy()
