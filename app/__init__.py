from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GUSS IT'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# migrate=Migrate(app,db)

from . import routes