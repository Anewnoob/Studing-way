# 必选参数，默认参数  
略  
# 可变参数---参数个数不确定  
定义： def func(*numbers):  
调用： func(a,b,c)  
若输入的参数是list 或者tuple类型,在调用的时候可以用如下方式(在传入参数之前就进行组装):  
func(*nums) #nums为列表或者元组  
# 关键字参数---方便之后函数的重写和扩展(任意的)  
定义: def func(name, age, **kw):  
调用： func("Anewnoob",18,city = "ChengDu")  
同样地，在传入参数之前就可以进行组装，如:  
extra = {'city': 'Beijing', 'job': 'Engineer'}  
func("Anewnoob",18, **extra)  
# 命名关键字参数  
检查某个参数是否在关键字参数里:  
if 'city' in kw  
如果要限制关键字参数的名字，可以采用命名关键字参数，用*隔开，如果中间又可变参数存在，则不需要用*单独隔开  
定义：def func(name, age, *, city, job)  
      def func(name, age, *args, city, job):
      
总结：参数定义顺序可归为：必选参数、默认参数、可变参数、命名关键字参数和关键字参数




