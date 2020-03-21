## **python中 and和or的用法：**

python中的and从左到右计算表达式，若所有值为真，则返回最后一个值，若存在假，返回第一个假值。

or 也是从左到右计算表达式，返回第一个为真的值。

```python
# a 与b 均为真，返回最后一个为真的值，返回b的值
a = 1
b = 2
print(a and b)  >>>> 2

# c 与 d 有一个为假，返回第一个为假的值，返回c的值
c = 0
d = 2
print(c and d) >>>>>0

# e 与f 均为真，返回第一个 为真的值，返回e的结果
e = 1
f = 2
print(e or f) >>>>>>1

# g 与h 为假，返回第一个 为真的值，返回h的结果
g= ''
h=1
print(g or h)  >>>>>1
```


类似三目表达式的用法：bool? a : b
```shell
a ='first'
b ='second'
1and a or b   # 等价于 bool = true时的情况,a与b均为真
'first'
>>>0and a or b   # 等价于 bool = false时的情况
'second'
>>> a =''
>>>1and a or b   # a为假时，则出现问题
'second'
>>>(1and[a]or[b])[0]# 安全用法，因为[a]不可能为假，至少有一个元素
```
