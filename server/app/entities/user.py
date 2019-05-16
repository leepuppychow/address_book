import logging, os, datetime
import jwt
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
  def find(email):
    return User.query.filter_by(email=email).first()

  @staticmethod
  def decode_auth_token(token):
    try:
      payload = jwt.decode(token, os.environ['JWT_SECRET'])
      return True, payload["sub"]
    except jwt.ExpiredSignatureError:
      return False, "Signature expired. Please login again."
    except jwt.InvalidTokenError:
      return False, "Invalid token. Please login again."

  def encode_auth_token(self, user_id):
    try:
      payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
      }
      return jwt.encode(
        payload,
        os.environ['JWT_SECRET'],
        algorithm="HS256"
      )
    except Exception as err:
      logging.error(err)

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)