## 复制字体文件
复制字体文件到文件夹下,文件夹的名字可以随意写,最好是字体文件的名字
将这个文件夹保存在复制&剪切到`/usr/share/fonts/truetype/`这个目录下
因为这个字体是truetype字体，所以必须外层嵌套一个文件夹,不能直接将字体文件复制到这个目录下。

第三步：执行一系列命令，总之就是在系统中注册，让系统知道你安装了这些字体。
```shell
mkfontdir
mkfontscale
fc-cache
sudo reboot
```
接下来，重启系统就可以在Clion中看到这个字体了。