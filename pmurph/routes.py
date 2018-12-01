from flask import flash, redirect, render_template, url_for

from pmurph import app, bcrypt, db
from pmurph.forms import LoginForm, RegistrationForm
from pmurph.models import Post, User
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Kyle VanZandt',
        'title': 'Blog Post 1',
        'content': 'This is made using python so suck only reworte the whole website 4 times so far',
        'date_posted': '11/26/2018', 
    },
    {
        'author': 'Kyle VanZandt',
        'title': 'Blog Post 2',
        'content': 'Testing',
        'date_posted': '11/27/2018', 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/testing")
def testing():
    return render_template('testing.html', title='Testing')

@app.route("/videos")
def videos():
    return render_template('videos.html', title='Videos')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')