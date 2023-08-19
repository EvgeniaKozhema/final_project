from mini_project.database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func

session = SessionLocal()

class User(Base):
    __tablename__ = 'user'
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    id = Column(Integer, primary_key=True)
    os = Column(String)
    source = Column(String)

if __name__ == '__main__':
     users = session.query(User.country, User.os, func.count('*'))\
        .filter(User.exp_group==3)\
        .group_by(User.country, User.os)\
        .having(func.count('*') > 100)\
        .order_by(func.count('*').desc())\
        .all()
     print(users)


