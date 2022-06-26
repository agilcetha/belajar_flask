import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    #cek apakah user sudah login
    #jika sudah login, maka arahkan ke '/home'
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    #

    form = RegistrationForm() #fungsi membuat form
    if form.validate_on_submit(): #apakah form yg di submit sudah valid
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    #jika tidak valid atau belum submit, maka akan render register html    
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
            flash('Login Unsuccesful. Please Check email and Password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    # MEmbuat random string: "8534ba56dae8617e" 
    random_hex = secrets.token_hex(8)

    # Memisah path dan extension file
    # /tmp/gambar_ahsan.jpg
    # _ : /tmp/gambar_ahsan
    # f_ext: .jpg
    _, f_ext = os.path.splitext(form_picture.filename)

    # 8534ba56dae8617e + .jpg
    # 8534ba56dae8617e.jpg
    picture_fn = random_hex + f_ext
    # /home/idnmedia/playground/belajar_flask/ => app.root_path
    # /home/idnmedia/playground/belajar_flask/static/profile_pics =>app.root_path  + static/profile_pics +  8534ba56dae8617e.jpg
    # /home/idnmedia/playground/belajar_flask/static/profile_pics/8534ba56dae8617e.jpg
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    # ukuran gbr
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    # fungsi update username dan email
    if form.validate_on_submit():
        if form.picture.data: 
            picture_file = save_picture(form.picture.data) # kjasjdf3.jpg
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))

    #mengecek username dan email sudah terdaftar atau belum   
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', 
                            image_file=image_file, form=form)
    
