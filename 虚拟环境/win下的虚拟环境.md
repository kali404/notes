# windows下安装Python虚拟环境virtualenvwrapper-win



## 1 前言

由于Python的版本众多，还有Python2和Python3的争论，因此有些软件包或第三方库就容易出现版本不兼容的问题。

通过 `virtualenv` 这个工具，就可以构建一系列 `虚拟的Python环境` ，然后在每个环境中安装需要的软件包(配合 `pip` 使用)，这一系列的环境是相互隔离的。作为一个独立的环境就不容易出现版本问题，还方便部署。

## 2 安装

```
pip install virtualenv
```

## 3 virtualenv的基本使用

### 3.1 创建虚拟环境

```
virtualenv venv
```

为环境指定Python解释器:

```
virtualenv -p c:\python27\python.exe venv
```

### 3.2 激活虚拟环境

```
activate venv
```

### 3.3 停止虚拟环境

```
deactivate
```

### 3.4 删除虚拟环境

直接删除目录即可.

```
rmvirtualenv venv　
```

## 4 virtualenvwrapper

为了使用virtualenv更方便，可以借助 `virtualenvwrapper`

### 4.1 安装virtualenvwrapper

```
pip install virtualenvwrapper-win
```

### 4.2 创建虚拟环境

默认创建的虚拟环境位于**C:\Users\username\envs**,可以通过环境变量 `WORKON_HOME` 来定制。

通过计算机-->属性-->高级系统设置-->环境变量-->在系统变量中新建“变量名”：WORKON_HOME,变量值：“你自定义的路径”。

创建后，会自动激活环境，注意看Shell提示符的改变:

```
(venv)c:\>
```

### 4.3列出所有虚拟环境

```
lsvirtualenv
```

### 4.4 激活虚拟环境

```
workon venv　
```

### 4.5 进入虚拟环境目录

```
cdvirtualenv
```

### 4.6 进入虚拟环境的site-packages目录

```
cdsitepackages
```

### 4.7列出site-packages目录的所有软件包

```
lssitepackages
```

### 4.8 停止虚拟环境

```
deactivate
```

### 4.9 删除虚拟环境

```
rmvitualenv venv
```

## 5 重建Python环境

### 5.1 冻结环境

所谓 `冻结(freeze)` 环境，就是将当前环境的软件包等固定下来:

```
pip freeze >packages.txt　　# 安装包列表保存到文件packages.txt中　
```

### 5.2 重建环境

`重建(rebuild)` 环境就是在部署的时候，在生产环境安装好对应版本的软件包，不要出现版本兼容等问题:

```
pip install -r packages.txt
```

配合pip，可以批量安装对应版本的软件包，快速重建环境，完成部署。