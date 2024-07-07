# app.route()装饰器
> app.route()是Flask框架中用于定义路由的装饰器函数，将url与函数绑定，实现映射。


现代 Web 应用的 URL 十分优雅，易于人们辨识记忆，这一点对于那些面向使用低速网络连接移动设备访问的应用特别有用。如果可以不访问索引页，而是直接访问想要的那个页面，他们多半会笑逐颜开而再度光顾。
如上所见， route() 装饰器把一个函数绑定到对应的 URL 上。

这里是一些基本的例子:
```python

@app.route('/')
def index():
return 'Index Page'

@app.route('/hello')
def hello():
return 'Hello World'
```

但是，不仅如此！你可以构造含有动态部分的 URL，也可以在一个函数上附着多个规则。

## 变量规则
要给 URL 添加变量部分，你可以把这些特殊的字段标记为 <variable_name> ， 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。这里有一些不错的例子:
```python
@app.route('/user/<username>')
def show_user_profile(username):
# show the user profile for that user
return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
return 'Post %d' % post_id

```

转换器有下面几种：
```python
int	接受整数
float	同 int ，但是接受浮点数
path	和默认的相似，但也接受斜线
唯一 URL / 重定向行为
Flask 的 URL 规则基于 Werkzeug 的路由模块。这个模块背后的思想是基于 Apache 以及更早的 HTTP 服务器主张的先例，保证优雅且唯一的 URL。

```

以这两个规则为例:
```python
@app.route('/projects/')
def projects():
return 'The project page'

@app.route('/about')
def about():
return 'The about page'
```

虽然它们看起来着实相似，但它们结尾斜线的使用在 URL 定义 中不同。 第一种情况中，指向 projects 的规范 URL 尾端有一个斜线。这种感觉很像在文件系统中的文件夹。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去。

然而，第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。

这个行为使得在遗忘尾斜线时，允许关联的 URL 接任工作，与 Apache 和其它的服务器的行为并无二异。此外，也保证了 URL 的唯一，有助于避免搜索引擎索引同一个页面两次。



## HTTP 方法
HTTP （与 Web 应用会话的协议）有许多不同的访问 URL 方法。默认情况下，路由只回应 GET 请求，但是通过 route() 装饰器传递 methods 参数可以改变这个行为。这里有一些例子:

```python

@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
do_the_login()
else:
show_the_login_form()
```
如果存在 GET ，那么也会替你自动地添加 HEAD，无需干预。它会确保遵照 HTTP RFC（描述 HTTP 协议的文档）处理 HEAD 请求，所以你可以完全忽略这部分的 HTTP 规范。同样，自从 Flask 0.6 起， 也实现了 OPTIONS 的自动处理。

你不知道一个 HTTP 方法是什么？不必担心，这里会简要介绍 HTTP 方法和它们为什么重要：

HTTP 方法（也经常被叫做“谓词”）告知服务器，客户端想对请求的页面 做 些什么。下面的都是非常常见的方法：

### GET
浏览器告知服务器：只  获取 页面上的信息并发给我。这是最常用的方法。
### HEAD
浏览器告诉服务器：欲获取信息，但是只关心  消息头 。应用应像处理  GET 请求一样来处理它，但是不分发实际内容。在 Flask 中你完全无需 人工 干预，底层的 Werkzeug 库已经替你打点好了。
### POST
浏览器告诉服务器：想在 URL 上  发布 新信息。并且，服务器必须确保 数据已存储且仅存储一次。这是 HTML 表单通常发送数据到服务器的方法。
### PUT
类似  POST 但是服务器可能触发了存储过程多次，多次覆盖掉旧值。你可 能会问这有什么用，当然这是有原因的。考虑到传输中连接可能会丢失，在 这种 情况下浏览器和服务器之间的系统可能安全地第二次接收请求，而 不破坏其它东西。因为  POST它只触发一次，所以用  POST 是不可能的。
### DELETE
删除给定位置的信息。
### OPTIONS
给客户端提供一个敏捷的途径来弄清这个 URL 支持哪些 HTTP 方法。 从 Flask 0.6 开始，实现了自动处理。
有趣的是，在 HTML4 和 XHTML1 中，表单只能以 GET 和 POST 方法提交到服务器。但是 JavaScript 和未来的 HTML 标准允许你使用其它所有的方法。此外，HTTP 最近变得相当流行，浏览器不再是唯一的 HTTP 客户端。比如，许多版本控制系统就在使用 HTTP。