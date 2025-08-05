# 📅 Day 1 — Working with URLs and Parameters in FastAPI

## ✅ What I Learned Today

- How to **install** `fastapi` and `uvicorn` using pip
- Created my **first FastAPI app**
- Learned how to **launch the server** with:
  ```bash
  uvicorn main:app --reload
  ```
- Handled **dynamic path parameters** like:
  ```
  /items/{id}
  ```
- Worked with **query parameters** such as:
  ```
  /search?post_id=123
  ```
- Handled **404 Not Found** errors using:
  ```python
  from fastapi import HTTPException
  raise HTTPException(status_code=404, detail="Item not found")
  ```

## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://youtu.be/wCH-eFnqz00?si=00GSpnXWCJ-hLhrV)

---

### 🧠 Notes To My Future Self

- Use `@app.get("/path")` to define routes
- Path params go inside `{}` — they must be included in the URL
- Query params are optional and go after `?`
- Always use `--reload` while developing for hot reload

---

### 🚀 What’s Next?

- Learn how to use **Pydantic models** to handle request bodies
- Explore **POST** requests and input validation