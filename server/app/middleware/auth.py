import logging, os, datetime
import jwt
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth("Bearer")

@auth.verify_token
def verify_token(token):
  valid, _ = decode_auth_token(token)
  return valid

def decode_auth_token(token):
  try:
    payload = jwt.decode(token, os.environ['JWT_SECRET'])
    return True, payload["sub"]
  except jwt.ExpiredSignatureError:
    return False, "Signature expired. Please login again."
  except jwt.InvalidTokenError:
    return False, "Invalid token. Please login again."

def encode_auth_token(user_id):
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
