from flask import Flask, render_template, flash, redirect, url_for, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Post, User
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
            email=form.email.data,
            password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash(f"Your account has been created! You are now able to log in.", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form, title="Register")

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
            if next_page:
                return redirect(next_page)

            return redirect(url_for('home'))
        else:
            flash('Login unseccessful, Please check email and password', 'danger')

    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title="Account")
