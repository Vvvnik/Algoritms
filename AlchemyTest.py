
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

DATABASE = {
        'drivername': 'postgres', #Тут можно использовать MySQL или другой драйвер
        'host': 'localhost',
        'port': '5432',
        'username': 'youuser',
        'password': 'youpassword',
        'database': 'youdb'
}

engine  = create_engine(URL(**DATABASE))


from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)

    def __repr__(self):
        return "".format(self.code)
