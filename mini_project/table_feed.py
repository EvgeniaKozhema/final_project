from mini_project.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from table_post import Post
from table_user import User
from sqlalchemy.orm import relationship

class Feed(Base):
    __tablename__ = 'feed_action'
    action = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    time = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user = relationship(User)
    post = relationship(Post)

