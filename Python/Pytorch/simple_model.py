import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import argparse
import random

#init argument
parser = argparse.argumentparser()
parser.add_argument('--batch_size', default = 128, help='batchsize')
parser.add_argument('--delta', type=float, default=0.5, help='delta')
parser.add_argument('--epsilon', type=float,default=1e-7)
parser.add_argument('--beta1', type=float, default=0.9)
parser.add_argument('--beta2', type=float,default=0.999)
parser.add_argument('--lr', type=float,default=1e-3)
parser.add_argument('--manualSeed', type=int, help='manual seed')
opt = parser.parse_args()


#Random Seed init
if opt.manualSeed is None:
    opt.manualSeed = random.randint(1, 10000)
    random.seed(opt.manualSeed)   　　
    torch.manual_seed(opt.manualSeed)  #为CPU设置种子用于生成随机数，以使得结果是确定的   　　 
    #torch.cuda.manual_seed(opt.manualSeed) #为当前GPU设置随机种子  　　
    #torch.cuda.manual_seed_all(opt.manualSeed) #为所有GPU设置随机种子  
    #cudnn.deterministic = True  #卷积网络使用---将卷积算法固定
    
    
#device 
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
cuda = True if torch.cuda.is_available() else False


from model.model_name import model_name
model = model_name(opt)


loss_fn = nn.MSELoss()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1e10)
if cuda:
    model.cuda()
    loss_fn.cuda()
lr = opt.lr
optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(opt.beta1, opt.beta2))

if __name__ == '__main__':
    for epoch in range(epochs):
        for x,y in training_set:
            model.train()
            optimizer.zero_grad()
            res = model(x)
            loss = loss_fn(res,y)
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad()
        for x,y in testing_set:
            res = model(x)
            mse_loss = MSE(res,y)
            
        #torch.save(model.state_dict(), '{}/{}-{}.pt'.format(save_path,opt.model,opt.target_year))
        #optimizer = torch.optim.Adam(model.parameters(), lr=lr/2, betas=(opt.beta1, opt.beta2))


  
