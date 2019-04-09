## DOM

把 ==JavaScript DOM==的操作用 JQuery 的方法从新实现一遍。

------

## 获取元素

```
// id
$('#id')

// class
$('.className')

// tagName
$('tag')

/*
 上面三个对应的就是 getElements... 三个方法
*/
```

------

```
二级查找
/*
例如这种结构
<div>
 <p>...</p>
</div>
*/

// 下面两种是JQuery 二级查找的方法，JQuery 的选择器语法可以参考 “CSS 教程 - 选择器”
// $('div p') 返回的是一个 JQuery 对象，里面包含了元素的集合，$('div p')[0] 通过索引可以获取到集合里面的元素 [object HTMLParagraphElement]
$('div p')
$('div').find('p')
```

------

```
对象筛选
$('div').parent() // 当前元素的父元素
$('div').first() // 元素集合的第一个元素
$('div').last() // 元素集合的最后一个元素
$('div').eq(0) // 指定获取元素集合中第几个元素
$('div').next() // 当前元素的下一个元素
$('div').prev('.active') // 过滤掉 class=".active" 的 div 元素
```

------

```
元素遍历
/*
 <ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
 </ul>
*/

// each 方法
$('ul li').each(function(index, li) {
 console.log(index) // 当前索引
 console.log(li) // 当前元素
})

/*
遍历结果
0 | <p>1</p>
1 | <p>2</p>
2 | <p>3</p>
*/
```

------

## 操作元素

```
内容
/*
 <div>
  <p>内容</p>
 </div>
*/

console.log($('div').eq(0).html()) // <p>内容</p> | 获取 div 里面的所有内容，包括 HTML
console.log($('div').eq(0).text()) // 内容 | 获取文本内容
		
$('div').eq(0).html('为空是获取，写上内容就是修改')

/*
 $().eq().find().css()... 只要返回的结果是 JQuery 对象，就能一直 “.” 下去
 这样特性在 JQuery 中被称为 “连缀”
*/
```

------

```
属性
$().attr('class') // 获取属性
$().attr('class', 'red') // 修改属性
$().removeAttr() // 移除属性
```

------

```
样式
$().css('color', '#ccc') // 设置颜色
$().css('background', '#ccc') // 设置背景颜色，语法同 “css”
```

------

```
大小
/*
 大小是一组方法 .width() & .height()
*/

$(window).width() // 浏览器窗口大小
$(document).width() // 内容可视区域大小
$('div').width() // 指定区域大小
```

------

## 插入元素

```
// <ul></ul>

// 下级插入
$('ul').prepend('<li>1</li>') // 开头
$('ul').append('<li>2</li>') // 结尾

// 同级插入
$('ul li').eq(0).after($('ul').html()) // 之后
$('ul li').eq(0).before($('ul').html()) // 之前
```

------

## 移除元素

```
$('body').remove() // 整个页面都被移除了
```