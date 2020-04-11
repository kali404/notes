> 每当重新安装树莓派的系统或者初始化一块全新的树莓派都会遇到这样的问题：连接WIFI。那当我们没有显示器和键盘的情况下怎末可以将树莓连接到当前的WIFI网络呢？

## 在烧录完系统之后
方法非常简单，首先在SD卡的根目录下添加一个名为 wpa_supplicant.conf的文件，然后在该文件内添加以下的内容
```json
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
  ssid="你的WIFI名"
  psk="WIFI密码"
}
```
插入SD卡启动树莓派就能直接连接到你的WIFI网络了（切记树莓派现时只支持802.11.n的WIFI标准所以只能连接2.4G网络，所以你需要确保你所连接的是2.4G的通道而不是5G的。

## 开机状态配置
在ssh工具上,输入命令行
```shell
sudo raspi-config
```

### 网络配置

### 输入wifi密码

### 输入Wifi密码

