import os
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from wtforms.fields import StringField, SubmitField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm
if os.path.exists("env.py"):
    import env # noqa



app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from review_app import routes