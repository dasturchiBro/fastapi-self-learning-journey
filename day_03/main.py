from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

class User(BaseModel):
	id: int  
	name: str  
	age: int  

class createPost(BaseModel):
	title: str
	body: str  
	author: int

class Post(BaseModel):
	id: int  
	title: str  
	body: str
	author: User


users = [
	{
		"id": 1,
		"name": "John Smith",
		"age": 19
	},
	{
		"id": 2,
		"name": "William Johnson",
		"age": 56
	},
	{
		"id": 3,
		"name": "Usher Botson",
		"age": 27
	},
]

posts = [
	{
		"id": 1,
		"title": "Python - FastAPI",
		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
		"author": users[2],
	},
	{
		"id": 2,
		"title": "Python - FastAPI",
		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
		"author": users[0],
	},
	{
		"id": 3,
		"title": "Python - FastAPI",
		"body": "Today, we will delve deeper into the topic of creating APIs with FastAPI",
		"author": users[1],
	},
]



@app.get("/{id}")
async def writePost(id: int) -> Dict[str, Optional[Post]]:
	for post in posts:
		if post["id"] == id:
			return {"detail": Post(**post)}
	return {"detail": None}

@app.post("/")
async def add_post(post: createPost) -> Post:
	author = next((user for user in users if user["id"] == post.author), None)

	if author:
		new_post = {
			"id": len(posts) + 1,
			"title": post.title,
			"body": post.body,
			"author": author,
		}
		posts.append(new_post)
		return Post(**new_post)
	raise HTTPException(status_code=404, detail="Author Not Found")