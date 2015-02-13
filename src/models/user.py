from src.helper import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64))  
    password = db.Column('password' , db.String(32))
    email = db.Column('email', db.String(32), unique=True, index=True)
    role = db.Column('role', db.String(32), index=True)
    registered_at = db.Column('registered_at' , db.DateTime)
    updated_at = db.Column('updated_at' , db.DateTime)
    posts = db.relationship("Post",backref="user")

    def __init__(self, name, password, email, role='normal'):
        self.name = name
        self.password = password
        self.email = email
        self.role = role
        time = datetime.utcnow()
        self.registered_at = time
        self.updated_at = time

    def __repr__(self):
        return '<User %r>' % self.id

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.name)
    
    
