# 高阶函数  
接受另外一个函数作为参数输入  
例如：   
```
f = abs  
def add(x, y, f):  
    return f(x) + f(y)  
```
# map/reduce
def map(func_name,iterator)  
lsit(map(str,[1,2,3,4,5]))#把列表所有int转换为str,并把结果Iterator转化为list  
reduce---把结果继续和序列的下一个元素做累积计算  
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  
例如: reduce(add, [1, 3, 5, 7, 9]) #25  
把序列[1, 3, 5, 7, 9]变换成整数13579：
```
from functools import reduce  
def func(x,y):  
    return x*10+y  
reduce(func,[1,3,5,7,9])  
```
上述函数可以利用lambda函数简化：  
reduce(lambda x,y\:x*10+y,[1,3,5,7,9])
