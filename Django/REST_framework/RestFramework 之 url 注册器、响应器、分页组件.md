## 一，url 注册器

之前我们再写数据类的增删该查视图时，如果使用视图类组件的话，需要写这样两条 url:

```
url(r"^author/$", views.AuthorView.as_view({"get": "list", "post": "create"})), 
url(r"^author/(?P<pk>\d+)/$", views.AuthorView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
```


每次都这么写，太麻烦了，所以 restframework 给我们提供了一种便捷的方式，就是 url 注册器；

在 urls.py 中这么写：



```
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
```


```
from rest_framework import routers
router = routers.DefaultRouter()
router.register("author", views.AuthorView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r"^author/$", views.AuthorView.as_view({"get": "list", "post": "create"})),
    # url(r"^author/(?P<pk>\d+)/$", views.AuthorView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
    url(r"^", include(router.urls)),
]
```




也以看到，它帮我们写了这么多 url

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921175440623-1421549240.png)

根据这个规则，我们不仅可以写我们原来的拿两条 url, 还可以有两条 url:

如：

```
http://127.0.0.1:8000/author.json/?token=552d69c2-4503-4d16-bacb-cc8da5f1b52c
```


直接就是返回的数据了：

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921180100408-580456031.png)

```
http://127.0.0.1:8000/author/1.json?token=552d69c2-4503-4d16-bacb-cc8da5f1b52c
```


![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921180409438-1228518901.png)

[回到顶部](#_labelTop)<a></a>

## 二，响应器

当我们用浏览器访问 restframework 搭建的服务器是，返回的是一个页面

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921190457308-408727331.png)

而不是数据，这是 restframework 帮我们做了这件事，只要是浏览器发的请求就会返回一个页面，使用 postman 等工具发送请求时，就返回数据；

我们可以看到在 apisettings 中，有这个默认配置：

```
'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
```


而帮我返回页面的响应器就是第二个，BrowsableAPIRenderer，只要我们在全局中配置这个属性，然后把这个类注释掉，就可以让浏览器也返回的是数据了；

settings 中的配置：

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}
```


这样浏览器发请求就不会返回页面了；

[回到顶部](#_labelTop)<a></a>

## 三，分页组件

### 1，视图类需要自己写逻辑

即需要自己写 get(), post() 方法等逻辑的，就是需要自己获取某个表的 queryset 时：

以 book 表的查看 (get()) 为例：



```
from rest_framework.pagination import PageNumberPagination
```


```
class BookView(APIView):
    # parser_classes = [FormParser, ]

    def get(self, request):
    
        class MyPageNumberPagination(PageNumberPagination):
            page_size = 2
            page_query_param = "page_num"  # 即url上的那个参数，默认时page
    
            page_size_query_param = "size"  # 临时要取数据的时候，可以在url上加的参数
            max_page_size = 3  # 限制上面那个size最多可以取的数据数量
    
        book_list = models.Book.objects.all()
        pnp = MyPageNumberPagination()
        paged_book_list = pnp.paginate_queryset(book_list, request)
        bs = BookSerializer(paged_book_list, many=True)
        # print(bs.data)
        return Response(bs.data)
```




url 上：

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921201503061-790919108.png)

使用 size: 获取 4 条，但是 max_page_size = 3 最大限制取三条：

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921201711268-871240170.png)

也可混合使用：

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921201815017-1533292247.png)

### 2 ，视图类继承 ModelViewSet

当我们的使用 modelviewset 时，也就是我们不用自己写 get(),post() 方法等逻辑了，那我们要怎么使用分页？

这个时候需要看看源码了! 看看源码中是怎么写 list() 方法的：

list() 方法：



```
class ListModelMixin(object):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
    
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```




找  self.paginate_queryset(queryset):



```
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
```




可以看到这个方法中，是用 self.paginator 再调用我们真正做分页的那个 paginate_queryset() 方法 (这个类中的 PageNumberPagination)！

明显这个 self.paginator 是个静态方法：



```
@property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()  # 这里注意分开看是self._paginator = self.pagination_class先找这个类，再去加()实例化
        return self._paginator
```




也就是他使用的那个分页类是  self.pagination_class，还是原来那套，先在自己的视图类中找 self.pagination_class 中找，然后再去全局 settings 中找，再去默认的；

默认的是：

```
pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
'DEFAULT_PAGINATION_CLASS': None,  可以看到默认的是None
```


所以使用分页器，我们只需要在自己的视图类中写上 pagination_class ，把我们自己的分页类加进去，就可以了：

**视图类：**



```
class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page_num"  # 即url上的那个参数，默认时page

    page_size_query_param = "size"  # 临时要取数据的时候，可以在url上加的参数size
    max_page_size = 3  # 限制上面那个size最多可以取的数据数量

class AuthorView(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = MyPageNumberPagination
```




![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921212518248-1708423696.png)