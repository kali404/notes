## MYSQL用户管理

### 1.权限表

MYSQL是一个多用户的数据库，MYSQL的用户可以分为两大类：

（1）       超级管理员用户（root），拥有全部权限

（2）       普通用户，由root创建，普通用户只拥有root所分配的权限

#### 1.1权限表的位置

数据库：mysql

与权限相关的数据表：user,db,host,tables_priv,columns_priv，procs_priv等

#### 1.2 user表

User表存储了：

（1）用户的信息：hots（用户所在的主机）,user（用户名）,password（密码）

（2）用户的权限信息：_priv

（3）安全性相关的信息：ssl_,x509,记录用户登录的验证操作等

（4）与资源分配相关的信息：max_，

max_questions表示用户在一个小时内最多可以进行的查询次数。

max_updates表示用户在一个小时内最多可以进行的更新次数，也包括增加数据、删除数据。

Max_connections：表示用户最多可以建立的连接数

##### 1.2.1 user表的内容

（1）host列

Localhost表示本机的用户或者超级管理员

%表示任何主机上的root用户

说明：_priv权限是全局权限，不受数据库的范围限制

### 1.3 DB表

（1）与用户相关的字段：hots（用户所在的主机）,user（用户名）,

（2）与权限相关的字段：_priv，DB字段规定了_priv权限的有效范围。

### 1.4 host表

（1）与用户相关的字段：hots（用户所在的主机）

（2）与权限相关的字段：_priv，DB字段规定了_priv权限的有效范围。

说明：

（1）       记录主机上的用户对数据库拥有的权限，侧重点在主机，而不在用户，例如假设select_priv=Y,那个这个主机上的所有数据库用户都拥有select权限。

（2）       Host表的优先级大于db表，如果db表规定这个用户没有权限，但是host表规定了这台主机的用户有权限，那么db的这个用户也是拥有权限的。

### 1.5 tables_priv 表

设定了用户对某个表拥有的权限，该表记录了用户的信息，以及某个表的权限信息table_priv(select ,lnsert,alter等等)，以及表上的某个列的权限信息column_priv。

### 1.6 column_priv表

记录某用户对某表的某个列所拥有的权限。

### 1.7procs_priv表

​    规定了用户关于存储过程及存储函数的操作权限，主要字段：proc_priv

 

 

## 创建数据库用户

 

### 2.1创建普通用户

#### A.CREATE USER

CREATE USER`用户名称` [@主机名称’]

例：CREATE USER 'user1';

验证是否创建成功：

mysql> SELECT user FROM mysql.user;

+-------+

| user  |

+-------+

| user1 |

| root  |

| root  |

|       |

| pma   |

| root  |

+-------+

6 rows in set (0.00 sec)  说明新创建的用户已经进入user表内

说明：使用CREATE USER来创建的用户，均无任何权限，user表的权限字段的值均为N

 

#### B.创建带有主机名的用户

CREATE USER `用户名称` [@`主机名称`] [INDENTIFIED BY `用户密码`]

CREATE USER 'user2' @'localhost';

 

mysql> select user,host from mysql.user;

+-------+---------------------+

| user  | host      |

+-------+---------------------+

| user1 | %         |

| root  | 127.0.0.1 |

| root  | ::1       |

|       | localhost |

| pma   | localhost |

| root  | localhost |

| user2 | localhost |

+-------+---------------------+

7 rows in set (0.00 sec)

 

说明：host字段的%表示不受任何主机的限制

 

#### C.创建带密码的用户

CREATE USER 'user3' @'localhost'  [INDENTIFIED BY ‘用户密码’];

 

例子：

CREATE USER 'user3' @'localhost' IDENTIFIED BY '123333';

 

验证：

mysql> SELECT user,password,host FROM mysql.user;

+-------+-------------------------------------------------------------------------+-----------+

| user  | password                                  | host      |

+-------+-------------------------------------------------------------------------+-----------+

| root  |                                           | localhost |

| root  |                                           | 127.0.0.1 |

| root  |                                           | ::1       |

|       |                                           | localhost |

| pma   |                                           | localhost |

| user1 |                                           | %         |

| user2 |                                           | localhost |

| user3 | *0166E21E66009700F528CA21179AF9AD81120DA2 | localhost |

+-------+-------------------------------------------------------------------------+-----------+

8 rows in set (0.00 sec)

 

说明：密码是哈希码的形式显示的

 

 

### 2.1.2使用GRANT 来创建用户，以及授予权限

GRANT是用来给用户授权的，但是也可以用来创建用户，GRANT在给用户进行授权的时候，如果用户是不存在的，那么GRANT会自动创建这个用户，然后再给这个用户进行授权。

 

#### A.添加权限

 

grant`权限`on`数据库`.`表` to`用户名` @`登录主机`'  [INDENTIFIED BY `用户密码`];

 

权限： select ,update,delete,insert(表数据)、create,alert,drop(表结构)、references(外键)、create temporary tables(创建临时表)、index(操作索引)、create view,show view(视图)、create routine,alert routine,execute(存储过程)、all,all privileges(所有权限)

 

数据库：数据库名或者*(所有数据库)

 

表：表名或者*(某数据库下所有表)，*.*表示所有数据库的所有表

 

主机:主机名或者%(任何其他主机)

 

例：grant selec,insert,update,delete on *.* to 'jifei'@'%';

 

GRANT SELECT ON *.* TO 'user4' @'localhost' IDENTIFIED BY '123333';

 

 

mysql> SELECT user,password,host FROM mysql.user;

+-------+-------------------------------------------------------------------------------+-----------+

| user  | password                                    | host      |

+-------+-------------------------------------------------------------------------------+-----------+

| root  |                                             | localhost |

| root  |                                             | 127.0.0.1 |

| root  |                                             | ::1      |

|       |                                            | localhost |

| pma   |                                            | localhost |

| user1 |                                              | %      |

| user2 |                                             | localhost |

| user3 | *0166E21E66009700F528CA21179AF9AD81120DA2   | localhost |

| user4 | *0166E21E66009700F528CA21179AF9AD81120DA2   | localhost |

+-------+-------------------------------------------------------------------------------+-----------+

9 rows in set (0.00 sec)

 

#### B.为用户授予指定数据库、指定表、指定列的权限

GRANT UPDATE(cid,cname) ON mysqlpart2.custom TO 'user3'@'localhost';

 

授权成功后，可以在以下表中查看到授权信息：

数据库: mysql » 表: tables_priv "Table privileges"

数据库: mysql » 表: columns_priv "Column privileges"

 

#### C.用户权限表

位置：数据库: information_schema »表: USER_PRIVILEGES

 

表的说明：

GRANTEE:授权者

PRIVILEGE_TYPE:权限名称

 

用户表：数据库: mysql »表: user "Users and global privileges"

说明：user表中，”_priv”的值域USER_PRIVILEGES表的PRIVILEGE_TYPE的值是一一对应的。

 

#### D.权限的层级关系

①权限的层级关系，就是指权限的适用范围。

②权限的最高层级是**全局级**，所谓全局级就是可以在任何数据库的任何数据表上进行操作。

③数据库级：只能在某个数据库上进行操作。

④表级：**权限信息所在位置：数据库: mysql »表: tables_priv "Table privileges"

⑤列级：权限信息所在位置：数据库: mysql »表: columns_priv "Column privileges"

⑥子程序级：权限信息所在位置：数据库: mysql »表: procs_priv "Procedure privileges"

#### E.撤销权限

REVOKE`权限` ON `数据库`.`表` FROM  `用户名`@`登录主机`;

说明：赋权与撤销权限的区别，就是REVOKE是将to改为from

例：revoke all on *.* from  ‘jifei’  @’%’;

 REVOKE UPDATE(cid,cname) ON mysqlpart2.custom FROM 'user3'@'localhost';

#### F.查看权限 

SHOW GRANTS;  -- 自己

SHOW GRANTS FOR`用户名称`@`主机名称`； 

例：

SHOW GRANTS FOR  dba@localhost;//指定用户指定host

mysql> SHOW GRANTS FOR user3@localhost;

+---------------------------------------------------------------------------------------------------------------+

| Grants for user3@localhost                                                                                    |

+---------------------------------------------------------------------------------------------------------------+

| GRANT SELECT ON *.* TO 'user3'@'localhost' IDENTIFIED BY PASSWORD '*975B2CD4FF9AE554FE8AD33168FBFC326D2021DD' |

| GRANT UPDATE (cname, cid) ON `mysqlpart2`.`custom` TO 'user3'@'localhost'                                     |

+---------------------------------------------------------------------------------------------------------------+

2 rows in set (0.00 sec)

说明：所有SHOW关键字后面的词都是复数，所有CREATE关键字后面的词都是单数

### 通过mysql.columns_priv表来查看权限：

#### A.SELECT * FROM mysql.columns_priv WHERE user='user3' AND host='localhost';

#### mysql> SELECT * FROM mysql.columns_priv WHERE user='user3' AND host='localhost'\G

*************************** 1. row ***************************

​       Host: localhost

​         Db: mysqlpart2

​       User: user3

 Table_name: custom

Column_name: cid

  Timestamp: 0000-00-00 00:00:00

Column_priv: Update

*************************** 2. row ***************************

​       Host: localhost

​         Db: mysqlpart2

​       User: user3

 Table_name: custom

Column_name: cname

  Timestamp: 0000-00-00 00:00:00

Column_priv: Update

2 rows in set (0.00 sec)

 

 

#### 2.1.3关于以直接向user表插入记录的方式来创建用户

可以使用INSERT的方式，直接向user表插入记录，以此来创建用户，但是因为user表的字段很多，而且全部字段均不允许为空，这就需要为每一个列赋值，所以不推荐使用这种方式来创建用户。

 

#### 2.1.4 CREATE USER与GRANT两种方式创建用户的区别

（1）CREATE USER 创建用户的优点：语法简单

（2）CREATE USER 创建用户的不足：用户无权限

（3）GRANT 创建用户的优势：创建的用户有权限

（4）GRANT 创建用户的不足：语法较CREATE USER 繁琐

 

删除MYSQL的用户

 

delete from mysql.user where user='****用户名称****' and host='****主机名称****';**

 

例：DELETE FROM mysql.user WHERE user='user3' AND host='localhost';

 

删除后使用：**FLUSH PRIVILEGES** **来刷新权限**

 

说明：

使用DELETET删除用户后，必须使用FLUSH PRIVILEGES 来刷新权限，否则将无法继续创建用户名与已删用户的用户名相同的用户，即使在user表中看不到已删除的用户，如果不刷新权限，也是无法再新建的。

 

例：

删除用户user3：

mysql> DELETE FROM mysql.user WHERE user='user3' AND host='localhost';

Query OK, 1 row affected (0.00 sec)

 

查看用户表，user3已删除成功：

mysql> select user from mysql.user;

+-------+

| user  |

+-------+

| user1 |

| root  |

| root  |

|       |

| pma   |

| root  |

| user2 |

| user4 |

+-------+

8 rows in set (0.00 sec)

 

创建用户****user3****失败：**

mysql> CREATE USER 'user3' @'localhost' IDENTIFIED BY 'pwd';

ERROR 1396 (HY000): Operation CREATE USER failed for 'user3'@'localhost'

 

刷新权限：

FLUSH PRIVILEGES;

 

再次创建用户，成功：

mysql> CREATE USER 'user3' @'localhost' IDENTIFIED BY 'pwd';

Query OK, 0 rows affected (0.00 sec)

 

### 4.修改用户密码

 

UPDATE mysql.user SET password=PASSWORD('****新密码****') WHERE user='****用户名

[AND host=`主机名称`;

UPDATE mysql.user SET password=PASSWORD('111111') WHERE user='root';

 

注意：

(1)如果不加WHERE 条件，则会把所有用户的密码都修改为’新密码’

(2)密码修改完成后，需要进行权限刷新操作才能生效，FLUSH PRIVILEGES;

 

例：

UPDATE mysql.user SET password=PASSWORD('111') WHERE user='user1';

 

 

（****1****）修改密码的权限**

ROOT用户可以修改自己的密码，也可以修改其他用户的密码

其他用户只能修改自己的密码

 

（****2****）****PASSWORD****函数**

用于把密码明文进行加密,所得到的密码为原密码的哈希值。

例：

mysql> SELECT PASSWORD('111');

+-------------------------------------------+

| PASSWORD('111')                           |

+-------------------------------------------+

| *832EB84CB764129D05D498ED9CA7E5CE9B8F83EB |

+-------------------------------------------+

1 row in set (0.07 sec)

 

（****3****）****ROOT****用户、普通用户****修改自己的密码**

SET PASSWORD=PASSWORD(‘****新密码****’);**

 

（****4****）****ROOT** **用户为其他用户修改密码：**

SET PASSWORD FOR ‘****用户名称****’  @’****主机名称****’  = password(‘****新密码****’);**

 

例，以下两种修改密码的方式结果相同：

SET PASSWORD FOR 'user1' @'%'=PASSWORD('111');

UPDATE mysql.user SET password=PASSWORD('111') WHERE user='user1';