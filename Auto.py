import sqlalchemy
from data.db_session import SqlAlchemyBase


class Auto(SqlAlchemyBase):
    __tablename__ = 'Auto.db'
    Name_auto = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    Length = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Width = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Height = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Engines_power = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Engines_volume = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Max_speed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Country_maker = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Class_auto = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Made_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
