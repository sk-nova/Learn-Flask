from flask import render_template, flash, redirect, url_for
from flask import Blueprint
from flask_login import current_user, login_user, logout_user, login_required

from app.forms import LoginForm, RegistrationForm
from app.models import User


# Root Blueprint
root_bp = Blueprint("root", __name__)


# Index Route
@root_bp.route("/")
@root_bp.route("/index")
@login_required
def index():
    return render_template(template_name_or_list="index.html", title="Home")


# Login route
@root_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("root.index"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("root.login"))

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for("root.dashboard"))

    return render_template("auth/login.html", form=form)


# Login route
@root_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(
            first_name=first_name, last_name=last_name, email=email, username=username
        )

        user.set_password_hash(password)

        # Save the user in DB
        user.save()

        flash("User registered successfully")

        return redirect(url_for("root.login"))

    return render_template("auth/register.html", form=form)


# Logout Route
@root_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("root.index"))


# Dashboard Route
@root_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
