from review_app import db, UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)

class GearItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)