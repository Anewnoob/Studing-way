# 生成器

生成器优点：通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。

而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

生成器里装的是生成结果的算法，因此能节省大量的空间

创建一个generator，有很多种方法

## 方法一：

将一个列表生成式的[]改成()，就创建了一个generator：

```
g = (x * x for x in range(10)) #创建

next(g) 访问下一个值

for i in g:  #通过迭代访问

    print(i)
```

## 方法二

在生成函数中使用yield关键字, 函数中执行的过程中遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

```
#斐波拉契数列

def fib(max):

    n, a, b = 0, 0, 1
    
    while n < max:
    
        yield b
        
        a, b = b, a + b
        
        n = n + 1
        
    return 'done'
```

若想要拿到return的值，需要捕获StopIteration错误，返回值包含在StopIteration的value中

```
g = fib(6)

while True:

     try:
     
         x = next(g)
         
         print('g:', x)
         
     except StopIteration as e:
     
         print('Generator return value:', e.value)
         
         break
```
