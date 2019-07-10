
# flask使用操作指南1

### 1. flask介绍

Flask是一个基于Python实现的web开发的'微'框架

[中文文档地址](http://docs.jinkan.org/docs/flask/)

Flask和Django一样，也是一个基于MVC设计模式的Web框架

flask流行的主要原因：

	a）有非常齐全的官方文档，上手非常方便
	
	b) 有非常好的拓展机制和第三方的拓展环境，工作中常见的软件都有对应的拓展，自己动手实现拓展也很容易

 	c) 微型框架的形式给了开发者更大的选择空间

### 2. 安装flask

#### 2.1虚拟环境搭建

	virtualenv --no-site-packages falskenv
	
	激活windows下虚拟环境
	cd Scripts
	activate

#### 2.2 安装

	pip install flask


### 3. 基于flask的最小的应用

创建hello.py文件
	
	from flask import Flask
	
	app = Flask(__name__)
	
	@app.route('/')
	def gello_world():
		return 'Hello World'
	
	if __name__ == '__main__':
	
		app.run()

运行：python hello.py

### 4. 初始化参数

```python
from flask import Flask

app = Flask(__name__)
```

* import_name
  * Flask程序所在包(模块)的位置,传`__name__`
* static_url_path 
  * 静态资源访问路径,默认为`/+static/+静态资源文件名`
* static_folder
  * 静态文件存放路径,如果为默认的话将在当前(与`__name__`有关)执行文件下的`static`目录
* templat_folder
  * 模板文件储存的文件夹,可以不传,默认为执行文件下的`templates`文件夹

```python
from flask import Flask

app = Flask(__name__,static_url_path='/ss',static_folder='ss',template_folder='aa')


@app.route('/')
def index():
    return 'hello flask'

if __name__ == '__main__':
    app.run()

```

> 目录结构

```
----
  |---aa
  |		|---1.html
  |---ss
  |     |--- a.png
  |---helloworld.py
```

> 访问 127.0.0.1:5000/ss/a.png 则可以看见a.png



### 5. Flask程序的配置参数

**Flask将配置信息保存到了app.config属性中，该属性可以按照字典类型进行操作。**

#### 读取

- `app.config.get(name)`
- `app.config[name]`

#### 设置

* 配置对象加载

  * 定义一个普通的类

  * app.config.from_object(定义配置信息类的名字)
    
    ```python
    class DefaultConfig(object):
        """默认配置"""
        SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
    
    app = Flask(__name__)
    
    app.config.from_object(DefaultConfig)
    
    @app.route("/")
    def index():
        return app.config['SECRET_KEY']
    ```
    
    > 访问后展示了SECRET_KEY的值
    
  * 以类的方式存储,可以复用,也就是说针对于不同的配置信息可以采用多继承的方式来加载配置信息

    ```python
    from flask import Flask
    
    app = Flask(__name__,static_url_path='/ss',static_folder='ss',template_folder='aa')
    
    class K(object):
        SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
        REDIS_URL = '127.0.0.1:3666'
        MYSQL_URL = '127.0.0.1:3306'
    
    class K2(K):
        MYSQL_URL = '192.168.0.55:8809'
        SECRET_KEY = 'ASDfgwer658965tyERTY2145TYU7uhgcf9852'
    
    app.config.from_object(K2)
    
    @app.route('/')
    def index():
        return app.config.get('SECRET_KEY')
    
    if __name__ == '__main__':
        app.run()
    ```

    > 访问后展示了 K2类中的配置信息.

  * 缺点

    * 暴漏了敏感的配置信息

* 从配置文件中加载

  * 单独的配置文件

    ```python
    SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
    REDIS_URL = '127.0.0.1:3666'
    # 以变量赋值方式来进行编写就好
    ```

  * app.config.from_pyfile(配置文件)

    ```python
    from flask import Flask
    
    app = Flask(__name__)
    app.config.from_pyfile('setting.py')
    
    @app.route('/')
    def index():
        return app.config.get('SECRET_KEY')
    
    if __name__ == '__main__':
        app.run()
    ```

    > 访问后也可以展示配置信息

  * 优点 : 一定程度保证配置文件的安全

  * 缺点 :  仍然不够安全 而且配置文件的文件名固定

* 从环境变量中加载

  * 通过环境变量值找到配置文件,环境变量的值为配置文件的绝对路径

    ```
    export PROJECT_SETTING='~/setting.py'
    ```

  * app.config.from_envvar('环境变量名')

    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    app.config.from_envvar('PROJECT_SETTING', silent=True)
    # True 表示当环境变量不存在时将不给予理睬,程序继续执行
    
    @app.route("/")
    def index():
        return app.config['SECRET_KEY']
    ```

    > 访问可以看见配置信息

  * 优点: 安全性更高;环境变量名字和值不用固定

  * 缺点: 使用特别麻烦

  * silent 没有设置相应值时是否抛出异常

    * False 表示不安静的处理，没有值时报错通知，默认为False
    * True 表示安静的处理，即时没有值也让Flask正常的运行下去

* 使用工厂模式创建Flask app，并结合使用配置对象与环境变量加载配置

  ```python
  from flask import Flask
  
  def create_flask_app(config):
      """
      创建Flask应用
      :param config: 配置对象
      :return: Flask应用
      """
      app = Flask(__name__)
      app.config.from_object(config)
  
      # 从环境变量指向的配置文件中读取的配置信息会覆盖掉从配置对象中加载的同名参数
      app.config.from_envvar("PROJECT_SETTING", silent=True)
      return app
  
  class DefaultConfig(object):
      """默认配置"""
      SECRET_KEY = 'itcast1'
  
  class DevelopmentConfig(DefaultConfig):
      DEBUG=True
  
  # app = create_flask_app(DefaultConfig)
  app = create_flask_app(DevelopmentConfig)
  
  @app.route("/")
  def index():
      print(app.config['SECRET_KEY'])
      return "hello world"
  ```

### 6.服务启动

```python
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug = True)
```

注意： \_\_name\_\_ == '\_\_main\_\_'在此处使用是用于确保web服务已经启动当脚本被立即执行。当脚本被另一个脚本导入，它被看做父脚本将启动不同的服务，所以app.run()调用会被跳过。

一旦服务启动，它将进入循环等待请求并为之服务。这个循环持续到应用程序停止，例如通过按下Ctrl-C。

**参数有如下**：

	debug 是否开启调试模式，开启后修改python的代码会自动重启
	
	port 启动指定服务器的端口号
	
	host主机，默认是127.0.0.1

在1.0版本之后，Flask调整了开发服务器的启动方式，由代码编写`app.run()`语句调整为命令`flask run`启动。 

* 终端启动

  ```$ export FLASK_APP=helloworld  # 指定运行的是那个flask的程序

  $ flask run

   * Running on http://127.0.0.1:5000/
  ```


  - `flask run -h 0.0.0.0 -p 8000` 绑定地址 端口

  - `flask run --help` 获取帮助

  - 生产模式与开发模式的控制

    通过`FLASK_ENV`环境变量指明

    - `export FLASK_ENV=production` 运行在生产模式，未指明则默认为此方式
    - `export FLASK_ENV=development`运行在开发模式


### 7.路由与视图

#### 查询路由信息

1. flask routes #查看flask 的路由信息,同样需要配置环境变量,来告诉查看哪个flask程序
2. 在flask内部查看路由信息
```python
print(app.url_map)# 此种方式,回多出来两个两个默认的请求方式 options,head

for rule in app.url_map.iter_rules():
    print('name={} path={}'.format(rule.endpoint, rule.rule)) 

```

#### 设置请求方式

- GET
- OPTIONS(自带)
- HEAD(自带)

通过methods=[] 指明允许的请求方式

```python
@app.route("/itcast1", methods=["POST"])
def view_func_1():
    return "hello world 1"

@app.route("/itcast2", methods=["GET", "POST"])
def view_func_2():
    return "hello world 2"
```



如果以不支持的请求方式访问 flask  返回405  method not allowed-

**get方式访问**

```http
GET  /

HTTP/1.1 200 OK
Content-Type: application/json
..
\r\n\r\n
'helloword'
```

**head方式访问**

HEAD -> 等同于GET请求方式，但是仅返回GET方式中 应该返回的响应状态码和响应头，不会返回响应体

```http
HEAD /

HTTP/1.1 200 OK
Content-Type: application/json
```

**option**

OPTIONS -> 询问服务器关于接口的访问信息

```http
options /  
返回举例： 支持的请求方式 支持的访问域名等
```

CORS 解决跨域问题 利用了options请求

django-cors扩展 django flask 或者其他扩展 解决思路

1. 编写中间件，在中间件中拦截处理options
2. 判断请求方式是否是options，如果不是opitons，不做处理，进入视图执行，否则，按照下面的流程处理
3. 从options请求中取出访问域名，与白名单中的允许域名对比，
4. 如果在白名单中，则返回允许跨域访问，否则返回不允许

