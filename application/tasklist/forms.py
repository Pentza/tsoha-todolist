from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TaskListForm(FlaskForm):
    name = StringField("TaskList name", [validators.Length(min=2, max=15)])

    class Meta:
        csrf = False

class EditTaskListForm(FlaskForm):
    new_name = StringField("TaskList name", [validators.Length(min=2, max=15)])

    class Meta:
        csrf = False