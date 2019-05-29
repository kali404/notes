## 一，RestFramework 之频率组件源码部分

频率组件的源码部分和权限组件流程一模一样的，这里就不说了，直接上源码的主要逻辑部分：



```python
    def check_throttles(self, request):
        """
        Check if request should be throttled.
        Raises an appropriate exception if the request is throttled.
        """
        for throttle in self.get_throttles():
            if not throttle.allow_request(request, self):
                self.throttled(request, throttle.wait())
```




明确表示我们写的频率类需要一个 allow_request() 方法：

**频率类**（完成一分钟同一个 ip 只能访问三次）：



```python
import time
from rest_framework.throttling import BaseThrottle

class MyThrottle(BaseThrottle):
    visited_record = {}

    def __init__(self):
        self.history = None

    def allow_request(self, request, my_cbv):

        # 这个my_cbv是源码中传的我们的视图类，这里我们也要传进去
        # print(self.get_ident(request))  # 可以获取本次请求的ip
        ip = request.META.get("REMOTE_ADDR")
        if ip not in self.visited_record:
            self.visited_record[ip] = []

        current_time = time.time()
        history = self.visited_record[ip]
        self.history = history
        print(history)

        while history and current_time - history[-1] > 60:  # 把大于60秒的时间都删掉
            history.pop()

        if len(history) > 2:  # 第三次访问，列表中只有2个值，也满足条件
            return False
        history.insert(0, current_time)
        return True

    def wait(self):
        """
        用于返回还剩多少时间访问；

        本次访问时间：9:50:55
        [09:50:30, 09:50:20, 09:50:10]   剩余 60 - (9:50:55 - 09:50:10)秒才能访问
        :return:
        """
        c_time = time.time()
        return 60 - (c_time - self.history[-1])  
```




**视图类：**



```python
class BookView(generics.GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = [UserAuth]
    permission_classes = [VipPermission]
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```




效果如下：

![](https://img2018.cnblogs.com/blog/1304968/201809/1304968-20180921162618025-1909534286.png)

可以在全局 settings 配置



```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': 
        'app01.utils.auth_class.UserAuth',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'app01.utils.permission_class.VipPermission',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'app01.utils.throttle_class.MyThrottle',
    ),
}
```

##  二，使用 restframework 组件中的提供的访问限制

实现方式和我们上面的方式基本相同；

基于限制 ip 的类：SimpleRateThrottle   基于限制用户的：UserRateThrottle 等等；

基于 ip 的访问限制：

**频率类：**



```python
from rest_framework.throttling import SimpleRateThrottle

class MyThrottle(SimpleRateThrottle):

    scope = "visit_rate"  # 这个值决定了在配置时使用那个变量描述限制的频率

    def get_cache_key(self, request, view):  # 这个方法也是必须要有
        return self.get_ident(request)
```




这次只能在 setttings 中配置：



```python
REST_FRAMEWORK = {
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'app01.utils.throttle_class.MyThrottle',
    # ),
    'DEFAULT_THROTTLE_CLASSES': (
        'app01.utils.throttle_class.MyThrottle',
    ),
    "DEFAULT_THROTTLE_RATES": {
        "visit_rate": "10/m",   # 这个参数就是频率类中定义的那个参数scope， 其中第一个数字10表示10次，后面的m表示一分钟，还有s，一秒， h, 一小时， d, 一天
    }
}
```




```python
 duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
```

