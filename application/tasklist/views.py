from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.tasklist.models import Tasklist
from application.tasks.models import Task
from application.tasklist.forms import TaskListForm


@app.route("/tasklists", methods=["GET"])
@login_required
def tasklists_index():
	return render_template("tasklist/list.html", tasklists = Tasklist.query.filter(Tasklist.account_id==current_user.id).all())

@app.route("/tasklist/<list_id>", methods=["GET"])
@login_required
def show_tasklist(list_id):
    current_list = Tasklist.query.get(list_id)
    account_lists = Tasklist.query.filter(Tasklist.account_id==current_user.id).all()
    tasklist_tasks = Task.query.filter(Task.tasklist_id==list_id).all()
    return render_template("tasklist/list.html", tasks = tasklist_tasks, tasklists = account_lists, current_list = current_list)

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

    return redirect(url_for("show_tasklist", list_id = t.id))

#@app.route("/tasklist/delete/<list_id>", methods=["POST"])
#@login_required
#def tasklist_delete(list_id):
#
#    print(Tasklist.count())
