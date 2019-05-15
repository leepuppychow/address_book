import logging
from flask_script import Manager
from app import app, db
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
    logging.error("Error deleting DB data", err)
    db.session.rollback()

def insert_users_and_addresses():
  try:
    user1 = User('test@test.com', 'password')
    user2 = User('test2@test.com', 'password2')
    db.session.add(user1)
    db.session.add(user2)
    db.session.flush()

    addresses = [
      Address(user1.id, "123 Test way", 'Denver', 'CO', '81111'),
      Address(user1.id, "456 Test way", 'Denver', 'CO', '81111'),
      Address(user2.id, "789 Test way", 'Denver', 'CO', '81111'),
      Address(user2.id, "111 Test way", 'Denver', 'CO', '81111')
    ]
    db.session.bulk_save_objects(addresses)
    db.session.commit()
    print('\n\nDATABASE SEEDING COMPLETE\n\n')
  except Exception as err:
    logging.error("Error deleting DB data", err)
    db.session.rollback()

if __name__ == "__main__":
  manager.run()