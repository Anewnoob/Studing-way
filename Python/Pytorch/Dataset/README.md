
import pandas as pd

from torch.utils.data import Dataset

#define the function len and getitem to write your own dataset

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
        
        
#define the dataset use torch API
 
    train_data = torch.utils.data.TensorDataset(train_X,train_Y)
                                                
    val_data = torch.utils.data.TensorDataset(val_X,val_Y)
                                              
    test_data = torch.utils.data.TensorDataset(test_X,test_Y)
    
    dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)

    dataloader = DataLoader(val_data, batch_size=batch_size, shuffle=False)

    dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
