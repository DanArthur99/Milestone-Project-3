import os
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin, LoginManager, login_required, login_user, logout_user,
    current_user)
from wtforms.fields import (
    StringField, SubmitField, PasswordField, EmailField, SelectField)
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

db.create_all()

# Imports the routes module from review_app
from review_app import routes
