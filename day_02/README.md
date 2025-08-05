# 📅 Day 2 — Pydantic and Cleaner Code

## ✅ What I Learned Today

- What is **Pydantic**?
- How to create **models** with **BaseModel**?
`from pydantic import BaseModel`
- Keeping the code cleaner and safer:
  ```
  class Post(BaseModel):
    id: int
    title: str
    body: str
  ```
- Using created models with functions:
  ```
  @app.get("/{id}")
    async def getPostById(id: int) -> Post:
      for post in posts:
        if post['id'] == id:
          return Post(**post)
      raise HTTPException(status_code=404, detail="Post by Id Not Found :(")
  ```
- How to use a model inside a model:
  ```
  class User(BaseModel):
    id: int
    name: str  
    age: int  

  class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User
  ```

## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://www.youtube.com/watch?v=RUddtw-oqFU&list=PL0lO_mIqDDFXDGav-t4qzQYdX6cfoLxXr)

---

### 🧠 Notes To My Future Self

- **Pydantic** is used to stop the app from accepting garbage :)
- It make your code _cleaner and safer_.
- **FastAPI** only reads routes in the _order_ they're defined
- if `post` is a **dict** → use `post['author']['id']`

---
