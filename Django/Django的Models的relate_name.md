# 关于 django Models 的个人理解和 related_name 的使用

Django 提供了三种最为通用的数据库关系模型

　　 1 mang-to-many(对对多关系)

　　 2 many-to-one(多对一关系)

　　3 one-to-one(一对一关系) 

 

## 一，多对一关系：

　　用 ForeignKey 来定义多对一的关系。用法和其他的 Field 是一样的, 把它放到模型中类的属性定义中就行了。ForeignKey 需要一个与之相关联的类作为

*位置参数。在这里我用 django book 中的一个比较经典的实例来和大家一起分享一下：首先，定义了三个模型分别为：Publisher(出版商),Author(作者) 和 Book(书)*

```python
 1 class Publisher(models.Model):
 2     name = models.CharField(max_length=30)
 3     address = models.CharField(max_length=50)
 4     city = models.CharField(max_length=60)
 5     state_province = models.CharField(max_length=30)
 6     country = models.CharField(max_length=50)
 7     website = models.URLField()
 8     def __unicode__(self):
 9          return self.name
10 
11 
12 class Meta:
13         ordering = ['name']
14 
15 
16 class Author(models.Model):
17     first_name = models.CharField(max_length=30)
18     last_name = models.CharField(max_length=40)
19     email = models.EmailField(blank=True)
20     def __unicode__(self):
21          return  u'%s %s' % (self.first_name, self.last_name)
22 
23 
24 class Book(models.Model):
25     title = models.CharField(max_length=100)
26     authors = models.ManyToManyField(Author)
27     publisher = models.ForeignKey(Publisher, related_name = "publisher_set")
28     publication_date = models.DateField(blank=True, verbose_name='e-mail')
29     num_pages = models.IntegerField(blank=True, null=True)
30     # objects = BookManager()
31     objects = models.Manager()           # The default manager.
32     dahl_objects = DahlBookManager()     # The Dahl-specific manager
33 
34     # .
35     def __unicode__(self):
36          return self.title
```

要建立一个递归的关系，即一个对象和自身的多对一关系，你可以这样写：`models.ForeignKey('self') :`

```python
class Employee(models.Model): 2 manager = models.ForeignKey('self') 
```

如果你创建关系时, 所需的模型还没有被定义, 你可以不使用模型对象本身, 而是使用那个模型的名字。

 

```python
1 class Car(models.Model):
2 manufacturer = models.ForeignKey('Manufacturer')
3 ...
4 class Manufacturer(models.Model):
```

但是, 你要记住, 只能对在同一个 models.py 文件中的模型使用字符串引用, 对于其他应用程序中的模型或者从其他地方导入的模型是不能使用名字对其做引用的。
Django 在数据库中使用的列名称是对应的字段的名称后追加 _id 得到的字符串。再前面的那个例子中, Car 模型对应的数据库表中会有一个名字是 manufacturer_id 的列,(你可以通过指定 db_column 来显式改变这个名字, 参见前面的 db_column 一节) 但是, 如果你不需要写定制的 SQL 语句的话, 你永远不要去处理数据库列名, 只需要处理你的模型对象中的
字段名称。

## ForeignKey 选项

#### 1.edit_inline：

如果不设为 False 的话, 它对应的对象就可以在页面上内联编辑, 就是说这个对象有自 己独立的
管理界面。如果设为 models.TABULAR 或者 models.STACKED 的话, 这个内 联编辑对象分别显
示成一个表格或者一些字段的集合。

#### 2.limit_choices_to：

*可以限定对象的值的范围的一个参数和值的字典。结合 Python 的 datetime 模块的*

*函数可以根据日期来限定对象。例如, 下面的代码:limit_choices_to = {'pub_date__lte': datetime.now}把可选对象限定到 pub_date 早于当前时间的对象中。除字典外, 这里也可以是一个可以执行更复杂的查询的 Q 对象这个选项和 edit_inline 是不兼容的。*

#### 3.max_num_in_admin

于内联编辑对象, 这个是要在管理界面里显示的相关对象的最多个数。所以, 如果披萨最多 只会
有 10 种配料, max_num_in_admin=10 会保证用户最多输入 10 种配料。
记住, 本项并不保证不会创建 10 种以上的配料, 他只是控制管理界面, 而不是在 Python 的 API 层和
数据库层做什么限制。

#### 4.min_num_in_admin

在管理界面中要显示的相关的对象的最少个数。通常, 在创建的时候, 显示的内联对象的个数 为
num_in_admin 个, 在编辑的时候, 在当前的基础上又会多显示 num_extra_on_change 个空对
象, 但是显示的对象个数不会少于 min_num_in_admin 个。

#### 5.num_extra_on_change

修改对象时要额外显示的对象数目。

#### 6.num_in_admin

添加对象时要显示的内联对象的默认个数。

#### 7.raw_id_admin

为要键入的整数显示一个文本框, 而不是一个下拉列表。在关联对象有很多行时, 这个比显示 一个
列表选择框更实用。
使用 edit_inline 时, 本项无效。

#### 8.related_name

关联对象反向引用描述符。

#### 9.to_field

关联对象的用于关联的字段, Django 默认使用关联对象的主键。

要学习 ForeignKey 并了解深刻的话，可以先对以上 ForeignKey 的这些选项有一定的了解。这样可以加深你对 ForeignKey 的印象。

　　通过 Book 这张表去访问 Publisher 和 Author 都是可以直接访问的，因为 Book 这张表中有外键和这两张表关联，因此可以直接通过语句去访问 Book 和 Publisher 表。

 这一步相信大家都是知道的，即使不知道，等你看了笔者的这篇博客之后肯定也会一目了然的。但是，假如反过来该怎么去查询呢？

（通过 Publisher 或者 Author 表查询 Book 表中的内容）在这里就要用到一个相当重要的 ForeignKey 选项，通过该选项你可以随便访问 Books

中的任意字段。