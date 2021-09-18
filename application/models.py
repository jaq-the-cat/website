# type: ignore
from application import db
import os

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __repr__(self):
        print(f'Post<{title}>')
