from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasklist = db.relationship("TaskList", backref='account', lazy = True)

    # tasks = db.relationship("Task", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def find_users_with_no_tasks(done=False):
        stmt = text("SELECT Account.id, Account.name FROM Account"
            " LEFT JOIN task_list ON task_list.account_id = Account.id"
            " LEFT JOIN Task ON Task.tasklist_id = task_list.id"
            " WHERE (Task.done IS null OR Task.done = :done)"
            " GROUP BY Account.id"
            " HAVING COUNT(Task.id) = 0").params(done=done)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response