# Tensor

import torch

### create a tensor

a = torch.Tensor([[1,2],[3,4],[5,6]])        ,tensor([[1., 2.],[3., 4.],[5., 6.]])


### create a tensor filled with zero or random values

c = torch.zeros((3,2))    ,shape(3,2)        ,tensor([[0., 0.],[0., 0.],[0., 0.]])
 
d = torch.randn((3,2)), random value
