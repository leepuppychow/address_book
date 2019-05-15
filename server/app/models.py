from app import db

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(80))
  password = db.Column(db.String(80))

  def __init__(self, email=None, password=None):
    self.email = email
    self.password= password



