import logging, os, datetime
import jwt
from sqlalchemy.orm import relationship
from app import db, ma, bcrypt

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  password = db.Column(db.String(500))
  address = relationship("Address", cascade="all, delete, delete-orphan")

  def __init__(self, email=None, password=None):
    self.email = email
    self.password= password
  
  @staticmethod
  def find(email):
    return User.query.filter_by(email=email).first()
  
  @staticmethod
  def create(email, password):
    already_exists = User.find(email)
    if already_exists:
      return None
    else: 
      user = User(
        email=email,
        password=bcrypt.generate_password_hash(password)
      )
      db.session.add(user)
      db.session.commit()
      return user

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)