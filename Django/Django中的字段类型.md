## Django字段类型介绍

一，通过makemigrations，migrate来修改数据，

1.Django的ORM支持修改表结构，修改完以后，执行

```shell
python manage.py makemigrations
python manage.py migrate
```
这两句，就会看到更新了。超过长度的数据就会丢了。

#### CharField

```python
<1> CharField
        #字符串字段, 用于较短的字符串.
        #CharField 要求必须有一个参数 maxlength, 用于从数据库层和Django校验层限制该字段所允许的最大字符数.
```
#### IntegerField
```python
<2> IntegerField
       #用于保存一个整数.
```
#### FloatField
```python
<3> FloatField
        # 一个浮点数. 必须 提供两个参数:
        #
        # 参数    描述
        # max_digits    总位数(不包括小数点和符号)
        # decimal_places    小数位数
                # 举例来说, 要保存最大值为 999 (小数点后保存2位),你要这样定义字段:
                #
                # models.FloatField(..., max_digits=5, decimal_places=2)
                # 要保存最大值一百万(小数点后保存10位)的话,你要这样定义:
                #
                # models.FloatField(..., max_digits=19, decimal_places=10)
                # admin 用一个文本框(<input type="text">)表示该字段保存的数据.
```
#### AutoField
```python
<4> AutoField
        # 一个 IntegerField, 添加记录时它会自动增长. 你通常不需要直接使用这个字段; 
        # 自定义一个主键：my_id=models.AutoField(primary_key=True)
        # 如果你不指定主键的话,系统会自动添加一个主键字段到你的 model.
```
#### BooleanField
```python
<5> BooleanField
        # A true/false field. admin 用 checkbox 来表示此类字段.
```
#### 
```python
<6> TextField
        # 一个容量很大的文本字段.
        # admin 用一个 <textarea> (文本区域)表示该字段数据.(一个多行编辑框).
```
#### EmailField
```python
<7> EmailField
        # 一个带有检查Email合法性的 CharField,不接受 maxlength 参数.
```
#### DateField
```python
<8> DateField
        # 一个日期字段. 共有下列额外的可选参数:
        # Argument    描述
        # auto_now    当对象被保存时,自动将该字段的值设置为当前时间.通常用于表示 "last-modified" 时间戳.
        # auto_now_add    当对象首次被创建时,自动将该字段的值设置为当前时间.通常用于表示对象创建时间.
        #（仅仅在admin中有意义...)
```
#### DateTimeField
```python
<9> DateTimeField
        #  一个日期时间字段. 类似 DateField 支持同样的附加选项.
```
#### ImageField
```python
<10> ImageField
        # 类似 FileField, 不过要校验上传对象是否是一个合法图片.#它有两个可选参数:height_field和width_field,
        # 如果提供这两个参数,则图片将按提供的高度和宽度规格保存.
```
#### FileField
```python
<11> FileField
     # 一个文件上传字段.
     #要求一个必须有的参数: upload_to, 一个用于保存上载文件的本地文件系统路径. 这个路径必须包含 strftime #formatting, 
     #该格式将被上载文件的 date/time 
     #替换(so that uploaded files don't fill up the given directory).
     # admin 用一个<input type="file">部件表示该字段保存的数据(一个文件上传部件) 
     #注意：在一个 model 中使用 FileField 或 ImageField 需要以下步骤:
     #（1）在你的 settings 文件中, 定义一个完整路径给 MEDIA_ROOT 以便让 Django在此处保存上传文件. 
     # (出于性能考虑,这些文件并不保存到数据库.) 定义MEDIA_URL 作为该目录的公共 URL. 要确保该目录对 
     #  WEB服务器用户帐号是可写的.
     #（2） 在你的 model 中添加 FileField 或 ImageField, 并确保定义了 upload_to 选项,以告诉 Django
     # 使用 MEDIA_ROOT 的哪个子目录保存上传文件.你的数据库中要保存的只是文件的路径(相对于 MEDIA_ROOT). 
     # 出于习惯你一定很想使用 Django 提供的 get_<#fieldname>_url 函数.举例来说,如果你的 ImageField 
     # 叫作 mug_shot, 你就可以在模板中以 {{ object.#get_mug_shot_url }} 这样的方式得到图像的绝对路径.
```
#### URLField
```python
<12> URLField
      # 用于保存 URL. 若 verify_exists 参数为 True (默认), 给定的 URL 会预先检查是否存在( 即URL是否被有效装入且
      # 没有返回404响应).
      # admin 用一个 <input type="text"> 文本框表示该字段保存的数据(一个单行编辑框)
```
#### NullBooleanField
```python
<13> NullBooleanField
       # 类似 BooleanField, 不过允许 NULL 作为其中一个选项. 推荐使用这个字段而不要用 BooleanField 加 null=True 选项
       # admin 用一个选择框 <select> (三个可选择的值: "Unknown", "Yes" 和 "No" ) 来表示这种字段数据.
```
#### SlugField
```python
<14> SlugField
       # "Slug" 是一个报纸术语. slug 是某个东西的小小标记(短签), 只包含字母,数字,下划线和连字符.#它们通常用于URLs
       # 若你使用 Django 开发版本,你可以指定 maxlength. 若 maxlength 未指定, Django 会使用默认长度: 50.  #在
       # 以前的 Django 版本,没有任何办法改变50 这个长度.
       # 这暗示了 db_index=True.
       # 它接受一个额外的参数: prepopulate_from, which is a list of fields from which to auto-#populate 
       # the slug, via JavaScript,in the object's admin form: models.SlugField
       # (prepopulate_from=("pre_name", "name"))prepopulate_from 不接受 DateTimeFields.
```
#### XMLField
```python
<13> XMLField
        #一个校验值是否为合法XML的 TextField,必须提供参数: schema_path, 它是一个用来校验文本的 RelaxNG schema #的文件系统路径.
```
#### FilePathField
```python
<14> FilePathField
        # 可选项目为某个特定目录下的文件名. 支持三个特殊的参数, 其中第一个是必须提供的.
        # 参数    描述
        # path    必需参数. 一个目录的绝对文件系统路径. FilePathField 据此得到可选项目. 
        # Example: "/home/images".
        # match    可选参数. 一个正则表达式, 作为一个字符串, FilePathField 将使用它过滤文件名.  
        # 注意这个正则表达式只会应用到 base filename 而不是
        # 路径全名. Example: "foo.*\.txt^", 将匹配文件 foo23.txt 却不匹配 bar.txt 或 foo23.gif.
        # recursive可选参数.要么 True 要么 False. 默认值是 False. 是否包括 path 下面的全部子目录.
        # 这三个参数可以同时使用.
        # match 仅应用于 base filename, 而不是路径全名. 那么,这个例子:
        # FilePathField(path="/home/images", match="foo.*", recursive=True)
        # ...会匹配 /home/images/foo.gif 而不匹配 /home/images/foo/bar.gif
```
#### IPAddressField
```python
<15> IPAddressField
        # 一个字符串形式的 IP 地址, (i.e. "24.124.1.30").
```
#### CommaSeparatedIntegerField
```python
<16> CommaSeparatedIntegerField
        # 用于存放逗号分隔的整数值. 类似 CharField, 必须要有maxlength参数.
```

## 参数

#### 1、null=True
​		数据库中字段是否可以为空
#### 2、blank=True
　　django的 Admin 中添加数据时是否可允许空值
#### 3、primary_key = False
　　主键，对AutoField设置主键后，就会代替原来的自增 id 列
#### 4、auto_now 和 auto_now_add
　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  自动创建---永远是创建时的时间
#### 5、choices
GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
gender = models.CharField(max_length=2,choices = GENDER_CHOICE) 
　　这里我们用在内存创建一个关联,来取代再创建一个简单的表来关联
#### 6、max_length    限制最大长度
#### 7、default　　默认值
#### 8、verbose_name　　Admin中字段的显示名称
#### 9、name|db_column　　数据库中的字段名称
#### 10、unique=True　　不允许重复   
　　例如用户名注册时候是不允许重复的,在username字段里设置,不让重复
#### 11、db_index = True　　数据库索引    
#### 12、editable=True　　在Admin里是否可编辑
#### 13、error_messages=None　　错误提示   
   把错误提示修改成你想要的报错,这里加个字典来完成 gender = models.CharField(max_length=2,choices = GENDER_CHOICE,error_messages={"错误类型":"错误原因"})
#### 14、auto_created=False　　自动创建
#### 15、help_text　　在Admin中提示帮助信息
#### 16、validators=[]    提示区间,例如电话号码范围
#### 17、upload-to   文件上传功能 在 FileField 里加入 例如: file = modles.FileField(upload-to = "./upload

#### /"      指明上传的文件防止根目录下的/upload/文件夹下