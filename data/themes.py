import datetime
import sqlalchemy

from data.db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm


class Themes(SqlAlchemyBase):
    __tablename__ = 'themes'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    course_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)