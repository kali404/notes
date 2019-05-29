
```python
#获取当前工作目录
os.getcwd()
'E:\\BaiduYunDownload\\python自动化\\课程\\第六天'

#递归创建目录，父目录不存在时先创建父目录
os.makedirs('e:/test/c/c')

#创建目录，父目录不能为空
os.mkdir('e:/test/d')

#删除指定的目录且是空目录
os.rmdir('e:/test/b/c')

#递归删除空目录且是空目录
os.removedirs('e:/test/c/c')

#删除文件
os.remove("e:/a/test.txt")

#列出目录下的所有文件、目录
os.listdir('E:\\BaiduYunDownload\\python自动化\\课程\\第六天\\day6')
['20180421.py', 'logs', 'logs.zip', 'mkdir.py', 'my_db.py', 'nhy.py', 'stu.xls', 'test', 'tools.py', 'x.py', '__pycache__', '写excel.py', '加密模块.py']

#当前系统的路径的分隔符
so.sep
'\\'

#当前系统的换行符
os.linesep
'\r\n'


#执行当前系统命令
os.system('ipconfig')

#可以获取到命令执行的结果
os.popen('ipconfig').read()  

#获取绝对路径
os.path.abspath(__file__)

#分割路径和文件名
os.path.split("/usr/hehe/hehe.txt")
('/usr/hehe', 'hehe.txt')


#获取父目录
os.path.dirname('e:/test/c/1.txt')
'e:/test/c'

#获取路径最后一级
os.path.basename("e:\\syz\\ly-code\\a.txt")
'a.txt'
os.path.basename("e:\\syz\\ly-code")
'ly-code'

#判断文件是否存在
os.path.exists('e:/test/c/1.txt')
False

#判断是否是绝对路径
os.path.isabs("../day5")
False
os.path.isabs("e:/day5")
True

#判断是否是文件，判断的文件是存在的
os.path.isfile("xiaohei.py")
False

#判断文件夹、目录是否存在
os.path.isdir('e:/test/b')
True

#拼接路径
os.path.join('e\:', 'b', 'c')
'e\\:\\b\\c'

#获取文件大小
os.path.getsize('e:/test/b/1.txt')
9
```

```python
for abs_path,dir,file in os.walk(r'e:\test'): #获取目录下内容  
    print('{}, {}, {}'.format(abs_path, dir, file))

e:\test, ['a', 'b'], []
e:\test\a, [], []
e:\test\b, ['c'], ['1.txt']
e:\test\b\c, ['新建文件夹'], []
e:\test\b\c\新建文件夹, [], []

第一个是绝对路径，第二个每层目录下面有哪些文件夹，第三个是目录下的所有文件
```

```python

#加入临时环境变量
import os,sys
base_dir=os.path.dirname(__file__)
sys.path.append(base_dir)  #临时修改环境变量
import sys,os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))  #获取到程序的主目录
sys.path.insert(0,BASE_PATH)
 
```
