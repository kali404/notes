
## eval() 函数

将字符串str当成有效的表达式来求值并返回计算结果。

语**法**：eval(source[, globals[, locals]]) ---> value

**参数：**

　　　　source：一个Python表达式或函数compile()返回的代码对象

　　　　globals：可选。必须是dictionary

　　　　locals：可选。任意map对象

```python
a = '[[1,2], [3,4], [5,6], [7,8]]'
print(type(a), a)  

>>> <class 'str'> [[1,2], [3,4], [5,6], [7,8]]

b = eval(a)
print(type(b), b)  

>>> <class 'list'> [[1, 2], [3, 4], [5, 6], [7, 8]]

c = '{"name":"aaa", "age":18}'
print(type(c), c)  
>>> <class 'str'> {"name":"aaa", "age":18}

d = eval(c)
print(type(d), d) 

>>> <class 'dict'> {'name': 'aaa', 'age': 18}

e = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(e), e)

>>> <class 'str'> ([1,2], [3,4], [5,6], [7,8], (9,0))

f = eval(e)
print(type(f), f)  

>>> <class 'tuple'> ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))
```


在编译语言里要动态地产生代码，基本上是不可能的，但动态语言是可以，意味着软件已经部署到服务器上了，但只要作很少的更改，只好直接修改这部分的代码，就可立即实现变化，不用整个软件重新加

```python
a=1
g={'a':20}
eval("a+1",g)
运行结果：21
```

## **hasattr(object, name) 函数：**

判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性返回True，否则返回False。

**注意： name要用括号括起来。**

```python
class function_demo():
    name = 'demo'
    def run(self):
        return "hello function"


functiondemo = function_demo()
res = hasattr(functiondemo, 'name')  #判断对象是否有name属性，True

res = hasattr(functiondemo, "run") #判断对象是否有run方法，True

res = hasattr(functiondemo, "age") #判断对象是否有age属性，Falsw
print(res)
```

## getattr(object, name[,default]) 函数:

获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。

**注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面添加括号()**

```python
class function_demo():
    name = 'demo'
    def run(self):
        return "hello function"


functiondemo = function_demo()
getattr(functiondemo, 'name') #获取name属性，存在就打印出来--- demo 

getattr(functiondemo, "run") #获取run方法，存在打印出 方法的内存地址---<bound method function_demo.run of <__main__.function_demo object at 0x10244f320>>

getattr(functiondemo, "age") #获取不存在的属性，报错如下：
Traceback (most recent call last):
  File "/Users/liuhuiling/Desktop/MT_code/OpAPIDemo/conf/OPCommUtil.py", line 39, in <module>
    res = getattr(functiondemo, "age")
AttributeError: 'function_demo' object has no attribute 'age'

getattr(functiondemo, "age", 18)  #获取不存在的属性，返回一个默认值
```

## setattr(object, name,values) 函数:

给对象的属性赋值，若属性不存在，先创建再赋值。

```python
class function_demo():
    name = 'demo'
    def run(self):
        return "hello function"


functiondemo = function_demo()
res = hasattr(functiondemo, 'age')  # 判断age属性是否存在，False
print(res)

setattr(functiondemo, 'age', 18 )  #对age属性进行赋值，无返回值

res1 = hasattr(functiondemo, 'age') #再次判断属性是否存在，True
print(res1)
```

## 综合使用

```python
class function_demo():
    name = 'demo'
    def run(self):
        return "hello function"


functiondemo = function_demo()
res = hasattr(functiondemo, 'addr') # 先判断是否存在
if res:
    addr = getattr(functiondemo, 'addr')
    print(addr)
else:
    addr = getattr(functiondemo, 'addr', setattr(functiondemo, 'addr', '北京首都'))
    #addr = getattr(functiondemo, 'addr', '河南许昌')
    print(addr)
```


