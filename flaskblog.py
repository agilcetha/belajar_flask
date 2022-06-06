from flask import Flask, render_template, url_for
from forms RegristrationForm, LoginForm

app = Flask (__name__)

app.config['SECRET_KEY'] = 'c3ad988476f38be5dad6667d4229e18d'

posts = [
    {
        'author': 'Rahmad Hidayat',
        'title' : 'Blog Post 1',
        'content': 'Post Konten Pertama',
        'date_posted': 'May 20, 2022'
    },
    {
        'author': 'Ahmad Ahsan',
        'title' : 'Blog Post 2',
        'content': 'Post Konten Kedua',
        'date_posted': 'May 21, 2022'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegristrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True) # penulisan debug=True tidak usah spasi