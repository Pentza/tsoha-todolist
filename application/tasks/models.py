from application import db
from application.models import Base

class Task(Base):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(144), nullable=False)
	urgency = db.Column(db.Integer)
	done = db.Column(db.Boolean, nullable=False)

	tasklist_id = db.Column(db.Integer, db.ForeignKey('task_list.id'), nullable=False)

	def __init__(self, name):
		self.name = name
		self.done = False
