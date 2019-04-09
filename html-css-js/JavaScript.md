# JavaScript

----------
# 引入

1.行内式
```html
<input type="button" name="" onclink="alert('OK!');">
```
2.内嵌式
```html
<script type="text/javascript">
		aleart('ok');
</script>
```
3.外链式

```html
<script type="text/javascript" src="js/index.js">
## 变量
```
弱类型语言下不需要指定变量类型,由他的值来确定他的类型,声明变量用var来声明

var iNum = 123;
var sTr = 'hello';

数据类型

数字

number

字符串

string

布尔值

boolean

未初始化类型

undefined

复合类型

object

命名规范

区分大小写

第一个字符必须是字母下划线

其他字符是大小写下划线和数字

匈牙利命名风格

第一个小写字符为类型的首拼第二个字符大写例如
数字 iNum
字符串sStr

## 对属性进行操作(修改)

先通过document.getElementById获取元素赋值给一个变量,然后可以对页面标签的属性进行修改

``` html
<style type="text/css">
    .sty01{
        font-size:20px;
        color:red;
    }
    .sty02{
        font-size:30px;
        color:pink;
        text-decoration:none;
    }

</style>

<script type="text/javascript">

    window.onload = function(){
        var oInput = document.getElementById('input1');
        var oA = document.getElementById('link1');
        // 读取属性值
        var sValue = oInput.value;
        var sType = oInput.type;
        var sName = oInput.name;
        var sLinks = oA.href;

        // 操作class属性,需要写成“className”
        oA.className = 'sty02';

        // 写(设置)属性
        oA.style.color = 'red';
        oA.style.fontSize = sValue;
    }

</script>

<input type="text" name="setsize" id="input1" value="20px">
<a href="#" id="link01" class="sty01">这是一个链接</a>
```

### 获取设置酒额标签包裹的内容

```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementById('div1');
        //读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        //写入
        oDiv.innerHTML = '<a href="http://www.itcast.cn">传智播客<a/>';
    }
</script>
<div id="div1">这是一个div元素</div>
```
## 常用操作

var 标签对象 = document.getElementById('id名称'); -> 获取标签对象

var 变量名 = 标签对象.属性名 -> 读取属性

标签对象.属性名 = 新属性值 -> 设置属性

##定时器

指一段时间后执行的一段代码
```html
setTimeout(func[,delay,param1,param2,...])以指定的时间间隔(毫秒)调用一次函数的定时器

<script> 
    function hello(){ 
        alert('hello'); 
    } 

    // 执行一次函数的定时器
    setTimeout(hello, 500);
</script>
```
```html
setInterval(func[,delay,param1,param2,...])以指定的时间间隔(毫秒)重复调用函数的定时器

<script> 
    function hello(){ 
        alert('hello'); 
    } 
    // 重复执行函数的定时器
    setInterval(hello, 1000);
</script>
```
**参数说明**

第一个参数 func , 表示定时器要执行的函数名

第二个参数 delay, 表示时间间隔，默认是0，单位是毫秒

第三个参数 param1, 表示定时器执行函数的第一个参数，一次类推传入多个执行函数对应的参数

清除定时器

clearTimeout

为调用 setTimeout 函数时所获得的返回值，使用该返回标识符作为参数，可以取消该 setTimeout 所设定的定时执行操作。

```html
<script>
    function hello(){
        alert('hello');
        // 清除只执行一次的定时器
        clearTimeout(t1)
    }
    // 执行一次函数的定时器
    t1 = setTimeout(hello, 500);
</script>
```

**clearInterval**

 为调用 setInterval 函数时所获得的返回值，使用该返回标识符作为参数，可以取消该 setInterval 所设定的定时执行操作

```html
<script>
    function hello(){
        alert('hello');
        // 清除只执行一次的定时器
        clearTimeout(t1)
    }
    // 执行一次函数的定时器
    t1 = setTimeout(hello, 500);
</script>
```


是运行在浏览器端的脚本语言,简称JS,能够让浏览器和用户有交互


函数

函数定义
```html
<script type="text/Javascript">
	funciton fnAlert(参数1,参数2){
		alert('hello');
		return hello;     //函数返回值,函数体内return代表结束函数
}
</script>
```
函数作用域

全局变量

函数内可以调用,修改

局部变量

不能全局使用,和被其他函数调用

判断语句
```

if\if...else...\if...elseif...
```
比较运算符
```
==
```
值是否相等
```
!=
```
不相等
```
===
```
值和类型是否相等
```
===
```
是否大于
```
<=
```
小于等于

逻辑运算符
```
&&
```
and
与
```
||
or
```
或
```
!

not
```
非

循环语句

for循环

```html
var array = [1, 4, 5];

for(var index = 0; index < array.length; index++){
    result = array[index];
    alert(result);
}

while

var array = [1, 4, 5];        
var index = 0;

while (index < array.length) {
    result = array[index];
    alert(result);
    index++;
}

do-while

var array = [1, 4, 5];
var index = 0;

do {
    result = array[index];
    alert(result);
    index++;
} while (index < array.length);
```

获取标签元素
```
<script type="text/javascript">
    window.onload = function(){   //设置页面加载完成执行的函数，在执行函数里面获取标签元素
//onload是页面所有元素加载完成的事件，给onload设置函数时，当事件触发就会执行设置的函数
        var oDiv = document.getElementById('div1');
//内置对象 document 上的 getElementById 方法来获取页面上设置了id属性的标签元素，获取到的是一个html对象，然后将它赋值给一个变量
    }
</script>
```
数组的定义

定义
```html
var aList = new Array(1,2,3,4)

var aList2 = [1,2,3,4]
```
多维数组
```
[[1,2,5],[6]]
```
操作

增加

参见: 数组.splice(开始删除的索引[不可以省略],删除的个数[可选],增加的数据[可选\可多个]) (增加)

数组.push(添加的数据);//向后添加

删除

下标删除

数组.splice(开始删除的索引[不可以省略],删除的个数[可选],增加的数据[可选\可多个])

增加 (增加)

数组.pop();//从后删除

修改

查询

获取长度

数组.length

下标取值
