> DVWA(dema vulnerable web application)是一个基于PHP/MYSQL环境写的一个web应用。他的主要目的是帮助安全专业员去测试他们的技术和工具在合法的环境里面也帮助开发人员更好的理解如何加固他们开发的web系统同时帮助老师或者学生去教或者学习web应用安全在教学环境里面。DVWA开源地址：https://github.com/ethicalhack3r/DVWA

## 下载DVWA

```shell
git clone https://github.com/ethicalhack3r/DVWA
```

## 安装PHP

注意需要**PHP5的版本**

```shell
# 添加PPA
sudo add-apt-repository ppa:ondrej/php
# 更新
sudo apt-get update
sudo apt-get upgrade
# 安装
sudo apt-get install php5.6
sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml
sudo apt-get install -y php5.6-gd
```

## 安装apache2

```shell
sudo apt-get install apache2
```

## 开启apache2服务

```shell
sudo service apache2 restart
# 查看php响应状态
sudo a2enmod php5.6
```

## 准备文件

把下载好的DVWA给放在/var/www/html下

并且更改文件夹的权限

```shell
sudo cp ./dvwa /var/www/html/
sudo chmod g+w /var/www/html/dvwa/ -R
```

## 打开浏览器

访问 http://127.0.0.1/dvwa/

## 更改配置文件

```shell
sudo vim /etc/php/5.6/apache2/php.ini
# 将下列选项改为=on
#allow_url_include = Off
allow_url_include = On
```

## 安装MYSQL

```shell
sudo apt-get install mysql-server
sudo apt install mysql-client
sudo apt install libmysqlclient-dev
#开启myssql
sudo service mysql restart
```

**注意一条一条安装,否则会出现没有密码的情况,较为繁琐**
## 登录到Mysql(无密码)
```shell
sudo cat /etc/mysql/debian.cnf 
# 使用文本当中的用户和密码登录
mysql -u用户名 -p
```
```sql
use mysql;
update user set authentication_string=PASSWORD("自定义密码") where user='root';
update user set plugin="mysql_native_password";
flush privileges;
-- 切换用户登录mysql -- 
```
进入mysql数据库

```shell
mysql -uroot -p
```

```sql
create database dvwa charset=utf8;
-- 创建一个名为'dvwa'的数据库 --
create user dvwa identified by 'dvwa1234';
-- 创建一个用户dvwa,密码为dvwa1234 -- 
grant all on dvwa.* to 'dvwa'@'%';
-- 将dvwa用户的权限只能操作dvwa数据库(后边 --
flush privileges;
-- 刷新权限
```

## 修改dvwa配置

```shell
sudo vim /var/www/html/dvwa/config/config.inc.php
# 将下列选项依次更改为自己创建的数据库
$_DVWA[ 'db_server' ]   = '127.0.0.1';
$_DVWA[ 'db_database' ] = 'dvwa';
$_DVWA[ 'db_user' ]     = 'root';
$_DVWA[ 'db_password' ] = '';
# 改为数据库默认端口3306
$_DVWA[ 'db_port '] = '3306';
# 给你们的福利(需要自己域名申请)
$_DVWA[ 'recaptcha_public_key' ]  = '6LdK7xITAAzzAAJQTfL7fu6I-0aPl8KHHieAT_yJg';
$_DVWA[ 'recaptcha_private_key' ] = '6LdK7xITAzzAAL_uw9YXVUOPoIHPZLfw2K1n5NVQ';
# 修改完成后保存退出
```

## 修改文件的用户组

```shell
sudo chgrp www-data hackable/uploads/
sudo chgrp www-data /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt
sudo chgrp www-data config/
# 重启apache2服务
sudo service apache2 restart
```

## 打开浏览器
访问: http://127.0.0.1/dvwa/setup.php





出现全部为绿色时点击crete按钮即可进入登陆界面

至此安装配置已经全部完成,**出现问题可以加左上角群询问**