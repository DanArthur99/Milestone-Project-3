from flask import render_template, request, redirect, url_for, flash
from review_app import app, db, login_user, LoginManager, login_required, logout_user, current_user
from review_app.models import User, Gear, Category, Brand, Review
import bcrypt

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = bytes(request.form.get("password"), "utf-8")
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user:
            user_password = bytes(user.password, "utf-8")
            if bcrypt.checkpw(entered_password, user_password):
                login_user(user)
                flash("Login successful!")
                return redirect(url_for("dashboard"))
            else:
                flash("Password not recognised")
        else:
            flash("User not recognised")
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        password = bytes(request.form.get("password"), "utf-8")
        confirm_password = bytes(request.form.get("confirm_password"), "utf-8")
        if password != confirm_password:
            flash("Passwords don't match")
        else:
            hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt()) 
            user = User(
                username=request.form.get("username"),
                email=request.form.get("email"),
                password=hashed_pw.decode("utf-8")
            )
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully")
            return redirect(url_for("home"))
    return render_template("sign_up.html")

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")
