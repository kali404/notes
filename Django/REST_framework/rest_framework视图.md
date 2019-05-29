## 一，版本一

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^book/$", views.BookView.as_view()),
    url(r"^book/(?P<pk>\d+)/$", views.SBookView.as_view()),  # 注意命名分组，名字必须是PK
]
```

```python
from app01 import models
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        # fields = ["title", "price", "publishDate"]  # 可以指定字段
        fields = "__all__"  # 所有字段
```

```python
from app01.serializer import BookSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework import generics

class BookView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Book.objects.all()  # 这两个参数得指定
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SBookView(generics.GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

去看看源码：

```python
class GenericAPIView(views.APIView):  # 这个类是继承了APIView
        queryset = None
        serializer_class = None
        
       ''' 还有其他的处理方法'''
```


```python
# 这5个类替我们写好了每种请求要做的事情，我们不同自己写，只需要继承它们就可以;

class ListModelMixin(object):   # 查看所有 get
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):


class CreateModelMixin(object):  # 添加 post
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):


class UpdateModelMixin(object):  # 更新 put(\d+)
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):


class DestroyModelMixin(object):  # 删除  delete(\d+)
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):


class RetrieveModelMixin(object):  # 查看单条记录  get/(\d+)
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
```


**但是，这样写我们每个表都要写get, post, put,delete,get/(\d+),还是有重复代码，继续下一版：**

## 二，版本二

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls)，
    url(r"^publish/$", views.PublishView.as_view()),
    url(r"^publish/(?P<pk>\d+)/$", views.SPublishView.as_view()),
]
class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publish
        fields = "__all__"
```
```
from rest_framework import generics
from app01 import models

class PublishView(generics.ListCreateAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = PublishSerializer


class SPublishView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = PublishSerializer
```



不用我们自己写每个请求的方法了，去看看源码：**其实是源码帮我们写了 我们要写的了。**



```python
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class RetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            GenericAPIView):
    """
    Concrete view for retrieving, updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

**但是，我们还是要写两个这个：**

```python
queryset = models.Publish.objects.all()
 serializer_class = PublishSerializer
```

在优化一次：


## 三，终极版


```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^author/$", views.AuthorView.as_view({"get": "list", "post": "create"})),
    url(r"^author/(?P<pk>\d+)/$", views.AuthorView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
]
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"
from app01.serializer import AuthorSerializer
from rest_framework.viewsets import ModelViewSet
class AuthorView(ModelViewSet):
    queryset = models.Author.objects.all()   # 只需要写这一次就可以了
    serializer_class = AuthorSerializer 
```

简单到不能再简单了！

看看**restframework源码**怎么操作的，真牛逼：

第一步： ModelViewSet类， 继承了放有具体执行每种操作的类(list, create, update, destroy, retrieve)


```python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```


第二步：GenericViewSet， 这个类啥都没看，继续看父类
```python
class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
    """
    The GenericViewSet class does not provide any actions by default,
    but does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """
    pass
```



第三步： ViewSetMixin


```python
class ViewSetMixin(object):
    """
    This is the magic.

    Overrides `.as_view()` so that it takes an `actions` keyword that performs
    the binding of HTTP methods to actions on the Resource.

    For example, to create a concrete view binding the 'GET' and 'POST' methods
    to the 'list' and 'create' actions...

    view = MyViewSet.as_view({'get': 'list', 'post': 'create'})
    """

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        """
        Because of the way class based views create a closure around the
        instantiated view, we need to totally reimplement `.as_view`,
        and slightly modify the view function that is created and returned.
        """
        # The suffix initkwarg is reserved for displaying the viewset type.
        # eg. 'List' or 'Instance'.
        cls.suffix = None

        # The detail initkwarg is reserved for introspecting the viewset type.
        cls.detail = None

        # Setting a basename allows a view to reverse its action urls. This
        # value is provided by the router through the initkwargs.
        cls.basename = None

        # actions must not be empty
        if not actions:
            raise TypeError("The `actions` argument must be provided when "
                            "calling `.as_view()` on a ViewSet. For example "
                            "`.as_view({'get': 'list'})`")

        # sanitize keyword arguments
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r" % (
                    cls.__name__, key))

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            # We also store the mapping of request methods to actions,
            # so that we can later set the action attribute.
            # eg. `self.action = 'list'` on an incoming GET request.
            self.action_map = actions

            # Bind methods to actions
            # This is the bit that's different to a standard view
            for method, action in actions.items():    # actions ---> {"get": "list", "post": "create"}   {"put": "update", "delete": "destroy", "get": "retrieve"}
                handler = getattr(self, action) # 第一种get请求  self.list = getattr(self, list)  第二种 get请求  self.retrieve = getattr(self, retrieve)
                setattr(self, method, handler)  # 第一种get请求 self.get = self.list  第二种get请求  self.get = self.retrieve

            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get

            self.request = request
            self.args = args
            self.kwargs = kwargs

            # And continue as usual
            return self.dispatch(request, *args, **kwargs)

        # take name and docstring from class
        update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=())

        # We need to set these on the view function, so that breadcrumb
        # generation can pick out these bits of information from a
        # resolved URL.
        view.cls = cls
        view.initkwargs = initkwargs
        view.suffix = initkwargs.get('suffix', None)
        view.actions = actions
        return csrf_exempt(view)
```


这个类里面有as_view(cls, actions=None, **initkwargs)方法， 也就是我们的url里面写的as_view({"get": "list", "post": "create"}),执行的是这个类中的as_view()方法，而不是APIView种的as_view()方法了！

把那个参数字典传给actions,在放回的view函数中，把每种请求要执行的那种方法 setattr()设置了（看代码中注释）；

然后当用户来访问时，执行那个view函数，正常执行dispatch()方法，根据请求方式分发到每种请求的方法中，**这次这个方法，是使用setattr()方法设置给self的，没有具体写**，也就能正常执行每种方法了。