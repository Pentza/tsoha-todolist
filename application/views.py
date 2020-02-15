from flask import render_template
from application import app
from application.auth.models import User
from application.tasklist.models import Tasklist
from flask_login import login_required, current_user

@app.route("/")
def index():
	if current_user.is_authenticated:
		return render_template("index.html", needs_tasks=User.find_users_with_no_tasks(), tasklists = Tasklist.query.filter(Tasklist.account_id==current_user.id).all())
	else:
		return render_template("index.html", needs_tasks=User.find_users_with_no_tasks(), tasklists =[("---")])
