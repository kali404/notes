## 从sql注入到sqli-labs
SQLI，sql injection，我们称之为sql 注入。何为sql，英文：Structured Query Language，叫做结构化查询语言。常见的结构化数据库有MySQL，MS SQL ,Oracle 以及Postgresql。Sql
语言就是我们在管理数据库时用到的一种。在我们的应用系统使用sql 语句进行管理应用数
据库时，往往采用拼接的方式形成一条完整的数据库语言，而危险的是，在拼接sql 语句的
时候，我们可以改变sql 语句。从而让数据执行我们想要执行的语句，这就是我们常说的sql
注入。
原理性的东西我们这里就不进行详细的讲解了，从sqli-labs 以下的每一个关卡中，你能
真正体会到什么是sql 注入。Ps:有些朋友对工具比较熟悉，例如sqlmap，可以从sqlmap 的
日志中分析每个关卡的原理。但是我个人建议先去了解原理，再去使用工具。这样在使用工
具的时候你也能深刻的理解工具起到了什么样的作用。更近一步你应该想着如果让你自己写
代码实现攻击，你应该如何写。
Sqli-labs 项目地址---Github 获取：https://github.com/Audi-1/sqli-labs
有些朋友对工具比较熟悉，例如sqlmap，可以从sqlmap 的
日志中分析每个关卡的原理。但是我个人建议先去了解原理，再去使用工具。这样在使用工
具的时候你也能深刻的理解工具起到了什么样的作用。更近一步你应该想着如果让你自己写
代码实现攻击，你应该如何写。
Sqli-labs 是一个印度程序员写的，用来学习sql 注入的一个游戏教程

## Sqli-labs 安装
需要安装以下环境
apache+mysql+php
我个人使用的是`windows 7`+`phpstudy`
当然也可以使用linux来搭建
后边可能会使用到`Tomcat`+`java`(部分关卡)
下面说下windows安装方法
下载并安装phpstudy
将下载好的sqli文件夹放在phpstudy解析目录下
更改数据库的配置文件
打开浏览器,输入 http://localhost/sqli/
点击`Setup/reset Database for labs`
出现

至此成功安装

## sql注入的知识体系

* 基于从服务器接收到的响应

  * 错误信息的sql注入
  * 联合查询
  * 堆查询
  * 盲注
    * 布尔
    * 时间
    * 报错

* 基于如何处理输入的sql查询

  * 字符串
  * 整形

* 基于程度和顺序的注入

  * 一介

    指输入的注射语句对WEB 直接产生了影响，出现了结果

  * 二阶

    类似存储型XSS，是指输入提交的语句，无法直接对WEB 应用程序产生影响，通过其它的辅助间
    接的对WEB 产生危害

* 注入点的位置

  * 用户提交的表单
  * cookie
  * 服务器(请求头)

## sql系统级别命令

version()——MySQL 版本

user()——数据库用户名

database()——数据库名

@@datadir——数据库路径

@@version_compile_os——操作系统版本

## 尝试语句
```sql
or 1=1--+
'or 1=1--+
"or 1=1--+
)or 1=1--+
')or 1=1--+
") or 1=1--+
"))or 1=1--+
```
一般的sql查询语句为:

```mysql
$slq = 'SELECT * FROM users WHERE id='$id' LIMIT 0,1'
```

但是在php当中需要将执行语句加上一对`''`此时我们需要考虑的是

闭合前面你的‘ 另一个是处理后面的‘ ，一般采用两种思
路，闭合后面的引号或者注释掉，注释掉采用--+ 或者#

**注意: --+可以用#替换，url 提交过程中Url 编码后的#为%23**

## sql中的逻辑运算问题

提出一个问题Select * from users where id=1 and 1=1; 这条语句为什么能够选择出id=1
的内容，and 1=1 到底起作用了没有？

这里就要清楚sql 语句执行顺序了。
同时这个问题我们在使用万能密码的时候会用到。
```sql
Select * from admin where username=’admin’ and password=’’
```
我们可以用’or 1=1# 作为密码输入。原因是为什么？
这里涉及到一个逻辑运算，当使用上述所谓的万能密码后，构成的sql 语句为：
```sql
Select * from admin where username=’admin’ and password=’’or 1=1#’
```
上面的这个语句执行后，我们在不知道密码的情况下就登录到了admin 用户了。
原因是在where 子句后， 我们可以看到三个条件语句
username=’admin’ 
password=’’
1=1
三个条件用`and` 和`or`进行连接。在sql 中，我们and 的运算优先
级大于or 的元算优先级。因此可以看到第一个条件（用a 表示）是真的，第二个条件（用
b 表示）是假的，a and b = false(python 同理),第一个条件和第二个条件执行and 后是假，再与第三
个条件or 运算，因为第三个条件1=1 是恒成立的，所以结果自然就为真了
这篇文章先到这明天我们开整第一关