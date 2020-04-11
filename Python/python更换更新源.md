## python 更换 PIP 源
因为天朝有墙有些时候我们pip 安装包的时候下载速度特别慢,所以我们可以将pip的更新源换成我们国内的保证install时包的下载速度

## 国内源

```python
阿里云 http://mirrors.aliyun.com/pypi/simple/ 
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
豆瓣 http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

```
## 临时修改
可以在使用pip的时候在后面加上-i参数，指定pip源 
```shell
pip install [包名] -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## 永久修改
### Linux
许多教程需要修改 ~/.pip/pip.conf
但是我建议先全局搜索下`pip.conf`
```shell
sudo find / name pip.conf
```
如果没有则
修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

### Windows
windows下，直接在user目录中创建一个pip目录，再新建文件pip.ini。
(例如：C:\Users\xxx\pip\pip.ini)内容同上。

## pip.conf 内容

```conf
[global] 
index-url = https://pypi.tuna.tsinghua.edu.cn/simple  # 替换成你喜欢的国内源
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn  # trusted-host 此参数是为了避免麻烦，否则使用的时候可能会提示不受信任

timeout = 120  # 指定超时间
```
