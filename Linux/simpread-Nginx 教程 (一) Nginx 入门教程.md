# Nginx 入门教程

Nginx 是一款轻量级的 Web 服务器 / 反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个 BSD-like 协议下发行。由俄罗斯的程序设计师 IgorSysoev 所开发，供俄国大型的入口网站及[搜索引擎](http://lib.csdn.net/base/searchengine "搜索引擎知识库") Rambler（俄文：Рамблер）使用。其特点是占有内存少，并发能力强，事实上 nginx 的并发能力确实在同类型的网页服务器中表现较好。

Nginx ("engine x") 是一个高性能的 HTTP 和 反向代理 服务器，也是一个 IMAP/POP3/SMTP 代理服务器。 Nginx 是由 Igor Sysoev 为俄罗斯访问量第二的 Rambler.ru 站点开发的，第一个公开版本 0.1.0 发布于 2004 年 10 月 4 日。其将源代码以类 BSD 许可证的形式发布，因它的稳定性、丰富的功能集、示例配置文件和低系统资源的消耗而闻名。

它已经在众多流量很大的俄罗斯网站上使用了很长时间，这些网站包括 Yandex、Mail.Ru、 VKontakte，以及 Rambler。据 Netcraft 统计，在 2012 年 8 月份，世界上最繁忙的网站中有 11.48% 使用 Nginx 作为其服务器或者代理服务器。目前互联网主流公司 360、百度、新浪、腾讯、阿里等，目前中国互联网企业 70% 以上公司都在使用 nginx 作为自己的 web 服务器。Nginx 特点是占有内存少，并发能力强，事实上 nginx 的并发能力确实在同类型的网页服务器中表现较好。Nginx 由内核和模块组成，其中，内核的设计非常微小和简洁，完成的工作也非常简单，仅仅通过配置文件将客户端请求映射到一个 location block（location 是 Nginx 配置中的一个指令，用于 URL 匹配），而在这个 location 中所配置的每个指令将会启动不同的模块去完成相应的工作。

Nginx 相对于 Apache 优点：
1) 高并发响应性能非常好，官方 Nginx 处理静态文件并发 5w/s
2) 反向代理性能非常强。（可用于负载均衡）
3) 内存和 cpu 占用率低。（为 Apache 的 1/5-1/10）
4) 对后端服务有健康检查功能。
5) 支持 PHP cgi 方式和 fastcgi 方式。
6) 配置代码简洁且容易上手。

2\. Nginx 工作原理及安装配置
Nginx 由内核和模块组成，其中，内核的设计非常微小和简洁，完成的工作也非常简单，仅仅通过查找配置文件将客户端请求映射到一个 location block（location 是 Nginx 配置中的一个指令，用于 URL 匹配），而在这个 location 中所配置的每个指令将会启动不同的模块去完成相应的工作。
Nginx 的模块从结构上分为

核心模块、基础模块和第三方模块：

核心模块：HTTP 模块、 EVENT 模块和 MAIL 模块
基础模块： HTTP Access 模块、HTTP FastCGI 模块、HTTP Proxy 模块和 HTTP Rewrite 模块，
第三方模块：HTTP Upstream Request Hash 模块、 Notice 模块和 HTTP Access Key 模块。

Nginx 的高并发得益于其采用了 epoll 模型，与传统的服务器程序架构不同，epoll 是 linux 内核 2.6 以后才出现的。 Nginx 采用 epoll 模型，异步非阻塞，而 Apache 采用的是 select 模型

Select 特点：select 选择句柄的时候，是遍历所有句柄，也就是说句柄有事件响应时，
select 需要遍历所有句柄才能获取到哪些句柄有事件通知，因此效率是非常低。

epoll 的特点：epoll 对于句柄事件的选择不是遍历的，是事件响应的，就是句柄上事
件来就马上选择出来，不需要遍历整个句柄链表，因此效率非常高

## 1.1 Nginx 下载安装

1、Nginx 下载：[nginx-1.13.0.tar.gz](http://nginx.org/download/nginx-1.8.1.tar.gz)，下载到：/usr/local/software/

wget http://nginx.org/download/nginx-1.13.0.tar.gz

![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522223128273-1991774600.png)

2、Nginx 解压安装：

 tar -zxvf nginx-1.13.0.tar.gz -C ./

 3、Nginx 编译

./configure

报错



![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522223719882-802587161.png)

1.  解决./configure: error: C compiler cc is not found 错误：

错误原因：缺少编译环境，安装编译源码所需要的工具和库：

执行命令：yum install gcc gcc-c++ ncurses-devel perl 

     再次编译：./configure --prefix=/usr/local/nginx

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522223738367-1371487902.png)

1.  解决./configure: error: the HTTP rewrite module requires the PCRElibrary. 错误：

错误原因：缺少 HTTP rewrite module 模块，禁用或者安装所需要的模块。我们选择安装模块：

      执行命令：yum install pcre pcre-devel

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522223822632-1565323478.png)

1.  解决./configure: error: the HTTP gzip module requires the zliblibrary. 错误：

　　错误原因：缺少 HTTP zlib 类库，我们选择安装模块：

　　执行命令：

　　yuminstall zlib gzip zlib-devel

4\. 编译成功

![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224025179-766877461.png)

 5\. 安装 Nginx：

安装命令：make & make install



 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224132085-1938565244.png)

![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224232976-2035615941.png)

## 1.2 Nginx 启动

1、查看安装目录：cd

conf 存放配置文件

html 网页文件

logs 存放日志

sbin   shell 启动、停止等脚本

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224519445-1647195041.png)

 2、启动 nginx

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224632195-9714321.png)

查看进程

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224813648-1853132125.png)

常见问题：

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224843163-1272194712.png)

解决 nginx:[emerg] bind() to 0.0.0.0:80 failed (98: Address already in use) 错误：

错误原因：不能绑定 80 端口，80 端口已经被占用。

3、停止 nginx，重新加载配置文件

执行命令：kill –INT 进程号

启动成功：

 ![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522224925007-1679847369.png)

 重新读取配置文件：

nginx-s reload

4、Nginx 信号控制

| TERM, INT | 快速停止（杀死进程）                 |
| --------- | ------------------------------------ |
| QUIT      | 优雅的关闭进程，即等请求结束后再关闭 |
| HUP       | 改变配置文件，平滑的重读配置文件     |
| USR1      | 重读日志，在日志按月/日分割时有用    |
| USR2      | 平滑的升级                           |
| WINCH     | 优雅关闭旧的进程（配合USR2进行升级） |

5\. 打开浏览器

![](https://images2015.cnblogs.com/blog/464291/201705/464291-20170522225252460-98273170.png)

## 1.3 常用命令

 进去 nginx 的安装目录

![](https://images2015.cnblogs.com/blog/464291/201707/464291-20170711114022978-1572821345.png)

进去 sbin

![](https://images2015.cnblogs.com/blog/464291/201707/464291-20170711114051775-1776909757.png)

常用命令



```
启动
./nginx 

检查 nginx.conf配置文件
./nginx -t

重启
./nginx -s reload

停止

./nginx -s stop
```


