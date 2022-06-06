from flask_wtf import FlaskForm
from wtform import StringField, PasswordField, SubmitField, BooleanField
from wtform.validators import DataRequired, Length, Email, EqualTo

# form regristrasi
class RegristrationForm(FlaskForm)
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email    = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('paswoord')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm)
    email    = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    