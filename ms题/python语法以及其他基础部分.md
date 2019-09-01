#### python语法以及其他基础部分

1. 可变与不可变类型； 

   | 可变类型   | 不可变类型   |
   | ---------- | ------------ |
   | dict 字典  | str字符串    |
   | list 列表  | int 整型     |
   | tuple 元组 | float 浮点数 |
   | set 集合   |              |

2. 浅拷贝与深拷贝的实现方式、区别；deepcopy如果你来设计，如何实现

   > **copy浅拷贝：**没有拷贝子对象，所以原始数据改变，子对象改变
   >
   > **deepcopy深拷贝：**包含对象里面的子对象的拷贝，所以原始对象的改变不会造成深拷贝里的任何子元素的改变
   >
   > Python里的赋值符号“=”只是将对象进行了引用，如果想新开辟进行了引用，如果想新开辟地址new出一个新对象，要用copy模块里copy.copy()，但是用这个方法得到的对象就是新对象，但是数据还是引用。
   >
   > 如果要完全得到一个一模一样的对象，要用copy.deepcopy()方法。这样，在改变更新对象的时候，原对象才能不受影响，也就是保持原始数据不变。

3. `__new__() 与 __init__()`的区别； 

   > __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
   >
   > __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
   >
   > 故而“ 本质上 ”来说，__new__（）方法负责创建实例，而__init__()仅仅是负责实例属性相关的初始化而已，执行顺序是，先new后init。


4. 你知道几种设计模式； 

   > 工厂模式
   >
   > 建造者模式
   >
   > 原型模式
   >
   > 适配器模式
   >
   > 装饰器模式
   >
   > 外观模式
   >
   > MVC模式
   >
   > 责任链模式

5. 编码和解码你了解过么； 

   > Python 里面的编码和解码也就是 unicode 和 str 这两种形式的相互转化。
   >
   > 编码是 unicode -> str，相反的，解码就是 str -> unicode。
   >
   > 不同编码格式的字符串之间相互转换编码格式的话，都要先解码成unicode，再编码成其他编码格式的字符串。就拿上面的str1来说，将str1转成utf-8编码的字符串，需要这么做：
   > str1.decode(‘gb2312’).encode(‘utf-8’)。

6. 列表推导list comprehension和生成器的优劣； 

   > 生成器: **每次处理一个对象，而不是一口气处理和构造整个数据结构，这样做的潜在优点是可以节省大量的内存**。`()`
   >
   > 推导式 :**如果生成列表的方式不太复杂，这是建议使用列表推导式，其内部是通过cpython来实现的比用for循环要快**`[]`

7. 什么是装饰器；如果想在函数之后进行装饰，应该怎么做；

   >  是对函数的一种包装。它能使函数的功能得到扩充，而同时不用修改函数本身的代码。它能够增加函数执行前、执行后的行为，而不需对调用函数的代码做任何改变。
   >
   >  ```python
   >  # 装饰器
   >  def a(func):
   >  	print(1)
   >  	def b():
   >       print(1)
   >  		func()
   >  		print(3)
   >  	return b
   >  @a
   >  def c():
   >  	print(4)
   >  c()
   >  ```
   >
   >  ```python
   >  # 装饰器工厂
   >  def func1(flag):
   >      def func2(func):
   >          def func3(a,b):
   >              print(flag)
   >              func(a,b)
   >          return func3
   >      return func2
   >  
   >  @func1('a')
   >  def a(a,b):
   >      print(a,b)
   >  
   >  a(1,2)
   >  ```
   >
   >  

8. 手写个使用装饰器实现的单例模式； 

   ```python
   # 使用装饰器实现单例模式
   def singleton(cls, *args, **kwargs):
       instance = {}
       def _instance():
           if cls not in instance:
               instance[cls] = cls(*args, *kwargs)
           return instance[cls]
       return _instance
   
   @singleton
   class Test_singleton:
       def __init__(self):
           self.num = 0
   
       def add(self):
           self.num = 99
   
   ts1 = Test_singleton()
   ts2 = Test_singleton()
   print(ts1)
   print(ts2)
   '''
   <__main__.Test_singleton object at 0x000001D4CFDCC7F0>
   <__main__.Test_singleton object at 0x000001D4CFDCC7F0>
   '''
   ```

   

9. 使用装饰器的单例和使用其他方法的单例，在后续使用中，有何区别； 

   > **单例模式（Singleton Pattern）**是一种常用的软件设计模式，该模式的主要目的是确保**某一个类只有一个实例存在**。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
   >
   > **方法:**
   >
   > **使用模块**
   >
   > **Python 的模块就是天然的单例模式**，因为模块在第一次导入时，会生成 `.pyc` 文件，当第二次导入时，就会直接加载 `.pyc` 文件，而不会再次执行模块代码。
   >
   > **使用装饰器** 
   >
   > ```python
   > def Singleton(cls):
   >     _instance = {}
   > 
   >     def _singleton(*args, **kargs):
   >         if cls not in _instance:
   >             _instance[cls] = cls(*args, **kargs)
   >         return _instance[cls]
   >     return _singleton
   > 
   > @Singleton
   > class A(object):
   >     a = 1
   >     def __init__(self, x=0):
   >         self.x = x
   > 
   > a1 = A(2)
   > a2 = A(3)
   > ```
   >
   > **使用类**
   >
   > ```python
   > import time
   > import threading
   > class Singleton(object):
   >     _instance_lock = threading.Lock()
   > 
   >     def __init__(self):
   >         time.sleep(1)
   > 
   >     @classmethod
   >     def instance(cls, *args, **kwargs):
   >         if not hasattr(Singleton, "_instance"):
   >             with Singleton._instance_lock:
   >                 if not hasattr(Singleton, "_instance"):
   >                     Singleton._instance = Singleton(*args, **kwargs)
   >         return Singleton._instance
   > ```
   >
   > **基于`__new__`方法实现（推荐）**
   >
   > ```python
   > import threading
   > class Singleton(object):
   >     _instance_lock = threading.Lock()
   > 
   >     def __init__(self):
   >         pass
   > 
   > 
   >     def __new__(cls, *args, **kwargs):
   >         if not hasattr(Singleton, "_instance"):
   >             with Singleton._instance_lock:
   >                 if not hasattr(Singleton, "_instance"):
   >                     Singleton._instance = object.__new__(cls)  
   >         return Singleton._instance
   > 
   > obj1 = Singleton()
   > obj2 = Singleton()
   > ```
   >
   > **基于metaclass实现**
   >
   > ```python
   > import threading
   > 
   > class SingletonType(type):
   >     _instance_lock = threading.Lock()
   >     def __call__(cls, *args, **kwargs):
   >         if not hasattr(cls, "_instance"):
   >             with SingletonType._instance_lock:
   >                 if not hasattr(cls, "_instance"):
   >                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
   >         return cls._instance
   > 
   > class Foo(metaclass=SingletonType):
   >     def __init__(self,name):
   >         self.name = name
   > 
   > 
   > obj1 = Foo('name')
   > obj2 = Foo('name')
   > print(obj1,obj2)
   > ```
   >
   > 

10. 手写：正则邮箱地址； 

    > ^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$

11. 介绍下垃圾回收：引用计数/分代回收/孤立引用环； 

    > 当一个对象的引用计数器归零时,它将被垃圾回收机制处理掉
    >
    > **引用计数（跟踪和回收垃圾）**
    >
    > 1. 可通过sys包中的getrefcount(引用名)来查看某个对象的引用计数
    > 2. 当将某个引用作为实参传递给getrefcount（）时，参数实际上创建了一个临时的引用。因此，引用计数结果比实际值多1
    > 3. 对于python的容器（container）对象，如：列表、字典等，其内部包含的并不是对象，而是对象的引用。
    > 4. 词典对象用于记录所有全局变量的引用。可通过内置函数globals()查看该词典
    > 5. 容器对象的引用可能会构成很复杂的拓扑结构。可通过objgraph包中的show_refs（）函数来进行查看
    > 6. objgraph包的安装（windows）：pip install xdot   /   pip install objgraph
    >
    >  **分代回收（以空间换时间进一步提高垃圾回收效率）**
    >
    > 1. python同时采用分代回收策略。该策略假设：存活时间越久的对象，越不可能在后边的程序当中编程垃圾。
    > 2. python将所有对象分为0， 1， 2三代对象。
    > 3. 所有的新建对象都是0代对象。当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象。垃圾回收启动时，一定会扫描所有的0代对象。如果0代经过一定次数垃圾回收，那么就启动对0代和1代的扫描清理。当1代也经历了一定次数的垃圾回收后，那么会启动对0，1，2，即对所有对象进行扫描
    >
    > **孤立的引用环**
    >      两个表对象，互相引用对方构成一个引用环。删除了a，b引用之后，这两个对象不可能再从程序中调用，就没有什么用处了。但是由于引用环的存在，这两个对象的引用计数都没有降到0，不会被垃圾回收。
    > 	为了回收这样的引用环，Python复制每个对象的引用计数，可以记为gc_ref。假设，每个对象i，该计数为gc_ref_i。Python会遍历所有的对象i。对于每个对象i引用的对象j，将相应的gc_ref_j减1。
    > 	遍历后，gc_ref不为0的对象，和这些对象引用的对象，以及继续更下游引用的对象，需要被保留。而其它的对象则被垃圾回收。

12. 多进程与多线程的区别；CPU密集型适合用什么； 

    >**线程**是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。
    >
    >一个程序的执行实例就是一个**进程**。每一个进程提供执行程序所需的所有资源。（进程本质上是资源的集合）一个进程有一个虚拟的地址空间、可执行的代码、操作系统的接口、安全的上下文（记录启动该进程的用户和权限等等）、唯一的进程ID、环境变量、优先级类、最小和最大的工作空间（内存空间），还要有至少一个线程。每一个进程启动时都会最先产生一个线程，即主线程。然后主线程会再创建其他的子线程。
    >
    >```
    >同一个进程中的线程共享同一内存空间，但是进程之间是独立的。
    >同一个进程中的所有线程的数据是共享的（进程通讯），进程之间的数据是独立的。
    >对主线程的修改可能会影响其他线程的行为，但是父进程的修改（除了删除以外）不会影响其他子进程。
    >线程是一个上下文的执行指令，而进程则是与运算相关的一簇资源。
    >同一个进程的线程之间可以直接通信，但是进程之间的交流需要借助中间代理来实现。
    >创建新的线程很容易，但是创建新的进程需要对父进程做一次复制。
    >一个线程可以操作同一进程的其他线程，但是进程只能操作其子进程。
    >线程启动速度快，进程启动速度慢（但是两者运行速度没有可比性）。
    >```
    >
    >多进程适用于在cpu密集操作,浮点数运算
    >
    >多线程适用于io密集型操作
    >
    >线程并发 同一时刻多任务同时允许行
    >
    >进程并行,同一时间间隔内多任务的运行,但不会在同一时刻运行,交替运行

13. 进程通信的方式有几种； 

    > 主要Queue和Pipe这两种方式，Queue用于多个进程间实现通信，Pipe是两个进程的通信

14. 介绍下协程，为何比线程还快； 

    > 协程，又称微线程，纤程。协程是单线程的，单线程就意味着所有的任务需要在单线程上排队执行，也就是前一个任务没有执行完成，后一个任务就没有办法执行。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方（线程调度时候寄存器上下文及栈等保存在内存中），在切回来的时候，恢复先前保存的寄存器上下文和栈。因此：
    >
    > 协程能保留上一次调用时的状态（即所有局部状态的一个特定组合），每次过程重入时，就相当于进入上一次调用的状态，换种说法：进入上一次离开时所处逻辑流的位置。

15. range和xrange的区别（他妹的我学的py3…）； 

    > 1.python3 没有xrange,用range代替.
    > 2.range返回的是一个list对象，而xrange返回的是一个生成器对象(xrange object)。
    > 3.xrange则不会直接生成一个list，而是每次调用返回其中的一个值，内存空间使用极少，因而性能非常好。

16. 由于我有C/C++背景，因此要求用C来手写：将IP地址字符串（比如“172.0.0.1”）转为32位二进制数的函数。

    > 我没有c的背景啊~我不写

#### 算法排序部分

1. 手写快排；堆排；几种常用排序的算法复杂度是多少；快排平均复杂度多少，最坏情况如何优化；(彪标)

   ```python
   def quick_sort(tlist,start,end):
   
       # 0. 规定递归的跳出条件
       if start >= end:
           return
   
       # 1. 初始化，确定基准pivot
       leftPointer = start
       rightPointer = end
       pivot = tlist[start]
   
       # 2. 分区操作（partition）
       while leftPointer < rightPointer:
           while leftPointer < rightPointer and tlist[rightPointer] >= pivot:
               rightPointer -= 1
           tlist[leftPointer]=tlist[rightPointer]
           while leftPointer < rightPointer and tlist[leftPointer] < pivot:
               leftPointer += 1
           tlist[rightPointer]=tlist[leftPointer]
       tlist[rightPointer] = pivot
       quick_sort(tlist,0,rightPointer-1)
       quick_sort(tlist,rightPointer+1,end)
   
       return tlist
   
   
   if __name__ == '__main__':
       tlist = [7850, 76892, 49169, 44721, 51861, 66149, 18273, 94882, 63497, 8427, 65300, 20822, 15745, 12270, 31608, 38276, 36210, 21632, 33084, 61789]
       print(quick_sort(tlist,0,len(tlist)-1))
   ```
   
   ```python
   # 冒泡
   def bubble(context):
       print("the old array is %s" % context)
   
       n = 1
       while n < len(context):
           for i in range(len(context)-1):
               if context[i] > context[i + 1]:
                   context[i], context[i + 1] = context[i + 1], context[i]
           n += 1
   
       print("the new array is %s " % context)
   

   if __name__ == '__main__':
       context = [18422, 15669, 9854, 12705, 18350, 19424, 9072, 14817, 11030, 16525]
       bubble(context)
   
   ```
   
   
   
2. 手写：已知一个长度n的无序列表，元素均是数字，要求把所有间隔为d的组合找出来，你写的解法算法复杂度多少；（彪标）

   ```python
   def a(tlist, d):
       for item in range(len(tlist)-1):
           base = tlist[item]
           for each in tlist:
               if abs(base - each) == d:
                   return base, each
   
   if __name__ == '__main__':
       d = 6791
       tlist = [18075, 11284, 18219, 8819, 9522, 12419, 9591, 15202, 13609, 10782]
       print(a(tlist, d))
   ```
   
3. 手写：一个列表A=[A1，A2，…,An]，要求把列表中所有的组合情况打印出来；

   ```python
   from itertools import combinations
   li = []
   l = [1, 2, 3, 4, 5]
   for i in range(2,len(l)+1):
       li.append(list(combinations(l, i)))
   
   print(li)
   ```

4. 手写：用一行python写出1+2+3+…+10**8 ；

   ```python
   ret = sum([i for i in range(10**8-1)])
   ```

5. 手写python：用递归的方式判断字符串是否为回文；

   ```python
   def is_palindrome(s):
       if s =="":
           return True
       else:
           if s[0]==s[-1]:
               return is_palindrome(s[1:-1])
           else:
               return False
   
   # print(is_palindrome('1234321'))
   # print(is_palindrome('1234121'))
   ```

6. 单向链表长度未知，如何判断其中是否有环；

   ```PYTHON
   class Node():  
       def __init__(self, item=None):
           self.item = item  // 数据域
           self.next = None  // 指针域
   
   
   // 判断是否为环结构并且查找环结构的入口节点
   def findbeginofloop(head): 
       // 默认环不存在，为False
       loopExist = False  
       // 如果头节点就是空的，那肯定就不存在环结构
       if head == None:  
           return "不是环结构"
           
       s = set()
       while head.next:  
           // 判断遍历的节点是否在set中 
           if id(head) in s:
               // 返回环入口
               print("存在环结构")
               return head.item
           s.add(id(head))
           head = head.next
           
       return "不是环结构"
   
   if __name__ == "__main__":
       // 构建环
       node1 = Node(1)
       node2 = Node(2)
       node3 = Node(3)
       node4 = Node(4)
       node5 = Node(5)
       node1.next = node2
       node2.next = node3
       node3.next = node4
       node4.next = node5
       node5.next = node2
       print(findbeginofloop(node1))
   ```

7. 单向链表如何使用快速排序算法进行排序；

   

8. 手写：一个长度n的无序数字元素列表，如何求中位数，如何尽快的估算中位数，你的算法复杂度是多少；(谁会用堆解决下）

   ```python
   def median(data):
       '''先排序再取中位
       下标为列表长度整除和整除取反的平均数'''
       data.sort() # 可换排序算法,求时间复杂度
       half = len(data) // 2
       return (data[half] + data[~half])/2
   if __name__ == '__main__':
       print(median([1,4,2,3]))
   ```

   

9. 如何遍历一个内部未知的文件夹（两种树的优先遍历方式）

   ```python
   import os
   import os.path
   rootdir = "" # 指明被遍历的文件夹
   
   for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
       for dirname in  dirnames:                       #输出文件夹信息
           print "parent is:" + parent
           print  "dirname is" + dirname
   
   　　for filename in filenames:                        #输出文件信息
           print "parent is": + parent
           print "filename is:" + filename
           print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
   ```

   

#### 网络基础部分

1. TCP/IP分别在模型的哪一层； 

   | 网络七大层 | 包含协议                                                     |
   | ---------- | ------------------------------------------------------------ |
   | 物理层     | EIA/TIA-232, EIA/TIA-499, V.35, V.24, RJ45, Ethernet, 802.3, 802.5, FDDI, NRZI, NRZ |
   | 数据链路层 | Frame Relay, HDLC, PPP, IEEE 802.3/802.2, FDDI, ATM,         |
   | 网络层     | ARP;IPV4;IPV6;IP                                             |
   | 传输层     | TCP;UDP;SCTP;DCCP                                            |
   | 会话层     | RPC,SQL,NFS,NetBIOS,names,AppleTalk,ASP,DECnet,SCP           |
   | 表示层     | TIFF,GIF,JPEG,PICT,ASCII,EBCDIC,encryption,MPEG,MIDI,HTML    |
   | 应用层     | SSH,HTTP,POP,FTP,WWW,Telnet,NFS,SMTP,Gateway,SNMP            |

   

2. socket长连接是什么意思； 

   > Socket 是 TCP 层的封装，通过 socket，我们就能进行 TCP 通信。
   >
   > 很常见的事，每建立一次TCP连接是要消耗资源的，总不能老是断开了连，连完了断，这样资源消耗是非常大的。在一些操作频繁，并发数不是很多（长时间持有连接也消耗资源）的点对点情况下，适合使用长链接。而在一些操作不多，但并发很大一点对多点的情况下，使用短连接较为适合。
   >
   > 啥是长连接，字面意思理解，就是连接的时间长呗，没错确实是这么个意思，但定量上理解，不能一直这么长下去吧。确实不能，最终还是要断的，好好说吧，即是客户端和服务器端建立连接后，连接在一次通讯过后不会立即断开，依然存在，供后续的数据读写服务。客户端和服务器端通过心跳保持连接，在所有的读写结束后，断开连接。而短链接指的是建立连接--通讯--断开这样的一次通讯。通讯结束后即刻断开连接，释放资源。

3. select和epoll你了解么，区别在哪； 

   > 两种模式的区别：
   >
   > LT模式下，只要一个句柄上的事件一次没有处理完，会在以后调用epoll_wait时重复返回这个句柄，而ET模式仅在第一次返回。
   >
   > 两种模式的实现：
   >
   > 当一个socket句柄上有事件时，内核会把该句柄插入上面所说的准备就绪list链表，这时我们调用epoll_wait，会把准备就绪的socket拷贝到用户态内存，然后清空准备就绪list链表，最后，epoll_wait检查这些socket，如果是LT模式，并且这些socket上确实有未处理的事件时，又把该句柄放回到刚刚清空的准备就绪链表。所以，LT模式的句柄，只要它上面还有事件，epoll_wait每次都会返回。

   > select缺点:
   >
   > 最大并发数限制：使用32个整数的32位，即32*32=1024来标识fd，虽然可修改，但是有以下第二点的瓶颈；
   > 效率低：每次都会线性扫描整个fd_set，集合越大速度越慢；
   > 内核/用户空间内存拷贝问题。
   > epoll的提升：
   >
   > 本身没有最大并发连接的限制，仅受系统中进程能打开的最大文件数目限制；
   > 效率提升：只有活跃的socket才会主动的去调用callback函数；
   > 省去不必要的内存拷贝：epoll通过内核与用户空间mmap同一块内存实现。
   > 当然，以上的优缺点仅仅是特定场景下的情况：高并发，且任一时间只有少数socket是活跃的。
   >
   > 如果在并发量低，socket都比较活跃的情况下，select就不见得比epoll慢了（就像我们常常说快排比插入排序快，但是在特定情况下这并不成立）。

4. TCP UDP区别；三次握手四次挥手讲一下； 

三次握手
   >    ```
   >    （1）第一次握手：
   >    Client将标志位SYN置为1，随机产生一个值seq=J，并将该数据包发送给Server，Client进入SYN_SENT状态，等待Server确认。
   >    （2）第二次握手：
   >    Server收到数据包后由标志位SYN=1知道Client请求建立连接，Server将标志位SYN和ACK都置为1，ack=J+1，随机产生一个值seq=K，并将该数据包发送给Client以确认连接请求，Server进入SYN_RCVD状态。
   >    （3）第三次握手：
   >    Client收到确认后，检查ack是否为J+1，syn是否为1，如果正确则将标志位ACK置为1，ack=k+1，并将该数据包发送给Server，Server检查ack是否为K+1，ACK是否为1，如果正确则连接建立成功，
   >    Client和Server进入ESTABLISHED状态，完成三次握手，随后Client与Server之间可以开始传输数据了。
   >    ```

四次握手

   > ```
   > 第一次挥手：
   > Client发送一个FIN，用来关闭Client到Server的数据传送，Client进入FIN_WAIT_1状态。
   > 第二次挥手：
   > Server收到FIN后，发送一个ACK给Client，确认序号为收到序号+1（与SYN相同，一个FIN占用一个序号），Server进入CLOSE_WAIT状态。
   > 第三次挥手：
   > Server发送一个FIN，用来关闭Server到Client的数据传送，Server进入LAST_ACK状态。
   > 第四次挥手：
   > Client收到FIN后，Client进入TIME_WAIT_2状态，接着发送一个ACK给Server，确认序号为收到序号+1，Server进入CLOSED状态，完成四次挥手。
   > ```

为啥链接是三次握手,而关闭是四次握手

> ```
> 这是因为服务端在LISTEN状态下，收到建立连接请求的SYN报文后，把ACK和SYN放在一个报文里发送给客户端。而关闭连接时，当收到对方的FIN报文时，
> 仅仅表示对方不再发送数据了但是还能接收数据，己方也未必全部数据都发送给对方了，所以己方可以立即close，也可以发送一些数据给对方后，
> 再发送FIN报文给对方来表示同意现在关闭连接，因此，己方ACK和FIN一般都会分开发送。
> ```


5. TIME_WAIT过多是因为什么； 
6. http一次连接的全过程：你来说下从用户发起request——到用户接收到response； 

> 1.用户向浏览器输入网址
> 2.浏览器向DNS服务器查询域名对应的ip地址
> 3.浏览器向服务器发送HTTP请求(建立了TCP/IP)连接
> 4.**服务器的永久重定向响应**
> 5.浏览器跟踪重定向地址
> 6.服务器处理请求nginx-->uwsgi--->WEB程序
> 7.根据WEB程序处理结果返回response请求


5. http连接方式。get和post的区别，你还了解其他的方式么； 

   > 超文本传输协议(HyperText Transfer Protocol -- HTTP)是一个设计来使客户端和服务器顺利进行通讯的协议。
   >
   > HTTP在客户端和服务器之间以request-response protocol（请求-回复协议）工作。

   > GET：Get， 它用于获取信息，注意，他只是获取、查询数据，也就是说它不会修改服务器上的数据，从这点来讲，它是数据安全的不包含主体；
   > POST：Post，它是可以向服务器发送修改请求，从而修改服务器的。	包含主体。

6. restful你知道么； 

   > RESTful是一种软件架构风格、设计风格，而**不是**标准，只是提供了一组设计原则和约束条件。
   >
   > 表现层状态转换,例如:GTE表示获取资源,POST表示新建资源,PUT更新资源,DELETE表示删除资源
   >
   > * 每个URL代表一种资源
   > * 客户端和服务器之间,传递这种资源的某种表现层
   > * 客户 

7. 状态码你知道多少，比如200/403/404/504等等；

   > - 200("OK")
   >   一切正常。实体主体中的文档（若存在的话）是某资源的表示。
   > - 500("Bad Request")
   >   客户端方面的问题。实体主题中的文档（若存在的话）是一个错误消息。希望客户端能够理解此错误消息，并改正问题。
   > - 500("Internal Server Error")
   >   服务期方面的问题。实体主体中的文档（如果存在的话）是一个错误消息。该错误消息通常无济于事，因为客户端无法修复服务器方面的问题。
   > - 301("Moved Permanently")
   >   当客户端触发的动作引起了资源URI的变化时发送此响应代码。另外，当客户端向一个资源的旧URI发送请求时，也发送此响应代码。
   > - 404("Not Found") 和410("Gone")
   >   当客户端所请求的URI不对应于任何资源时，发送此响应代码。404用于服务器端不知道客户端要请求哪个资源的情况；410用于服务器端知道客户端所请求的资源曾经存在，但现在已经不存在了的情况。
   > - 409("Conflict")
   >   当客户端试图执行一个”会导致一个或多个资源处于不一致状态“的操作时，发送此响应代码。
   > - 403("Forbidden")
   >   重要程度：中等。
   >
   > 客户端请求的结构正确，但是服务器不想处理它。这跟证书不正确的情况不同--若证书不正确，应该发送响应代码401。该响应代码常用于一个资源只允许在特定时间段内访问，
   > 或者允许特定IP地址的用户访问的情况。403暗示了所请求的资源确实存在。跟401一样，若服务器不想透露此信息，它可以谎报一个404。既然客户端请求的结构正确，那为什么还要把本响应代码放在4XX系列（客户端错误），而不是5XX系列（服务端错误）呢？因为服务器不是根据请求的结构，而是根据请求的其他方面（比如说发出请求的时间）作出的决定的。
   >
   > - 503("Service Unavailable")
   >   重要程度：中等到高。
   >
   > 此响应代码表明HTTP服务器正常，只是下层web服务服务不能正常工作。最可能的原因是资源不足：服务器突然收到太多请求，以至于无法全部处理。由于此问题多半由客户端反复发送请求造成，因此HTTP服务器可以选择拒绝接受客户端请求而不是接受它，并发送503响应代码。
   >
   > 响应报头：服务器可以通过Retry-After报头告知客户端何时可以重试。



#### 数据库部分

1. MySQL锁有几种；死锁是怎么产生的； 

   > **1.表级锁定（table-level）**
   > 开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低。
   > **2.行级锁定（row-level）**
   > 开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高。
   > **3.页级锁定（page-level）**
   > 开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般。

   死锁产生原因

   > 是指两个或两个以上的进程在执行过程中,因争夺资源而造成的一种互相等待的现象,若无外力作用，它们都将无法推进下去.此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。表级锁不会产生死锁.所以解决死锁主要还是针对于最常用的InnoDB。
   >
   > 死锁的关键在于：两个(或以上)的Session加锁的顺序不一致。
   >
   > 那么对应的解决死锁问题的关键就是：让不同的session加锁有次序

2. 为何，以及如何分区、分表；

   > 1为了保证数据的完整性，需要对表进行表锁定或者行锁定。
   >
   > 2我们的数据库数据越来越大，随之而来的是单个表中数据太多，以至于查询速度过慢，而且由于表的锁机制导致应用操作也受到严重影响，出现数据库性能瓶颈。

   >
   > 分区
   >  就是把一张表的数据分成N个区块，在逻辑上看最终只是一张表，但底层是由N个物理区块组成的
   >
   > 分表
   >  就是把一张数据量很大的表按一定的规则分解成N个具有独立存储空间的实体表。系统读写时需要根据定义好的规则得到对应的字表明，然后操作它。表名可以按照某种业务hash进行映射。
   >
   > 分库
   >  一旦分表，一个库中的表会越来越多

3. MySQL的char varchar text的区别； 

   > **char：**存储定长数据很方便，CHAR字段上的索引效率级高，必须在括号里定义长度，可以有默认值，比如定义char(10)，那么不论你存储的数据是否达到了10个字节，都要占去10个字节的空间（自动用空格填充），且在检索的时候后面的空格会隐藏掉，所以检索出来的数据需要记得用什么trim之类的函数去过滤空格。
   >
   > **varchar：**存储变长数据，但存储效率没有CHAR高，必须在括号里定义长度，可以有默认值。保存数据的时候，不进行空格自动填充，而且如果数据存在空格时，当值保存和检索时尾部的空格仍会保留。另外，varchar类型的实际长度是它的值的实际长度+1，这一个字节用于保存实际使用了多大的长度。

   > 1、经常变化的字段用varchar；
   >
   > 2、知道固定长度的用char；
   >
   > 3、超过255字节的只能用varchar或者text；
   >
   > 4、能用varchar的地方不用text；
   >
   > 5、能够用数字类型的字段尽量选择数字类型而不用字符串类型，这会降低查询和连接的性能，并会增加存储开销。这是因为引擎在处理查询和连接回逐个比较字符串中每一个字符，而对于数字型而言只需要比较一次就够了；
   >
   > 6、同一张表出现多个大字段，能合并时尽量合并，不能合并时考虑分表

4. 了解join么，有几种，有何区别，A LEFT JOIN B，查询的结果中，B没有的那部分是如何显示的（NULL）； 

   > JOIN的含义就如英文单词“join”一样，连接两张表，大致分为内连接，外连接，右连接，左连接，自然连接。
   >
   > 这样的话 left join 和 right join可能会出现null字段, 因为在左(右)表中的全部数据不一定在右表(左表)都右匹配，这样没有匹配到的话就会出现null字段

5. 索引类型有几种，BTree索引和hash索引的区别（我没答上来这俩在磁盘结构上的区别）； 

   > **主要 MyISAM 与 InnoDB 两个引擎，其主要区别如下：**
   >
   > **一、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM就不可以了；**
   >
   > **二、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到安全性较高的应用；**
   >
   > **三、InnoDB 支持外键，MyISAM 不支持；**
   >
   > **四、MyISAM 是默认引擎，InnoDB 需要指定；**
   >
   > **五、InnoDB 不支持 FULLTEXT 类型的索引；**
   >
   > **六、InnoDB 中不保存表的行数，如 select count(\*) from table 时，InnoDB；需要扫描一遍整个表来计算有多少行，但是 MyISAM 只要简单的读出保存好的行数即可。注意的是，当 count(\*)语句包含 where 条件时 MyISAM 也需要扫描整个表；**
   >
   > **七、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM表中可以和其他字段一起建立联合索引；**
   >
   > **八、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；**
   >
   > **九、InnoDB 支持行锁（某些情况下还是锁整表，如 update table set a=1 where  user like '%lee%'**

6. 手写：如何对查询命令进行优化； 

   > 1.对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引。
   > 2.应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描，如：select id from t where num is null可以在num上设置默认值0，确保表中num列没有null值，然后这样查询：select id from t where num=0
   > 3.应尽量避免在 where 子句中使用!=或<>操作符，否则引擎将放弃使用索引而进行全表扫描。
   > 4.应尽量避免在 where 子句中使用or 来连接条件，否则将导致引擎放弃使用索引而进行全表扫描，如：select id from t where num=10 or num=20可以这样查询：select id from t where num=10 union all select id from t where num=20
   > 5.in 和 not in 也要慎用，否则会导致全表扫描，如：select id from t where num in(1,2,3) 对于连续的数值，能用 between 就不要用 in 了：select id from t where num between 1 and 3
   > 6.下面的查询也将导致全表扫描：select id from t where name like ‘%李%’若要提高效率，可以考虑全文检索。
   > 7.如果在 where 子句中使用参数，也会导致全表扫描。因为SQL只有在运行时才会解析局部变量，但优化程序不能将访问计划的选择推迟到运行时；它必须在编译时进行选择。然 而，如果在编译时建立访问计划，变量的值还是未知的，因而无法作为索引选择的输入项。如下面语句将进行全表扫描：select id from t where num=@num可以改为强制查询使用索引：select id from t with(index(索引名)) where num=@num
   > 8.应尽量避免在 where 子句中对字段进行表达式操作，这将导致引擎放弃使用索引而进行全表扫描。如：select id from t where num/2=100应改为:select id from t where num=100*2
   > 9.应尽量避免在where子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描。如：select id from t where substring(name,1,3)=’abc’ ，name以abc开头的id应改为:
   > select id from t where name like ‘abc%’
   >
   > 10.不要在 where 子句中的“=”左边进行函数、算术运算或其他表达式运算，否则系统将可能无法正确使用索引。
   > 11.在使用索引字段作为条件时，如果该索引是复合索引，那么必须使用到该索引中的第一个字段作为条件时才能保证系统使用该索引，否则该索引将不会被使用，并且应尽可能的让字段顺序与索引顺序相一致。
   > 12.不要写一些没有意义的查询，如需要生成一个空表结构：select col1,col2 into #t from t where 1=0
   > 这类代码不会返回任何结果集，但是会消耗系统资源的，应改成这样： 
   > create table #t(…)
   >
   > 13.很多时候用 exists 代替 in 是一个好的选择：select num from a where num in(select num from b)
   > 用下面的语句替换： 
   > select num from a where exists(select 1 from b where num=a.num)
   >
   > 14.并不是所有索引对查询都有效，SQL是根据表中数据来进行查询优化的，当索引列有大量数据重复时，SQL查询可能不会去利用索引，如一表中有字段sex，male、female几乎各一半，那么即使在sex上建了索引也对查询效率起不了作用。
   >
   > 15.索引并不是越多越好，索引固然可 以提高相应的 select 的效率，但同时也降低了 insert 及 update 的效率，因为 insert 或 update 时有可能会重建索引，所以怎样建索引需要慎重考虑，视具体情况而定。一个表的索引数最好不要超过6个，若太多则应考虑一些不常使用到的列上建的索引是否有 必要。
   > 16.应尽可能的避免更新 clustered 索引数据列，因为 clustered 索引数据列的顺序就是表记录的物理存储顺序，一旦该列值改变将导致整个表记录的顺序的调整，会耗费相当大的资源。若应用系统需要频繁更新 clustered 索引数据列，那么需要考虑是否应将该索引建为 clustered 索引。
   > 17.尽量使用数字型字段，若只含数值信息的字段尽量不要设计为字符型，这会降低查询和连接的性能，并会增加存储开销。这是因为引擎在处理查询和连接时会逐个比较字符串中每一个字符，而对于数字型而言只需要比较一次就够了。
   > 18.尽可能的使用 varchar/nvarchar 代替 char/nchar ，因为首先变长字段存储空间小，可以节省存储空间，其次对于查询来说，在一个相对较小的字段内搜索效率显然要高些。
   > 19.任何地方都不要使用 select * from t ，用具体的字段列表代替“*”，不要返回用不到的任何字段。
   > 20.尽量使用表变量来代替临时表。如果表变量包含大量数据，请注意索引非常有限（只有主键索引）。
   > 21.避免频繁创建和删除临时表，以减少系统表资源的消耗。
   > 22.临时表并不是不可使用，适当地使用它们可以使某些例程更有效，例如，当需要重复引用大型表或常用表中的某个数据集时。但是，对于一次性事件，最好使用导出表。
   > 23.在新建临时表时，如果一次性插入数据量很大，那么可以使用 select into 代替 create table，避免造成大量 log ，以提高速度；如果数据量不大，为了缓和系统表的资源，应先create table，然后insert。
   > 24.如果使用到了临时表，在存储过程的最后务必将所有的临时表显式删除，先 truncate table ，然后 drop table ，这样可以避免系统表的较长时间锁定。
   > 25.尽量避免使用游标，因为游标的效率较差，如果游标操作的数据超过1万行，那么就应该考虑改写。
   > 26.使用基于游标的方法或临时表方法之前，应先寻找基于集的解决方案来解决问题，基于集的方法通常更有效。
   > 27.与临时表一样，游标并不是不可使 用。对小型数据集使用 FAST_FORWARD 游标通常要优于其他逐行处理方法，尤其是在必须引用几个表才能获得所需的数据时。在结果集中包括“合计”的例程通常要比使用游标执行的速度快。如果开发时 间允许，基于游标的方法和基于集的方法都可以尝试一下，看哪一种方法的效果更好。
   > 28.在所有的存储过程和触发器的开始处设置 SET NOCOUNT ON ，在结束时设置 SET NOCOUNT OFF 。无需在执行存储过程和触发器的每个语句后向客户端发送DONE_IN_PROC 消息。
   > 29.尽量避免大事务操作，提高系统并发能力。
   > 30.尽量避免向客户端返回大数据量，若数据量过大，应该考虑相应需求是否合理。

7. NoSQL了解么，和关系数据库的区别；redis有几种常用存储类型；

   > 非关系型数据库具有**原子性、一致性隔离性**和吃就行吧
   >
   > String（字符串）Hash（哈希）List（列表）Set（集合）zset(sorted set：有序集合)

| 类型                 | 简介                                                   | 特性                                                         | 场景                                                         |
| :------------------- | :----------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| String(字符串)       | 二进制安全                                             | 可以包含任何数据,比如jpg图片或者序列化的对象,一个键最大能存储512M | ---                                                          |
| Hash(字典)           | 键值对集合,即编程语言中的Map类型                       | 适合存储对象,并且可以像数据库中update一个属性一样只修改某一项属性值(Memcached中需要取出整个字符串反序列化成对象修改完再序列化存回去) | 存储、读取、修改用户属性                                     |
| List(列表)           | 链表(双向链表)                                         | 增删快,提供了操作某一段元素的API                             | 1,最新消息排行等功能(比如朋友圈的时间线) 2,消息队列          |
| Set(集合)            | 哈希表实现,元素不重复                                  | 1、添加、删除,查找的复杂度都是O(1) 2、为集合提供了求交集、并集、差集等操作 | 1、共同好友 2、利用唯一性,统计访问网站的所有独立ip 3、好友推荐时,根据tag求交集,大于某个阈值就可以推荐 |
| Sorted Set(有序集合) | 将Set中的元素增加一个权重参数score,元素按score有序排列 | 数据插入集合时,已经进行天然排序                              | 1、排行榜 2、带权重的消息队列                                |

#### Linux部分

1. 讲一下你常用的Linux/git命令和作用； 
----Linux命令和作用----------
 ```shell
 tar –xvf file.tar //解压 tar包
 tar -xzvf file.tar.gz //解压tar.gz
 tar -xjvf file.tar.bz2 //解压 tar.bz2
 tar –xzvf file.tar.Z //解压tar.Z
 tail -n 数字 文件名 查看文件后多少行的内容
 ps 对系统中进程进行监测控制
grep 命令通常与管道命令一起使用，用于对一些命令的输出进行筛选加工等等
cp 复制
chmod 修改文件权限
vim 文本编辑
 ```
----git命令和作用-------------
```shell
git init [project-name]  新建一个目录，将其初始化为Git代码库
git clone 克隆代码
git pull 下拉远程仓库代码到本地
git add . 添加当前目录的所有文件到暂存区
git commit -m [message]  提交暂存区到本地仓库区
git push 推送本地仓库代码到远程仓库
git branch 查看所有本地分支
git checkout -b [branch] 新建一个分支，并切换到该分支
git checkout [branch-name]  切换到指定分支，并更新工作区
git status  显示有变更的文件
git diff HEAD  显示工作区与当前分支最新commit之间的差异
git reflog 显示当前分支的最近几次提交
```
-----------------git merge [branch]   合并指定分支到当前分支------------------


2. 查看当前进程是用什么命令，除了文件相关的操作外，你平时还有什么操作命令； 
`ps -aux | grep 
kill -9 PID 杀死指定进程`


#### django项目部分

1. 都是让简单的介绍下你在公司的项目，不管是不是后端相关的，主要是要体现出你干了什么； 

2. 你在项目中遇到最难的部分是什么，你是怎么解决的； 略

3. 你看过django的admin源码么；看过flask的源码么；你如何理解开源； 

4. MVC / MTV；

> ----所谓MVC就是把web应用分为模型(M),控制器(C),视图(V)三层；他们之间以一种插件似的，松耦合的方式连接在一起。
> 模型负责业务对象与数据库的对象(ORM),视图负责与用户的交互(页面)，控制器(C)接受用户的输入调用模型和视图完成用户的请求。
   > ----Django的MTV模式本质上与MVC模式没有什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同，Django的MTV分别代表：
   >     Model(模型)：负责业务对象与数据库的对象(ORM)
   >     Template(模版)：负责如何把页面展示给用户
   >     View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
   >     此外，Django还有一个url分发器，它的作用是将一个个URL的页面请求分发给不同的view处理，view再调用相应的Model和Template

5. 缓存怎么用； 

  > 使用缓存的目的就是减少数据库访问次数降低数据库的压力和提升程序的响应时间
  > --先更新数据库，再更新缓存
  > --先删缓存，再更新数据库
  > 以上两者容易出现脏数据--------------
  > --先更新数据库，再删缓存

6. 中间件是干嘛的； 

  > 中间件是一种独立的系统软件或服务程序，介于操作系统和应用软件之间，分布式应用软件借助这种软件在不同的技术之间共享资源。
  > 中间件位于客户机/ 服务器的操作系统之上，管理计算机资源和网络通讯。通过中间件，应用程序可以工作于多平台或 OS 环境。
  > 比较出名的中间件产品有方正飞鸿SOA中间件

7. CSRF是什么，django是如何避免的；XSS呢； 

  > -----CSRF（Cross-site request forgery）跨站请求伪造，也被称为“One Click Attack”或者Session Riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。
  > 尽管听起来像跨站脚本（XSS），但它与XSS非常不同，XSS利用站点内的信任用户，而CSRF则通过伪装成受信任用户的请求来利用受信任的网站。
  > 与XSS攻击相比，CSRF攻击往往不大流行（因此对其进行防范的资源也相当稀少）和难以防范，所以被认为比XSS更具危险性。
  > -----在网页中加入csrf_token的标签就可以通过csrf校验
  > -----跨站脚本攻击(Cross Site Scripting)，为了不和层叠样式表(Cascading Style Sheets, CSS)的缩写混淆，故将跨站脚本攻击缩写为XSS。
  > 恶意攻击者往Web页面里插入恶意的Script代码，当用户浏览该页之时，嵌入其中Web里面的Script代码会被执行，从而达到恶意攻击用户的目的。

8. 如果你来设计login，简单的说一下思路； 

   > get请求来展示登录页面
   >
   > post 请求携带将用户名和密码
   >
   > 后端接收请求
   >
   > 验证 （用户名和密码）————多账号
   >
   > 处理————更新一下登录时间。。。
   >
   > 成功则返回到之前页面（根据第一次请求的查询字符串）
   >
   > 失败提示用户名或密码错误

9. session和cookie的联系与区别；session为什么说是安全的； 

  > cookie和session的共同之处在于：cookie和session都是用来跟踪浏览器用户身份的会话方式。
  > cookie 和session的区别是：cookie数据保存在客户端，session数据保存在服务器端。

10. uWSGI和Nginx的作用； 

    > WSGI（Python Web Server GateWay Interface）:它是用在 python web 框架编写的应用程序与后端服务器之间的规范让你写的应用程序可以与后端服务器顺利通信。在 WSGI 出现之前你不得不专门为某个后端服务器而写特定的 API，并且无法更换后端服务器， **WSGI 就是一种统一规范， 所有使用 WSGI 的服务器都可以运行使用 WSGI 规范的 web 框架，反之亦然。**
    >
    > uWSGI: 是一个Web服务器，它实现了WSGI协议、uwsgi、http等协议。用于接收前端服务器转发的动态请求并处理后发给 web 应用程序。
    >
    > uwsgi: 是uWSGI服务器实现的独有的协议， 网上没有明确的说明这个协议是用在哪里的，我个人认为它是用于前端服务器与 uwsgi 的通信规范，相当于 FastCGI的作用。当然这只是个人见解，我在知乎进行了相关提问，欢迎共同讨论。
