from turtle import title
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import Registration, Logins


app = Flask(__name__)
app.config['SECRET_KEY'] = "837377gu9y3883838"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    email = db.Column(db.String(125), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = "default.jpg")
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self): 
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    

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




if __name__ == "__main__":
    app.run(debug=True)