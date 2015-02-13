'''
Created on Dec 21, 2014

@author: fcmeng
'''

import os
from src.helper import *

from src.models import *

@manager.command
def hello():
    print("hello")

@manager.command
def create_users():
    new_user = User(name='jesse', password='test', email='hello0@world.com', role='admin')
    db.session.add(new_user)
    new_user = User(name='lucy', password='test', email='hello1@world.com')
    db.session.add(new_user)
    new_user = User(name='john', password='test', email='hello2@world.com')
    db.session.add(new_user)
    new_user = User(name='marry', password='test', email='hello3@world.com')
    db.session.add(new_user)
    db.session.commit()

@manager.command
def create_posts():
    new_post = Post(user_id=1, title='hello1', content='world1')
    db.session.add(new_post)
    new_post = Post(user_id=1, title='hello2', content='world2')
    db.session.add(new_post)
    new_post = Post(user_id=1, title='hello3', content='world3')
    db.session.add(new_post)
    db.session.commit()

@manager.command
def run():
    port = int(os.environ.get('PORT', 4444))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    manager.run()
