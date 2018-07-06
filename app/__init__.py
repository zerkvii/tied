# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GUSS IT'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# migrate=Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'info'
login_manager.login_view = 'login'
from . import routes
