# 运维shell

### 作用

项目部署
项目监控

### 什么是shell

shell是一个程序,/bin/bash/,是一个命令解释器所有linux命令都由他来执行,打开终端就进入了 shell的交互式命令

### 运行方式

* bash *.sh
* 更改可执行权限后使用./*.sh来执行
* shource *.sh 

### 语法

* 没有缩进要求,缩进是没有意义的

* 注释使用`#`

* 双引号`""`内嵌入变量是解释变量

* 单引号`''`内写什么,就是什么,不会解释变量

* `shource`不会开启新的进程来执行脚本,可以跟当前窗口共享进程,以及变量`所以变量可以使用普通变量`

* 反引号&&`$()` 内嵌命令将命令执行之后的结果写进变量

* 变量的使用

  ```shell
  # 设 变量名为 name 且有值 调取变量方式如下
  echo $name
  echo ${name)
  echo "$name"
  echo "${name}" #规范写法
  ```

* 测试语句(判断)

  利用`text`和`[]`来结合内置变量`$?`来进行判断语句

  ```shell
  #方法1
  text 2 = 2 # 条件前后必须加空格
  $?
  #方法2
  [ 1 = 2 ] # `[]`内前后追加空格
  $?
  ```

`$?`结果0为真 1为假

### 变量

* 本地变量

  在当前系统的某个环境下生效的变量作用范围小

  * 普通变量

    只在当前命令窗口*环境*下才可以调用

  ```shell
  name=langwang  # 注意的是shell脚本是没有pep8的代码风格要求所以不需要加任何空格,加空格就会报错
  echo $name # $变量名 来使用本地变量,变量是没有类型的而且不能加入空格
  # 变量默认值  
  # a=1
  echo ${a-123} # 变量a如果有内容,那么就输出a的变量值
  # 变量a如果没有内容,那么就输出默认的内容,也就是123
  b=18
  echo ${b+22} #无论变量a是否有内容,都输出默认值,也就是22
  ```

* 命令变量

```shell
ml=`pwd` # 只是在当前环境下执行命令(给命令起了一个别名)
ml=$(pwd) #与上写法想同
```

  

* 全局变量

  当前shell以及其派生出来的子shell中都有效的变量。

  在当前以及子进程shell窗口都能加载全局变量

  ```shell
  env #查看全局变量
  name=xiao
  export name
  echo $name
  # 简写形式
  export age=112
  ```

  任何窗口下都可以使用的变量,全局变量永久有效

  ```shell
  sudo vim /etc/profile  #将变量写入这个文件即可实现在全局使用
  source /etc/profile
  ```

  

* shell内置变量

  可以直接拿过来使用实现某种具体的功能
  
  ```shell
  $0  # 获取当前shell脚本文件名
  ${n}  # 获取当前执行的shell脚本的第n个参数值，n=1..9，当n为0时表示脚本的文件名，如果n大于9就要用大括号括起来${10}
  $#  # 获取当前shell命令行中参数的总个数
  $?  # 获取执行上一个指令的返回值（0为成功，非0为失败）
  ```
  

#### 字符串操作

* 精确截取

```shell
file='hello world'
${file:0:5}		# 从第1个字符开始，截取5个字符
${file::5}		# 从第1个字符开始，截取5个字符
${file:5:5}		# 从第6个字符开始，截取5个字符
${file:5}		# 从第6个字符开始，截取后面所有的字符
${file:0-5}		# 从倒数第5个字符开始，截取后面所有的字符
${file:0-6:3}	# 从倒数第6个字符开始，截取之后的3个字符
```

### 条件表达式

`&&` :且,`命令1 &&  命令2`  命令1执行成功才会执行命令2 如果命令1 失败 则命令2不会执行

`||`: 或,`命令1 || 命令2`  如果命令1执行成功，那么命令2不执行   如果命令1执行失败，那么命令2执行

* 文件运算符

`-f` 判断是否是一个文件

`-d`判断是否为一个文件夹(目录)

`-e`判断文件或者目录是否存在

`-x`判断是否可执行

`-r`判断文件可读权限

`-w`判断文件可写权限

* 字符串比较运算符

 `-z` string  如果 string长度为零,则为真 

`-n`string 如果string 长度不为零,则为真

string1`=` string2  如果 string1与 string2相同，则为真 

string1 `!=` string2  如果 string1与 string2不同，则为真

* 算术比较运算符

`-eq`等于

`-ne`不等于

`-lt`小于

`-le`小于等于

`-gt`大于

`-ge`大于等于

* 计算表达式

`$(())`双括号内放计算表达式,只能加减乘除的整数运算

`let`表达式必须是一个整体，中间不能出现空格等特殊字符

```shell
age=10
echo $((age-8))
2
i=2
let i=age-i
echo $i
8
```

### 常见符号

* 重定向符号

  * `>`覆盖右侧 文件内容

    ```shell
    ls > a.txt #将ls输出结果覆盖写入a.txt
    ```

  * `>>`追加到右侧文件内容

  ```shell
  ls -alh >> a.txt  # 将文件输出结果追加写入
  ```

  *只把正确结果写入,如果想要把错误结果写入在`>`前加2,默认不写为1*

  ```shell
  bash xxx.sh 1> ak.txt 2> err.txt
  bash xxx.sh 1> a.text > &1  #正确错误都写入a.text
  ```

   

* 管道符

  * `|`

    命令1 | 命令2

    管道符左侧命令1 执行后的结果，**传递**给管道符右侧的命令2使用

* 其他

  * 后台展示符号 `&`

    就是将一个命令从前台转到后台执行

    引用

    ```shell
    ping www.baidu.com &
    ping www.baidu.com > /edv/null 2>&1 & #  正确错误的结果都丢进垃圾桶 
    ```

* 常用命令

  * grep

    * grep [参数] <文件名> [-r]#文件目录要加-r

      ```shell
      grep -n aa xxx.txt # 查找txt文件中的aa 并显示行号
      -n #显示行号
      -i #忽略大小写
      -v #不包含文件的所有行
      ```

  * find 

    * find [路径] [参数] [关键字] 

      ```shell
      -name # 查找文件名
      -type # 查找文件类型 下面是支持的常见文件类型
      -b # 块设备文件
      -d # 目录
      -c # 字符设备文件
      -p # 管道文件
      -l # 符号链接文件
      -f # 普通文件
      ```

### sed命令

* 行文件编辑工具

sed [参数] 条件 [动作] [文件名]

参数
参数为空	表示显示更改效果,不对文件进行编辑
-i  	  表示对文件进行编辑更改不会显示效果
条件
'/关键字/'
隔离符号可以为`#``@``!`根据具体情况进行使用
动作
a	匹配内容下一行增加内容
i	匹配内容上一行增加内容
d	删除匹配内容
s	替换匹配内容
*以上的动作 必须在-i参数下使用


  ```shell
 # 假设有文件123.txt其内容为
  # hello sed sed sed 
  # hello sed sed sed 
  sed "s#sed#SED#" 123.txt # 每一行匹配的第一个小写替换为大写,只是对修改进行展示,并不会对文件进行修改
  # 输出为
  # hello SED sed sed
  #	hello SED sed sed
  sed "s#sed#SED#g" 123.txt # 匹配的小写全部替换为大写,只是对修改进行展示,并不会对文件进行修改
  # 输出为
  # hello SED SED SED
  # hello SED SED SED
  sed "1s#sed#SED#" 123.txt # 对第一行第一个匹配的小写sed替换为大写,只是对修改进行展示,并不会对文件进行修改
  # 输出为
  # hello SED sed sed
  # hello sed sed sed
    sed "2s#sed#SED#2" 123.txt # 对第二行第二个匹配的小写替换为大写,只是对修改进行展示,并不会对文件进行修改
  # 输出为
  # hello SED SED SED
  # hello SED SED SED
  sed "a#hello" 123.txt # 对所有行进行增加,对修改进行展示,并不会对文件进行修改
  # 输出为
  #hello sed sed sed
  #hello
  #hello sed sed sed
  #hello
  sed "2a#hello2" 123.txt # 对所有行进行增加,对修改进行展示,并不会对文件进行修改
  # 输出为
  #hello sed sed sed
  #hello2
  #hello
  #hello sed sed sed
  #hello
  ```

  	不一一列举了

### awk命令

awk  [参数] '[动作]' [文件名]

参数

` -F`	指定分隔符号,默认为空格

`-v`	设置变量

`-f`	指定运行的awk脚本

动作

`print` 	显示内容

`$0` 	显示所有行列内容

`$n`	显示当前行第n列内容

常见内置变量

`FILENAME`  当前输入文件的文件名，该变量是只读的

`NR`     指定显示行的行号

`NF`     输出最后一列的内容

`OFS`     输出格式的列分隔符，缺省是空格

`FS`     输入文件的列分融符，缺省是连续的空格和Tab

#### 基本用法

 一段文本：cat log.txt 

```text
2 this is a test
3 Are you like awk
This's a test
10 There are orange,apple,mongo
```

```shell
awk ‘{[pattern] action}’ {filenames} 
# 行匹配语句 awk ” 只能用单引号
```

实例：

```shell
# 每行按空格或TAB分割（默认情况），输出文本中的1、4项
$ awk '{print $1,$4}' log.txt
---------------------------------------------
2 a
3 like
This's
10 orange,apple,mongo
---------------------------------------------
# 正则格式化输出
$ awk '{printf "%-8s %-10s\n",$1,$4}' log.txt
---------------------------------------------
2        a
3        like
This's
10       orange,apple,mongo
----------------------------------------------
$ awk '{print FILENAME} log.txt'
-----------------------------------------------
log.txt
log.txt
log.txt
log.txt
```

```shell
awk -F
#-F相当于内置变量FS, 指定分割字符
```

实例：

```shell
$  awk -F, '{print $1,$2}'   log.txt
---------------------------------------------
2 this
3 Are you like awk

# 使用多个分隔符.先使用空格分割，然后对分割结果再使用","分割
$ awk -F '[ ,]'  '{print $1,$2,$5}'   log.txt
---------------------------------------------
2 this
3 Are
```

```shell
awk -v #设置变量
```

实例:

```shell
$ awk -va=1 '{print $1,$1+a}' log.txt
---------------------------------------------
2 3
3 4
This's 1
10 11
$ awk -va=1 '{print $1,$(1+a)}' log.txt
---------------------------------------------
2 this
3 Are
This's a
10 There
$ awk -va=1 -vb=s '{print $1,$1+a,$1b}' log.txt
---------------------------------------------
2 3 2s
3 4 3s
This's 1 This'ss
10 11 10s
```

### 流程控制语句

#### 语法格式

```shell
if [ 条件]
then 
	指令
elif [ 条件2 ]
then
	指令
else 
	指令
fi
```

#### case选择语句

```shell
read  -p "输入性别

```

### 循环语句

#### for循环

实例:do

```shell
#将当前文件夹下的所有文件拷贝到bak
for file in $(ls)
do
echo "文件:$file"
cp "$file" bak/"${file}-baK"
done
```

### while循环

```shell
count =0
while [ $count -le 5]
do 
echo "count: $count"
let count=count+1
done
```

### 函数/方法

```shell
函数名(){
	函数体
}
```

实例

```shell
echo "文件名:$0  参数个数:$# 第一个参数:$1"
hanshu(){
echo "这是一个函数"
}
echo "文件名:$0  参数个数:$# 第一个参数:$1"
hanshu  z x c#调用
--------------------------------------------------------------------
bash xxx.sh a s d#运行上面这些脚本
---------------------------------------------------------------------
文件名:xxx.sh 参数个数:3 第一个参数:a
文件名:xxx.sh 参数个数:3 第一个参数:z
```



