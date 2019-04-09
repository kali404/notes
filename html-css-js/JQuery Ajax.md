## Ajax

JQuery 对 XMLHttpRequest 对象的封装更是简化到了极致，让我们能相对优雅的使用 `Ajax`。

```
$.ajax("url", {
 // 自定义请求头
 headers: {},
 method: 'GET', // POST PUT 默认 GET
 // 请求格式 (服务器根据格式解析数据)
 contentType: 'application/json' // POST 默认 application/x-www-form-urlencoded;charset=UTF-8
 // 发送数据
 data: {}
 // 接受格式
 dataType: 'html' // json text xml
    
}).done(function(data) {
 // 成功调用
 // data 服务器返回的数据
    
}).fail(function (xhr, status) {
 // 失败调用
 // xhr, status 错误的信息

}).always(function () {
 // 无论成功失败

})
```

------

## 上传文件

上传文件其实就是构建一个 `multipart formdata` 的 HTTP 请求，需要借助 `FormData 对象`。

```
// 构建数据
var data = new FormData()
data.append('name', $('[name=name]').val())
data.append('file', $('[name=thumb]')[0].files[0]) // file 对象

// 提交
$.ajax('url',{
 method: 'POST',
 data: data,
 processData: false, // 默认 | 不处理数据
 contentType: false // 默认 | 不设置内容类型
 ...
})

/*
 跟普通表单只有一处区别，就是普通表单的数据 data 是一个 json，上传文件是 FormData
*/
```