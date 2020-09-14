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

# Variable
from torch.autograd import Variable
x = Variable(torch.Tensor([1]),requires_grad = True)
w = Variable(torch.Tensor([2]),requires_grad = True)
b = Variable(torch.Tensor([3]),requires_grad = True)

y = w*x+b

y.backward()   # perform one step backward

print(x.grad)  #2  

print(w.grad)  #1

print(b.grad)  #1

### Dataset

import pandas as pd

from torch.utils.data import Dataset

class myDataset(Dataset):

    def __init__(self, csv_file, txt_file, root_dir, other_file):
    
        self.csv_data = pd.read_csv(csv_file)
        
        with open(txt_file, 'r') as f:
        
            data_list = f.readlines()
            
        self.txt_data = data_list
        
        self.root_dir = root_dir
        
        
    def __len__(self):
    
        return len(self.csv_data)
    
    def __getitem(self,idx):
    
        data = (self.csv_data[idx],self.txt_data[idx])
        
        return data
