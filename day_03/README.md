# 📅 Day 3 — Processing HTTP requests 

## ✅ What I Learned Today

- How to work with POST HTTP requests:
  `@app.post()`
- How to get data from POST requests and insert into a list:
  ```
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
  ```
- Using models(Pydantic -> BaseModel) to get data from POST requests in a cleaner way:
  ```
  class createPost(BaseModel):
    title: str
    body: str  
    author: int


  ......

  async def add_post(post: createPost) -> Post: ...
  ```
- Testing POST requests from `/docs` page.

## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://www.youtube.com/watch?v=RUddtw-oqFU&list=PL0lO_mIqDDFXDGav-t4qzQYdX6cfoLxXr)

---

### 🧠 Notes To My Future Self

- User **n for n in N if n == m** structure to keep your code cleaner :)
- `next()` gives you the next item from an iterator:
  ```
    next((x for x in [1, 2, 3] if x > 2), None)  # → 3
  ```
- There are other types of HTTP requests: `put, delete`

---
