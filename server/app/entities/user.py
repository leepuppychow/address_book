import logging
from sqlalchemy.orm import relationship
from app import db, ma

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  password = db.Column(db.String(80))
  address = relationship("Address", cascade="all, delete, delete-orphan")

  def __init__(self, email=None, password=None):
    self.email = email
    self.password= password

  @staticmethod
  def all():
    return User.query.all() 

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)