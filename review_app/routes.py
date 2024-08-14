from flask import render_template, request, redirect, url_for, flash
from review_app import app, db, login_user, LoginManager, login_required, logout_user, current_user
from review_app.models import User, Gear, Category, Brand, Review
from review_app.forms import LoginForm, SignUpForm, AddReviewForm, SearchForm
import bcrypt

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    form = SearchForm()
    return render_template("base.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        entered_password = bytes(form.password.data, "utf-8")
        user = User.query.filter_by(email=form.email.data).first()
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
    return render_template("login.html", form=form)

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
    form = SignUpForm()
    if form.validate_on_submit():
        password = bytes(form.password.data, "utf-8")
        confirm_password = bytes(form.confirm_password.data, "utf-8")
        if password != confirm_password:
            flash("Passwords don't match")
        else:
            hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt()) 
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_pw.decode("utf-8")
            )
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully")
            return redirect(url_for("home"))
    return render_template("sign_up.html", form=form)

@app.route("/search", methods=["POST"])
def search():
    form = SearchForm()
    gear_items = Gear.query
    if form.validate_on_submit():
        gear_searched = form.searched.data
        gear_items = gear_items.filter(Gear.name.ilike('%' + gear_searched + '%'))
        gear_items = gear_items.order_by(Gear.name).all()
        return render_template("search.html", form=form, searched=gear_searched, gear_items=gear_items)

@app.route("/add_review/<gear>", methods=["GET", "POST"])
@login_required
def add_review(gear):
    form = AddReviewForm()
    if form.validate_on_submit():
        review_content = form.review.data
        rating = form.rating.data
        gear_name = gear.replace("-", " ").title()
        gear_item = Gear.query.filter_by(name=gear_name).first()
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
    return render_template("add_review.html", form=form, title=gear_item.name)

@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    return render_template("add_product.html")

@app.route("/about_gear/<gear>")
def about_gear(gear):
    form = SearchForm()
    gear_name = gear.replace("-", " ").title()
    gear_item = Gear.query.filter_by(name=gear_name).first()
    reviews = Review.query.filter_by(gear_id=gear_item.id)
    return render_template("about_gear.html", form=form, gear_item=gear_item, title=gear_item.name, gear_url=gear, reviews=reviews)

