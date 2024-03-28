import datetime
import sqlalchemy

from data.db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm, PrimaryKeyConstraint


class UserCourse(SqlAlchemyBase):
    __tablename__ = 'users_courses'
    __table_args__ = (
        PrimaryKeyConstraint('id_course', 'user_id'),
    )

    user = orm.relationship('User')
    course = orm.relationship('Course')
    id_course =  sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("courses.id"))
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
