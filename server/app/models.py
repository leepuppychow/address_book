from app import db, ma
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

  @staticmethod
  def all():
    return User.query.all() 

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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
  
  @staticmethod
  def all():
    return Address.query.all() 
      
  @staticmethod
  def find(id):
    return Address.query.get(id)

class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'street', 'city', 'state', 'zip')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)