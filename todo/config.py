#encoding: utf-8


DEBUG = True
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'todo_db'
SECRET_KEY = b'\x19\x10\x01\nv\x07Uy2\xb0s\x98\x04\xea.\xe7[\xdf\xa9.\x1b"\xd6x'
WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
