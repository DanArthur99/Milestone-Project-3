from review_app import StringField, SubmitField, PasswordField, EmailField, FlaskForm, DataRequired, SelectField, TextArea
from review_app.models import Brand, Category

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddReviewForm(FlaskForm):
    review = StringField("Enter your review", widget=TextArea(), validators=[DataRequired()])
    rating = SelectField(u"Rating out of 5", choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddBrandForm(FlaskForm):
    brand_name = StringField("Enter Brand Name", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddCategoryForm(FlaskForm):
    category_name = StringField("Enter Category Name", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddProductForm(FlaskForm):
    name = StringField("Enter the name of the product", validators=[DataRequired()])
    brand = SelectField(u"Select a Brand", choices=[(brand.id, brand.brand_name) for brand in Brand.query.order_by(Brand.brand_name)], validators=[DataRequired()])
    category = SelectField(u"Select a Category", choices=[(category.id, category.category_name) for category in Category.query.order_by(Category.category_name)], validators=[DataRequired()])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UpdateDetailsForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

class NewPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")