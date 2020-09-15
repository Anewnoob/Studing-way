from torch.autograd import Variable

x = Variable(torch.Tensor([1]),requires_grad = True)

w = Variable(torch.Tensor([2]),requires_grad = True)

b = Variable(torch.Tensor([3]),requires_grad = True)

y = w*x+b

y.backward()   # perform one step backward

print(x.grad)  #2  

print(w.grad)  #1

print(b.grad)  #1
