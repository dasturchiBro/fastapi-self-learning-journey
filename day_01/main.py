from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/items")
async def introduction() -> list[dict]:
	return news

news = [
	{
		"id": 1,
		"title": "News 1",
		"body": "In todays fast-paced worlds, it has become increasingly common for people to lead a sedentary lifestyle."
	},
	{
		"id": 2,
		"title": "News 2",
		"body": "In todays fast-paced worlds, it has become increasingly common for people to lead a sedentary lifestyle."
	},
	{
		"id": 3,
		"title": "News 3",
		"body": "In todays fast-paced worlds, it has become increasingly common for people to lead a sedentary lifestyle."
	},
	{
		"id": 4,
		"title": "News 4",
		"body": "In todays fast-paced worlds, it has become increasingly common for people to lead a sedentary lifestyle."
	},

]

def lookUp(id):
	for post in news:
		if post["id"] == id:
			return post
	raise HTTPException(status_code=404, detail=f"The news post by ID({id}) not found!")

@app.get("/items/{id}")
async def getNewsById(id: int):
	return lookUp(post_id)

@app.get("/search")
async def search(post_id: Optional[int] = None):
	if post_id:
		return lookUp(post_id)
	return {"Message": f"No Post Found by ID: {post_id}"}
