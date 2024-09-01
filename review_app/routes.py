from flask import (
    render_template, request, redirect, url_for, flash)
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from review_app import (
    app, db, login_user, LoginManager, login_required, logout_user,
    current_user)
from review_app.models import User, Gear, Category, Brand, Review
from review_app.forms import (
    LoginForm, SignUpForm, AddReviewForm, SearchForm, AddProductForm,
    UpdateDetailsForm, NewPasswordForm, AddBrandForm, AddCategoryForm)
from psycopg2.errors import UniqueViolation
import bcrypt

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    """Function for the home page"""
    form = SearchForm()
    return render_template("home.html", form_b=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Checks if the user with the entered email exists, and if true,
    then the password is checked using bcrypt."""
    form = LoginForm()
    form_b = SearchForm()
    if form.validate_on_submit():
        try:
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
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There was an error logging on")
    return render_template("login.html", form=form, form_b=form_b)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """Logs the user out when called."""
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("login"))


@app.route("/dashboard/<int:id>", methods=["GET", "POST"])
@login_required
def dashboard(id):
    form = SearchForm()
    """Checks to see if the user authorized to access the page, and if true,
    renders the dashboard page."""
    if not current_user.admin and current_user.id != id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        form = SearchForm()
        user = User.query.get_or_404(id)
        return render_template("dashboard.html", form_b=form, user=user)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """Hashes the password adds it to the database alongside the entered
    username and email."""
    form = SignUpForm()
    form_b = SearchForm()
    if form.validate_on_submit():
        try:
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
                return redirect(url_for("login"))
        except (IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There was an error signing you up")
            return redirect(url_for("sign_up"))
    return render_template("sign_up.html", form=form, form_b=form_b)


@app.route("/search_buffer", methods=["GET", "POST"])
def search_buffer():
    form = SearchForm()
    if form.validate_on_submit():
        try:
            searched = form.searched.data
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("sorry, we are having difficulties")
            return redirect(url_for("home"))
        return redirect(url_for("search", searched=searched))
    else:
        return redirect(url_for("home"))


@app.route("/search/<searched>", methods=["GET", "POST"])
def search(searched):
    """Queries the database using the entered string, and renders the results
    on screen."""
    form = SearchForm()
    gear_items = Gear.query
    try:
        gear_searched = searched
        gear_items = gear_items.filter(
            Gear.name.ilike('%' + gear_searched + '%'))
        gear_items = gear_items.order_by(Gear.name).all()
    except (
        IntegrityError, UniqueViolation, PendingRollbackError) as e:
        flash("There was a problem when searching for a product")
        return redirect(url_for("home"))
    return render_template(
        "search.html", form_b=form, searched=gear_searched,
        gear_items=gear_items)


@app.route("/search_users")
@login_required
def search_users():
    """Checks if the user is admin, and if true, the page is rendered with all
    users displayed on screen."""
    form = SearchForm()
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        users = User.query
        return render_template("search_users.html", form=form, form_b=form, users=users)


@app.route("/list_of_users", methods=["POST"])
@login_required
def list_of_users():
    """Queries the database using the entered string, and renders the results
    on screen."""
    form = SearchForm()
    form_b = SearchForm()
    users = User.query
    if form.validate_on_submit():
        try:
            users_searched = form.searched.data
            users = users.filter(User.username.ilike(
                '%' + users_searched + '%'))
            users = users.order_by(User.username).all()
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash(
                "Apologies, we seem to have encountered an error")
            return redirect(url_for("home"))
        return render_template(
            "list_of_users.html", form=form, form_b=form_b,
            searched=users_searched, users=users)


@app.route("/update_user/<int:id>", methods=["GET", "POST"])
@login_required
def update_user(id):
    """Checks if the user is authorized, and if true,
    updates the queried user's details on submit."""
    form = UpdateDetailsForm()
    form_b = SearchForm()
    user = User.query.get_or_404(id)
    if not current_user.admin and current_user.id != id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        if form.validate_on_submit():
            try:
                user.username = form.username.data
                user.email = form.email.data
                db.session.add(user)
                db.session.commit()
                if current_user.id == user.id:
                    flash("Your details have been updated")
                else:
                    flash(f"{user.username}'s details have been updated")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                if current_user.id == user.id:
                    flash("There was an error updating your details")
                else:
                    flash(
                        f"There was an error updating this user's details")
            return redirect(url_for("dashboard", id=user.id))
        form.username.data = user.username
        form.email.data = user.email
        return render_template(
            "update_user.html", form=form, form_b=form_b, user=user)


@app.route("/update_password/<int:id>", methods=["GET", "POST"])
@login_required
def update_password(id):
    """Checks if the user is authorized, and if true,
    the user's password is updated."""
    form_b = SearchForm()
    if not current_user.admin and current_user.id != id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        form = NewPasswordForm()
        user = User.query.get_or_404(id)
        if form.validate_on_submit():
            password = bytes(form.password.data, "utf-8")
            confirm_password = bytes(form.confirm_password.data, "utf-8")
            if password != confirm_password:
                flash("Passwords don't match")
            else:
                try:
                    hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
                    user.password = hashed_pw.decode("utf-8")
                    db.session.add(user)
                    db.session.commit()
                    flash("Password updated")
                    return redirect(url_for("home"))
                except (
                    IntegrityError, UniqueViolation, PendingRollbackError) as e:
                    flash("There was an error updating your password")
                    return redirect(url_for("home"))
        return render_template(
            "update_password.html", form=form, form_b=form_b, user=user)


@app.route("/add_review/<int:gear_id>", methods=["GET", "POST"])
@login_required
def add_review(gear_id):
    """Checks if the user has already written a review, and if false,
    adds a new review."""
    gear_item = Gear.query.filter_by(id=gear_id).first()
    reviews = Review.query.filter_by(gear_id=gear_item.id).all()
    review_user_ids = set()
    for review in reviews:
        review_user_ids.add(review.user_id)
    form = AddReviewForm()
    form_b = SearchForm()
    if form.validate_on_submit():
        if current_user.id in review_user_ids:
            flash("You have already written a review for this product")
            return redirect(url_for("about_gear", id=gear_item.id))
        else:
            try:
                review = Review(
                    review_contents=form.review.data,
                    review_rating=form.rating.data,
                    user_id=current_user.id,
                    gear_id=gear_item.id
                )
                db.session.add(review)
                db.session.commit()
                flash("Thanks for your product review")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error adding this review")
            return redirect(url_for("about_gear", id=gear_item.id))
    return render_template(
        "add_review.html", form=form, form_b=form_b, title=gear_item.name)


@app.route("/edit_review/<int:id>", methods=["GET", "POST"])
@login_required
def edit_review(id):
    """Checks if the user has authorised access, and if true,
    allows the review to be changed by the user."""
    review = Review.query.get_or_404(id)
    form = AddReviewForm()
    form_b = SearchForm()
    gear = Gear.query.get_or_404(review.gear.id)
    if not current_user.admin and current_user.id != review.user.id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        if form.validate_on_submit():
            try:
                review.review_contents = form.review.data
                review.review_rating = form.rating.data
                db.session.add(review)
                db.session.commit()
                flash("Your review has been updated")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error editing this review")
            return redirect(url_for("about_gear", id=gear.id))
        form.review.data = review.review_contents
        form.rating.data = review.review_rating
        return render_template(
            "edit_review.html", title=gear.name, form=form, form_b=form_b)


@app.route("/delete_review/<int:id>")
@login_required
def delete_review(id):
    """Checks if the user is authorised, and if true,
    deletes the review from the database."""
    review = Review.query.get_or_404(id)
    gear = Gear.query.filter_by(id=review.gear.id).first()
    if not current_user.admin and current_user.id != review.user.id:
        flash("You are not authorized for this functionality")
        return redirect(url_for("home"))
    else:
        try:
            db.session.delete(review)
            db.session.commit()
            flash("Review successfully deleted")
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There seems to be a problem with deleting this post")
        return redirect(url_for("about_gear", id=gear.id))


@app.route("/delete_gear/<int:id>")
@login_required
def delete_gear(id):
    """Checks if the user is admin, and if true,
    the product is deleted from the database."""
    if not current_user.admin:
        flash("You are not authorized for this functionality")
        return redirect(url_for("home"))
    else:
        gear = Gear.query.get_or_404(id)
        try:
            db.session.delete(gear)
            db.session.commit()
            flash("Gear successfully deleted")
            return redirect(url_for("home"))
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There seems to be a problem with deleting this item")
            return redirect(url_for("home"))


@app.route("/add_brand", methods=["GET", "POST"])
@login_required
def add_brand():
    """Checks if the user is admin, and if true,
    adds a new brand to the database."""
    form = AddBrandForm()
    form_b = SearchForm()
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("brands"))
    else:
        if form.validate_on_submit():
            try:
                brand = Brand(
                    brand_name=form.brand_name.data.replace(
                        " ", "-").lower()
                )
                db.session.add(brand)
                db.session.commit()
                flash("This brand has been added")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error adding this brand")
            return redirect(url_for("brands"))
        return render_template(
            "add_brand.html", form=form, form_b=form_b)


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    """Checks if the user is admin, and if true,
    adds a new category to the database."""
    form = AddCategoryForm()
    form_b = SearchForm()
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("categories"))
    else:
        if form.validate_on_submit():
            try:
                category = Category(
                    category_name=form.category_name.data.replace(
                        " ", "-").lower()
                )
                db.session.add(category)
                db.session.commit()
                flash("This category has been added")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error adding this category")
            return redirect(url_for("categories"))
        return render_template("add_category.html", form=form, form_b=form_b)


@app.route("/edit_brand/<int:id>", methods=["GET", "POST"])
@login_required
def edit_brand(id):
    """Checks if the user is admin, and if true, updates the brand name."""
    brand = Brand.query.get_or_404(id)
    form = AddBrandForm()
    form_b = SearchForm()
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        if form.validate_on_submit():
            try:
                brand.brand_name = form.brand_name.data.replace(
                    " ", "-").lower()
                db.session.add(brand)
                db.session.commit()
                flash("This brand has been updated")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error updating this category")
            return redirect(url_for("brands"))
        form.brand_name.data = brand.brand_name.replace("-", " ").title()
        return render_template(
            "edit_brand.html", form=form, form_b=form_b, 
            title=brand.brand_name.replace(
                "-", " ").title())


@app.route("/edit_category/<int:id>", methods=["GET", "POST"])
@login_required
def edit_category(id):
    """Checks if the user is admim, and if true, updates the category name."""
    category = Category.query.get_or_404(id)
    form = AddCategoryForm()
    form_b = SearchForm()
    if not current_user.admin:
        flash("You are not authorized to access this page")
        return redirect(url_for("categories"))
    else:
        if form.validate_on_submit():
            try:
                category.category_name = form.brand_name.data.replace(
                    " ", "-").lower()
                db.session.add(category)
                db.session.commit()
                flash("This brand has been updated")
            except (
                IntegrityError, UniqueViolation, PendingRollbackError) as e:
                flash("There was an error editing this category")
            return redirect(url_for("categories"))
        form.category_name.data = category.category_name.replace(
            "-", " ").title()
        return render_template(
            "edit_brand.html", form=form, 
            form_b=form_b, title=category.category_name.replace(
                "-", " ").title())


@app.route("/delete_brand/<int:id>")
@login_required
def delete_brand(id):
    """Checks if the user is admin, and if true,
    deletes the brand along with all relations, from the database."""
    form = SearchForm()
    if not current_user.admin:
        flash("You are not authorized for this functionality")
        return redirect(url_for("brands"))
    else:
        brand = Brand.query.get_or_404(id)
        try:
            db.session.delete(brand)
            db.session.commit()
            flash("Brand successfully deleted")
            return redirect(url_for("brands"))
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There seems to be a problem with deleting this brand")
            return redirect(url_for("brands"))


@app.route("/delete_category/<int:id>")
@login_required
def delete_category(id):
    """Checks if the user is admin, and if true,
    deletes the category along with all relations, from the database."""
    if not current_user.admin:
        flash("You are not authorized for this functionality")
        return redirect(url_for("categories"))
    else:
        category = Category.query.get_or_404(id)
        try:
            db.session.delete(category)
            db.session.commit()
            flash("Category successfully deleted")
            return redirect(url_for("categories"))
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There seems to be a problem with deleting this category")
            return redirect(url_for("categories"))


@app.route("/delete_user/<int:id>")
@login_required
def delete_user(id):
    """Checks if the current user is admin, and if true, the selected."""
    user = User.query.get_or_404(id)
    if not current_user.admin and current_user != user.id:
        flash("You are not authorized for this functionality")
        return redirect(url_for("home"))
    else:
        user = User.query.get_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            flash("User successfully deleted")
            return redirect(url_for("home"))
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There seems to be a problem with deleting this item")
            return redirect(url_for("home"))


@app.route("/categories")
def categories():
    """Renders all categories from the database onto the screen."""
    form = SearchForm()
    categories = Category.query.order_by(Category.category_name).all()
    return render_template("categories.html", categories=categories, form_b=form)


@app.route("/brands")
def brands():
    """Renders all brands from the database onto the screen"""
    form = SearchForm()
    brands = Brand.query.order_by(Brand.brand_name).all()
    return render_template("brands.html", brands=brands, form_b=form)


@app.route("/brand_gear_list/<int:brand_id>")
def brand_gear_list(brand_id):
    """Renders all products with a matching brand id
    from the database onto the screen."""
    brand = Brand.query.filter_by(id=brand_id).first()
    form = SearchForm()
    gear = Gear.query.filter_by(brand_id=brand.id).all()
    return render_template(
        "brand_gear_list.html", gear=gear, form_b=form,
        title=brand.brand_name.replace("-", " "))


@app.route("/category_gear_list/<int:category_id>", methods=["GET", "POST"])
def category_gear_list(category_id):
    """Renders all products with a matching category id
    from the database onto the screen."""
    category = Category.query.filter_by(id=category_id).first()
    form = SearchForm()
    gear = Gear.query.filter_by(category_id=category.id).all()
    return render_template(
        "category_gear_list.html", gear=gear, form_b=form,
        title=category.category_name.replace("-", " "))


@app.route("/user_reviews/<int:id>", methods=["GET", "POST"])
@login_required
def user_reviews(id):
    """Checks user authorisation, and if true,
    render's the page displaying the chosen user's reviews."""
    form = SearchForm()
    user = User.query.get_or_404(id)
    if not current_user.admin and current_user.id != id:
        flash("You are not authorized to access this page")
        return redirect(url_for("home"))
    else:
        user_reviews = Review.query.filter_by(user_id=user.id).all()
        if len(user_reviews) == 0:
            user_reviews = None
        return render_template(
            "user_reviews.html", user_reviews=user_reviews, form_b=form,
            user=user)


@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    """Adds new product to the database from the user's form inputs"""
    form = AddProductForm()
    form_b = SearchForm()
    if form.validate_on_submit():
        try:
            product = Gear(
                name=form.name.data.replace(" ", "-").lower(),
                brand_id=form.brand.data,
                category_id=form.category.data
            )
            db.session.add(product)
            db.session.commit()
            flash("Your product has been added")
            return redirect(url_for("about_gear", id=product.id))
        except (
            IntegrityError, UniqueViolation, PendingRollbackError) as e:
            flash("There was an error adding this product")
            return redirect(url_for("home"))
    return render_template("add_product.html", form=form, form_b=form_b)


@app.route("/about_gear/<int:id>")
def about_gear(id):
    """Queries the selected product, and displays the reviews,
    as well the review score."""
    form = SearchForm()
    gear_item = Gear.query.get_or_404(id)
    reviews = Review.query.filter_by(gear_id=gear_item.id).all()
    gear_rating_total = float(0)
    for review in reviews:
        gear_rating_total += float(review.review_rating)
    if len(reviews) > 0:
        gear_rating_mean = round((gear_rating_total / len(reviews)), 1)
    else:
        gear_rating_mean = None
    return render_template(
        "about_gear.html", form_b=form, title=gear_item.name, gear=gear_item,
        reviews=reviews, score=gear_rating_mean)


@app.errorhandler(404)
def not_found_error(e):
    """Handles 404 error"""
    form = SearchForm()
    return render_template("404.html", form_b=form), 404


@app.errorhandler(500)
def not_found_error(e):
    """Handles 500 error"""
    form = SearchForm()
    return render_template("500.html", form_b=form), 500
