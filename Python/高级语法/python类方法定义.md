# python 中 @classmethod @staticmethod 区别

Python 中 3 种方式定义类方法, 常规方式, @classmethod 修饰方式, @staticmethod 修饰方式.

```python
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)    
a = A()
```

### 1. 定义方式

普通的类方法 foo() 需要通过 self 参数隐式的传递当前类对象的实例。 @classmethod 修饰的方法 class_foo() 需要通过 cls 参数传递当前类对象。@staticmethod 修饰的方法定义与普通函数是一样的。

self 和 cls 的区别不是强制的，只是 PEP8 中一种编程风格，slef 通常用作实例方法的第一参数，cls 通常用作类方法的第一参数。即通常用 self 来传递当前类对象的实例，cls 传递当前类对象。

### 2. 绑定对象

```
foo方法绑定对象A的实例，class_foo方法绑定对象A，static_foo没有参数绑定。
>>> print(a.foo)
<bound method A.foo of <__main__.A object at 0x0278B170>>
>>> print(a.class_foo)
<bound method classmethodclassmethod
```

### 3. 调用方式

foo 可通过实例 a 调用，类对像 A 直接调用会参数错误。

```
>>> a.foo(1)
executing foo(<__main__.A object at 0x0278B170>,1)
self: <__main__.A object at 0x0278B170>
>>> A.foo(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() missing 1 required positional argument: 'x'
```

但 foo 如下方式可以使用正常，显式的传递实例参数 a。

```
>>> A.foo(a, 1)
executing foo(<__main__.A object at 0x0278B170>,1)
self: <__main__.A object at 0x0278B170>
```

class_foo 通过类对象或对象实例调用。

```
>>> A.class_foo(1)
executing class_foo(<class '__main__.A'>,1)
cls: <class '__main__.A'>
>>> a.class_foo(1)
executing class_foo(<class '__main__.A'>,1)
cls: <class '__main__.A'>
```

static_foo 通过类对象或对象实例调用。

```
>>> A.static_foo(1)
executing static_foo(1)
>>> a.static_foo(1)
executing static_foo(1)
```

### 4. 继承与覆盖普通类函数是一样的。

```
class B(A):
    pass
b = B()
b.foo(1)
b.class_foo(1)
b.static_foo(1)
# executing foo(<__main__.B object at 0x007027D0>,1)
# self: <__main__.B object at 0x007027D0>
# executing class_foo(<class '__main__.B'>,1)
# cls: <class '__main__.B'>
# executing static_foo(1)
```

问题：@staticmethod 修饰的方法函数与普通的类外函数，为什么不直接使用普通函数？
@staticmethod 是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。