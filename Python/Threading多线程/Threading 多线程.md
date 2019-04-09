# Threading 多线程

在Python3中，通过threading模块提供线程的功能。原来的thread模块已废弃。但是threading模块中有个Thread类（大写的T，类名），是模块中最主要的线程类，一定要分清楚了，千万不要搞混了。

## threading方法

| 方法与属性         | 描述                                                         |
| ------------------ | :----------------------------------------------------------- |
| current_thread()   | 返回当前线程                                                 |
| active_count()     | 返回当前活跃的线程数，1个主线程+n个子线程                    |
| get_ident()        | 返回当前线程                                                 |
| enumerater()       | 返回当前活动 Thread 对象列表                                 |
| main_thread()      | 返回主 Thread 对象                                           |
| settrace(func)     | 为所有线程设置一个 trace 函数                                |
| setprofile(func)   | 为所有线程设置一个 profile 函数                              |
| stack_size([size]) | 返回新创建线程栈大小；或为后续创建的线程设定栈大小为 size    |
| TIMEOUT_MAX        | Lock.acquire(), RLock.acquire(), Condition.wait() 允许的最大超时时间 |

## threading下面的类

| 类名      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| Thread    | 基本线程类                                                   |
| Lock      | 互斥锁                                                       |
| Rlock     | 可重入锁,使得一个线程再次获得已持有的锁(递归锁)              |
| Condition | 条件锁，使得一个线程等待另一个线程满足特定条件，比如改变状态或某个值。 |
| Semaphore | 信号锁。为线程间共享的有限资源提供一个”计数器”，如果没有可用资源则会被阻塞。 |
| Event     | 事件锁，任意数量的线程等待某个事件的发生，在该事件发生后所有线程被激活 |
| Timer     | 一种计时器                                                   |
| Barrier   | Python3.2新增的“阻碍”类，必须达到指定数量的线程后才可以继续执行。 |

### Threadi类

Thread是线程类，有两种使用方法

#### 构造方法

`直接传入要运行的方法`

```python
# coding:utf-8
import threading
import time
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(1)
    print 'the arg is:%s\r' %arg

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'
```

> group: 线程组，目前还没有实现，库引用中提示必须是None； 
> target: 要执行的方法； 
> name: 线程名； 
> args/kwargs: 要传入方法的参数。

#### 实例方法

`从Thread继承并覆盖run():`

```python
# coding:utf-8
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print 'the arg is:%s\r' % self.arg

for i in xrange(4):
    t =MyThread(i)
    t.start()
    
```

> isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
>
> get/setName(name): 获取/设置线程名。 
>
> start():  线程准备就绪，等待CPU调度
>
> is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
>
> 如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
> 如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
>
> start(): 启动线程。 
>
> join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。

### Lock、Rlock类

由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。

Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

==Lock属于全局，Rlock属于线程==

**构造方法： Lock()，Rlock（)**
**推荐使用Rlock()**

**实例方法：**

> acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。 
> release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

例:

```python
# coding:utf-8
import threading
import time

g_num = 0


def show(rags):
    global g_num
    time.sleep(rags)
    g_num += 1
    print(g_num)


for i in range(10):
    t = threading.Thread(target=show, args=(1,))
    t.start()

print('我运行完啦!')
```

>   从运行结果我们可以看出多次运行会产生混乱,这种场景下就是适合使用锁的场景

例2

```python
# coding:utf-8

import threading
import time

gl_num = 0

lock = threading.RLock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print gl_num
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
```

>   运行结果就是12345678910

`Lock`

```python
#coding:utf-8
 
import threading
lock = threading.Lock() #Lock对象
lock.acquire()
lock.acquire()  #产生了死锁。
lock.release()
lock.release()
print lock.acquire()
```

`Rlock`

```python
import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire() #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()
```

### **Condition类**

　　Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

　　可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

#### 构造方法：

 Condition([lock/rlock])

#### 实例方法：

acquire([timeout])/release(): 调用关联的锁的相应方法。 
　　wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。 
　　notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
　　notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

例1

```python
# encoding: UTF-8
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()


# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print 'produce...'
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
#重复产生消费过程
```

例2:

```python
import threading
import time

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print "Producer(%s):deliver one, now products:%s" %(self.name, products)
                    condition.notify()#不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print "Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products)
                    condition.wait();#自动释放锁定
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print "Consumer(%s):consume one, now products:%s" %(self.name, products)
                    condition.notify()
                    condition.release()
                else:
                    print "Consumer(%s):only 1, stop consume, products:%s" %(self.name, products)
                    condition.wait();
                time.sleep(2)

if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 3):
        c = Consumer()
        c.start()
```

例3:

```python
import threading
 
alist = None
condition = threading.Condition()
 
def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()
 
def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()
 
def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()
 
tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()
```

### Event类

　　Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。

　　Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

**构造方法：**

​	Event()

**实例方法：** 　　

​	isSet(): 当内置标志为True时返回True。 
　　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。 
　　clear(): 将标志设为False。 
　　wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。

```python
# encoding: UTF-8
import threading
import time

event = threading.Event()


def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()

    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print 'MainThread set event.'
event.set()

```

运行

```python
Thread-1 wait for event...
Thread-2 wait for event...

#2秒后。。。
MainThread set event.
Thread-1 recv event.
 Thread-2 recv event.
```

### Timer类

Timer是Thread的派生类,用于在指定时间后调用一个方法。

**构造方法：** Timer(interval, function, args=[], kwargs={}) 

>   interval: 指定的时间 
>   function: 要执行的方法 
>   args/kwargs: 方法的参数

**实例方法:**

没有实例方法,因为Timer是Therad的派生类

```python
# encoding: UTF-8
import threading


def func():
    print 'hello timer!'


timer = threading.Timer(5, func)
timer.start()
#线程在5秒后执行
```

### local类

　　local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。

　　可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、再使用属性名作为key检索属性值的细节。

```python
# encoding: UTF-8
import threading
 
local = threading.local()
local.tname = 'main'
 
def func():
    local.tname = 'notmain'
    print local.tname
 
t1 = threading.Thread(target=func)
t1.start()
t1.join()
 
print local.tname
```

运行结果:

```python
notmain
main
```

