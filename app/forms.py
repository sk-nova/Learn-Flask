from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    BooleanField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length

from app.models import User


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember Me", validators=[DataRequired()])
    submit = SubmitField(label="Login")


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    username = StringField(label="Username", validators=[DataRequired()])
    email = EmailField(label="Email Address", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    conf_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo("password", "Password did not match")],
    )
    submit = SubmitField(label="Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")


# Profile Edit Form
class ProfileEditForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired()])
    last_name = StringField(label="Last Name", validators=[DataRequired()])
    username = StringField(label="Username", validators=[DataRequired()])
    email = EmailField(label="Email Address", validators=[DataRequired(), Email()])
    about_me = TextAreaField("About Me", validators=[Length(min=0, max=140)])
    submit = SubmitField(label="Update")
