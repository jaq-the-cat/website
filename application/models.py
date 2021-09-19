# type: ignore
from application import db
from datetime import datetime as dt
from uuid import uuid4
import os

def _today():
    td = dt.today()
    return dt(td.year, td.month, td.day, td.hour, td.minute)

class Post(db.Model):
    __tablename__ = 'posts'
    uid = db.Column(db.String(36), primary_key=True, nullable=False, default=str(uuid4()))
    title = db.Column(db.String(120), nullable=False)
    post_time = db.Column(db.DateTime, nullable=False, default=_today())
    body = db.Column(db.String(1000), nullable=False)

    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body

    def __repr__(self):
        print(f'Post<{title}>')

    @staticmethod
    def add(title: str, body: str):
        db.session.add(Post(title, body))
        db.session.commit()
