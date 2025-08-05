from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI()

users = [
  {"id": 1, "name": "Alice", "age": 25},
  {"id": 2, "name": "Bob", "age": 34},
  {"id": 3, "name": "Charlie", "age": 29},
  {"id": 4, "name": "Diana", "age": 41},
  {"id": 5, "name": "Eve", "age": 22},
  {"id": 6, "name": "Frank", "age": 38},
  {"id": 7, "name": "Grace", "age": 27},
  {"id": 8, "name": "Hank", "age": 45},
  {"id": 9, "name": "Ivy", "age": 31},
  {"id": 10, "name": "Jack", "age": 24}
]


posts = [
  {
    "id": 1,
    "title": "HelloWorld in Python",
    "body": "WHY are you learning programming?",
    "author": users[0],
  },
  {
    "id": 2,
    "title": "HelloWorld in Python",
    "body": "WHY are you learning programming?",
    "author": users[3],
  },
  {
    "id": 3,
    "title": "HelloWorld in Python",
    "body": "WHY are you learning programming?",
    "author": users[4],
  },
  {
    "id": 4,
    "title": "HelloWorld in Python",
    "body": "WHY are you learning programming?",
    "author": users[6],
  },
]



class User(BaseModel):
  id: int
  name: str  
  age: int  

class Post(BaseModel):
  id: int
  title: str
  body: str
  author: User

@app.get("/getPostsByAuthor")
async def getPostsByAuthor(author_id: Optional[int] = None) -> Dict[str, Optional[List]]  :
  author_posts = []
  for post in posts:
    if post["author"]["id"] == author_id:
      author_posts.append(Post(**post))
  if author_posts:
    return {"data": author_posts}
  return {"data": None}


@app.get("/")
async def getPosts() -> List[Post]:
  return [Post(**post) for post in posts]

@app.get("/{id}")
async def getPostById(id: int) -> Post:
  for post in posts:
    if post['id'] == id:
      return Post(**post)
  raise HTTPException(status_code=404, detail="Post by Id Not Found :(")
