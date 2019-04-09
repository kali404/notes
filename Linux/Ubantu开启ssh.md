# Ubantu开启ssh

1.安装

```shell
sudo apt-get install openssh-server
```

2.开启

```shell
sudo service ssh start
```

3.查询服务状态

```shell
sudo ps -e | grep ssh
#或者
sudo service ssh status
```

4.修改配置文件

```shell
sudo vim /etc/ssh/sshd_config
```

重点修改链接端口

5.重启服务

```shell
sudo service ssh restart
# 停止这个服务
```



