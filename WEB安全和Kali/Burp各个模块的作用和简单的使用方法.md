# Burp各个模块的作用和简单的使用方法
> 在是上一篇播客中我们已经将**burp**进行了破解和汉化,简单的使用代理和网页爆破的方法,可是**Burp**的功能可不止网页爆破这么简单,今天让我们更加深入的了解**Burp**的各个模块

## 本文也将介绍一下几个特点

1.Target(目标)——显示目标目录结构的的一个功能
2.Proxy(代理)——拦截HTTP/S的代理服务器，作为一个在浏览器和目标应用程序之间的中间人，允许你拦截，查看，修改在两个方向上的原始数据流。
3.Spider(蜘蛛)——应用智能感应的网络爬虫，它能完整的枚举应用程序的内容和功能。
4.Scanner(扫描器)——高级工具，执行后，它能自动地发现web 应用程序的安全漏洞。
5.Intruder(入侵)——一个定制的高度可配置的工具，对web应用程序进行自动化攻击，如：枚举标识符，收集有用的数据，以及使用fuzzing 技术探测常规漏洞。
6.Repeater(中继器)——一个靠手动操作来触发单独的HTTP 请求，并分析应用程序响应的工具。
7.Sequencer(会话)——用来分析那些不可预知的应用程序会话令牌和重要数据项的随机性的工具。
8.Decoder(解码器)——进行手动执行或对应用程序数据者智能解码编码的工具。
9.Comparer(对比)——通常是通过一些相关的请求和响应得到两项数据的一个可视化的“差异”。
10.Extender(扩展)——可以让你加载Burp Suite的扩展，使用你自己的或第三方代码来扩展Burp Suit的功能。
11.Options(设置)——对Burp Suite的一些设置

## 简要分析
代理工具可以说是Burp Suite测试流程的一个心脏，它可以让你通过浏览器来浏览应用程序来捕获所有相关信息，并让您轻松地开始进一步行动，在一个典型的测试中，侦察和分析阶段包括以下任务：

手动映射应用程序-使用浏览器通过BurpSuite代理工作，手动映射应用程序通过以下链接，提交表单，并通过多步骤的过程加强。这个过程将填充代理的历史和目标站点地图与所有请求的内容，通过被动蜘蛛将添加到站点地图，可以从应用程序的响应来推断任何进一步的内容(通过链接、表单等)。也可以请求任何未经请求的站点(在站点地图中以灰色显示的)，并使用浏览器请求这些。

在必要是执行自动映射-您可以使用BurpSuite自动映射过程中的各种方法。可以进行自动蜘蛛爬行，要求在站点地图未经请求的站点。请务必在使用这个工具之前，检查所有的蜘蛛爬行设置。

使用内容查找功能发现，可以让您浏览或蜘蛛爬行可见的内容链接以进一步的操作。

使用BurpSuite Intruder(入侵者)通过共同文件和目录列表执行自定义的发现，循环，并确定命中。

注意，在执行任何自动操作之前，可能有必要更新的BurpSuite的配置的各个方面，诸如目标的范围和会话处理。

分析应用程序的攻击面 - 映射应用程序的过程中填入代理服务器的历史和目标站点地图与所有的BurpSuite已抓获有关应用程序的信息。这两个库中包含的功能来帮助您分析它们所包含的信息，并评估受攻击面的应用程序公开。此外，您可以使用BurpSuite的目标分析器报告的攻击面的程度和不同类型的应用程序使用的URL 。

接下来主要介绍下BurpSuite的各个功能吧。先介绍Proxy功能，因为Proxy起到一个心脏功能，所有的应用都基于Proxy的代理功能。

## Burp Suite功能按钮键翻译对照(汉化版请忽略)
导航栏
|   英   | 中   |  英    | 中     |
| ---- | ---- | ---- | ---- |
|   Burp   |  --    |  save state wizard    | 保存状态向导     |
|     resture state | 恢复状态     |    Remember setting  |    记住设置  |
|    Start attack  |   开始攻击   | Actively scan |defined insertion points    |   定义主动扫描插入点   |
|Repeater |	中继器 |	New tab behavior |	新标签的行为|
|Automatic payload positions| 	自动负载位置 |	config predefined payload lists |	配置预定义的有效载荷清单|
|Update content-length |	更新内容长度 |	unpack gzip/deflate 	| 解压gzip/放弃 |
|Follow redirections |	跟随重定向 |	process cookies in redirections |	在重定向过程中的cookies|
|View |	视图 |	Action |	行为 |

功能项

|   英   | 中   |  英    | 中     |
| ---- | ---- | ---- | ---- |
|Target |	目标 |	Proxy |	代理|
|Spider 	|蜘蛛 |	Scanner |	扫描|
|Intruder |	入侵者 |	Repeater |	中继器|
|Sequencer |	定序器 |	Decoder |	解码器|
|Comparer |	比较器 |	Extender |	扩展|
Options |	设置 |	Detach |	分离|
|Filter |	过滤器 |	SiteMap |	网站地图|
|Scope |	范围 	|Filter by request type| 	通过请求过滤|
|Intercept |	拦截 |	response Modification| 	响应修改|
|match and replace |	匹配和替换 |	ssl pass through |	SSL通过|
|Miscellaneous |	杂项 |	spider status |	蜘蛛状态|
|crawler settings |	履带式设置 |	passive spidering |	被动蜘蛛|
|form submission |	表单提交 |	application login |	应用程序登录|
|spider engine |	蜘蛛引擎 	|scan queue |	扫描队列|
|live scanning |	现场扫描 	|live active scanning |	现场主动扫描|
|live passive scanning |	现场被动扫描 |	attack insertion points 	|攻击插入点|
active scanning optimization |	主动扫描优化 |	active scanning areas |	主动扫描区域|
|passive scanning areas |	被动扫描区域 |	Payload |	有效载荷|
|payload processing |	有效载荷处理 |	select live capture request |	选择现场捕获请求|
|token location within response |	内响应令牌的位置 |	live capture options |	实时捕捉选项|
|Manual load |	手动加载 |	Analyze now |	现在分析|
|Platform authentication |	平台认证 |	Upstream proxy servers 	上游代理服务器|
|Grep Extrack 	|提取 	  	 |


## Proxy功能
