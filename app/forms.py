# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='输入不为空'), Length(min=2, max=22, message='长度2-22')])
    email = StringField('邮箱', validators=[DataRequired(message='输入不为空'), Email(message='邮箱格式不合法')])
    password = PasswordField('密码', validators=[DataRequired(message='输入不为空'),
                                               Regexp('^[a-zA-Z][a-zA-Z0-9]+$', message='密码必须包含大小写字母数字'),
                                               Length(6, 20, message='长度为6-20')])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(message='输入不为空'), EqualTo('password', message='两次输入不一致')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('此用户名已存在')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('此邮箱已存在')


class LoginForm(FlaskForm):
    username = StringField('登录名', validators=[DataRequired(message='输入不为空')])
    password = PasswordField('密码', validators=[DataRequired(message='输入不为空')])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')


class UpdateAccountForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='输入不为空'), Length(min=2, max=22, message='长度2-22')])
    email = StringField('邮箱', validators=[DataRequired(message='输入不为空'), Email(message='邮箱格式不合法')])
    picture = FileField('上传照片 ', validators=[FileAllowed(['jpg', 'png'], message='请选择jpg或者png格式文件')])
    submit = SubmitField('更新')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('此用户名已存在')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('此邮箱已存在')


class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(message='标题不为空')])
    content = TextAreaField('内容', validators=[DataRequired(message='内容不为空')])
    submit = SubmitField('提交')
