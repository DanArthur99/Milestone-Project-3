from review_app import db, UserMixin


class User(db.Model, UserMixin):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    reviews = db.relationship(
        "Review", backref="user", cascade="all, delete", lazy=True)
    admin = db.Column(db.Boolean, default=False, nullable=False)


class Gear(db.Model):
    """Gear Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey(
        "brand.id", ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    reviews = db.relationship(
        "Review", backref="gear", cascade="all, delete", lazy=True)


class Category(db.Model):
    """Category Model"""
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    gear = db.relationship(
        "Gear", backref="category", cascade="all, delete", lazy=True)


class Brand(db.Model):
    """Brand Model"""
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(25), unique=True, nullable=False)
    gear = db.relationship(
        "Gear", backref="brand", cascade="all, delete", lazy=True)


class Review(db.Model):
    """Review Model"""
    id = db.Column(db.Integer, primary_key=True)
    review_contents = db.Column(db.String, unique=False, nullable=True)
    review_rating = db.Column(db.Integer, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=False)
    gear_id = db.Column(db.Integer, db.ForeignKey(
        "gear.id", ondelete="CASCADE"), nullable=False)
