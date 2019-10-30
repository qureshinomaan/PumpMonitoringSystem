from flask import Flask
from flask_bcrypt import Bcrypt 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#App is the instance of the flask class 
#When we run the app from python the name is __main__
app = Flask(__name__)
app.config['SECRET_KEY'] = '1c6abcb262aff7fe6ad060521592aec4'

#Creating the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db is an instance of sqlalchemy database class connected with flask app
db = SQLAlchemy(app)

class data(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	temperature = db.Column(db.Integer, nullable=False)
	humidity = db.Column(db.Integer, nullable=False)
	flow = db.Column(db.Integer,nullable=False)
	power = db.Column(db.Integer,nullable =False)
	current = db.Column(db.Integer, nullable =False)
	efficiency = db.Column(db.Integer, nullable =False)

from basics import routes