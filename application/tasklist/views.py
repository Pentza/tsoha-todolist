from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.tasklist.models import Tasklist
from application.tasklist.forms import TaskListForm

@app.route("/tasklist/new")
@login_required
def tasklist_form():
    return render_template("tasklist/new.html", form = TaskListForm())

@app.route("/tasklist/", methods=["POST"])
@login_required
def tasklist_create():
    form = TaskListForm(request.form)

    if not form.validate():
        return render_template("tasklist/new.html", form = form)

    t = Tasklist(form.name.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))