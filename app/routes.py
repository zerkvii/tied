from .models import User, Post
from . import app, bcrypt, db
from flask import render_template, flash, redirect, url_for, request
from .forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'成功创建账户{form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('登录失败，请检查账号或者密码', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    form = UpdateAccountForm()
    return render_template('account.html', title='Account', form=form)
