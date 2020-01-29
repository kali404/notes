# skipfish WEB安全扫描

Skipfish是一款主动的Web应用程序安全侦察工具。它通过执行递归爬取和基于字典的探测来为目标站点准备交互式站点地图。最终的地图然后用来自许多活动（但希望是不中断的）安全检查的输出来注释。该工具生成的最终报告旨在作为专业Web应用程序安全评估的基础。

 

主要特征：
高速：纯C代码，高度优化的HTTP处理，最小的CPU占用空间 - 轻松实现响应目标的每秒2000个请求。
易于使用：启发式支持各种古怪的Web框架和混合技术站点，具有自动学习功能，动态词汇表创建和表单自动完成功能。
尖端的安全逻辑：高质量，低误报率，差分安全检查，能够发现一系列细微的缺陷，包括盲注入矢量。

* 常见使用方式

```shell
skipfish -o test http://1.1.1.1 # test是扫描结果存放的目录
skipfish -o test @url.txt # 扫描域名列表
skipfish -o test -S complet.wl -W a.wl http://1.1.1.1 # 指定字典
```

* 常用参数

  -I 只检查包含 string 的url
   -X 不检查包含 string的url
   -K 不进行指定参数的Fuzz
   -D 跨站爬行另一个域
   -l 每秒最大请求数
   -m 每ip最大并发连接数
   --config 指定配置文件

* 身份认证

http认证：
 `skipfish -A user:pass -o test http://1.1.1.1`
 cookie认证：
 `skipfish -C “name=val” -o test http://1.1.1.1`
 表单认证：
 `--auth-form`指定登录地址
 `--auth-user`指定登录用户
 `--auth-pass`指定登录密码
 `--auth-user-field`指定用户名表单
 `--auth-pass-field`指定密码表单
 `--auth-form-target`指定提交到的页面

