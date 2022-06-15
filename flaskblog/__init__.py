from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config['SECRET_KEY'] = 'c3ad988476f38be5dad6667d4229e18d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

from flaskblog import routes