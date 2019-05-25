import logging
from flask_script import Manager
from app import app, db, bcrypt
from models import User, Address

manager = Manager(app)

@manager.command
def seed():
  truncate_tables()
  insert_users_and_addresses()
  
def truncate_tables():
  try:
    db.session.query(Address).delete()
    db.session.query(User).delete()
    db.session.commit()
  except Exception as err:
    logging.error(err)
    db.session.rollback()

def insert_users_and_addresses():
  try:
    user1 = User('test@test.com', bcrypt.generate_password_hash("password").decode('utf-8'))
    user2 = User('test2@test.com', bcrypt.generate_password_hash("password").decode('utf-8'))
    db.session.add(user1)
    db.session.add(user2)
    db.session.flush()

    addresses = [
      Address(user1.id, "first1", "last1", "720342373", "test1@test.com", "123 Test way", 'Denver', 'CO', '81111', False),
      Address(user1.id, "first2", "last2", "720342373", "test2@test.com", "456 Test way", 'Denver', 'CO', '81111', False),
      Address(user2.id, "first3", "last3", "720342373", "test3@test.com", "789 Test way", 'Denver', 'CO', '81111', False),
    ]
    db.session.bulk_save_objects(addresses)
    db.session.commit()
    print('\n\nDATABASE SEEDING COMPLETE\n\n')
  except Exception as err:
    logging.error(err)
    db.session.rollback()

if __name__ == "__main__":
  manager.run()