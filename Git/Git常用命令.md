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
  git rm/home/python/hello.py           
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

  

## 新建repository

　　本地目录下，在命令行里新建一个代码仓库（repository）
　　里面只有一个README.md
　　命令如下：
　　**touch README.md**
　　**git init**
　　初始化repository


　　**git add README.md**
　　将README.md加入到缓存区

　　（可以用**git add --a**将所有改动提交到缓存（注意是两个杠））

 

　　**git commit -m "first commit"**
　　提交改变，并且附上提交信息"first commit"

 

##  Push

　　**git remote add origin https://github.com/XXX(username)/YYYY(projectname).git**

　　加上一个remote的地址，名叫origin，地址是github上的地址（Create a new repo就会有）
　　因为Git是分布式的，所以可以有多个remote.


　　**git push -u origin master**
　　将本地内容push到github上的那个地址上去。

　　**参数-u**
　　用了参数-u之后，以后就可以直接用不带参数的git pull从之前push到的分支来pull。

​    

　　此时如果origin的master分支上有一些本地没有的提交,push会失败.

　　所以解决的办法是, 首先设定本地master的上游分支:

　　**git branch --set-upstream-to=origin/master**

　　然后pull:
　　**git pull --rebase**

　　最后再push:

　　**git push**

 

## 分支

　　新建好的代码库有且仅有一个主分支（**master**），它是自动建立的。
　　可以新建分支用于开发：
　　**git branch develop master**
　　新建一个叫develop的分支，基于master分支

　　切换到这个分支：
　　**git checkout develop**
　　现在可以在这个develop分支上做一些改动，并且提交。
　　**注意**：切换分支的时候可以发现，在Windows中的repository文件夹中的文件内容也会实时相应改变，变成当前分支的内容。

 

**push方法1：**

　　现在如果想直接Push这个develop分支上的内容到github

　　**git push -u origin**

　　如果是新建分支第一次push，会提示：　　fatal: The current branch develop has no upstream branch.
　　To push the current branch and set the remote as upstream, use
　　git push --set-upstream origin develop
　　输入这行命令，然后输入用户名和密码，就push成功了。

　　以后的push就只需要输入**git push origin**

　　

　　

**push方法2：**

　　比如新建了一个叫dev的分支，而github网站上还没有，可以直接：

　　**git push -u origin dev**

　　这样一个新分支就创建好了。

 

**push方法3：**

　　提交到github的分支有多个，提交时可以用这样的格式：

　　**git push -u origin local:remote**
　　

　　比如：**git push -u origin master:master**
　　表明将本地的master分支（冒号前）push到github的master分支（冒号后）。
　　**如果左边不写为空，将会删除远程的右边分支。**

 

## **创建分支的另一种方法**

　　用命令**git checkout -b develop2 develop**
　　可以新建一个分支develop2，同时切换到这个分支

 

## 删除分支

　　**git branch**可以查看所有的分支
　　**git branch -d develop2** 将develop2分支删除

 

## Clone

　　使用git clone+github地址的方法，项目默认只有master分支。**git branch**也只有master

　　要看所有的分支：**git branch -a**或者是**git branch -r**

　　这时候要新建一个分支，叫做dev，基于远程的dev分支：**git checkout -b dev origin/dev**

 

## 加Tag

　　**git tag tagname develop**
　　git tag中的两个参数，一个是标签名称，另一个是希望打标签的点develop分支的末梢。

 

## **合并分支**

　　**git checkout master**

　　先转到主分支
　　**git merge --no-ff develop**

　　然后把develop分支merge过来

　　**参数意义：**
　　不用参数的默认情况下，是执行快进式合并。
　　使用参数--no-ff，会执行正常合并，在master分支上生成一个新节点。
　　merge的时候如果遇到冲突，就手动解决，然后重新add，commit即可。