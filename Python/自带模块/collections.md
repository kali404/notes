# 不可不知的 Python 模块: collections 

## 基本介绍

我们都知道，Python 拥有一些内置的数据类型，比如 str, int, list, tuple, dict 等， collections 模块在这些内置数据类型的基础上，提供了几个额外的数据类型：

- `namedtuple()`: 生成可以使用名字来访问元素内容的 tuple 子类
- `deque`: 双端队列，可以快速的从另外一侧追加和推出对象
- `Counter`: 计数器，主要用来计数
- `OrderedDict`: 有序字典
- `defaultdict`: 带有默认值的字典

### namedtuple()

namedtuple 主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些 tuple 类型的数据时尤其好用。

#### 举个栗子

```python
"""
比如我们用户拥有一个这样的数据结构，每一个对象是拥有三个元素的tuple。
使用namedtuple方法就可以方便的通过tuple来生成可读性更高也更好用的数据结构。
"""
from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print website



Website(name='Sohu', url='http://www.google.com/', founder=u'\u5f20\u671d\u9633')
Website(name='Sina', url='http://www.sina.com.cn/', founder=u'\u738b\u5fd7\u4e1c')
Website(name='163', url='http://www.163.com/', founder=u'\u4e01\u78ca')
```

### deque

deque 其实是 `double-ended queue` 的缩写，翻译过来就是双端队列，它最大的好处就是实现了从队列 头部快速增加和取出对象: `.popleft()`, `.appendleft()` 。

你可能会说，原生的 list 也可以从头部添加和取出对象啊？就像这样：

```python
l.insert(0, v)
l.pop(0)
```

但是值得注意的是，list 对象的这两种用法的时间复杂度是 `O(n)` ，也就是说随着元素数量的增加耗时呈 线性上升。而使用 deque 对象则是 `O(1)` 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用 deque。

作为一个双端队列，deque 还提供了一些其他的好用方法，比如 `rotate` 等。

#### 举个栗子

```python
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print('\r%s' % ''.join(fancy_loading),)
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

```

### Counter

计数器是一个非常常用的功能需求，collections 也贴心的为你提供了这个功能。

#### 举个栗子

```python
"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()

c = Counter(s)

print(c.most_common(5))

[(' ', 54), ('e', 32), ('s', 25), ('a', 24), ('t', 24)]
```

### OrderedDict

在 Python 中，dict 这个数据结构由于 hash 的特性，是无序的，这在有的时候会给我们带来一些麻烦， 幸运的是，collections 模块为我们提供了 OrderedDict，当你要获得一个有序的字典对象时，用它就对了。

#### 举个栗子

```python
from collections import OrderedDict

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v

print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v



Regular Dict:
A 1
C 3
B 2
Ordered Dict:
A 1
B 2
C 3
```

### defaultdict

我们都知道，在使用 Python 原生的数据结构 dict 的时候，如果用 `d[key]` 这样的方式访问， 当指定的 key 不存在时，是会抛出 KeyError 异常的。

但是，如果使用 defaultdict，只要你传入一个默认的工厂方法，那么请求一个不存在的 key 时， 便会调用这个工厂方法使用其结果来作为这个 key 的默认值。

# from collections import defaultdict

```python
members = [

    ['male', 'John'],
    
    ['male', 'Jack'],
    
    ['female', 'Lily'],
    
    ['male', 'Pony'],
    
    ['female', 'Lucy'],

]


result = defaultdict(list)

for sex, name in members:

    result[sex].append(name)

print(result)

defaultdict(<type 'list'>, {'male': ['John', 'Jack', 'Pony'], 'female': ['Lily', 'Lucy']})
```