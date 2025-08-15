# 📅 Day 5 — Working with Database - Part 1

## ✅ What I Learned Today
- Creating schemes in schemes.py:
  ``` 
    class UserBase(BaseModel):  
      name: str  
      age: int

    class User(UserBase):
      id: int  
      
      class Config:
        orm_mode = True   ...                                       
  ```
- Connecting to database in FastAPI (`database.py`):
   This line creates the SQLAlchemy engine:
    `engine = create_engine(SQL_URL, connect_args={"check_same_thread": False})`

   This line sets up a template to create sessions, which are used to talk to the database safely:
    `session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)`

   This line creates a base class for the ORM models:
    `base = declarative_base()`



## 📺 Learning Source

- YouTube Video: [FastAPI Crash Course](https://www.youtube.com/watch?v=RUddtw-oqFU&list=PL0lO_mIqDDFXDGav-t4qzQYdX6cfoLxXr)
- Today's lesson: [Working with Database](https://youtu.be/ZXEOw_9h0hg?t=600)

---

### 🧠 Notes To My Future Self
- Without `orm_mode`, `Pydantic` can’t handle SQLAlchemy objects directly.
- `orm_mode = True` lets your `Pydantic` schema read data directly from ORM objects (like SQLAlchemy models) instead of only from dictionaries.
- `SQLAlchemy` is a Python library that helps work with databases using Python code instead of writing raw SQL.
- In `database.py`, you make connections to the database. 
  In `schemes.py`, you set structures about what data you will get and respond. 
  In `models.py`, you create tables and all that stuff in the database.
---
