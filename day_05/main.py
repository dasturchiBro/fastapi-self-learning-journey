from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel, Field
from typing import Dict, Optional, Annotated


app = FastAPI()



class createUser(BaseModel):
	name: Annotated[
		str,
		Field(..., title='The name of the user you want to add.')
	]
	age: Annotated[
		int,
		Field(..., title='Age of the user you want to add.')
	]


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
async def get_Post(id: Annotated[int, Path(..., title="Get a post by ID. ", le=100)]) -> Dict[str, Optional[Post]]:
	for post in posts:
		if post["id"] == id:
			return {"detail": Post(**post)}
	return {"detail": None}

@app.post("/post/add")
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


@app.post("/user/add")
async def add_user(user: Annotated[
		createUser,
		Body(..., example={
				"name": "User's fullname",
				"age": "User's age in numbers"
			}
		)
	]) -> User:
	next_id = len(users) + 1
	new_user = {
		"id": next_id,
		"name": user.name,
		"age": user.age,
	}
	users.append(new_user)
	return User(**new_user)