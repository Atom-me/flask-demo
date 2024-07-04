# 导入flask
from flask import Flask, render_template, jsonify

# 创建flask应用对象
app = Flask(__name__)


# 路由+视图函数 hello_world
@app.route('/')
def hello_world():  # put application's code here
    # 返回字符串给浏览器的数据,支持 HTML标签
    # return 'Hello World!'
    return '<h1>Hello World!</h1>'


# 添加一个路由和视图函数
@app.route('/index')
def index():
    # 模版渲染,，支持传递变量给模版文件
    return render_template('index.html', userName="Atom")


@app.route('/json')
def json():
    # 直接返回字典数据也可以
    # return {'name': "atom", "age": 44}

    # jsonify : 序列化
    return jsonify({'name2': "atom2", "age": 55})


if __name__ == '__main__':
    # 启动服务器
    # 运行app.run(host="0.0.0.0",port=9000,debug=True)，但是服务启动后，还是默认的ip和端口http://127.0.0.1:5000，debug模式也是off。
    # 因为pycharm识别出你是flask项目。
    # 你运行时,切换为python的运行模式即可。(选择edit configurations....)
    # 或者直接terminal中执行： python app.py
    app.run(debug=True, port=5670, host='0.0.0.0')

    """
    run() 启动的时候还可以添加参数：
    debug 是否开启调试模式，开启后修改过python代码会自动重启
    port 启动指定服务器端口号，默认是5000
    host 主机，默认是127.0.0.1，指定 0.0.0.0 代表本机所有IP
    """
