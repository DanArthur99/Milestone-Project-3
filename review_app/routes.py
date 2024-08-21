from flask import render_template, request, redirect, url_for, flash
from review_app import app, db, login_user, LoginManager, login_required, logout_user, current_user
from review_app.models import User, Gear, Category, Brand, Review
from review_app.forms import LoginForm, SignUpForm, AddReviewForm, SearchForm, AddProductForm, UpdateDetailsForm
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
                return redirect(url_for("dashboard", id=current_user.id))
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


@app.route("/dashboard/<int:id>", methods=["GET", "POST"])
@login_required
def dashboard(id):
    if current_user.id != id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        form = SearchForm()
        return render_template("dashboard.html", form=form)

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
            try: 
                db.session.add(user)
                db.session.commit()
                flash("Account created successfully")
                return redirect(url_for("login"))
            except:
                flash("There was an error signing you up")
                return redirect(url_for("sign_up"))
            
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

@app.route("/search_users")
@login_required
def search_users():
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        form = SearchForm()
        users = User.query
        return render_template("search_users.html", form=form, users=users)

@app.route("/list_of_users", methods=["POST"])
@login_required
def list_of_users():
    form = SearchForm()
    users = User.query
    if form.validate_on_submit():
        users_searched = form.searched.data
        users = users.filter(User.username.ilike('%' + users_searched + '%'))
        users = users.order_by(User.username).all()
        return render_template("list_of_users.html", form=form, searched=users_searched, users=users)


@app.route("/user_info/<int:id>", methods=["GET", "POST"])
@login_required
def user_info(id):  
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        form = SearchForm()
        user = User.query.get_or_404(id)
        return render_template("user_info.html", form=form, user=user)


@app.route("/add_review/<int:gear_id>", methods=["GET", "POST"])
@login_required
def add_review(gear_id):
    gear_item = Gear.query.filter_by(id=gear_id).first()
    reviews = Review.query.filter_by(gear_id=gear_item.id).all()
    review_user_ids = set()
    for review in reviews:
        review_user_ids.add(review.user_id)
    form = AddReviewForm()
    if form.validate_on_submit():
        review_content = form.review.data
        rating = form.rating.data
        current_user_id = current_user.id 
        if current_user_id in review_user_ids:
            flash("You have already written a review for this product")
            return redirect(url_for("about_gear", gear_id=gear_item.id))
        else:
            review = Review(
                review_contents=review_content,
                review_rating=rating,
                user_id=current_user_id,
                gear_id=gear_item.id
            )
            db.session.add(review)
            db.session.commit()
            flash("Thanks for your product review")
            return redirect(url_for("about_gear", gear_id=gear_item.id))
    return render_template("add_review.html", form=form, title=gear_item.name)

@app.route("/edit_review/<int:id>", methods=["GET", "POST"])
@login_required
def edit_review(id):
    review = Review.query.get_or_404(id)
    form = AddReviewForm()
    gear = Gear.query.filter_by(id=review.gear_id).first()
    if review.user_id != current_user.id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        if form.validate_on_submit():
            review.review_contents = form.review.data
            review.review_rating = form.rating.data
            db.session.add(review)
            db.session.commit()
            flash("Your review has been updated")
            return redirect(url_for("about_gear", gear=gear.id))
        form.review.data = review.review_contents
        form.rating.data = review.review_rating
        return render_template("edit_review.html", title=gear.name, form=form)

@app.route("/delete_review/<int:id>")
@login_required
def delete_review(id):
    form = SearchForm()
    review = Review.query.get_or_404(id)
    gear = Gear.query.filter_by(id=review.gear_id).first()
    try:
        db.session.delete(review)
        db.session.commit()
        flash("Review successfully deleted")
        reviews = Review.query.filter_by(gear_id=review.gear_id).all() 
        return render_template("about_gear.html", form=form, reviews=reviews, title=gear.name)
    except:
        flash("There seems to be a problem with deleting this post")
        reviews = Review.query.filter_by(gear_id=review.gear_id).all() 
        return render_template("about_gear.html", form=form, reviews=reviews, title=gear.name)

@app.route("/categories")
def categories():
    form = SearchForm()
    categories = Category.query.order_by(Category.category_name).all()
    return render_template("categories.html", categories=categories, form=form)

@app.route("/brands")
def brands():
    form = SearchForm()
    brands = Brand.query.order_by(Brand.brand_name).all()
    return render_template("brands.html", brands=brands, form=form)

@app.route("/brand_gear_list/<int:brand_id>")
def brand_gear_list(brand_id):
    brand = Brand.query.filter_by(id=brand_id).first()
    form = SearchForm()
    gear = Gear.query.filter_by(brand_id=brand.id).all()
    return render_template("brand_gear_list.html", gear=gear, form=form, title=brand.brand_name)

@app.route("/category_gear_list/<int:category_id>", methods=["GET", "POST"])
def category_gear_list(category_id):
    category = Category.query.filter_by(id=category_id).first()
    form = SearchForm()
    gear = Gear.query.filter_by(category_id=category.id).all()
    return render_template("category_gear_list.html", gear=gear, form=form, title=category.category_name)


@app.route("/user_reviews/<int:id>", methods=["GET", "POST"])
@login_required
def user_reviews(id):
    form = SearchForm()
    user = User.query.get_or_404(id)
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        user_reviews = Review.query.filter_by(user_id=user.id)
        return render_template("user_reviews.html", user_reviews=user_reviews, form=form, user=user)


@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product = Gear(
            name=form.name.data,
            brand_id = form.brand.data,
            category_id = form.category.data
        )
        db.session.add(product)
        db.session.commit()
        flash("Your product has been added")
        return redirect(url_for("home"))
    return render_template("add_product.html", form=form)


@app.route("/about_gear/<int:gear_id>")
def about_gear(gear_id):
    form = SearchForm()
    gear_item = Gear.query.filter_by(id=gear_id).first()
    reviews = Review.query.filter_by(gear_id=gear_item.id).all()
    return render_template("about_gear.html", form=form, title=gear_item.name, gear_id=gear_item.id, reviews=reviews)


@app.errorhandler(404)
def not_found_error(e):
    form = SearchForm()
    return render_template("404.html", form=form), 404

@app.errorhandler(500)
def not_found_error(e):
    form = SearchForm()
    return render_template("500.html", form=form), 500