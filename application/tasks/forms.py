from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class TaskForm(FlaskForm):
	name = StringField("Task name", [validators.Length(min=2, max=20)])
	urgency = IntegerField("Urgency", [validators.optional(), validators.NumberRange(min=1, max=3, message="Number must be between 1 and 3. (Leave empty if not urgent)")], render_kw={"placeholder": "Optional: 1-3"})
	done = BooleanField("Done")

	class Meta:
		csrf = False

