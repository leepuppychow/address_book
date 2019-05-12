import os

class Development(object):
  DEBUG = True
  TESTING = False
  JWT_SECRET = os.getenv('JWT_SECRET')  
  DATABASE_URL = os.getenv('DATABASE_URL')

class Production(object):
  DEBUG = False
  TESTING = False
  JWT_SECRET = os.getenv('JWT_SECRET')  
  DATABASE_URL = os.getenv('DATABASE_URL')

app_config = {
  'development': Development,
  'production': Production,
}

