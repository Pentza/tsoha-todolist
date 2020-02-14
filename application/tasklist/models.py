from application import db

class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(144), nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

    tasks = db.relationship("Task", backref='TaskList', lazy = True)

    def __init__(self, name):
        self.name = name

#    @staticmethod
#    def find_user_tasklist():
#        stmt = text("SELECT Task.name FROM Task"
#           " JOIN TaskList ON Task.account_id = Account.id"
#            " WHERE (Task.done IS null OR Task.done = :done)"
#            " GROUP BY Account.id"
#            " HAVING COUNT(Task.id) = 0").params(done=done)
#
#        res = db.engine.execute(stmt)
#
#        response = []
#        for row in res:
#            response.append({"id":row[0], "name":row[1]})
#
#        return response