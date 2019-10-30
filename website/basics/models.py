from datetime import datetime 
from basics import db,login_manager
from flask_login import UserMixin


class data(db.Model, UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	temperature = db.Column(db.Integer, nullable=False)
	humidity = db.Column(db.Integer, nullable=False)
	flow = db.Column(db.Integer,nullable=False)
	power = db.Column(db.Integer,nullable =False)
	current = db.Column(db.Integer, nullable =False)
	efficiency = db.Column(db.Integer, nullable =False) 

	#repr defines how the class is represented.
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"