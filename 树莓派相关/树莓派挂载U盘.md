## 识别U盘
首先把 U 盘插入树莓派，然后查看一下是否有被识别到。
```shell
sudu fdisk -l
```

其中 / dev/mmc 表示的是 TF 卡，容量是 8G，而 / dev/sda / 表示的是我们的第一个硬件（U 盘），容量也是 8G，只有一个分区。

## 挂载
新建一个目录
```shell
sudo mkdir /home/pi/usb_flash
```
然后挂载设备
```shell
sudo mount /dev/sda1 ~/usb_flash/
```
虽然挂载成功，但是迅雷远程下载的时候提示 “没有检测到存储设备” 好像挂载后普通用户没权限写入的问题，挂载的时候加入归属。
```shell
sudo mount -o uid=pi,gid=pi /dev/sda1 ~/usb-flash/
```
开机自动挂载
打开`/etc/fstab`最后一行加入
```shell
/dev/sda1       /home/pi/usb_flash/    ntfs    defaults    0   0
```
需要拔出 U 盘的时候，可以这样取消挂载
```shell
sudo umount ~/usb_flash
```
如果提示设备在忙，那么可以使用下面的方法尝试。
问题现象：
```shell
umount /dev/sda1
# umount: /mnt/usb: device is busy
```
查找占用目录进程：
```shell
lsof |grep /mnt/usb
# bash 1971 root cwd DIR 8,1 16384 1 /mnt/usb/
# bash 2342 root 3r DIR 8,1 16384 1 /mnt/usb/
```
杀掉进程：
```shell
kill -9 1971
kill -9 2342
```
卸载：
```shell
umount /mnt/usb
```