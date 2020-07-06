## 简介
hydra是著名黑客组织thc的一款开源的暴力密码破解工具，可以在线破解多种密码。 每个密码安全研究显示表明，最大的安全漏洞之一是密码。 而九头蛇是一个并发的登录破解程序，支持许多协议攻击。
官 网：http://www.thc.org/thc-hydra ,可支持AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP, HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-PROXY, HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MYSQL , NCP, NNTP, Oracle Listener , Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, RDP, Rexec, Rlogin, Rsh, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP, SOCKS5, SSH (v1 and v2), Subversion, Teamspeak (TS2), Telnet, VMware-Auth, VNC and XMPP等类型密码。 Kali Linux 自带这个工具

## 安装

```shell
wget --no-check-certificate https://www.thc.org/releases/hydra-8.1.tar.gz
tar zxvf hydra-8.1.tar.gz 
cd hydra-8.1 
./configure 
make && make install 
```

### Git项目地址

> https:*//github.com/vanhauser-thc/thc-hydra.git*

开发版本,不是稳定版

## 参数说明(帮助信息)

```html
hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e ns] 
[-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-f] [-s PORT] [-S] [-vV] server service [OPT] 
-R 继续从上一次进度接着破解。 
-S 采用SSL链接。 
-s PORT 可通过这个参数指定非默认端口。 
-l LOGIN 指定破解的用户，对特定用户破解。 
-L FILE 指定用户名字典。 
-p PASS 小写，指定密码破解，少用，一般是采用密码字典。 
-P FILE 大写，指定密码字典。 
-e ns 可选选项，n：空密码试探，s：使用指定用户和密码试探。 
-C FILE 使用冒号分割格式，例如“登录名:密码”来代替-L/-P参数。 
-M FILE 指定目标列表文件一行一条。 
-o FILE 指定结果输出文件。 
-f 在使用-M参数以后，找到第一对登录名或者密码的时候中止破解。 
-t TASKS 同时运行的线程数，默认为16。 
-w TIME 设置最大超时的时间，单位秒，默认是30s。 
-v / -V 显示详细过程 
-I 跳过等待
server 目标ip 
service 指定服务名，支持的服务和协议：telnet ftp pop3[-ntlm] imap[-ntlm] smb smbnt 
http-{head|get} http-{get|post}-form http-proxy cisco cisco-enable vnc 
ldap2 ldap3 mssql mysql oracle-listener postgres nntp socks5 rexec 
rlogin pcnfs snmp rsh cvs svn icq sapr3 ssh smtp-auth[-ntlm] pcanywhere 
teamspeak sip vmauthd firebird ncp afp等等。 
OPT 可选项
```

## SSH

```shell
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns ip ssh 
hydra -l 用户名 -p 密码字典 -t 线程 -o save.log -vV ip ssh 
```

## FTP

```shell
hydra ip ftp -l 用户名 -P 密码字典 -t 线程(默认16) -vV 
hydra ip ftp -l 用户名 -P 密码字典 -e ns -vV 
```

## HTTP-GET

```shell
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns ip http-get /admin/ 
hydra -l 用户名 -p 密码字典 -t 线程 -vV -e ns -f ip http-get /admin/index.php
```

## HTTP-POST

```shell
hydra -l 用户名 -P 密码字典 -s 80 ip http-post-form "/admin/login.php:username=^USER^&password=^PASS^&submit=login:sorry password" 
hydra -t 3 -l admin -P pass.txt -o out.txt -f 10.36.16.18 http-post-form "login.php:id=^USER^&passwd=^PASS^:<title>wrong username or password</title>" 
```
（参数说明：-t同时线程数3，-l用户名是admin，字典pass.txt，保存为out.txt，-f 当破解了一个密码就停止， 10.36.16.18目标ip，http-post-form表示破解是采用http的post方式提交的表单密码破解,<title>中的内容是表示错误猜解的返回信息提示。）

## HTTPS

```shell
hydra -m /index.php -l muts -P pass.txt 10.36.16.18 https
```

## teamspeak
```shell
hydra -l 用户名 -P 密码字典 -s 端口号 -vV ip teamspeak
```
## smb
```shell
hydra -l administrator -P pass.txt 10.36.16.18 smb
```
## rdp
```shell
hydra ip rdp -l administrator -P pass.txt -V
```

大同小异,不一一列举了......

