from application import db
from application.models import Base

from sqlalchemy.sql import text


class Task(Base):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(144), nullable=False)
	urgency = db.Column(db.Integer)
	done = db.Column(db.Boolean, nullable=False)

	tasklist_id = db.Column(db.Integer, db.ForeignKey('tasklist.id'), nullable=False)

	#account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

	def __init__(self, name):
		self.name = name
		self.done = False


	@staticmethod
	def total_urgent_tasks(accountID):
		stmt = text("SELECT Task.name, Tasklist.name FROM Account"
			" LEFT JOIN Tasklist ON Tasklist.account_id = Account.id"
			" LEFT JOIN Task ON Task.tasklist_id = Tasklist.id"
			" WHERE Account.id = :accountID AND Task.urgency=3").params(accountID=accountID)

		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"name":row[0], "listname":row[1]})

		return response
