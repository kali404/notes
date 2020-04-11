

|名称 |	类型  |	使用模式  |	功能  |	功能评价|
| ---- | ---- | ---- | ---- | ---- |
|dmitry|	信息收集	|shell	|whois查询/子域名收集/端口扫描|	whois并不简单明了；子域名和邮箱依赖google；端口扫描速度一般|
|dnmap	|信息收集	|	用于组建分布式nmap，dnmap_server为服务端；|dnmap_client为客户端|	用起来并不是那么方便，不是实在不行不是很必要|
|ike-scan|	信息收集|		收集ipsec vpn server指纹信息|	好像用于攻击vpn，|不太懂|
|maltegoce	|信息收集|	|	域名/账号等关联性收集展示	|关联性展示功能确实很好，但效果可能没有那么理想，特别是对国内而言
|netdiscover|	信息收集|		|主动发出arp包和截获arp包|	就arp探测功能就此功能本身而言做得算很好了|
|nmap|	信息收集|	|	端口服务探测和端口漏洞扫描	|端口扫描集大成者|
|p0f	|信息收集|		监听网卡收发的数据包，从数据包中读取远端机器操作系统服务版本等信息|	毕竟只是截取数据 包中的版本信息，效果期望不要很大|
|regon-ng|	信息收集|	|	模仿msf的信息侦查框架|	类似将站长工具等东西命令行化，想法挺好但是用起来感觉不是那么直观|
|sparta|	暴力破解|	|	图形版的hydra，加了端口服务扫描功能	还行图形界面聊胜于无|
|zenmap|	信息收集|	|	图形界面版的nmap|	还行图形界面聊胜于无|
|golismero|	web扫描	|	就是一个文本版的类似awvs的web扫描器|	感觉可以提升对扫描器原理的认识|
|lynis	|系统审计	|	感觉有点像360首页的“立即体验”，不过只是扫描告警不能一键修复|	shell脚本写成颇为有趣|
|nikto|	web扫描|	web扫描器	|就喜欢这种直接告漏洞的扫描器（不过事实上很少能有可用的漏洞）|
|unix-privesc-check|	系统审计|	|	|审计系统中的关键文件权限是否有异常	还是没有总结性展示和修复功能|
|bed|	系统扫描|	|	通过发送各种模糊数据测试多种服务的缓冲区溢出漏洞的工具	可能还不错|
|burpsuite|	web代理|	|	功能强大不能要求更多|
|commix|	注入检测	|	|	|
|httrack	|网站克隆|	|	|	
|owasp-zap|	web代理|		|	和burpsuite相比弱化了截包功能，强化了web漏洞扫描功能，不过感觉也没扫出什么东西|
|paros	|web扫描	|	|	和owasp-zap差不多|
|skipfish|	web扫描|	cmd-line|	一个全自动化的web漏洞扫描工具	|其工作一是爬行网站页面，然后分析页面漏洞，最后生html报告|
|sqlmap|	sql注入扫描|	cmd-line|	|一个强大的sql注入扫描工具	|
|w3af|	web扫描|	shell/gui|	一个web漏洞扫描框架	|所谓框架就是有一堆扫描模块，然后你选定其中一些模块去扫描网站；感觉一般没说的那么好|
|webscarab|	http代理|	|	|更专业的网站树型结构分析工具	|
|wpscan|	web扫描|		|针对wordpress的漏洞扫描工具	|
|bbqsql	|盲注扫描|	shell|	|	|
|hexorbase|	数据库管理|	gui|	|	|
|jsql|	数据库探测|	gui|	根据url探测数据库类型/参数注入测试/探测后台页而/探测重要文件|	|
|mdb-sql|	数据库管理|	cmd-line|	可用来连接access数据库文件（mdb）然后通过sql语句查询数据|	|
|oscaner|	数据库猜解|	cmd-line|	用字典探查oracle数据库是否监听及猜解服务名|	|
|sidguesser|	数据库猜解|	|	|	|
|sqllite database|	数据库管理|	gui|	sqlite数据库客户端|	|
|sqlinja|	数据库猜解|	cmd-line|	用于猜解ms| sql	|
|sqlsus|	sql注入检测|	|	|用于mysql的盲注检测	|
|tnscmd10g|	数据库探测|	|	|	|
|cewl|	口令文件制作|	|	|爬取给定的URL并依据限制条件截取网页中的单词生成口令集合|	
|crunch|	口令文件制作|	cmd-line|	依据限定的条件生成口令集合|	|
|hashcat|	hash爆破|	cmd-line|	多种hash的爆力猜解工具，速度快所耗CPU小（相对）|	
|john|	系统口令破解|	cmd-line|	用于对系统口令文件的破解（如/etc/passwd）还原出密码明文|	|
|johnny|	系统口令破解|	|gui|	john的gui版本|	|
|medusa|	口令猜解|	cmd-line|	可对IMAP, rlogin, SSH等进行口令猜解，类似hydra|	|
|ncrack|	口令猜解|	cmd-line|	可对IMAP, rlogin, SSH等进行口令猜解，类似hydra|	|
|ophcrack|	系统口令破解|	gui	|基于彩虹表的windows口令破解工具|	|
|pyrit|	wifi破解|	cmd-line|	WPA/WPA2加密的wifi的密码破解工具|	|
|rainbowcrack|	hash破解|	cmd-line|	具有彩虹表的生成、排序和使用排序好换彩虹表进行破解的功能|	|
|rcracki_mt|	hash破解|	cmd-line|	|	|
|wordlist|	口令文件|	cmd-line|	打印kali自带的一些口令文件存放的位置|	|
|aircrack-ng	|wifi破解	|cmd-line	|强大的wifi破解模块(本人测试最好用)	|
|chirp	|无线电拦截|	gui|	各种无线电数据包的拦截工具（？）|	|
|cowpatty|		wifi破解 |		|||基于字典的WEP和WPA加密的wifi破解工具	|			
|mfor|	IC卡破解|	cmd-line|	IC卡密钥破解程序|	各种免费吃饭充钱教程里用的工具你想不想学|
|mfterm|	IC卡破解|	shell|	交互式IC卡文件写入工具|	要修改卡内数据才是最终的IC卡破解|
|pixiewps|	wifi破解|	cmd-line|	针对开启WPS的wifi利用WPS随机数生成中的bug来破解	有说很快有说成功率比较低||
|reaver|	wifi破解|	cmd-line|	针对开启WPS的wifi进行暴力破解的工具	aircrack-ng后排名第二的wifi破解工具| |
|wifite|	wifi破解|	cmd-line|	较为自动化的wifi破解工具|	|
|apktool|	安卓逆向|	cmd-line|	从apk文件中还原出xml和图版等资源文件|	|
|clang|	编译器|	cmd-line	|类似gcc的编译器，更轻量，可编译c、c++、Objective-C|	|
|clang++|	编译器|	cmd-line|	C++编译器，与clang的关系类似gcc和g++的类系|	|
|edb-debug|	动态调试|	gui|	软件逆向动态调试工具|	Linux版Ollydbg||
|flashm|	反汇编|	cmd-line|	.swf文件的反汇编工具可反汇编出.swf中的脚本代码|	|
|jad|	反编译|	cmd-line	|dex2jar把文件还原成了.class，jad进一步把文件还原成.java文件|	|
|javasnoop|	fuzz|	gui	|java程序漏洞评估工具|	|
|nasm| shell|	汇编|	shell|	nasm是32位汇编编译器，这是一个nasm的shell|	|
|ollydbg	|动态调试|	gui|	windows平台大名鼎鼎的动态调试工具，Linux上是通过wine运行有点水土不服|	|
|radare2	|静态分析|	cmd-line|	类似ida的静态反汇编分析工具，功能强大，开源|	但是命令行操作这难度有点大||
|msf payload center|	漏洞利用|	cmd-line|	生成包含exp的windows/android等各平台的可执行文件，木马制作利器|	那这东西和msfvenom的区别是什么|
|netsniff-ng	|流量捕获|	cmd-line|	高性能的流量捕获套件，可能大流量时的捕获效果比较稳定|	|
|responder	|主机嗅探|	cmd-line|	被动嗅探与所在主机交互的主机的操作系统版本等信息|	|
|wireshark|	流量捕获|	gui|	拦截经过指定网卡的所有流量|sectools常年排行第一的工具，这就不用多说了吧|				
|exe2hex	|编码转换|	cmd	|顾名思义就是把exe文件转成十六进制文件|	不过这样的意义是什么，不是以十六进制就能打开了吗|
|Intersect|	脚本生成|	shell|	感觉是SQL 有攻击性Intersect语句的生成工具|	|
|mimikatz|	密码提取|	cmd-line|	用于从windows内存中提取密码|	|
|nishang	|后渗透|	cmd-line|	基于powershell的后渗透攻击工具|	|
|PowerSploit|	后渗透|	cmd-line|	也是一个基于powershell的后渗透攻击工具|	|
|proxychains	|多重代理|	cmd-line|	好像用来配置多种代理的|	|
|weevely	|webshell|	shell|	webshell连接工具不过好像要用自己生成的小马|	|		
|bulk_extractor	|要素提取	|cmd-line|	|扫描给定的目录或文件，如果发现一些如电话号码网址等关键的信息则输出到文件|	
|chkrootkit	|系统检查|	cmd-line|	扫描本机，查看本机是否存在受rootkit影响的地方|	理解成360的木马查杀也差不多|
|foremost	|文件恢复	|cmd-line|	文件恢复工具，用于被删除的文件的恢复，就是360等的那个文件恢复功能|	|
|galleta	|cookie文件|	cmd-line|	用于分析IE的cookie文件输出其中的有用信息|	
hash计算	|					
|casefile|	报告编写|	gui|	一个画图工具，packet tracer用来画网络拓扑，这用来画场景拓扑	|这写出高大上的报告啊|
|cutycapt|	网页截屏|	cmd-line|	一个基于WebKit内核的网页截图工具，就是指定一个url它就能用解析url并把url界面截下来|	各种扫描器中的截图就是使用类似的工具完成的，并不会真用个浏览器访问再截图下来|
|dradis	|报告生成|	web|	可解析burpsuite/nmap等生成的扫描文件，并可将扫描结果转存为pdf或html|	|
|faraday IDE	|报告管理|	gui|	|	|
|keepnote|	笔记本|	gui|	较之记事本，可建文件夹，支持富文本，可导出为其他格式|	
|magictree|	报告管理	|gui|	|	|
|pipal|	词频统计	|cmd-line	|说词频统计并不是很准确，文命令可分析统计给定文件中的词语的“各种最”	|
|recordmydesktop	|屏幕录制|	cmd-line|	屏幕录制，输出.ogv格式视频	|不过感觉这视频格式占用磁盘有点大啊|
|maltegoce|	关系分析|	gui|	通过网络搜索，获取某个IP或邮箱与其他IP或邮箱的拓扑关系|	这东西有那么强，但社工的东西还是没那么强，而且还是外国的工具在天朝的网络|