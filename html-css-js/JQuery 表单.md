# 表单

## 选择表单

需要注意的不多。

```
$('input')
$('select')
$('textarea')
$('[name=user]')
$('[type=checkbox]')
...
```

------

## 操作表单

JQuery 新增了一些操作表单的方法，列举常用几个。

```
// value
$('input').val() // 获取 value 的值
$('input').val('...') // 设置

// checkbox
$('[type=radio]').prop('checked') // 是否选中
$('[type=checkbox]').attr('checked', true) // true 选中 | false 反选
$('[type=checkbox]:checked') // 获取所有选中的对象, 返回JQ集合

// select
$('select').find('option:selected').val() // 当前选中的 option
.attr('selected', 'selected') // 选中
.removeAttr('selected') // 取消选中
```