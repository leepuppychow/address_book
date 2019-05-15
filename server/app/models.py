from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  password = db.Column(db.String(80))
  address = relationship("Address", cascade="all, delete, delete-orphan")

  def __init__(self, email=None, password=None):
    self.email = email
    self.password= password

class Address(db.Model):
  __tablename__ = "addresses"
  id = db.Column(db.Integer, primary_key=True)
  street = db.Column(db.String(120))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

  def __init__(self, user_id, street, city, state, zip):
    self.user_id = user_id
    self.street = street
    self.city = city
    self.state = state
    self.zip = zip




