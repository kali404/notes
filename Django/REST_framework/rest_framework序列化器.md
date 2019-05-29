#   REST_framework序列化器

## 一，自己手动序列化

```python
class Book(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
        book_list = models.Book.objects.all()
        temp = []
        for book in book_list:
            temp.append({"title": book.title, "publish_date": book.publishDate})  # 如果字段较多，不方便
        return JsonResponse(temp, safe=False)

    def post(self, request):
        print("post")
        print(request.data)
        return HttpResponse("ok")
```

## 二，使用django自带的序列化

```python
from django.core.serializers import serialize  # django自带的序列化
class Book(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
        book_list = models.Book.objects.all()
        data = serialize("json", book_list)  # 格式
        print(data)
        return HttpResponse(data)

    def post(self, request):
        print("post")
        print(request.data)
        return HttpResponse("ok")
```

get请求访问时，返回的数据：

```json
{"model": "app01.book", "pk": 1, "fields": {"title": "\u897f\u6e38\u8bb0", "price": "123.00", "publishDate": null, "publish": 1, "authors": [1, 2]}},
 {"model": "app01.book", "pk": 2, "fields": {"title": "\u4e09\u56fd\u6f14\u4e49", "price": "456.00", "publishDate": null, "publish": 2, "authors": [3]}},
 {"model": "app01.book", "pk": 3, "fields": {"title": "\u7ea2\u697c\u68a6", "price": "745.12", "publishDate": null, "publish": 3, "authors": [2]}}, 
{"model": "app01.book", "pk": 4, "fields": {"title": "\u6c34\u6d52\u4f20", "price": "456.23", "publishDate": null, "publish": 1, "authors": [3]}}]
```

默认的是这种格式，而且没有校验的功能；



## 三，使用restframework的序列化组件



### 1， get请求返回数据

```python
from rest_framework.response import Response
from rest_framework import serializers
 
class BookSerializer(serializers.Serializer):  # 在这个类中写什么字段，就序列化什么字段
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()


class Book(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
        book_list = models.Book.objects.all()
        bs = BookSerializer(book_list, many=True)  # 实例化上面那个类，传入一个queryset,mang=True表示很多序列化一条以上的数据
        print(bs.data)
        return Response(bs.data)

    def post(self, request):
        print("post")
        print(request.data)
        return HttpResponse("ok")
```

可以看到bs.data是一个列表中 放的一个个的有序字典：

```json
[OrderedDict([('title', '西游记'), ('price', '123.00'), ('publishDate', None)]),
 OrderedDict([('title', '三国演义'), ('price', '456.00'), ('publishDate', None)]), 
OrderedDict([('title', '红楼梦'), ('price', '745.12'), ('publishDate', None)]), 
OrderedDict([('title', '水浒传'), ('price', '456.23'), ('publishDate', None)])]
```

在前端响应中的数据是：

```json
[
    {
        "title": "西游记",
        "price": "123.00",
        "publishDate": null
    },
    {
        "title": "三国演义",
        "price": "456.00",
        "publishDate": null
    },
    {
        "title": "红楼梦",
        "price": "745.12",
        "publishDate": null
    },
    {
        "title": "水浒传",
        "price": "456.23",
        "publishDate": null
    }
]
```

### 2 ，post提交数据

使用book表：

```python
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publishDate = models.DateField(default="2018-09-18")
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE, default=1)
    authors = models.ManyToManyField(to="Author", default=2)

    def __str__(self):
        return self.title
```

先写那个序列化类：

对于普通字段：

```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()
```

在写我们的视图：

```python
class Book(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
        book_list = models.Book.objects.all()
        bs = BookSerializer(book_list, many=True)
        print(bs.data)
        return Response(bs.data)

    def post(self, request):
        print(request.data)
        bs = BookSerializer(data=request.data, many=False)  # many默认就是False,可以不写
        if bs.is_valid():  # 校验
            # 添加到数据库, 需要手动创建
            models.Book.objects.create(**request.data)
            return Response(bs.data)  # 创建成功，返回创建的数据
        else:
            return Response(bs.errors)  # 失败，返回错误信息
```



**序列化的过程：**

我们写了  bs = BookSerializer(data=request.data, many=False) 这句话的时候，

对于bs.data数据：

restframework序列化组件是这样做的：

```python
temp = [ ]
for obj in book_list:
　　temp.append({
　　　　"title": obj.title,  # 这里面的键就是我们写的字段
　　　　"price": obj.price,
　　　　"publishDate": obj.publishDate
})

json.dumps(temp)

```

那么，如果我们写了一对多，或者多对多字段，如：

```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()
    publish = serializers.CharField(max_length=32)  # 一对多关系
    authors = serializers.CharField(max_length=32)  # 多对多关系
```

在序列化过程中，就会出现obj.publish, 结果是publish的对象;  obj.authors, 结果是管理对象，即 app01.Author.None;

结果如下：



```json
# get请求的结果
[
    {
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish": "沙河出版社",  # 显示的str方法的结果
        "authors": "app01.Author.None"
    },
    {
        "title": "三国演义",
        "price": "456.00",
        "publishDate": null,
        "publish": "西二旗出版社",
        "authors": "app01.Author.None"
    },
    {
        "title": "红楼梦",
        "price": "745.12",
        "publishDate": null,
        "publish": "望京西出版社",
        "authors": "app01.Author.None"
    },
    {
        "title": "水浒传",
        "price": "456.23",
        "publishDate": null,
        "publish": "沙河出版社",
        "authors": "app01.Author.None"
    }]
```

所以，对于**一对多的字段：**



```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()
    publish_email = serializers.CharField(max_length=32, source="publish.email")
    publish_name = serializers.CharField(max_length=32, source="publish.name")
    authors = serializers.CharField(max_length=32)
```

**写上source之后，那里循环的时候就是采用的obj.source的内容了，所以前面的字段名称也就不一定要和表对齐了。**

```json
# get请求的结果
[
    {
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish_email": "132",
        "publish_name": "沙河出版社",
        "authors": "app01.Author.None"
    },
    {
        "title": "三国演义",
        "price": "456.00",
        "publishDate": null,
        "publish_email": "456",
        "publish_name": "西二旗出版社",
        "authors": "app01.Author.None"
    }]
```

对于**多对多字段**，我们当然也可以写source了，比如：

```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()
    publish_email = serializers.CharField(max_length=32, source="publish.email")
    publish_name = serializers.CharField(max_length=32, source="publish.name")
    authors = serializers.CharField(max_length=32, source="authors.all")
```

但是这样的话前端拿到的就是:

```json
[
    {
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish_email": "132",
        "publish_name": "沙河出版社",
        "authors": "<QuerySet [<Author: 觉先生>, <Author: 胡大炮>]>"  # 前端根本不能处理queryset类型，所以也就没有意义了
    }]
```

所以，**多对多字段**我们这么写：

```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publishDate = serializers.DateField()
    publish_email = serializers.CharField(max_length=32, source="publish.email")
    publish_name = serializers.CharField(max_length=32, source="publish.name")
    # authors = serializers.CharField(max_length=32)

    authors = serializers.SerializerMethodField()  # 多对多字段

    def get_authors(self, obj):  # 这里的obj是循环中的书籍对象， 函数名称必须是  get_多对多字段名
        ret = []
        for author in obj.authors.all():
            ret.append(
                {"name": author.name, "age": author.age}
            )
        return ret
```

前端拿到的数据：

```json

    {
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish_email": "132",
        "publish_name": "沙河出版社",
        "authors": [   # 这样前端就可以处理了
            {
                "name": "觉先生",
                "age": 18
            },
            {
                "name": "胡大炮",
                "age": 28
            }
        ]
    }
]
```

多对多字段的序列话的时候：

循环时，如果时多对多字段，那么

temp.append({

　　"字段名(authors)": get_authors()函数的返回值

})；

![img](1304968-20180918203620949-841282958.png)



## 四， 使用ModelSerializer

```python
from app01 import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        # fields = ["title", "price", "publishDate"]  # 可以指定字段
        fields = "__all__"  # 所有字段

 
class Book(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
        book_list = models.Book.objects.all()
        bs = BookSerializer(book_list, many=True)
        print(bs.data)
        return Response(bs.data)

    def post(self, request):
        print(request.data)
        bs = BookSerializer(data=request.data, many=False)  # many默认就是False,可以不写
        if bs.is_valid():  # 校验
            bs.save()  # 直接save()
            return Response(bs.data)  # 创建成功，返回创建的数据
        else:
            return Response(bs.errors)  # 失败，返回错误信息
```

**get请求数据**，结果为：

```json
[
    {
        "id": 1,
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish": 1,  # 默认取得都是主键
        "authors": [
            1,
            2
        ]
    },
    {
        "id": 2,
        "title": "三国演义",
        "price": "456.00",
        "publishDate": null,
        "publish": 2,
        "authors": [
            3
        ]
    },
    {
        "id": 3,
        "title": "红楼梦",
        "price": "745.12",
        "publishDate": null,
        "publish": 3,
        "authors": [
            2
        ]
    }
]
```

我们也可以自己配置， 方法和上面直接使用Serializer一致：

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        # fields = ["title", "price", "publishDate"]  # 可以指定字段
        fields = "__all__"  # 所有字段

    publish_email = serializers.CharField(max_length=32, source="publish.email")
    publish_name = serializers.CharField(max_length=32, source="publish.name")

    authors = serializers.SerializerMethodField()  # 多对多字段

    def get_authors(self, obj):  # 这里的obj是循环中的书籍对象
        ret = []
        for author in obj.authors.all():
            ret.append(
                {"name": author.name, "age": author.age}
            )
        return ret
```



get请求数据结果：

```json
[
    {
        "id": 1,
        "publish_email": "132",
        "publish_name": "沙河出版社",
        "authors": [
            {
                "name": "觉先生",
                "age": 18
            },
            {
                "name": "胡大炮",
                "age": 28
            }
        ],
        "title": "西游记",
        "price": "123.00",
        "publishDate": null,
        "publish": 1
    }
]
```

**post提交数据时**，数据库中没有的字段，就算是提交了，也不会报错，但是要是我们配置了某些字段，那么在提交时，这些字段也必须有，不然会校验失败；

如： 我们配置了 publish_email字段，所以提交数据，要求必须有这个字段，就算提交了这个字段，数据库也不会保存，但是不提交会校验失败。

**注意：对于post请求的时候，如果我们有扩展字段，如上面我们写的publish,author等字段，我们在get()查的时候可以，但是在post请求提交数据时会报错！**

看看源码：

```python
    def create(self, validated_data):
       
        raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        info = model_meta.get_field_info(ModelClass)  # 就是我们post请求传过来的数据
        many_to_many = {}
        for field_name, relation_info in info.relations.items():  # 循环post请求的数据
            if relation_info.to_many and (field_name in validated_data):  # 如果是多对多字段
                many_to_many[field_name] = validated_data.pop(field_name)  # 从validated_data中剔除，加到many_to_many字典中

        try:
            instance = ModelClass.objects.create(**validated_data)  # 此时的数据中已经没有多对多字段了，就可以直接create了
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                'Got a `TypeError` when calling `%s.objects.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.objects.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception was:\n %s' %
                (
                    ModelClass.__name__,
                    ModelClass.__name__,
                    self.__class__.__name__,
                    tb
                )
            )
            raise TypeError(msg)

        # Save many-to-many relationships after the instance is created.
        if many_to_many:  # 对于多对多字段，
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)  #  相当于 book.authors.set()
                field.set(value)

        return instance
```

因为源码中,会直接拿着我们写的覆盖人家的那个字段(publish, )去create,所以只要我们覆盖了默认的字段，源码会在这里抛出错误！

这里就需要我们配置参数来解决这个问题了：

对于某些字段只可读，就设置read_only = True，某些字段不需要传过去，但是提交的时候需要，就设为write_only = true;

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        # fields = ["title", "price", "publishDate"]  # 可以指定字段
        fields = "__all__"  # 所有字段
        extra_kwargs = {"publish": {"write_only": True}, "authors": {"write_only": True}}

    publish_email = serializers.CharField(max_length=32, source="publish.email", read_only=True)
    publish_name = serializers.CharField(max_length=32, source="publish.name", read_only=True)

    authors_info = serializers.SerializerMethodField()  # 多对多字段

    def get_authors_info(self, obj):  # 这里的obj是循环中的书籍对象
        ret = []
        for author in obj.authors.all():
            ret.append(
                {"name": author.name, "age": author.age}
            )
        return ret
```

这样我们在get获取数据的时候，结果：

```json
 {
        "id": 1,
        "publish_email": "132",
        "publish_name": "沙河出版社",
        "authors_info": [
            {
                "name": "觉先生",
                "age": 18
            },
            {
                "name": "胡大炮",
                "age": 28
            }
        ],
        "title": "西游记",
        "price": "123.00",
        "publishDate": null
    }
```

可以发现同时也没了默认的publish, authors字段，这是应为我们配置了：

```
extra_kwargs = {"publish": {"write_only": True}, "authors": {"write_only": True}}
```

让这两个字段只有在post提交的时候才生效，所以在post的时候这样传递数据也不会报错了！：



```json
 {
        "title": "西游sdsdf记",
        "price": "123.00",
        "publishDate": "2018-03-25",
        "publish": 1,
        "authors": [1,5]
    }
```

##  六，put,delete,get(\d+)请求

对于这三种请求，都需要一个参数,因为还有一个get的原因，我们不能这三个放在同一个视图中，所以需要再加一条路由线：

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^book/$", views.Book.as_view()),
    url(r"^book/(\d+)/$", views.SBook.as_view()),
]
```

他们的使用方式和modelform基本相同：

```python
class SBook(APIView):

    def delete(self, request, pk):
        models.Book.objects.filter(pk=pk).delete()
        return Response("")

    def put(self, request, pk):
        obj = models.Book.objects.filter(pk=pk).first()
        bs = BookSerializer(instance=obj, data=request.data)  # 注意instance
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def get(self, request, pk):
        obj = models.Book.objects.filter(pk=pk).first()
        bs = BookSerializer(obj, many=False)  # 传入单个对象，返回的就是一个序列化后的字典
        return Response(bs.data)
```



![img](1304968-20180920151315295-699685391.jpg)