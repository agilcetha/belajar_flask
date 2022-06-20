from flask import Flask, render_template, flash, redirect, url_for
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Post, User

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "Content 1",
        "date_posted": "May, 28 2022"
    },
    {
        "author": "Corey Schafer",
        "title": "Blog Post 2",
        "content": "Content 2",
        "date_posted": "May, 27 2022"   
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About page")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    
    return render_template('register.html', form=form, title="Register")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccessful, Please check username and password', 'danger')

    return render_template("login.html", title="Login", form=form)