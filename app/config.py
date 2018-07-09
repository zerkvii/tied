import os


class Config:
    SECRET_KEY = os.environ.get('GUESS IT') or 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '2330362931'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'uchbkqerldjeecig'
