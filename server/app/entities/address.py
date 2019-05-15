import logging
from sqlalchemy.orm import relationship
from app import db, ma

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
  
  @staticmethod
  def create(street, city, state, zip):
    # TODO: have function to get current_user, add ID here:
    temp_user = User.query.limit(1).all()[0]
    new_address = Address(temp_user.id, street, city, state, zip) 
    try:
      db.session.add(new_address)
      db.session.commit()
      return new_address
    except Exception as err:
      logging.error("Error adding address to DB", err)
      return None
  
  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
      return True
    except Exception as err:
      logging.error("Error deleting address from DB", err)
      return False
  
  def update(self, street, city, state, zip):
    try:
      self.street = street
      self.city = city
      self.state = state
      self.zip = zip
      db.session.commit()
      return self
    except Exception as err:
      logging.error("Error deleting address from DB", err)
      return False

class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'street', 'city', 'state', 'zip')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)