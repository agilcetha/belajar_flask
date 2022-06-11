from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

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

@app.route("/register", methods=['GET','POST'])
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
            flash('You have been logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please Check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True) # penulisan debug=True tidak usah spasi