from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, validators
from application.tasklist.models import TaskList
from flask_login import current_user

class TaskForm(FlaskForm):
	name = StringField("Task name", [validators.Length(min=2, max=20)])
	urgency = IntegerField("Urgency", [validators.optional(), validators.NumberRange(min=1, max=3, message="Number must be between 1 and 3. (Leave empty if not urgent)")], render_kw={"placeholder": "Optional: 1-3"})
	done = BooleanField("Done")

	tasklists_in_database = TaskList.query.all()

	user_tasklists = [(l.id, l.name) for l in tasklists_in_database]

	tasklist = SelectField("TaskList", coerce=int, choices=user_tasklists)

	class Meta:
		csrf = False

