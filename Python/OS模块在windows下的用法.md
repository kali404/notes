

# os模块win

在自动化测试中，经常需要查找操作文件，比如说查找配置文件（从而读取配置文件的信息），查找测试报告（从而发送测试报告邮件），经常要对大量文件和大量路径进行操作，这就依赖于os模块，所以今天整理下比较常用的几个方法。网上这方面资料也很多，每次整理，只是对自己所学的知识进行梳理，从而加深对某个模块的使用。

**1.当前路径及路径下的文件**

os.getcwd()：查看当前所在路径。

os.listdir(path):列举目录下的所有文件。返回的是列表类型。

```python
>>> import os
>>> os.getcwd()
'D:\\pythontest\\ostest'
>>> os.listdir(os.getcwd())
['hello.py', 'test.txt']
```

 

**2.绝对路径**

os.path.abspath(path):返回path的绝对路径。

```python
>>> os.path.abspath('.')
'D:\\pythontest\\ostest'
>>> os.path.abspath('..')
'D:\\pythontest'
```

 

**3.查看路径的文件夹部分和文件名部分**

os.path.split(path):将路径分解为(文件夹,文件名)，返回的是元组类型。可以看出，若路径字符串最后一个字符是\,则只有文件夹部分有值；若路径字符串中均无\,则只有文件名部分有值。若路径字符串有\，且不在最后，则文件夹和文件名均有值。且返回的文件夹的结果不包含\.

os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除。

```python
>>> os.path.split('D:\\pythontest\\ostest\\Hello.py')
('D:\\pythontest\\ostest', 'Hello.py')
>>> os.path.split('.')
('', '.')
>>> os.path.split('D:\\pythontest\\ostest\\')
('D:\\pythontest\\ostest', '')
>>> os.path.split('D:\\pythontest\\ostest')
('D:\\pythontest', 'ostest')
>>> os.path.join('D:\\pythontest', 'ostest')
'D:\\pythontest\\ostest'
>>> os.path.join('D:\\pythontest\\ostest', 'hello.py')
'D:\\pythontest\\ostest\\hello.py'
>>> os.path.join('D:\\pythontest\\b', 'D:\\pythontest\\a')
'D:\\pythontest\\a'
```

os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'

```python
>>> os.path.dirname('D:\\pythontest\\ostest\\hello.py')
'D:\\pythontest\\ostest'
>>> os.path.dirname('.')
''
>>> os.path.dirname('D:\\pythontest\\ostest\\')
'D:\\pythontest\\ostest'
>>> os.path.dirname('D:\\pythontest\\ostest')
'D:\\pythontest'
```

os.path.basename(path):返回path中的文件名。

```python
>>> os.path.basename('D:\\pythontest\\ostest\\hello.py')
'hello.py'
>>> os.path.basename('.')
'.'
>>> os.path.basename('D:\\pythontest\\ostest\\')
''
>>> os.path.basename('D:\\pythontest\\ostest')
'ostest'
```

**4.查看文件时间**

 os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。

 os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。

 os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数。

```python
>>> os.path.getmtime('D:\\pythontest\\ostest\\hello.py')
1481695651.857048
>>> os.path.getatime('D:\\pythontest\\ostest\\hello.py')
1481687717.8506615
>>> os.path.getctime('D:\\pythontest\\ostest\\hello.py')
1481687717.8506615
```

**5.查看文件大小**

  os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0。

```python
>>> os.path.getsize('D:\\pythontest\\ostest\\hello.py')
58L
>>> os.path.getsize('D:\\pythontest\\ostest')
0L
```

**6.查看文件是否存在**

 os.path.exists(path):文件或文件夹是否存在，返回True 或 False。

```python
>>> os.listdir(os.getcwd())
['hello.py', 'test.txt']
>>> os.path.exists('D:\\pythontest\\ostest\\hello.py')
True
>>> os.path.exists('D:\\pythontest\\ostest\\Hello.py')
True
>>> os.path.exists('D:\\pythontest\\ostest\\Hello1.py')
False
```

**7.一些表现形式参数**

os中定义了一组文件、路径在不同操作系统中的表现形式参数，如：

```python
>>> os.sep
'\\'
>>> os.extsep
'.'
>>> os.pathsep
';'
>>> os.linesep
'\r\n'
```

```python
import os
def new_file(test_dir):
    #列举test_dir目录下的所有文件（名），结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

#返回D:\pythontest\ostest下面最新的文件
print new_file('D:\\system files\\workspace\\selenium\\email126pro\\email126\\report')
```
```python
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.popen("bash command).read()  运行shell命令，获取执行结果
os.environ  获取系统环境变量

os.path
os.path.abspath(path) 返回path规范化的绝对路径 os.path.split(path) 将path分割成目录和文件名二元组返回 os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
                        即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path) 返回path的大小
```