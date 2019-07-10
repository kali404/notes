
# flask使用操作指南2


### 1. 什么是蓝图

在Flask项目中可以用Blueprint(蓝图)实现模块化的应用，使用蓝图可以让应用层次更清晰，开发者更容易去维护和开发项目。蓝图将作用于相同的URL前缀的请求地址，将具有相同前缀的请求都放在一个模块中，这样查找问题，一看路由就很快的可以找到对应的视图，并解决问题了。

### 2.单一文件形式的蓝图

#### 2.1创建蓝图对象

```python
from flask import Blueprint

user_bp = Blueprint('user',__name__)
```

#### 2.2编写蓝图视图

```python
@user_bp.route('/login')
def login():
    return 'login page'
```

#### 2.3.注册蓝图(主程序)

```python
from flask import Flask
from user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp) # 注册蓝图对象

@app.route('/')
def index():
    return 'hello'
```

### 3.目录方式定义蓝图

> 目录结构

```
  |------ main.py # 启动文件
  |------ user  #用户蓝图 (文件内蓝图)
  |  |--- __init__.py  # 此处创建蓝图对象(包蓝图)
  |  |--- passport.py  
  |  |--- profile.py
  |  |--- ...
```

```python
#  main.py
from flask import Flask
from user import user_bp
from news import news_bp

app = Flask(__name__)

app.register_blueprint(user_bp) # 注册蓝图对象
app.register_blueprint(news_bp)

@app.route('/')
def index():
    return 'hello'
```

```python
#  __init__.py
from flask import Blueprint

news_bp = Blueprint('news',__name__)
from . import passport  #如果不在此处导入 那么主程序将找不到目录的蓝图文件,如果在之前导入(位置不对)则会发生循环导入的问题.
```

```python
#  passport.py
from . import new_bp

@new_bp.route('/get_passport')
def passport()
	return 'get passport'
```



### 4.蓝图扩展

* 通过`url-prefix`指定蓝图前缀

  ```
  app.register_blueprint(user_bp, url_prefix='/user')
  app.register_blueprint(goods_bp, url_prefix='/goods')
  ```

* 蓝图内部静态文件

  和应用对象不同，蓝图对象创建时不会默认注册静态目录的路由。需要我们在 创建时指定 static_folder 参数。

  ```
  admin = Blueprint("admin",__name__,static_folder='static_admin')
  admin = Blueprint("admin",__name__,static_folder='static_admin',static_url_path='/lib')
  ```

* 蓝图模板目录

  蓝图对象默认的模板目录为系统的模版目录，可以在创建蓝图对象时使用 template_folder 关键字参数设置模板目录

  ```python
  admin = Blueprint('admin',__name__,template_folder='my_templates')
  ```