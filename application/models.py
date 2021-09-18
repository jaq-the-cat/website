# type: ignore
from application import db
from uuid import uuid4
import os

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title: str, body: str):
        self.uid = uuid4()
        self.title = title
        self.body = body

    def __repr__(self):
        print(f'Post<{title}>')

    @staticmethod
    def add(title: str, body: str):
        db.session.add(Post(uid, title, body))
        db.session.commit()
