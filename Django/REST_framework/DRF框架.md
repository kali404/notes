# Django REST Framework

>### 0. 模型类与表的关系
>
>模型类 <==> 表（table）
>
>类属性 <==> 字段（竖列，Field）
>
>对象     <==> 元组（横行，）



### 1. 前后端分离开发

- 前后端不分离开发：使用模板渲染数据，后端人员需要自己写页面的数据展示
- 前后端分离开发：前端加载静态文件后，以ajax形式向后端请求数据，后端根据接口返回数据，交给前端展示



### 2. web接口

请求方式： GET  POST  PUT  DELETE

请求路径： 由后端人员定义，更具视图功能定义

请求参数： 路径参数（使用正则获取，直接传入）查询参数（request.GET）表单（.POST） 非form（.body）

返回结果： 根据前端人员的需要返回。一般为JSON格式

> Restful接口风格：资源名词复数作为路径，一个视图函数只完成单一资源的单一操作



### 3. JWT 跨域访问



### 4.  序列化器 Serializer

- 用来模式化完成操作数据库功能的类。
- 主要作用：完成传入数据的**验证**（反序列化验证），数据库的增删改查**处理**，数据的**返回**（序列化返回）
- 基本模式：指定查那张表，查那些字段

```python
class BookSerialzier(serializers.Serializer):
    btitle = serializers.CharField(max_length=20, min_length=5)
    bread = serializers.IntegerField(max_value=10000, min_value=1, default=10)
    bpub_date = serializers.DateField(required=False, write_only=True)  
    bcomment = serializers.IntegerField(allow_null=True, read_only=True)
    bauth = serializers.PrimaryKeyRelatedField(queryset=AUTH.objects.all()) # 外键
```

> 主要字段用于数据的展示：要操作的表有什么字段，就写什么字段。
>
> 括号内的内容用于反序列化验证：read_only() 只读；write_only() 只写。

- 额外内容：

  1. 关系属性字段查找：（关系属性统一加上many=True和read_only=True）

    ```python
  # 1. 返回关联属性对应id
  heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
  # 2. 换回关联模型类的str值
  heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)
  # 3. 嵌套一个序列化器 (被嵌套的序列化器一定要先于嵌套的序列化器定义)
  heroinfo_set = HeroInfoSerialzier(many=True)
    ```

  2. 额外的（反序列化）验证方法：

    ```python
  # 1.自定义单一字段：
  def validate_btitle(self, value):
      if value == 'python':
          raise serializers.ValidationError('书名不能是python')
      return value
  # 2.多个字段验证
  def validate(self, attrs):
      if attrs['bread'] < attrs['bcomment']:
          raise serializers.ValidationError('阅读量小于评论量')
      return attrs
    ```

  3. 定义`creat()` 和`update()`

    ```python
  def create(self, validated_data):
      """保存序列化器数据"""
      book = BookInfo.objects.create(**validated_data)  # 创建模型类对象并返回
      return book

  def update(self, instance, validated_data):
      """更新序列化器数据"""
      instance.btitle = validated_data['btitle']  # 更新指定字段
      instance.bread = validated_data['bread']
      instance.save()
      return instance  # 返回模型类
    ```

    > 在视图类函数中指定序列化器时传入查询对象，则ser.save()调用update()
    >
    > 在视图类函数中指定序列化器时未传入任何参数，则ser.save()调用create()

    ​     

### 5. 模型序列化器 ModelSerializer

- 主要作用：根据指定的表单自动生成序列化器
- 基本模式：

```python
class BookModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BookInfo  # 指定生成字段的模型类
        field = ('btitle', 'bread') # field = ("__all__")
```

> 在使用模型序列化器时，外键字段会自动生成（id模式）但是**关系属性不会**

- 额外内容：

  1. 关系属性查找

  2. 额外的（反序列化）验证方法

     2.1 在class meta前显示指明字段或者添加

     ```python
     bread = serializers.IntegerField(max_value=100, min_value=20)
     sms_code = serializers.CharField(max_length=6, min_length=6)
     ```

     2.2 使用extra_kwargs修改或者添加

     ```python
     extra_kwargs = {
                 "bcomment": {
                     'max_value': 1000
                 }
             }
     ```

     2.3 read_only()验证

     ```python
     read_only_fields=('btitle',)
     ```

     2.4 使用自定义函数添加验证

     ```python
     def validate_mobile(self, value):
         if not re.match(r'1[3-9]\d{9}', value):
             raise serializers.ValidationError('手机格式不对')
         return value
     ```



> 需要指出的是，只有create()和update()才可以在序列化器中重写，需要完成其他功能需要在视图中重写
>
> 自定义验证方法也可以在序列化器中重写，也就是说，除了create和update其他函数会被当作验证方法调用
>
> 将方法函数写serializer中，一旦返回为空，会导致数据无法保存



### 6. 基本视图 View 

- 视图的基本操作在 接受，处理，处理，返回 的基础上变为：

  接受数据，查找对象（查表），建立序列化器和验证（验证），保存/更新数据（处理），返回数据（返回）

- GET获取单一对象

  ```python
  def get(self, request,id):
      # 2.指定查询集
      book = BookInfo.objects.get(pk=id)
      # 3.建立序列化器对象
      ser = BookSerialzier(book)
      # 5.返回对象
      return JsonResponse(ser.data, safe=False)
  ```

- GET获取全部对象

  ```python
  def get(self, request):
      # 2.指定查询集
      books = BookInfo.objects.all()
      # 3.建立序列化器对象
      ser = BookSerialzier(books, many=True)
      # 5.返回对象
      return JsonResponse(ser.data, safe=False)
  ```

- POST新建对象

  ```python
  def post(self, request):
      # 1、获取前端数据
      data = request.body.decode()
      data_dict = json.loads(data)
      # 3、使用序列化器验证数据
      ser = BookSerialzier(data=data_dict)
      ser.is_valid(raise_exception=True) 
      # 4、使用序列化器保存数据
      book = ser.save()  # ser.save()只保存通过反序列化验证的数据
      # 5、返回结果
      return JsonResponse(ser.data, safe=False)
  ```

- PUT更新对象

  ```python
  def put(self, request, pk):
      # 1、获取前端数据
      data = request.body.decode()
      data_dict = json.loads(data)
      # 2、指定查询集
      try:
          book = BookInfo.objects.get(id=pk)
      except:
          return JsonResponse({'error': '错误信息'}, status=400)
  	# 3、使用序列化器验证数据
      ser = BookSerialzier(book, data=data_dict)  
      ser.is_valid(raise_exception=True)
      # 4、使用序列化器更新数据
      book = ser.save()  # 只有在建立序列化器时传入了模型类，save方法才会调用update
      # 5、返回结果
      return JsonResponse(ser.data, safe=False)
  ```

- DELETE 删除

  ```python
  def delete(self, request, pk):
      # 2、指定查询集
      try:
          book = BookInfo.objects.get(id=pk)
      except:
          return JsonResponse({'error': '错误信息'}, status=400)
      # 3、修改属性
      book.is_delete=True
      book.save()
      # 5、返回结果
      return JsonResponse({})
  ```

  

### 7. 基本类 APIView

- 基本操作逻辑与View是完全一样的，主要的变化有：

  >获取查询参数：data = request.query_params
  >获取表单参数：data = request.data
  >返回数据：不需要加 safe = true

- GET获取单一对象

  ```python
  def get(self, request,id):
      # 2.指定查询集
      book = BookInfo.objects.get(pk=id)
      # 3.建立序列化器对象
      ser = BookSerialzier(book)
      # 5.返回对象
      return JsonResponse(ser.data)
  ```

- GET获取全部对象

  ```python
  def get(self, request):
      # 2.指定查询集
      books = BookInfo.objects.all()
      # 3.建立序列化器对象
      ser = BookSerialzier(books, many=True)
      # 5.返回对象.data
      return Response(ser.data)
  ```

- POST新建对象

  ```python
  def post(self, request):
      # 1、获取前端数据
      data = request.data
      # 3、使用序列化器验证数据
      ser = BookSerialzier(data=data)
      ser.is_valid(raise_exception=True)
      # 4、使用序列化器保存数据
      ser.save()
      # 5、返回结果
      return Response(ser.data)
  ```

- PUT更新对象

  ```python
  def put(self, request, pk):
      # 1、获取前端数据
      data = request.data
      # 2、指定查询集
      try:
          book = BookInfo.objects.get(id=pk)
      except:
          return JsonResponse({'error': '错误信息'}, status=400)
      # 3、使用序列化器验证数据
      ser = BookSerialzier(book, data=data)  
      ser.is_valid(raise_exception=True)
      # 4、使用序列化器更新数据
      ser.save()  
      # 5、返回结果
      return Response(ser.data)
  ```

- DELETE 删除

  ```python
  def delete(self, request, pk):
      # 2、指定查询集
      try:
          book = BookInfo.objects.get(id=pk)
      except:
          return JsonResponse({'error': '错误信息'}, status=400)
      # 3、修改属性
      book.is_delete=True
      book.save()
      # 4、返回结果
      return JsonResponse({})
  ```



### 8. 基本类 GenericAPIView

- 主要使用其子类：拓展类，功能专一，一般不单独使用

- 相对于APIView主要改变有：

>1. 需要提前指定 **查询集** 和 **序列化器** 
>2. 视图函数内指定查询对象变为 `self.get_queryset()`
>3. 视图函数内序列化器对象变为 `self.get_serializer(data=data)`
>4. 视图函数内获得单一查询对象 `get_object()` 需要在put函数中传入pk 且 不能在括号内传值
>5. 可以使用分页器：`paginator`

```python
class Books(GenericAPIView):

    queryset = BookInfo.objects.all()   # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier   # 指定当前类视图使用的序列化器

    def get(self, request):
        """查询全部数据"""
        # 2.获取指定查询集中的全部数据
        books = self.get_queryset()
        # 3.使用制定序列化器，获取序列化器对象
        ser = self.get_serializer(many=True)
        # 5.返回数据
        return Response(ser.data)

    def post(self, request):
        """创建模型类，保存数据"""
        # 1、获取前端数据
        data = request.data
        # 2、使用序列化器验证数据
        ser = self.get_serializer(data=data)
        ser.is_valid(raise_exception=True)
        # 3、使用序列化器保存数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)


class BookDRFView(GenericAPIView):

    queryset = BookInfo.objects.all()   # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier   # 指定当前类视图使用的序列化器

    def put(self, request, pk):
        """更新数据"""
        # 1、获取前端数据
        data = request.data
        # 2、从查询集中获取指定的单一数据对象（不需要传参）
        try:
            book = self.get_object()
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        # 3、使用序列化器验证数据
        ser = self.get_serializer(book, data=data)
        ser.is_valid(raise_exception=True)
        # 4、使用序列化器验更新数据
        ser.save()  # 只有在建立序列化器时传入了模型类，save方法才会调用update
        # 5、返回结果
        return Response(ser.data)

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '错误信息'}, status=400)
        book.is_delete = True
        book.save()
        return Response({})
```

> serializer_class里可以放多个序列化器，函数中使用get_serializer_class()获取该列表，取出一个序列化器
>
> filter_queryset()函数可以用来过滤queryset，但是需要在api_settings.DEFAULT_FILTER_BACKENDS中设置过滤器
>
> GenericAPIView 的功能单一主要体现在其提供的内置方法只能根据pk查询，如果需要其他功能需要手写功能。



### 9. 扩展类 ModelMixin

- 扩展类不是genericaAPIView的子类，扩展类子类才是。

```python
class Books(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDRFView(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin)
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)  # 注意，此处的删除就不再是逻辑删除了
    
    def get(self, request, pk):
		return self.retrieve(request,pk)  # 展示单一对象
```

> 扩展类的功能主要通过genericAPIView实现，所以必须继承。



### 10. 扩展类子类

- 功能特化的扩展类，他们是genericAPIView的子类

- 使用方法和扩展类一样，而且他们不需要重写方法，实际使用中可以根据扩展类转换使用

```python
class CreateAPIView(mixins.CreateModelMixin,GenericAPIView):
class ListAPIView(mixins.ListModelMixin,GenericAPIView):
class RetrieveAPIView(mixins.RetrieveModelMixin,GenericAPIView):
class DestroyAPIView(mixins.DestroyModelMixin,GenericAPIView):
class UpdateAPIView(mixins.UpdateModelMixin,GenericAPIView):
    
class ListCreateAPIView  # 不传参数
class RetrieveUpdateAPIView  # 查询pk
class RetrieveDestroyAPIView  # 查询pk
class RetrieveUpdateDestroyAPIView  # 查询pk
```



### 11. 基本视图集 ViewSet 和 GenericViewSet

- 视图集和视图使用方法完全一样，单独的视图集不常用，一般使用模型类视图集ModelViewSet

- 视图集与扩展类无关，所以其所有功能必须手写
- 视图集主要有一下特点

> 1. 可以自定义视图函数名（需要在路由中指定对应的请求方式）
> 2. 除了增删改查，可以自定义功能函数
> 3. 可以自定义路由，和自动生成路由



### 12. 模型类视图集 ModelViewSet

- 基本模式

  ```python
  class BooksDRF(ModelViewSet):
      queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
      serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器
  ```

- 可以自动生成路由

  ```python
  router = DefaultRouter()  # 路由初始化(还可以是SimpleRouter())
  router.register('view', modelviewset.viewset, base_name='booksDRF')  # 注册路由信息
  urlpatterns += router.urls  # 将自定义路由列表添加到系统路由列表中
  ```

- 可以自定义视图函数的名字

  ```python
  # 自定义的功能函数需要在路由中指明对应的请求方式
  url(r'^books_drf/$', viewset.Books.as_view({'get': 'list', 'post': 'create'})),
  ```

- 可以自定义功能函数

  ```python
  @action(methods=['get'], detail=True)
  def lastdata(self, request, pk):
      """自定义视图集如果要自动生成路由，需要使用action装饰器，参数为请求方式和额外请求参数"""
      book = self.get_object()
      ser = self.get_serializer(book)
      return Response(ser.data)
  ```

  ```python
  # url(r'^books_drf/(?P<pk>\d+)/lastdata/$', viewset.BookDRFView.as_view({'get': 'lastdata'})),
  ```

  > 只有视图集ViewSet和他的子类可以自定义功能，因为扩展类一系全部继承自View，它的功能函数名字是固定为get, post, put, delete等。即使被封装过也只能是list, create, update, retreve, destory，不能自定义。

- 支持使用多个序列化器

  ```python
  # 根据不同的请求选择不同的序列化器
  def get_serializer_class(self):
      if self.action == 'lastdata':
          return BookSerialzier  # 选择序列化器1
      elif self.action == 'create':
          return BookSerialzier  # 选择序列化器2
      else:
          return BookSerialzier  # 选择序列化器3
  ```

  > genericAPIView同样可以指定多个序列化器，`get_seralizer_class()`方法来自鱼GenericView
  >
  > 除了重写`get_seralizer_class()`函数以外同样可以使用列表的形式传递序列化器



### 13. 只读视图集 ReadOnlyModelViewSet

- 继承自 RetrieveModelMixin 和 ListModelMixin ，可以完成单一和多个对象的查询

- 扩展类的子类中是没有相应的子类的。

  > 不可以使用一个视图同时继承ListAPIView和RetrieveAPIView，他们需要不同的路由参数
  >
  > 不可以写两个路由通入该视图中，因为as_view()函数通过请求方式判断调用函数，如果一个视图中有两个get方法的回调函数，视图将报错。





**综上所诉，我们在实际DRF开发中常用的视图有：**

**APIView,**  -  纯手写，支持复杂的功能

**ModelMixin, ChildModelMixin**  - （按pk）增删改查其中一个或多个功能

**ModelViewSet**   - （按pk）增删改查全部的功能，还可以自定义功能

ReadOnlyModelViewSet  -   （使用自动生成的路由）一个视图中完成单个和多个对象的展示，可以自定义功能

>视图类系列只能使用pk查表，要使用其他字段查询，需要重写genericAPIView，或者手写APIView；
>
>视图类的功能函数是固定的，如果要自定义，需要使用ViewSet视图集；



使用**ModelMixin, ChildModelMixin, ModelViewSet** 基本代码都只有三行

1）定义视图类：`class BooksDRF(ModelViewSet):`
2）指定查询集：`queryset = BookInfo.objects.all()` 
3）指定序列化器：` serializer_class = BookSerialzier` 

> 项目中实际上还有指定权限验证 和 指定分页器， 一共五行。
>
> 其他在视图类中定义的函数都是对功能函数的重写，只有视图集支持自定义功能。



使用**ModelSerializer**代码一共只有三行：

1）定义序列化器：`class BookModelSerialzier(serializers.ModelSerializer):`
   				 `class Meta:`
2）指定模型类：	        `model = BookInfo`  

3）指定查询字段：	    `field = ('btitle', 'bread') # field = ("__all__")`

> 序列化器只能有create()和update()是对功能函数的重写，其他的函数都是验证函数。

