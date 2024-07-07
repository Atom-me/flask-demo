# views.py ： 路由+ 视图函数
from flask import Blueprint, request
from .models import *

# 蓝图 blueprint， 使用蓝图管理我们的路由
# 蓝图也是一种规划，主要用来规划urls，（路由route）
# 在views.py 中初始化蓝图
# blue = Bluepriint('user',__name__)
# 然后在init文件中调用蓝图，进行路由注册

"""
name: 蓝图名称
__name__ ： 表示当前模块
"""
blue = Blueprint('user', __name__)
blue2 = Blueprint('product', __name__)


@blue.route('/')
def index():
    return 'index'


# String 类型参数
@blue.route('/string/<string:username>/')
def get_string(username):
    return username


# int 类型参数
# 必须传递整数，不能写小数，否则404
@blue.route('/int/<int:userId>/')
def get_int(userId):
    print(type(userId))
    return str(userId)


# float 类型参数
# 必须传递小数，不能写整数，否则404
@blue.route('/float/<float:money>/')
def get_float(money):
    print(type(money))
    return str(money)


# path 类型参数
# path类型参数支持斜杠，即参数内容可以包含斜杠，http://127.0.0.1:5000/mypath/hel/lo/
# 他会认为 “hel/lo” 是一个整体
@blue.route('/mypath/<path:anything>/')
def get_path(anything):
    print(type(anything))
    return str(anything)


# uuid 类型参数
# 参数必须是UUID格式的： 3c1ddce2-c1b0-49b8-ba75-5a7598a4f7aa
@blue.route('/testuuid/<uuid:id>/')
def get_uuid(id):
    print(type(id))
    return str(id)


@blue.route('/getuuid/')
def get_uuid2():
    import uuid
    return str(uuid.uuid4())


# any 类型参数
# 参数枚举,fruit参数值只能是 apple,orange,banana 中的一个。其他值返回404
@blue.route('/any/<any(apple,orange,banana):fruit>')
def get_any(fruit):
    print(type(fruit))
    return str(fruit)


# methods 请求方式
@blue.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    print("this is do_the_login")
    return "do_the_login"


def show_the_login_form():
    print("this is show_the_login_form")
    return "show_the_login_form"


@blue2.route('/goods')
def index():
    return 'xxxx'
