from review_app import (
    StringField, SubmitField, PasswordField, EmailField, FlaskForm,
    DataRequired, SelectField, TextArea)
from review_app.models import Brand, Category


class LoginForm(FlaskForm):
    """Login Form Object"""
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SignUpForm(FlaskForm):
    """Sign Up Form Object"""
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddReviewForm(FlaskForm):
    """Review Form Object"""
    review = StringField(
        "Enter your review", widget=TextArea(), validators=[DataRequired()])
    rating = SelectField(
        u"Rating out of 5",
        choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
        validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddBrandForm(FlaskForm):
    """Brand Form Object"""
    brand_name = StringField(
        "Enter Brand Name", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddCategoryForm(FlaskForm):
    """Category Form Object"""
    category_name = StringField(
        "Enter Category Name", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddProductForm(FlaskForm):
    """Product Form Object"""
    name = StringField(
        "Enter the name of the product", validators=[DataRequired()])
    brand = SelectField(
        u"Select a Brand",
        choices=[("", "---")]+[
            (brand.id, brand.brand_name.replace("-", " ").upper())
            for brand in Brand.query.order_by(Brand.brand_name)],
        validators=[DataRequired()])
    category = SelectField(
        u"Select a Category",
        choices=[
            (category.id, category.category_name.replace("-", " ").upper())
            for category in Category.query.order_by(Category.category_name)],
        validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    """Search Form Object"""
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UpdateDetailsForm(FlaskForm):
    """User Details Form Object"""
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


class NewPasswordForm(FlaskForm):
    """Update Password Form"""
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
