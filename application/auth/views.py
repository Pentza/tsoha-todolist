from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.tasklist.models import Tasklist
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # validoinnit

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    if not user.check_password(form.password.data):
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register")
def register_form():
    return render_template("auth/registerform.html", form = RegisterForm())

@app.route("/auth/", methods = ["POST"])
def auth_register():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    username_taken = User.query.filter_by(username=form.username.data).first()
    if username_taken:
        form.username.errors.append("Username is already in use")
        return render_template("auth/registerform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()

    u = User.query.filter_by(username=form.username.data).first()
    t = Tasklist('TaskList')
    t.account_id = u.id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("auth_login"))