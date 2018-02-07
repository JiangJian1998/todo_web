#encoding: utf-8
from flask_script import Manager
from exts import db
from todo import app

db_manager = Manager()



@db_manager.command
def init(): #初始化表  python manage.py db init
    with app.app_context():
        db.create_all()