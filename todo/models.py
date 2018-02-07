from exts import db


class Todo(db.Model):  # table
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    begin = db.Column(db.Date, nullable=False)
    end = db.Column(db.Date)
    complete = db.Column(db.Integer, nullable=False, default=0)
    complete_time = db.Column(db.Date)

    # 注意是类名
    author = db.relationship('User', backref=db.backref('todo'))

class User(db.Model):
    __tablename__ ='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=False)