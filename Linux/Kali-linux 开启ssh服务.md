# Kali-linux 开启ssh服务

1.

修改

```vi /etc/ssh/sshd_config
 update-rc.d ssh enable
```



> 1.将 permitrootlogin 前面的注释去掉,并且后面改为yes
> 如果没有则添加permitrootlogin  yes
> 2.将#PasswordAuthentication no的注释去掉，并且将NO修改为YES //kali中默认是yes
> 3.按Esc , 同时按shift和冒号键 ,输入wq ，回车保存

2.然后重启ssd服务

```
/etc/init.d/ssh restart
```

3.添加开机启动

```
 update-rc.d ssh enable
```

