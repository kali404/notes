##
 ### ----命令行连接MySql---------

### 启动mysql服务器
net start mysql

### 关闭   
net stop mysql  

### 进入
mysql -h 主机地址 -u 用户名 －p 用户密码 

### 退出
exit

### ---------------------------
### ----MySql用户管理---------

### 修改密码:首先在DOS 下进入mysql安装路径的bin目录下，然后键入以下命令:
mysqladmin -uroot -p123 password 456;

### 增加用户
### 格式:grant 权限 on 数据库.* to 用户名@登录主机 identified by '密码'
/*
如，增加一个用户user1密码为password1，让其可以在本机上登录， 并对所有数据库有查询、插入、修改、删除的权限。首先用以root用户连入mysql，然后键入以下命令： 
grant select,insert,update,delete on *.* to [user1@localhost](mailto:user1@localhost) Identified by "password1"; 
如果希望该用户能够在任何机器上登陆mysql，则将localhost改为"%"。 
如果你不想user1有密码，可以再打一个命令将密码去掉。 
grant select,insert,update,delete on mydb.* to [user1@localhost](mailto:user1@localhost) identified by ""; 
*/

grant all privileges on wpj1105.* to [sunxiao@localhost](mailto:sunxiao@localhost) identified by '123';   #all privileges 所有权限

### ----------------------------
### -----MySql数据库操作基础-----

### 显示数据库
show databases;

### 判断是否存在数据库wpj1105,有的话先删除
drop database if exists wpj1105;

### 创建数据库
create database wpj1105;

### 删除数据库
drop database wpj1105;

### 使用该数据库
use wpj1105;

### 显示数据库中的表
show tables;

### 先判断表是否存在,存在先删除
drop table if exists student;

### 创建表
create table student(
id int auto_increment primary key,
name varchar(50),
sex varchar(20),
date varchar(50),
content varchar(100)
)default charset=utf8;



### 查看表的结构
describe student;  #可以简写为desc student;

### 插入数据
insert into student values(null,'aa','男','1988-10-2','......');
insert into student values(null,'bb','女','1889-03-6','......');
insert into student values(null,'cc','男','1889-08-8','......');
insert into student values(null,'dd','女','1889-12-8','......');
insert into student values(null,'ee','女','1889-09-6','......');
insert into student values(null,'ff','null','1889-09-6','......');
### 查询表中的数据
select * from student;
select id,name from student;

### 修改某一条数据
update student set sex='男' where id=4;

### 删除数据
delete from student where id=5;

###  and 且
select * from student where date>'1988-1-2' and date<'1988-12-1';

###  or 或
select * from student where date<'1988-11-2' or date>'1988-12-1';

### between
select * from student where date between '1988-1-2' and '1988-12-1';

### in 查询制定集合内的数据
select * from student where id in (1,3,5);

### 排序 asc 升序  desc 降序
select * from student order by id asc;

### 分组查询 #聚合函数 
select max(id),name,sex from student group by sex;

select min(date) from student;

select avg(id) as '求平均' from student;

select count(*) from student;   #统计表中总数

select count(sex) from student;   #统计表中性别总数  若有一条数据中sex为空的话,就不予以统计~

select sum(id) from student;

### 查询第i条以后到第j条的数据(不包括第i条)
select * from student limit 2,5;  #显示3-5条数据

### 巩固练习
create table c(
 id int primary key auto_increment,
 name varchar(10) not null,
 sex varchar(50) ,  #DEFAULT '男' ,
 age int unsigned, #不能为负值(如为负值 则默认为0)
 sno int unique    #不可重复
);

drop table c;
desc c;

insert into c (id,name,sex,age,sno) values (null,'涛哥','男',68,1);
insert into c (id,name,sex,age,sno) values (null,'aa','男',68,2);
insert into c (id,name,sex,age,sno) values (null,'平平','男',35,3);
...

select * from c;

### 修改数据 
update c set age=66 where id=2;
update c set name='花花',age=21,sex='女' where id=2
delete from c where age=21;

### 常用查询语句
select name,age ,id from c
select * from c where age>40 and age<60;  #and
select * from c where age<40 or age<60;  #or
select * from c where age between 40 and 60 #between
select * from c where age in (30,48,68,99);     #in 查询指定集合内的数据
select * from c order by age desc;      #order by （asc升序 des降序）

### 分组查询
select name,max(age) from c group by sex;  #按性别分组查年龄最大值
### 聚合函数
select min(age) from c;
select avg(age) as '平均年龄 ' from c;
select count(*) from c;  #统计表中数据总数
select sum(age) from c;

### 修改表的名字
### 格式:alter table tbl_name rename to new_name
alter table c rename to a;

### 表结构修改
create table test
(
id int not null auto_increment primary key, #设定主键
name varchar(20) not null default 'NoName', #设定默认值
department_id int not null,
position_id int not null,
unique (department_id,position_id) #设定唯一值
);

### 修改表的名字
### 格式:alter table tbl_name rename to new_name
alter table test rename to test_rename;

### 向表中增加一个字段(列)
### 格式:alter table tablename add columnname type;/alter table tablename add(columnname type);
alter table test add  columnname varchar(20);

### 修改表中某个字段的名字
alter table tablename change columnname newcolumnname type;  #修改一个表的字段名
alter table test change name uname varchar(50);

select * from test;

#表position 增加列test
alter table position add(test char(10));
#表position 修改列test
alter table position modify test char(20) not null;
#表position 修改列test 默认值
alter table position alter test set default 'system';
#表position 去掉test 默认值
alter table position alter test drop default;
#表position 去掉列test
alter table position drop column test;
#表depart_pos 删除主键
alter table depart_pos drop primary key;
#表depart_pos 增加主键
alter table depart_pos add primary key PK_depart_pos
(department_id,position_id);

### 用文本方式将数据装入数据库表中（例如D:/mysql.txt）
load data local infile "D:/mysql.txt" into table MYTABLE;

### 导入.sql文件命令（例如D:/mysql.sql）
source d:/mysql.sql;  #或者  /. d:/mysql.sql;