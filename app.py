from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0b9b554632cd3f07b0593457f58d09fc'
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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)