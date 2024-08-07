from review_app import db, UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    reviews = db.relationship("Review", backref="user", cascade="all, delete", lazy=True)
    admin = db.Column(db.Boolean, default=False, nullable=False)

class Gear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.id", ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    gear = db.relationship("Gear", backref="category", cascade="all, delete", lazy=True)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(25), unique=True, nullable=False)
    gear = db.relationship("Gear", backref="brand", cascade="all, delete", lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    gear_id = db.Column(db.Integer, db.ForeignKey("gear.id", ondelete="CASCADE"), nullable=False)