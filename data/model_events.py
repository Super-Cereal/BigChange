import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Event(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    address = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    ll = sqlalchemy.Column(sqlalchemy.String)
    additions = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    comments = sqlalchemy.orm.relation("Comment", backref="event")
    photo = sqlalchemy.orm.relation("File", uselist=False)
    # user = sqlalchemy.orm.relation("User")
