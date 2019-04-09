# Multiprocessing-子进程返回值

​	在实际使用多进程的时候，可能需要获取到子进程运行的返回值。如果只是用来存储，则可以将返回值保存到一个数据结构中；如果需要判断此返回值，从而决定是否继续执行所有子进程，则会相对比较复杂。另外在Multiprocessing中，可以利用Process与Pool创建子进程，这两种用法在获取子进程返回值上的写法上也不相同。这篇中，我们直接上代码，分析多进程中获取子进程返回值的不同用法，以及优缺点。

## 初级用法（Pool）

目的：存储子进程返回值

说明：如果只是单纯的存储子进程返回值，则可以使用Pool的apply_async异步进程池；当然也可以使用Process，用法与threading中的相同，这里只介绍前者。

实例：当进程池中所有子进程执行完毕后，输出每个子进程的返回值。

```python
from multiprocessing import Pool
def test(p):     
    return p
if __name__=="__main__":
    pool = Pool(processes=10)
    result=[]
    for i  in xrange(50000):
       '''
       for循环执行流程：
       （1）添加子进程到pool，并将这个对象（子进程）添加到result这个列表中。（此时子进程并没有运行）
       （2）执行子进程（同时执行10个）
       '''
       result.append(pool.apply_async(test, args=(i,)))#维持执行的进程总数为10，当一个进程执行完后添加新进程.       
    pool.join()
    '''
    遍历result列表，取出子进程对象，访问get()方法，获取返回值。（此时所有子进程已执行完毕）
    '''
    for i in result:
        print i.get()
```

错误:

```python
for i  in xrange(50000):
   t=pool.apply_async(test, args=(i,)))
   print t.get()
```

说明：这样会造成阻塞，因为get()方法只能等子进程运行完毕后才能调用成功，否则会一直阻塞等待。如果写在for循环内容，相当于变成了同步，执行效率将会非常低。

## 高级用法（Pool）

目的：父进程实时获取子进程返回值，以此为标记结束所有进程。

### 实例（一）

执行子进程的过程中，不断获取返回值并校验，如果返回值为True则结果所有进程。

```python
from multiprocessing import Pool
import Queue
import time
def test(p):
    time.sleep(0.001)
    if p==10000:
        return True
    else:
        return False
if __name__=="__main__":
    pool = Pool(processes=10)
    q=Queue.Queue()
    for i  in xrange(50000):
    	'''
    	将子进程对象存入队列中。
    	'''
        q.put(pool.apply_async(test, args=(i,)))#维持执行的进程总数为10，当一个进程执行完后添加新进程.       
    '''
    因为这里使用的为pool.apply_async异步方法，因此子进程执行的过程中，父进程会执行while，获取返回值并校验。
    '''
    while 1:
        if q.get().get():
            pool.terminate() #结束进程池中的所有子进程。
            break
    pool.join()
```

说明：总共要执行50000个子进程（并发数量为10），当其中一个子进程返回True时，结束进程池。因为使用了apply_async为异步进程，因此在执行完for循环的添加子进程操作后（只是添加并没有执行完所有的子进程），可以直接执行while代码，实时判断子进程返回值是否有True，有的话结束所有进程。

优点：不必等到所有子进程结束再结束程序，只要得到想要的结果就可以提前结束，节省资源。

不足：当需要执行的子进程非常大时，不适用，因为for循环在添加子进程时，要花费很长的时间，虽然是异步，但是也需要等待for循环添加子进程操作结束才能执行while代码，因此会比较慢。

### 实例（二）

多线程+多进程，添加执行子进程的过程中，不断获取返回值并校验，如果返回值为True则结果所有进程。

```python
from multiprocessing import Pool
import Queue
import threading
import time
def test(p):
    time.sleep(0.001)
    if p==10000:
        return True
    else:
        return False
if __name__=="__main__":
    result=Queue.Queue() #队列
    pool = Pool()
    def pool_th():
        for i  in xrange(50000000): ##这里需要创建执行的子进程非常多
            try:
                result.put(pool.apply_async(test, args=(i,)))
            except:
                break
    def result_th():
        while 1:
            a=result.get().get() #获取子进程返回值
            if a:
                pool.terminate() #结束所有子进程
                break
    '''
    利用多线程，同时运行Pool函数创建执行子进程，以及运行获取子进程返回值函数。
    '''
    t1=threading.Thread(target=pool_th)
    t2=threading.Thread(target=result_th)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pool.join()
```

执行流程：利用多线程，创建一个执行pool_th函数线程，一个执行result_th函数线程，pool_th函数用来添加进程池，开启进程执行功能函数并将子进程对象存入队列，而result_th()函数用来不停地从队列中取子进程对象，调用get（）方法获取返回值。等发现其中存在子进程的返回值为True时，结束所有进程，最后结束线程。

优点：弥补了实例（一）的不足，即使for循环的子进程数量很多，也能提高性能，因为for循环与判断子进程返回值同时进行。