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
@login_required
def add_review():
    gear_items = list(Gear.query.order_by(Gear.name).all())
    if request.method == "POST":
        review_content = request.form.get("review")
        rating = request.form.get("rating")
        gear_item = Gear.query.filter_by(id=request.form.get("gear")).first()
        current_user_id = current_user.id 
        review = Review(
            review_contents=review_content,
            review_rating=rating,
            user_id=current_user_id,
            gear_id=gear_item.id
        )
        db.session.add(review)
        db.session.commit()
        flash("Thanks for your product review")
        return redirect(url_for("home"))
    return render_template("add_review.html", gear_items=gear_items)

@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    return render_template("add_product.html")

