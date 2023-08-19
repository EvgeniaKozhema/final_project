from fastapi import FastAPI
from typing import List
from mini_project.schema import PostGet
from mini_project.database import SessionLocal
from mini_project.table_feed import Feed
from sqlalchemy import func
from mini_project.table_post import Post

app = FastAPI()

@app.get("/post/recommendations/", response_model=List[PostGet])
def recomm(id:int, limit : int = 10):
    session = SessionLocal()
    posts = session.query(Post)\
        .select_from(Feed)\
        .filter(Feed.action == 'like')\
        .join(Post)\
        .group_by(Post.id)\
        .order_by(func.count(Post.id).desc())\
        .limit(limit)\
        .all()
    return posts

