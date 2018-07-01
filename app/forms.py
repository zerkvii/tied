from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='输入不为空'), Length(min=2, max=22, message='长度2-22')])
    email = StringField('邮箱', validators=[DataRequired(message='输入不为空'), Email(message='邮箱格式不合法')])
    password = PasswordField('密码', validators=[DataRequired(message='输入不为空'),
                                               Regexp('^[A-Za-z0-9]$', message='密码必须包含大小写字母数字'),
                                               Length(8, 20, message='长度为8-20')])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(message='输入不为空'), EqualTo('password', message='两次输入不一致')])
    submit = SubmitField('注册')


class LoginForm(FlaskForm):
    username = StringField('登录名', validators=[DataRequired(message='输入不为空')])
    password = PasswordField('密码', validators=[DataRequired(message='输入不为空')])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')
