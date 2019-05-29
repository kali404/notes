

## 一，RestFramework 之权限组件源码解析

restframework 的权限组件与认证组件源码类似, 都需要我们自己写一个类，然后放在 permission_classes 中，或者全局 settings 中配置；

我们直接看在 dispatch() 中的权限组件部分干了什么。



```python
    def initial(self, request, *args, **kwargs):

        self.format_kwarg = self.get_format_suffix(**kwargs)


        neg = self.perform_content_negotiation(request)
        request.accepted_renderer, request.accepted_media_type = neg
    

        version, scheme = self.determine_version(request, *args, **kwargs)
        request.version, request.versioning_scheme = version, scheme
    

        self.perform_authentication(request)
        self.check_permissions(request)  # 权限组件
        self.check_throttles(request)
```




再看 self.check_permissions(request)：



```python
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):  # 
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                )
```




可以看到，这个组件更加简单了，没有封装到 request 对象中，而是直接放在了 APIView 中；

根据源码我们写的类需要这么写：需要一个 has_permission() 的方法，这个方法要是返回 True，表示权限认证通过  ； 还可以定义一个 message，返回我们自定义的错误信息

**权限类：**



```python
from app01 import models
from rest_framework.permissions import BasePermission

class VipPermission(BasePermission):
    message = "您没有访问权限"

    def has_permission(self, request, my_cbv):
        if request.user.user_level >= 2:
            return True
        return False
```




**视图类：**



```python
class BookView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

    # authentication_classes = [UserAuth]
    permission_classes = [VipPermission]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```




也可以在 settings 中配置：



```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'app01.utils.auth_class.UserAuth',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'app01.utils.permission_class.VipPermission',  # 注意这里是要一个可迭代的，所以逗号不能少
    ),
}
```




**结果：**

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180920202816426-801356226.png)