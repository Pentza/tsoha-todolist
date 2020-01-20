from application import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(144), nullable=False)
	urgency = db.Column(db.Integer)
	done = db.Column(db.Boolean, nullable=False)

	def __init__(self, name):
		self.name = name
		self.done = False
