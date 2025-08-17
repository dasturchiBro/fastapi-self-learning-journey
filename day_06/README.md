# 📅 Day 6 — Working with Database - Part 2

## ✅ What I Learned Today

- Creating tables, columns, etc. in the database with SqlAlchemy
- Creating a User and Post in the database:
  ```
    @app.post('/users/', response_model=DBUser)
      async def createUser(user: UserCreate, db: Session = Depends(get_db)) -> User:
        db_user = User(name=user.name, age=user.id)
        db.add(db_user)
        db.commit()
        df.refresh(db_user)
    
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

  ```
- Getting Posts from the database:
  ```
    @app.get('/posts/', response_model=List[PostResponse])
      async def get_Posts(db: Session = Depends(get_db)) -> List[Post]:
        return db.query(Post).all()
  ```


## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://www.youtube.com/watch?v=RUddtw-oqFU&list=PL0lO_mIqDDFXDGav-t4qzQYdX6cfoLxXr)
- Today's lesson: [Working with Database](https://youtu.be/ZXEOw_9h0hg?si=Vd-OB8zNM-meE-dm)

---

### 🧠 Notes To My Future Self

- The `yield` keyword is used to return a list of values from a function.

---
