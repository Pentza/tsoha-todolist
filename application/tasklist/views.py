from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.tasklist.models import Tasklist
from application.tasks.models import Task
from application.tasklist.forms import TaskListForm, EditTaskListForm


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

@app.route("/tasklist/", methods=["GET"])
@login_required
def show_tasklist_first():
    
    if Tasklist.query.filter(Tasklist.account_id==current_user.id).first() == None:
        return redirect(url_for("tasklist_form"))

    current_list = Tasklist.query.filter(Tasklist.account_id==current_user.id).first()

    list_id = current_list.id

    

    account_lists = Tasklist.query.filter(Tasklist.account_id==current_user.id).all()
    tasklist_tasks = Task.query.filter(Task.tasklist_id==current_list.id).all()

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

@app.route("/tasklist/delete/<list_id>", methods=["POST", "GET"])
@login_required
def tasklist_delete(list_id):

    Task.query.filter(Task.tasklist_id==list_id).delete()

    Tasklist.query.filter(Tasklist.id==list_id).delete()

    db.session().commit()

    if Tasklist.query.filter(Tasklist.account_id==current_user.id).first() == None:
        return redirect(url_for("index"))

    return redirect(url_for("show_tasklist_first"))

@app.route("/tasklist/edit/<list_id>", methods=["GET", "POST"])
@login_required
def tasklist_edit(list_id):
	t = Tasklist.query.get(list_id)
	if request.method == "GET":
		return render_template("tasklist/edit.html", tasklist=t, form = EditTaskListForm(new_name=t.name))

	form = EditTaskListForm(request.form)

	if not form.validate():
		return render_template("tasklist/edit.html", tasklist=t, form = form)

	t.name = form.new_name.data

	db.session().commit()

	return redirect(url_for("show_tasklist", list_id = t.id))

@app.route("/tasklist/list_all")
@login_required
def tasklist_list_all():
    tasklists = Tasklist.query.filter(Tasklist.account_id==current_user.id).all()
    return render_template("tasklist/list_all.html", tasklists = tasklists)