from flask import g
import logging
from sqlalchemy.orm import relationship
from app import db, ma
from entities.user import User

class Address(db.Model):
  __tablename__ = "addresses"
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(120))
  last_name = db.Column(db.String(120))
  phone = db.Column(db.String(80))
  email = db.Column(db.String(200))
  favorite = db.Column(db.Boolean)
  street = db.Column(db.String(120))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip = db.Column(db.String(80))
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

  def __init__(self, user_id, first_name, last_name, phone, email, street, city, state, zip, favorite):
    self.user_id = user_id
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email
    self.street = street
    self.city = city
    self.state = state
    self.zip = zip
    self.favorite = favorite
  
  @staticmethod
  def all():
    return Address.query.all() 
      
  @staticmethod
  def find(id):
    return Address.query.get(id)
  
  @staticmethod
  def create(first_name, last_name, phone, email, street, city, state, zip, favorite):
    new_address = Address(g.user_id, first_name, last_name, phone, email, street, city, state, zip, favorite) 
    try:
      db.session.add(new_address)
      db.session.commit()
      return new_address
    except Exception as err:
      logging.error(err)
      return None
  
  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
      return True
    except Exception as err:
      logging.error(err)
      return False
  
  def update(self, first_name, last_name, phone, email, street, city, state, zip, favorite):
    try:
      self.first_name = first_name
      self.last_name = last_name
      self.phone = phone
      self.email = email
      self.street = street
      self.city = city
      self.state = state
      self.zip = zip
      self.favorite = favorite
      db.session.commit()
      return self
    except Exception as err:
      logging.error(err)
      return False

class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 'user_id', 'first_name', 'last_name', 'phone', 'email', 'street', 'city', 'state', 'zip', 'favorite')

address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)