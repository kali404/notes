## 运行 JQuery

在 [JQuery](http://jquery.com/) 的官网下载一个最新的版本，或者找到一家免费的公用 [CDN](https://cdn.baomitu.com/) 提供商，通过 script 标签引入之后，就可以执行 JQuery 的代码。

```
<!DOCTYPE html>
<html>
<head>
 <title>引入 JQery</title>
</head>
 <!-- cdn.baomitu.com 360 奇舞团 提供的免费 CDN 服务 -->
 <script type="text/javascript" src="https://lib.baomitu.com/jquery/2.2.4/jquery.min.js"></script>
<body>
</body>
</html>
```

------

## 执行顺序

DOM 的操作，必须等待页面的 DOM 加载完成，如果把 JavaScript 代码，写在 HTML 元素之前，那是获取不到 DOM 元素的。

```
<!DOCTYPE html>
<html>
<head>
 <title>执行顺序</title>
</head>
<body>
	
 <script type="text/javascript">
  alert(document.getElementsByTagName('div')[0]) // undefined
 </script>

 <div>...</div>

</body>
</html>
```

------

## load 事件

等待页面元素加载完成，触发的事件。

```
<!DOCTYPE html>
<html>
<head>
 <title>load 事件</title>
</head>
<body>

 <script type="text/javascript">
  window.onload = function() {
   alert(document.getElementsByTagName('div')[0]) // [object HTMLDivElement]
  }
 </script>

 <div>...</div>

</body>
</html>
```

这样就能获取得到后面的 div 元素。但是存在着一个问题，就是 `load 事件` 等待的是整个页面的元素都加载完毕才会触发，如果页面的元素足够的多，这个过程会耗时很久，照成了 JavaScript 执行卡顿。

由于网页的加载，是有 `加载级别` 的，我们可以把需要加载的元素归类，例如等待 `DOM` 加载完成完毕，就马上触发。DOM 通常只有很小的 `几K` 所有整个过程就会非常的快。

DOM 的加载完成挂载的是 `DOMContentLoaded 事件`，这一步通过 JQuery 来实现就非常简单。

------

## $

`$` 就是 `JQuery 对象`，通过它，我们就可以调用 `JQuery库` 的方法。

```
<!DOCTYPE html>
<html>
<head>
 <title>$</title>
</head>
<script type="text/javascript" src="https://lib.baomitu.com/jquery/2.2.4/jquery.min.js"></script>
<body>

 <script type="text/javascript">
  $(function() { // 这个代码块执行的，就是 DOM 被加载完毕触发
   alert(document.getElementsByTagName('div')[0]) // [object HTMLDivElement]
  })
 </script>

 <div>...</div>

</body>
</html>
```

总结一点 `JQuery 是什么` 就是基于 DOM 并且优化了 DOM 的操作。