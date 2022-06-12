from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import Registration, Logins
from flaskblog.models import User, Post



posts = [
    {
        'autor' : 'supri',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : ' 22 Mei 2022'
    },
    {
        'autor' : 'Haidar',
        'title' : 'blog post 2',
        'content' : 'first post content',
        'date_posted' : ' 23 Mei 2022'
    },
    {
        'autor' : 'oji',
        'title' : 'blog post 3',
        'content' : 'first post content',
        'date_posted' : ' 23 juni 2022'
    },
    {
        'autor' : 'jhon',
        'title' : 'blog post 4',
        'content' : 'first post content',
        'date_posted' : ' 23 juni 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts = posts)



@app.route('/about')
def about():
    return render_template("about.html", title = 'About')



@app.route('/register', methods=["GET","POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")  
        return redirect(url_for("home"))

    return render_template("register.html", title = "Register", form = form)



@app.route('/login', methods=["GET","POST"])

def login():
    form = Logins()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You Have Been Log In!", "success")
            return redirect(url_for("home"))
        else:
            flash("Loggin Unsuccessfull. Please Check username And password! ", 'danger')
    return render_template("login.html", title = "Login", form = form)
