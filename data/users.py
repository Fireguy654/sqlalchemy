import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


#class User1(SqlAlchemyBase):
#    __tablename__ = 'users'
#
#    id = sqlalchemy.Column(sqlalchemy.Integer,
#                           primary_key=True, autoincrement=True)
#    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#    email = sqlalchemy.Column(sqlalchemy.String,
#                              index=True, unique=True, nullable=True)
#    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
#                                     default=datetime.datetime.now)
#    news = orm.relation("News", back_populates='user')
#
#    def __repr__(self):
#        return f'{self.name} {self.about} {self.email}'
#
#    def set_password(self, password):
#        self.hashed_password = generate_password_hash(password)
#
#    def check_password(self, password):
#        return check_password_hash(self.hashed_password, password)


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)
