from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.tasks.models import Task
from application.tasks.forms import TaskForm, EditTaskForm

@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
	return render_template("tasks/list.html", tasks = Task.query.all(), id = current_user.id)

@app.route("/tasks/new", methods=["GET"])
@login_required
def tasks_form():
	tasklist_id = request.args.get('tasklist_id')
	return render_template("tasks/new.html", form = TaskForm(), tasklist_id=tasklist_id)

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

	t = Task.query.get(task_id)
	if t.done == False:
		t.done = True
	else:
		t.done = False
	db.session().commit()

	return redirect(url_for("show_tasklist", list_id = t.tasklist_id))

@app.route("/tasks/delete/<task_id>/", methods=["POST"])
@login_required
def tasks_delete(task_id):

	tasklist_id = Task.query.get(task_id).tasklist_id
	Task.query.filter(Task.id == task_id).delete()

	db.session().commit()

	return redirect(url_for("show_tasklist", list_id = tasklist_id))

@app.route("/tasks/", methods=["GET", "POST"])
@login_required
def tasks_create():
	
	form = TaskForm(request.form)
	tasklist_id = request.args.get('list_id')

	if not form.validate():
		return render_template("tasks/new.html", form = form, tasklist_id=tasklist_id)

	t = Task(form.name.data)
	t.urgency = form.urgency.data
	t.done = form.done.data

	t.tasklist_id = request.args.get('list_id')

	db.session().add(t)
	db.session().commit()

	return redirect(url_for("show_tasklist", list_id = t.tasklist_id))

@app.route("/task/edit/<task_id>", methods=["GET", "POST"])
@login_required
def task_edit(task_id):
	t = Task.query.get(task_id)
	if request.method == "GET":
		return render_template("tasks/edit.html", task=t, form = EditTaskForm(new_name=t.name, new_urgency=t.urgency))

	form = EditTaskForm(request.form)

	if not form.validate():
		return render_template("tasks/edit.html", task=t, form = form)

	t.name = form.new_name.data
	t.urgency = form.new_urgency.data

	db.session().commit()

	return redirect(url_for("show_tasklist", list_id = t.tasklist_id))
