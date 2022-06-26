from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class Registration(FlaskForm):
    username = StringField("Username", validators=[DataRequired(message="username minimal 2 karakter"), Length(min = 2, max = 50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if True:
            raise ValidationError('That username is taken. Please choose a different one.') 

    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if True:
            raise ValidationError('That email is taken. Please choose a different one.') 



class Logins(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me!")
    submit = SubmitField("Login")
    
