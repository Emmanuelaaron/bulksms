import jwt
from datetime import datetime, timedelta
from models.user import User
# from models.Forum_members import *

from app import db

from helpers.toDict import ToDict

class Forum(db.Model, ToDict):
    """ Forum table definition """

    _tablename_ = 'Forums'
    __table_args__ = (db.UniqueConstraint('name', name='forum_unique_name'),)

    # fields of the Forum table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, name):
        """ initialize with name, member and namespace """
        self.name = name


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()