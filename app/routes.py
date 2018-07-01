from .models import User, Post
from . import app
from flask import render_template, flash, redirect,url_for
from .forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'zerk',
        'title': 'today',
        'content': 'happy',
        'date': '2018-6-20'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='home')


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'成功创建账户{form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin@blog.com' or form.username.data == 'lk' and form.password.data == 'password':
            flash('登录成功', 'success')
            return redirect(url_for('home'))
        else:
            flash('登录失败，请检查账号或者密码', 'danger')
    return render_template('login.html', title='Login', form=form)
