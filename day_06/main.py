from fastapi import FastAPI, HTTPException, Path, Body, Depends
from typing import Dict, Optional, Annotated
from sqlalchemy.orm import Session  
from models import Base, User, Post  
from database import engine, session_local  
from schemas import UserCreate, PostCreate, PostResponse, User as DBUser
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
	db = session_local()
	try:
		yield db  
	finally:
		db.close()

@app.post('/users/', response_model=DBUser)
async def create_User(user: UserCreate, db: Session = Depends(get_db)) -> User:
	db_user = User(name=user.name, age=user.age)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)

	return db_user

@app.post('/posts/', response_model=PostResponse)
async def create_Post(post: PostCreate, db: Session = Depends(get_db)) -> Post:
	db_user = db.query(User).filter(User.id == post.author).first()

	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found :(")

	db_post = Post(title=post.title, body=post.body, author=post.author)
	db.add(db_post)
	db.commit()
	db.refresh(db_post)

	return db_post

@app.get('/posts/', response_model=List[PostResponse])
async def get_Posts(db: Session = Depends(get_db)) -> List[Post]:
	return db.query(Post).all()


# users = [
# 	{
# 		"id": 1,
# 		"name": "John Smith",
# 		"age": 19
# 	},
# 	{
# 		"id": 2,
# 		"name": "William Johnson",
# 		"age": 56
# 	},
# 	{
# 		"id": 3,
# 		"name": "Usher Botson",
# 		"age": 27
# 	},
# ]

# posts = [
# 	{
# 		"id": 1,
# 		"title": "Python - FastAPI",
# 		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
# 		"author": users[2],
# 	},
# 	{
# 		"id": 2,
# 		"title": "Python - FastAPI",
# 		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
# 		"author": users[0],
# 	},
# 	{
# 		"id": 3,
# 		"title": "Python - FastAPI",
# 		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
# 		"author": users[1],
# 	},
# ]

