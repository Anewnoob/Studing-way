# 高阶函数  
接受另外一个函数作为参数输入  
例如：   
```
f = abs  
def add(x, y, f):  
    return f(x) + f(y)  
```
