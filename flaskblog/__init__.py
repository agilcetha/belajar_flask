from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "837377gu9y3883838"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

from flaskblog import routes
