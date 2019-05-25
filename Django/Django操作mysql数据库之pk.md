# Django操作MySql数据库之pk

在使用django操作model的时候经常会用到根据id来查找某个对象，我们在官网上看到的是使用get(pk=1)这个方法，比如说：

```python
Student.objects.get(pk=1)  
```

但是我们还可以通过用另外一个方法得到相同的结果：

Students.objects.get(id=1)  

还有一种情况能够说明这一点，那就是在StudentAdmin里面有一个字段叫做list_display，相当于table里面的th，

我们可以这样写
```python
list_display = ['pk', 'name‘, 'age']  
```
 当但也可以写成：

```python
list_display = ['id', 'question', '']  
```
 结果显示都是它的主键的值

 那么这里面pk和id有什么不同和相同之处呢？

其实大部分情况来说pk和id是一样的，我们知道pk代表primary key的缩写，也就是任何model中都有的主键，那么id呢，大部分时候也是model的主键，所以在这个时候我们可以认为pk和id是完全一样的。

但是有时候不一样？什么时候？是的，你猜到了，当model的主键不是id的时候，这种情况虽然少，但是django为我们想到了，我们来看一下


```python
class Student(model.Model):  
​    my_id = models.AutoField(primary_key=True)  
​    name = models.Charfield(max_length=32)  
```
 这个时候，你可以用pk来找，因为django它知道Student的主键是my_id 但是，如果你用id去找的话，那就对不起，查无此人。