# type: ignore
from application import db
from datetime import datetime
from uuid import uuid4
import os

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.String(36), primary_key=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    post_time = db.Column(db.DateTime, nullable=False)
    body = db.Column(db.String(1000), nullable=False)

    def __init__(self, title: str, body: str):
        self.uid = str(uuid4())
        self.title = title
        self.body = body
        self.post_time = datetime.today()

    def __repr__(self):
        print(f'Post<{title}>')

    @staticmethod
    def add(title: str, body: str):
        db.session.add(Post(title, body))
        db.session.commit()
