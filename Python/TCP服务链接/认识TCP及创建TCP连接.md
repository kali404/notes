## 一、初识socket

socket 是网络连接端点，每个socket都被绑定到一个特定的IP地址和端口。IP地址是一个由4个数组成的序列，这4个数均是范围 0~255中的值（例如，220,176,36,76)；端口数值的取值范围是0~65535。端口数小于1024的都是为众所周知的网络服务所保留的 （例如Web服务使用的80端口）；最大的保留数被存储在socket模块的IPPORT_RESERVED变量中。你也可以为你的程序使用另外的端口数 值。

不是所有的IP地址都对世界的其它地方可见。实际上，一些是专门为那些非公共的地址所保留的（比如形如192.168.y.z或10.x.y.z）。地址127.0.0.1是本机地址；它始终指向当前的计算机。程序可以使用这个地址来连接运行在同一计算机上的其它程序。

IP地址不好记，你可以花点钱为特定的IP地址注册一个主机名或域名（比如使用www.biadu.com代替222.76.216.16）。域名服务器（DNS）处理名字到IP地址的映射。


在网络上的两个程序通过一个双向的通信连接实现数据的交换，这个链接的一端称为一个Socket（套接字），用于描述IP地址和端口。


建立网络通信连接至少要一对端口号（Socket），Socket本质是编程接口（API），对TCP/IP的封装，提供了网络通信能力。


每种服务都打开一个Socket，并绑定到端口上，不同的端口对应不同的服务，就像http对应80端口。

Socket是面向C/S（客户端/服务器）模型设计，客户端在本地随机申请一个唯一的Socket号，服务器拥有公开的socket，任何客户端都可以向它发送连接请求和信息请求。

`TCP和UDP是OSI七层模型中传输层提供的协议，提供可靠端到端的传输服务。`
​
**TCP**（Transmission Control Protocol，传输控制协议），面向连接协议，双方先建立可靠的连接，再发送数据。适用于可靠性要求高的应用场景。
**UDP**（User Data Protocol，用户数据报协议），面向非连接协议，不与对方建立连接，直接将数据包发送给对方，因此相对TCP传输速度快 。适用于可靠性要求低的应用场景。

多少信息通过一个网络被传送基于许多因素，其中之一就是使用的协议。许多的协议是基于简单的、低级协议以形成一个协议栈。例如HTTP协议，它是用在Web浏览器与Web服务器之间通信的协议，它是基于TCP协议，而TCP协议又基于IP协议。

TCP协议在两端间建立一个持续的连接，并且你所发送的信息有保证的按顺序到达它们 的目的地。

UDP不建立连接，它的速度快但不可靠。你发送的信息也可能到不了另一端；或它们没有按顺序到达。有时候一个信息的多个复制到达接收端，即使你只发送了一次。

#### 各类协议:

| 协议   | 功能用处                         | 端口号 | Python 模块                |
| ------ | -------------------------------- | ------ | -------------------------- |
| HTTP   | 网页访问                         | 80     | httplib, urllib, xmlrpclib |
| NNTP   | 阅读和张贴新闻文章，俗称为"帖子" | 119    | nntplib                    |
| FTP    | 文件传输                         | 20     | ftplib, urllib             |
| SMTP   | 发送邮件                         | 25     | smtplib                    |
| POP3   | 接收邮件                         | 110    | poplib                     |
| IMAP4  | 获取邮件                         | 143    | imaplib                    |
| Telnet | 命令行                           | 23     | telnetlib                  |
| Gopher | 信息查找                         | 70     | gopherlib, urllib          |

### 套接字

| 服务器端套接字 |                                                              |
| -------------- | ------------------------------------------------------------ |
| s.bind()       | 绑定地址（host,port）到套接字，在AF_INET下,以元组（host,port）的形式表示地址。 |
| s.listen()     | 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。 |
| s.accept()     | 被动接受TCP客户端连接,(阻塞式)等待连接的到来                 |

| 客户端套接字   |                                                              |
| -------------- | ------------------------------------------------------------ |
| s.connect()    | 主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。 |
| s.connect_ex() | connect()函数的扩展版本,出错时返回出错码,而不是抛出异常      |

| 公共用途的套接字函数                 |                                                              |
| ------------------------------------ | ------------------------------------------------------------ |
| s.recv()                             | 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。 |
| s.send()                             | 发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。 |
| s.sendall()                          | 完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。 |
| s.recvform()                         | 接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。 |
| s.sendto()                           | 发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。 |
| s.close()                            | 关闭套接字                                                   |
| s.getpeername()                      | 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。  |
| s.getsockname()                      | 返回套接字自己的地址。通常是一个元组(ipaddr,port)            |
| s.setsockopt(level,optname,value)    | 设置给定套接字选项的值。                                     |
| s.getsockopt(level,optname[.buflen]) | 返回套接字选项的值。                                         |
| s.settimeout(timeout)                | 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()） |
| s.gettimeout()                       | 返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。 |
| s.fileno()                           | 返回套接字的文件描述符。                                     |
| s.setblocking(flag)                  | 如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。 |
| s.makefile()                         | 创建一个与该套接字相关连的文件                               |

### 方法:

#### socket常用的方法:

| 方法                                     | 描述                                                         |
| ---------------------------------------- | ------------------------------------------------------------ |
| socket.socket([family[, type[, proto]]]) | socket初始化函数，（地址族，socket类型，协议编号）协议编号默认0 |
| socket.AF_INET                           | IPV4协议通信                                                 |
| socket.AF_INET6                          | IPV6协议通信                                                 |
| socket.SOCK_STREAM                       | socket类型，TCP                                              |
| socket.SOCK_DGRAM                        | socket类型，UDP                                              |
| socket.SOCK_RAW                          | 原始socket，可以处理普通socker无法处理的报文，比如ICMP       |
| socket.SOCK_RDM                          | 更可靠的UDP类型，保证对方收到数据                            |
| socket.SOCK_SEQPACKET                    | 可靠的连续数据包服务                                         |

#### socket.socket()创建类方法：

| 方法                      | 描述                                                         |
| ------------------------- | ------------------------------------------------------------ |
| accept()                  | 接受连接并返回(socket object, address info)，address是客户端地址 |
| bind(address)             | 绑定socket到本地地址，address是一个双元素元组（host，port）返回双元组数据ip地址和端口号 |
| listen(backlog)           | 开始接收连接，backlog是最大连接数，默认1                     |
| connect(address)          | 连接socket到远程地址                                         |
| connect_ex(address)       | 连接socket到远程地址，成功返回0，错误返回error值             |
| getpeername()             | 返回远程端地址(hostaddr, port)                               |
| gettimeout()              | 返回当前超时的值，单位秒，如果没有设置返回none               |
| recv(buffersize[, flags]) | 接收来自socket的数据，buffersize是接收数据量[接收数据]       |
| send(data[, flags])       | 发送数据到socket，返回值是发送的字节数,[发送数据]date是一个二进制数据 |
| sendall(data[, flags])    | 发送所有数据到socket，成功返回none，失败抛出异常             |
| setblocking(flag)         | 设置socket为阻塞（flag是true）或非阻塞（flag是flase）        |

1.  `str.encode(编码格式) 表示把字符串编码成为二进制`

2. `data.decode(编码格式) 表示把二进制解码成为字符串`
3. `方便传入send和接收recv`

例.服务端

**socket.socket(AddressFamily, Type)**

AddressFamily	表示IP地址类型 

Type	表示传输协议类型

```python
import socket
HOST = ''                              # 为空代表所有可用的网卡
PORT = 50007            				 # 任意非特权端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsocckopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)  # 进程关闭后立即释放端口占用
s.bind((HOST, PORT))  					#传入网卡和端口号
s.listen(1)   							# 最大连接数
conn, addr = s.accept() #返回conm套接字   # addr客户端地址(地址,以及链接端口)<-是个元组
print('上线', addr)
while 1:
    data = conn.recv(1024)             # 每次最大接收客户端发来数据1024字节 返回一个(可被加密的)消息
    if not data: break                 # 当没有数据就退出死循环 
    print "Received: ", data           # 打印接收的数据
    conn.sendall(data)                 # 把接收的数据再发给客户端
conn.close()
```

客户端:

```python
import socket
HOST = '192.168.1.120'                 # 远程主机IP
PORT = 50007                               # 远程主机端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')                 # 发送数据
data = s.recv(1024)                       # 接收服务端发来的数据
s.close()
print 'Received: ', data

```

1.  当 TCP 客户端程序想要和 TCP 服务端程序进行通信的时候必须要先建立连接

2. TCP 客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的。
3. TCP 服务端程序必须绑定端口号，否则客户端找不到这个 TCP 服务端程序。
4. listen 后的套接字是被动套接字，只负责接收新的客户端的连接请求，不能收发消息。
5. 当 TCP 客户端程序和 TCP 服务端程序连接成功后， TCP 服务器端程序会产生一个新的套接字，收发客户端消息使
  用该套接字。
6. 关闭 accept 返回的套接字意味着和这个客户端已经通信完毕。
7. 关闭 listen 后的套接字意味着服务端的套接字关闭了，会导致新的客户端不能连接服务端，但是之前已经接成功的
  客户端还能正常通信。
8. 当客户端的套接字调用 close 后，服务器端的 recv 会解阻塞，返回的数据长度为0，服务端可以通过返回数据的长
  度来判断客户端是否已经下线，反之服务端关闭套接字，客户端的 recv 也会解阻塞，返回的数据长度也为0。