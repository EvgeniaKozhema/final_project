from mini_project.database import Base, SessionLocal
from sqlalchemy import Integer, String, Column

session = SessionLocal()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == '__main__':
    business_posts = session.query(Post).filter(Post.topic == 'business').order_by(Post.id.desc()).limit(10).all()
    business_posts_id = [post.id for post in business_posts]
    print(business_posts_id)





