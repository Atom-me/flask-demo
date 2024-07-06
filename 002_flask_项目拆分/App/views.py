# views.py ： 路由+ 视图函数
from flask import Blueprint
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


@blue2.route('/goods')
def index():
    return 'xxxx'
