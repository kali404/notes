# 序. multiprocessing

python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。Python提供了非常好用的多进程包==multiprocessing==，只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到**并发执行**的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。

> Process（用于创建进程模块）
>
> Pool（用于创建管理进程池）
>
> Queue（用于进程通信，资源共享）
>
> Value，Array（用于进程通信，资源共享）
>
> Pipe（用于管道通信）
>
> Manager（用于资源共享）

## 1. Process

Process模块用来创建子进程，是Multiprocessing核心模块，使用方式与Threading类似，可以实现多进程的创建，启动，关闭等操作。

#### 创建进程的类:

Process([group [, target [, name [, args [, kwargs]]]]])

> #### target	表示调用对象，要执行的方法,或者是函数
>
> args	表示调用对象的位置参数元组。
> kwargs	表示调用对象的字典。
> name	为进程名字。
> group	线程组,目前还没实现,库引用中必须是None。

#### **方法**：

> is_alive()：返回进程是否在运行。
>
> join([timeout])：阻塞当前上下文环境的进程程，直到调用此方法的进程终止或到达指定的timeout（可选参数）。
>
> start()：进程准备就绪，等待CPU调度。
>
> run()：strat()调用run方法，如果实例进程时未制定传入target，这star执行t默认run()方法。
>
> terminate()：不管任务是否完成，立即停止工作进程。

#### **属性**：

> authkey
> daemon：和线程的setDeamon功能一样（将父进程设置为守护进程，当父进程结束时，子进程也结束）。
> exitcode(进程在运行时为None、如果为–N，表示被信号N结束）。
> name：进程名字。
> pid：进程号。

```python
from multiprocessing import Process  #导入Process模块 
import os  
def test(name):
	'''
	函数输出当前进程ID，以及其父进程ID。
	此代码应在Linux下运行，因为windows下os模块不支持getppid()
	'''
    print "Process ID： %s" % (os.getpid())  
    print "Parent Process ID： %s" % (os.getppid())  
if __name__ == "__main__": 
	'''
	windows下，创建进程的代码一下要放在main函数里面
	''' 
    proc = Process(target=test, args=('nmask',))  
    proc.start()  
    proc.join()
```



## 2.Pool

Pool模块是用来创建管理进程池的，当子进程非常多且需要控制子进程数量时可以使用此模块。
Multiprocessing.Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行它。在共享资源时，只能使用Multiprocessing.Manager类，而不能使用Queue或者Array。

#### 构造方法

Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

> processes ：使用的工作进程的数量，如果processes是None那么使用 os.cpu_count()返回的数量。
>
> initializer： 如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
>
> maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
>
> context: 用在制定工作进程启动时的上下文，一般使用 multiprocessing.Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context。

#### 实例方法

- apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞。
- apply(func[, args[, kwds]])是阻塞的。
- close() 关闭pool，使其不在接受新的任务。
- terminate() 关闭pool，结束工作进程，不在处理未完成的任务。
- join() 主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。

#### Pool使用方法

说明：此写法缺点在于只能通过map向函数传递一个参数。

```python
# Pool+map函数
from multiprocessing import Pool
def test(i):
    print i
if __name__=="__main__":
	lists=[1,2,3]
	pool=Pool(processes=2) #定义最大的进程数
	pool.map(test,lists)        #p必须是一个可迭代变量。
	pool.close()
	pool.join()
```



## 3.Queue

Queue模块用来控制进程安全，与线程中的Queue用法一样。

## 4.Pipe

Pipe模块用来管道操作。

## 5.Manager

Manager模块常与Pool模块一起使用，作用是共享资源。

# （二）Multiprocessing进程管理模块

说明：由于篇幅有限，模块具体用法结束请参考每个模块的具体链接。

## Process模块

Process模块用来创建子进程，是Multiprocessing核心模块，使用方式与Threading类似，可以实现多进程的创建，启动，关闭等操作。

## Pool模块

Pool模块是用来创建管理进程池的，当子进程非常多且需要控制子进程数量时可以使用此模块。


## Queue模块

Queue模块用来控制进程安全，与线程中的Queue用法一样。

## Pipe模块

Pipe模块用来管道操作。

## Manager模块

Manager模块常与Pool模块一起使用，作用是共享资源。