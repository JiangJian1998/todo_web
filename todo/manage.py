#encoding: utf-8

from flask_script import Manager
from todo import app
from exts import db
from db_scripts import db_manager
from flask_migrate import Migrate, MigrateCommand
from models import Todo, User

manager = Manager(app)

# 绑定
migrate = Migrate(app, db)
# 添加迁移命令 usage: migrate -> upgrade
manager.add_command('migrate', MigrateCommand)
# 添加db命令
manager.add_command('db',db_manager)

# manager命令
@manager.command
def runserver():
    app.run()


if __name__ == '__main__':
    manager.run()