# 📅 Day 4 — Annotation and Validation 

## ✅ What I Learned Today
- Annotation: `from typing import Annotated`
- Validation: `from fastapi import Path`
- `Annotated` is used to add extra meaning or rules to a variable’s type — like a label or hint.
- In FastAPI `Annotated` helps do things like validation or documentation:
  ```
    async def items(id: Annotated[int, Path(..., title='WRITE YOUR MESSAGE HERE!!! It will be seen in the documentation.')])
  ```
- `Path()` is used in FastAPI to validate path parameters and has parameters like:
    `title="WRITE YOUR MESSAGE HERE"` - gives a name or label to the path parameter
    `ge=1` - greater than or equal to 1
    `gt=1` - greater than 1
    `lt=100` - less than 100
    `le=100` - less than or equal to 100
    `min_length` and `max_length`
    ```
    @app.get("/{id}")
    async def getPost(id: Annotated[int, Path(..., title="Get a post by ID. ", le=100)]) -> Dict[str, Optional[Post]]:
      for post in posts:
        if post["id"] == id:
          return {"detail": Post(**post)}
      return {"detail": None}
    ```
- Using Query() for query parameters like `/search?id=2`:
  `from fastapi import Query`
- `Path()` for dynamic parameters while `Query()` for query parameters.`
- `Query()` - uses the same parameters as `Path()`
- Creating new users with `Pydantic` and `Annotation`
- For classes `Field()` is used instead of `Path()` or `Query()`: `from pydantic import Field`:
    ```
    class createUser(BaseModel):
      name: Annotated[
        str,
        Field(..., title='The name of the user you want to add.')
      ]
      age: Annotated[
        int,
        Field(..., title='Age of the user you want to add.')
      ]

    ```
- `Body()` is used when data is coming from the request body, not from the path or query: `from fastapi import Body`


## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://www.youtube.com/watch?v=RUddtw-oqFU&list=PL0lO_mIqDDFXDGav-t4qzQYdX6cfoLxXr)

---

### 🧠 Notes To My Future Self
- FastAPI has 2 docs: `/docs` and '/redoc'
- If you don't have dynamic parameter in your function, you cannot use `Path()`
- `...` in `Path()`, `Query()`, and `Field()` used to say 'this parameter is required'
- In short, FastAPI made it easier to write docs, so don't get lazy ;)
---
