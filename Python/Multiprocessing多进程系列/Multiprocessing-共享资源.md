# Multiprocessing-共享资源

　　在使用多进程的过程中，最好不要使用共享资源，如果非得使用，则请往下看。Multiprocessing类中共享资源可以使用3种方式，分别是Queue，Array，Manager。这三个都是Multiprocessing自带的组件，使用起来也非常方便。注意：普通的全局变量是不能被子进程所共享的，只有通过Multiprocessing组件构造的数据结构可以被共享。

## Queue类

使用Multiprocessing.Queue类，共享资源（share memory）（只适用Process类)

```python
from multiprocessing import Process, Queue  
def test(queue):  
    queue.put("Hello World")  
if __name__ == '__main__':
    q = Queue()  
    p = Process(target=test, args=(q,))  #需要将q对象传递给子进程
    p.start()
    print q.get()
```

缺点：不能再Pool进程池中使用。

## Array、Value类

使用Multiprocessing.Array类，共享资源（share memory）（只适用于Process类)

```python
from multiprocessing import Process, Array
def test(a):
    for i in range(len(a)):
        a[i] = -a[i]
if __name__ == '__main__':
    arr = Array('i', range(10))
    p = Process(target=test, args=(arr))  #需要将arr对象传递给子进程
    p.start()
    p.join()
    print arr[:]
```

缺点：无法与Pool一起使用。

## Manager类

使用Multiprocessing.Manager类，共享资源。（可以适用Pool类）

说明：由于windows操作系统下，创建Multiprocessing类对象代码一定要放在main()函数下，而linux不需要，因此这里区分2个版本。

实例目的：父进程在执行子进程的过程中，同步判断一个公共资源值，如果满足条件则结束所有进程。

### linux版本

```python
from multiprocessing import Manager,Pool
lists=Manager().list()    ##定义可被子进程共享的全局变量lists
def test(i):
     print i
     lists.append(i)
if __name__=="__main__":
    pool=Pool()
    for i in xrange(10000000):
    	'''
    	判断如果lists长度大于0，则不再往进程池中添加进程。
    	'''
        if len(lists)<=0:
            pool.apply_async(test,args=(i,))
        else:
            break
     pool.close()
     pool.join()
```

优点：可以跟Pool一起用，且速度比较快。

### windows版本

```python
from multiprocessing import Manager
def test(i,lists):
     print i
     lists.append(i)
if __name__=="__main__":
    pool=Pool()
    lists=Manager().list() #Manager类实例化代码只能写在main()函数里面
    for i in xrange(10000000):
        if len(lists)<=0:
        	'''
        	在创建子进程时，需要将lists对象传入，不然无法共享。
        	'''
            pool.apply_async(test,args=(i,lists))##需要将lists对象传递给子进程，这里比较耗资源，原因可能是因为Manager类是基于通信的。
        else:
            break
```

说明：与linux版本代码相比，windows下代码将lists的引用放在了main()之后，因为windows下只能在main函数下引用多进程。而在实例化子进程时，必须把Manager对象传递给子进程，否则lists无法被共享，而这个过程会消耗巨大资源，因此性能很差。