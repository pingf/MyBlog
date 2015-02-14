from src.helper import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'post'
    
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(32), index=True)
    content = db.Column(db.Text())
    parent_id = db.Column(db.Integer)
    access = db.Column('role', db.String(32), index=True)
    created_at = db.Column('registered_at' , db.DateTime)
    updated_at = db.Column('updated_at' , db.DateTime)
    

    def __init__(self, user_id, title, content, parent_id=0, access='normal'):
        self.user_id = user_id
        self.title, self.content = title, content
        self.parent_id = parent_id
        self.access = access
        time = datetime.utcnow()
        self.created_at = time
        self.updated_at = time


    def __repr__(self):
        return '<User %r>' % self.id

    
    
