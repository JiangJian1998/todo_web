import os, time, datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from models import Todo, User
from exts import db
from utils import login_log
import config

app = Flask(__name__)
app.config.from_object(config)  # 导入config
db.init_app(app)  # database

'''
查数据u = User.query.filter(User.username == 'weixiao').first()
filter条件间用逗号
'''

# 更新状态显示
update_project=[
    {'content':'更新动态建设','p':100,'s':'success'},
    {'content':'todo列表显示','p':75,'s':'info'},
    {'content':'登录功能','p':80,'s':'info'},
    {'content':'后台功能','p':0,'s':'action'},
    {'content':'todo详情','p':80,'s':'info'},
    {'content':'用多对多写todo的tags','p':0,'s':'action'},
    {'content':'查找功能','p':0,'s':'action'},
    {'content':'不允许重复登录','p':0,'s':'action'}
]



# 首页
@app.route('/')
def index():
    user_id = session.get('user_id')
    context = {
        'todo_no': Todo.query.filter(Todo.author_id==user_id, Todo.complete == 0, Todo.end!=None).order_by('end').all()
                   +Todo.query.filter(Todo.author_id==user_id, Todo.complete == 0, Todo.end==None).order_by('begin').all(),
        'todo_yes': Todo.query.filter(Todo.author_id==user_id, Todo.complete == 1).order_by('-complete_time').all(),
        'todo_all': Todo.query.filter(Todo.author_id==user_id).order_by('begin').all(),
        'now': time.strftime("%Y-%m-%d", time.localtime()),
        'cnt': [Todo.query.filter(Todo.author_id==user_id, Todo.complete == 0).count(), Todo.query.filter(Todo.author_id==user_id, Todo.complete == 1).count()],
        'pro': update_project
    }
    return render_template('index.html', **context)

@app.route('/todo_detail/<todo_id>', methods=['GET', 'POST'])
def todo_detail(todo_id):
    todo = Todo.query.filter(Todo.id == todo_id).first()
    if request.method == 'GET':
        return render_template('todo_detail.html', todo=todo)
    else:
        if request.form.get('finish') == 'finish':
            todo.complete = 1
            todo.complete_time = time.strftime("%Y-%m-%d", time.localtime())
            db.session.commit()
        elif request.form.get('delete') == 'delete':
            db.session.delete(todo)
            db.session.commit()

        # 重定向
        return redirect(url_for('index'))

# 工具箱
@app.route('/tools/')
def tools():
    return render_template('tools.html')


# 添加
@app.route('/add/', methods=['GET', 'POST'])
def add():
    # get返回页面，post操作todo
    if request.method == 'GET':
        return render_template('add.html')
    else:
        # 判断是否登录
        if g.user == None:
            return redirect(url_for('login'))

        # 获取数据
        title = request.form.get('title')
        content = request.form.get('content')
        begin = time.strftime("%Y-%m-%d", time.localtime())
        if request.form.get('end') != '':
            end = request.form.get('end')
        else:
            end = None
        # 数据库修改
        db.session.add(Todo(title=title, content=content, author_id=g.user.id, begin=begin, end=end, complete=0))
        db.session.commit()
        # 重定向
        return redirect(url_for('index'))


# 登陆后台
@app.route('/login_admin/', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'GET':
        return render_template('login_admin.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username==username, User.password==password, User.admin==1).first()
        if user:
            session['user_id'] = user.id
            if request.form.get('remember')=='on':
                session.permanent = True
            return redirect(url_for('index'))
        return render_template('login_admin.html')


#用户登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username==username, User.password==password).first()
        if user:
            session['user_id'] = user.id
            if request.form.get('remember')=='on':
                session.permanent = True
            return redirect(url_for('index'))
        return render_template('login.html')


# 注销
@app.route('/logout/')
def logout():
    session.pop('user_id')

    # session.clear()
    return redirect(url_for('index'))

# 获取登录状态
@app.before_request
def login_hook():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user
            return
    g.user = None


# 登录状态控制
@app.context_processor
def login_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user, 'login':1}
    return {'login':0}

# 是否为管理员
@app.context_processor
def admin_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            if user.admin == 1:
                return {'admin': 1}
    return {'admin': 0}



# 过滤器 计算时间剩余
@app.template_filter()
def time_clc(end):
    if end == None:
        return None
    end = str(end)
    return (datetime.datetime(int(end[:4]), int(end[5:7]), int(end[8:10])) - datetime.datetime.now()).days + 1




if __name__ == '__main__':
    app.run(host='192.168.1.100', port=80)
