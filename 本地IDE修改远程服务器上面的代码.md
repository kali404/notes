## 场景
在某些紧急的时候,我们需要对**服务器;远程主机;虚拟机**上面的代码进行修改和调试,那么如何在本地的IDE来对远程主机上的代码进行修改呢?我们来教大家用`vscode`和`pycharm`这两款IDE进行远程连接我们的项目

## 配置服务器或虚拟机

```shell
sudo vim /etc/ssh/sshd_config
```
如图所示:



将`PermitRootLogin`选项修改为yes,允许root来ssh进行连接
如果是使用用户名和密码来登陆的话`PasswordAuthentication`也改为yes

如果有安全方面的考虑的话,可以对端口号`Port`,允许连接的ip地址`ListenAddress`进行修改,来保证服务器的安全

修改完成后记得,重启ssh服务
```shell
sudo service ssh restart
```
## 安装vscode插件
如图,点击插件并搜索`SFTP`


安装完成后新建文件夹并且用vscode来打开这个文件夹,使用快捷键`ctrl+shift+P`搜素sftp,vscode左侧会出现json文件,修改这些配置文件来对远程主机的访问.如下图所示:


修改完json文件后保存,在左侧导航栏右键选择Download,如图

输入远程服务器的密码,就能将远程主机上面的文件下拉到本地,修改本地文件并保存就可以同步到服务器上了^v^

## pycharm 配置
新建文件夹并用pycharm打开这个文件夹,然后选择设置,python解释器配置,选择远程ssh解释器,新建新的配置项,如下图


填写服务器地址,端口号和用户名,点击下一步并且输入密码,如下图


选择python解释器和对应的目录后,就可以对远程服务器的代码进行编辑了

