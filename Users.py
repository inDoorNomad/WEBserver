import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Users(SqlAlchemyBase):
    __tablename__ = 'Users.db'
    Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Nickname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    About = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Registration_date = sqlalchemy.Column(sqlalchemy.DateTime,  nullable=False)
    Password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Dises = orm.relationship('Discuss', back_populates='Users')
