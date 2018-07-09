from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(message='标题不为空')])
    content = TextAreaField('内容', validators=[DataRequired(message='内容不为空')])
    submit = SubmitField('提交')
