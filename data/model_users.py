import time
import bcrypt
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    type = sqlalchemy.Column(sqlalchemy.Integer)
    last_time_in = sqlalchemy.Column(sqlalchemy.String,
                                     default=time.ctime)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    events = sqlalchemy.orm.relation("Event", backref="user")
    photo = sqlalchemy.orm.relation("File", uselist=False)

    def set_password(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.hashed_password)
