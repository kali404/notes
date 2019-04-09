## Git常用命令

+ git clone 	初试化方式也可以理解为下载到本地

  ```git
  git  clone  git://github.com/someone/some_project.git   some_project 
  # 中间为链接地址 后边的some_project为本地目录(默认为当前))	
  ```

+ git pull           从其他的版本库(可以是本地,也可以是网站上的)强制更新到本地

  ```git
  git pull git://github.com/xxxxx/xxxxx.git  some_project
  # 地址 强制下拉不管是什么版本  后边是本地位置 (默认当前)
  ```

+ git add          是将当前修改或者新增的文件加入到git的索引中(只是记录一下,还没上传),这是提交上传的必经操作

  ```git
  git add /home/python/           # linux
  git add /e/heima/python        #windows
  # 后边直接 接上 本地地址/目录 就行了 注意:这不是上传,只是标记
  ```

+ git rm             从标记中(或者叫索引中)删除文件

  ```git
  git rm/home/python/hello.py           # linux
  # 仅在标记中把hello.py给删除
  ```

+ git commit -m 'xxx'         本次修改了什么东西,-m " " 双引号后边写的是提交信息,我认为这是 上传前一步和标记的后一步

+ **git push**         上传

  ```git
  git push origin master
  #将本地的master分支推送到origin主机的master分支。如果master不存在，则会被新建
  git push origin
  #上面命令表示，把当前目录下的东西上传到origin
  ```

  
