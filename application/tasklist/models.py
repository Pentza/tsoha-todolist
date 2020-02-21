from application import db
from application.models import Base

from sqlalchemy.sql import text


class Tasklist(Base):
    name = db.Column(db.String(144), nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    tasks = db.relationship("Task", backref='tasklist', lazy = True)

    def __init__(self, name):
        self.name = name