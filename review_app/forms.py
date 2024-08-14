from review_app import StringField, SubmitField, PasswordField, EmailField, FlaskForm, DataRequired, TextArea

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
    review = StringField("Enter your review", widget=TextArea())
    rating = StringField("Enter your rating", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")