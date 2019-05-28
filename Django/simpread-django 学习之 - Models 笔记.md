1：创建数据库表

```
#单表
# app01_user 生成的表明为 tb1
class User(models.Model):
    name = models.CharField(max_length=32,db_index=True) # 单列创建索引
    email = models.CharField(max_length=32)

    class Meta: # 生成的表名：tb1
        #数据库中生成的表名称，默认app名称+下划线+类名
        db_table='tb1' （重要）

         index_together={ ('name','email')} # 这就是联合索引，如用户名+密码验证（重要）
         # 联合索引根据最左前缀的模式，name最左
         # select * from where name = 'xx' 命中索引速度快
         # select * from where name = 'xx' and email='xx' 命中索引速度快
         # select * from where email='xx' 无法命中索引速度慢
         unique_together=(('name','email),) # 联合唯一索引，组合唯一（重要）
         verbose_name = '上课记录'
         verbose_name_plural = '上课记录' # admin里生成的表名

# 一对多/一对一/多对多，其中一对一和多对多都是基于一对多衍生出来的。

一对多，重要参数：on_delete,related_name,
class UserType(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    ForiegnKey(to='UserTyep',to_field='id',on_delete=models.CASCADE) #on_delete有多个选项，这里这个选项表示删除一个类型，将会删除此类型对应的所有用户

```



多表关系以及参数



按 Ctrl+C 复制代码<textarea></textarea>按 Ctrl+C 复制代码

实例：通过外键实现 2 个表的正反向操作

models 代码

```
class UserType(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    ut = models.ForiegnKey(to='UserTyep', to_field='id')
```


views 代码


```
def index(request):
    #　正向操作
    v = models.User.objects.all()
    for item in v:
        print(v.user)
        print(v.pwd)
        print(v.ut.name) # 这个实现跨表操作
    # 跨表提取指定的字段: ut__name为UserType的name字段
    h = models.User.objects.all().values('user','ut__name')
    # 反向操作
    v = models.UserType.objects.all()
    for item in v:
        print(item.name)
        print(item.user_set.all()) # 提取当前类型对应的所有用户
    # 跨表提取指定的字段: ut__name为UserType的name字段
    h = models.UserType.objects.all().values('name','user__pwd')
    return HttpResponse('index')
```


另：

```
# 使用参数：related_name='b' ，反向查询写法：item.b.all()
# 使用参数：related_query_name='a' 反向查询写法：item.a_set.all()

# 一对一，继承外键，并且加入了唯一约束
OneToOneField(ForeignKey)
to,                         # 要进行关联的表名
to_field=None               # 要关联的表中的字段名称
on_delete=None,             # 当删除关联表中的数据时，当前表与其关联的行的行为

```


```
# 多对多,关注参数：through,through_fields=None(当使用第3种方法时使用)
    1：django创建第三张表,增删改查方法如下：
        m2m.add/remove/set/clear/filter
    2：自己创建第三章表（没有m2m字段），要自己实现第三章表的链表查询
    实例：
    class Blog(models.Model):
        site = models.CharField(max_length=32)
    class Tag(models.Model):
        name = models.CharField(max_length=32)
    class B2T(models.Model):
        b = models.ForeignKey('Blog')
        t = models.ForeignKey('Tag')

    3：自定义第三张表，（有m2m字段）
        # 通过m2m字段查操作
        # 通过m2m字段 clear
    实例：通过through指定第三张表，通过through_field指定第三张表的关联字段，会创建3张表，第三张表的操作需要自己手工对B2T表操作
    class Blog(models.Model):
        site = models.CharField(max_length=32)
        m = models.ManyToManyField('Tag',through='B2T',through_field=['b','t1'] # 只能实现查询对Tag表
    class Tag(models.Model):
        name = models.CharField(max_length=32)
    class B2T(models.Model):
        b = models.ForeignKey('Blog')
        t1 = models.ForeignKey('Tag')
        t2 = models.ForeignKey('Tag')
```
常用操作记录

```python
# 获取个数
# models.Tb1.objects.filter(name='seven').count()
 
# 大于，小于
# models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值
# models.Tb1.objects.filter(id__gte=1)              # 获取id大于等于1的值
         # models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值
         # models.Tb1.objects.filter(id__lte=10)             # 获取id小于0的值
         # models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
 
         # in
         #
         # models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
         # models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in 
         # isnull
         # Entry.objects.filter(pub_date__isnull=True)
 
         # contains
         #
         # models.Tb1.objects.filter(name__contains="ven")
         # models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
         # models.Tb1.objects.exclude(name__icontains="ven")
 
         # range
         #
         # models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and
 
         # 其他类似
         #
         # startswith，istartswith, endswith, iendswith,
 
         # order by
         #
         # models.Tb1.objects.filter(name='seven').order_by('id')    # asc
         # models.Tb1.objects.filter(name='seven').order_by('-id')   # desc
 
         # group by
         #
         # from django.db.models import Count, Min, Max, Sum
         # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
         # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"
 
         # limit 、offset
         #
         # models.Tb1.objects.all()[10:20]
 
         # regex正则匹配，iregex 不区分大小写
         #
         # Entry.objects.get(title__regex=r'^(An?|The) +')
         # Entry.objects.get(title__iregex=r'^(an?|the) +')
 
         # date
         #
         # Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
         # Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))
 
         # year
         #
         # Entry.objects.filter(pub_date__year=2005)
         # Entry.objects.filter(pub_date__year__gte=2005)
 
         # month
         #
         # Entry.objects.filter(pub_date__month=12)
         # Entry.objects.filter(pub_date__month__gte=6)
 
         # day
         #
         # Entry.objects.filter(pub_date__day=3)
         # Entry.objects.filter(pub_date__day__gte=3)
 
         # week_day
         #
         # Entry.objects.filter(pub_date__week_day=2)
         # Entry.objects.filter(pub_date__week_day__gte=2)
 
         # hour
         #
         # Event.objects.filter(timestamp__hour=23)
         # Event.objects.filter(time__hour=5)
         # Event.objects.filter(timestamp__hour__gte=12)
 
         # minute
         #
         # Event.objects.filter(timestamp__minute=29)
         # Event.objects.filter(time__minute=46)
         # Event.objects.filter(timestamp__minute__gte=29) 
         # second
         #
         # Event.objects.filter(timestamp__second=31)
         # Event.objects.filter(time__second=2)
         # Event.objects.filter(timestamp__second__gte=31)
```
querySet包含的功能



```python
def all(self)
    # 获取所有的数据对象

def filter(self, *args, **kwargs)
    # 条件查询
    # 条件可以是：参数，字典，Q

def exclude(self, *args, **kwargs)
    # 条件查询
    # 条件可以是：参数，字典，Q

def select_related(self, *fields)
     性能相关：表之间进行join连表操作，一次性获取关联的数据。
     model.tb.objects.all().select_related()
     model.tb.objects.all().select_related('外键字段')
     model.tb.objects.all().select_related('外键字段__外键字段')

def prefetch_related(self, *lookups)
    性能相关：多表连表操作时速度会慢，使用其执行多次SQL查询在Python代码中实现连表操作。
            # 获取所有用户表
            # 获取用户类型表where id in (用户表中的查到的所有用户ID)
            models.UserInfo.objects.prefetch_related('外键字段')

            from django.db.models import Count, Case, When, IntegerField
            Article.objects.annotate(
                numviews=Count(Case(
                    When(readership__what_time__lt=treshold, then=1),
                    output_field=CharField(),
                ))
            )

            students = Student.objects.all().annotate(num_excused_absences=models.Sum(
                models.Case(
                    models.When(absence__type='Excused', then=1),
                default=0,
                output_field=models.IntegerField()
            )))

def annotate(self, *args, **kwargs)
    # 用于实现聚合group by查询

    from django.db.models import Count, Avg, Max, Min, Sum

    v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id'))
    # SELECT u_id, COUNT(ui) AS `uid` FROM UserInfo GROUP BY u_id

    v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id')).filter(uid__gt=1)  #这里的filter相当于having
    # SELECT u_id, COUNT(ui_id) AS `uid` FROM UserInfo GROUP BY u_id having count(u_id) > 1

    v = models.UserInfo.objects.values('u_id').annotate(uid=Count('u_id',distinct=True)).filter(uid__gt=1) # distinct去重
    # SELECT u_id, COUNT( DISTINCT ui_id) AS `uid` FROM UserInfo GROUP BY u_id having count(u_id) > 1

def distinct(self, *field_names)
    # 用于distinct去重
    models.UserInfo.objects.values('nid').distinct()
    # select distinct nid from userinfo

    注：只有在PostgreSQL中才能使用distinct进行去重

def order_by(self, *field_names)
    # 用于排序
    models.UserInfo.objects.all().order_by('-id','age')

def extra(self, select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
    # 构造额外的查询条件或者映射，如：子查询

    Entry.objects.extra(select={'new_id': "select col from sometable where othercol > %s"}, select_params=(1,))
    Entry.objects.extra(where=['headline=%s'], params=['Lennon'])
    Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
    Entry.objects.extra(select={'new_id': "select id from tb where id > %s"}, select_params=(1,), order_by=['-nid'])

 def reverse(self):
    # 倒序
    models.UserInfo.objects.all().order_by('-nid').reverse()
    # 注：如果存在order_by，reverse则是倒序，如果多个排序则一一倒序

 def defer(self, *fields):
    models.UserInfo.objects.defer('username','id')
    或
    models.UserInfo.objects.filter(...).defer('username','id')
    #映射中排除某列数据

 def only(self, *fields):
    #仅取某个表中的数据
     models.UserInfo.objects.only('username','id')
     或
     models.UserInfo.objects.filter(...).only('username','id')

 def using(self, alias):
     指定使用的数据库，参数为别名（setting中的设置）

##################################################
# PUBLIC METHODS THAT RETURN A QUERYSET SUBCLASS #
##################################################

def raw(self, raw_query, params=None, translations=None, using=None):
    # 执行原生SQL
    models.UserInfo.objects.raw('select * from userinfo')

    # 如果SQL是其他表时，必须将名字设置为当前UserInfo对象的主键列名
    models.UserInfo.objects.raw('select id as nid from 其他表')

    # 为原生SQL设置参数
    models.UserInfo.objects.raw('select id as nid from userinfo where nid>%s', params=[12,])

    # 将获取的到列名转换为指定列名
    name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
    Person.objects.raw('SELECT * FROM some_other_table', translations=name_map)

    # 指定数据库
    models.UserInfo.objects.raw('select * from userinfo', using="default")

    ################### 原生SQL ###################
    from django.db import connection, connections
    cursor = connection.cursor()  # cursor = connections['default'].cursor()
    cursor.execute("""SELECT * from auth_user where id = %s""", [1])
    row = cursor.fetchone() # fetchall()/fetchmany(..)

def values(self, *fields):
    # 获取每行数据为字典格式

def values_list(self, *fields, **kwargs):
    # 获取每行数据为元祖

def dates(self, field_name, kind, order='ASC'):
    # 根据时间进行某一部分进行去重查找并截取指定内容
    # kind只能是："year"（年）, "month"（年-月）, "day"（年-月-日）
    # order只能是："ASC"  "DESC"
    # 并获取转换后的时间
        - year : 年-01-01
        - month: 年-月-01
        - day  : 年-月-日

    models.DatePlus.objects.dates('ctime','day','DESC')

def datetimes(self, field_name, kind, order='ASC', tzinfo=None):
    # 根据时间进行某一部分进行去重查找并截取指定内容，将时间转换为指定时区时间
    # kind只能是 "year", "month", "day", "hour", "minute", "second"
    # order只能是："ASC"  "DESC"
    # tzinfo时区对象
    models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.UTC)
    models.DDD.objects.datetimes('ctime','hour',tzinfo=pytz.timezone('Asia/Shanghai'))

    """
    pip3 install pytz
    import pytz
    pytz.all_timezones
    pytz.timezone(‘Asia/Shanghai’)
    """

def none(self):
    # 空QuerySet对象

####################################
# METHODS THAT DO DATABASE QUERIES #
####################################

def aggregate(self, *args, **kwargs):
   # 聚合函数，获取字典类型聚合结果
   from django.db.models import Count, Avg, Max, Min, Sum
   result = models.UserInfo.objects.aggregate(k=Count('u_id', distinct=True), n=Count('nid'))
   ===> {'k': 3, 'n': 4}

def count(self):
   # 获取个数

def get(self, *args, **kwargs):
   # 获取单个对象

def create(self, **kwargs):
   # 创建对象

def bulk_create(self, objs, batch_size=None):
    # 批量插入
    # batch_size表示一次插入的个数
    objs = [
        models.DDD(name='r11'),
        models.DDD(name='r22')
    ]
    models.DDD.objects.bulk_create(objs, 10)

def get_or_create(self, defaults=None, **kwargs):
    # 如果存在，则获取，否则，创建
    # defaults 指定创建时，其他字段的值
    obj, created = models.UserInfo.objects.get_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 2})

def update_or_create(self, defaults=None, **kwargs):
    # 如果存在，则更新，否则，创建
    # defaults 指定创建时或更新时的其他字段
    obj, created = models.UserInfo.objects.update_or_create(username='root1', defaults={'email': '1111111','u_id': 2, 't_id': 1})

def first(self):
   # 获取第一个

def last(self):
   # 获取最后一个

def in_bulk(self, id_list=None):
   # 根据主键ID进行查找
   id_list = [11,21,31]
   models.DDD.objects.in_bulk(id_list)

def delete(self):
   # 删除

def update(self, **kwargs):
    # 更新

def exists(self):
   # 是否有结果
```


2：操作数据库表

- 基本操作
- queryset 中的方法：
- 返回 queryset 类型（select_related,prefetch_related），这个 2 个涉及到性能

实例：依次举例普通的写法和提高性能的写法

```
    实例：sql效率不高的写法
    def index(request):
        # 加入用户表有10条数据
        users = models.User.objects.all()  # 这里执行一次sql请求
        for row in users:
            print(row.user,row.pwd,row_ut_id)
            print(row.ut.name)  # 这里外键会再次发起一次sql请求
            print(row.ut1.name)  # 这里外键会再次发起一次sql请求
    实例：相对以上，优化写法,但是缺点是这里取到的是字典，不是对象
    def index(request):
        # 加入用户表有10条数据
        users = models.User.objects.all().values('user','pwd','ut__name')
        for row in users:
            pass
    实例select_related：相对第一个，只需要加1个参数select_related()，即可将关联的表一次性拿到，可以在括号内加入关联的字段，注意只能加关联的字段，满足优化
    def index(request):
        # 加入用户表有10条数据
        users = models.User.objects.all().select_related('ut')
        for row in users:
            print(row.user,row.pwd,row_ut_id)
            print(row.ut.name)
            print(row.ut1.name)
    实例prefetch_related：会进行2次sql请求，第二次会根据第一次的结果在关联表进行sql查询。如果存在多个关联参数，每个参数将会进行一次sql请求。
    def index(request):
        # 加入用户表有10条数据
        users = models.User.objects.all().prefetch_related('ut')
        # 这里会进行2次数据库sql查询，第二次查询会根据第一次的结果进行查询，
        for row in users:
            print(row.user,row.pwd,row_ut_id)
            print(row.ut.name)
            print(row.ut1.name)
```


3：数据验证（弱）：一般不使用

    - full_clean 进行验证
        经历的步骤
        - 每个字段的正则
        - clean钩子
```
models.User.objects.create(name='root',email='123') 这种情况无法验证
obj = models.User(name='root',email='123')
obj.full_clean()  #使用这个方法可以验证,如果不通过，程序会直接报错
obj.save()
```
也可以在函数内自定义验证条件
实例：通过钩子clean重写，实现验证


```
    def User(models.Mode):
        name = models.CharField(max_length=32)
        email = models.EmailField()

        def clean(self):  # 这里的clean是models里的钩子，用于重写操作
            from django.core.exceptions import ValidationError
            c = User.object.filter(name=self.name).count()
            if c:
                raise ValidationError(message='用户名已经存在',code='i1'):
```

