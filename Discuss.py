import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Discuss(SqlAlchemyBase):
    __tablename__ = 'Discuss.db'
    Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    Dis_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Tag = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    creating_date = sqlalchemy.Column(sqlalchemy.DateTime)
    Autor = orm.relationship('Users')
    Users_name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("Users.Nickname"))
