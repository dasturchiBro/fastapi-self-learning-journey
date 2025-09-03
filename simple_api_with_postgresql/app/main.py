from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship, select
from typing import List, Optional
from datetime import datetime, timezone

app = FastAPI()

DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/fastapi_new"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False, max_length=50)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    full_name: Optional[str] = None
    role: str = Field(default="student")

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_active: bool = Field(default=True) 
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )

    posts: List["Post"] = Relationship(back_populates="author")

class PostBase(SQLModel):
    title: str
    body: str
    author_id: int = Field(foreign_key="user.id")

class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    

    author: Optional[User] = Relationship(back_populates="posts")

class UpdatePost(SQLModel):
    title: str  
    body: str  

@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post('/users/', response_model=User)
def create_user(user: UserBase, session: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.post('/posts/', response_model=Post)
def create_post(post: PostBase, session: Session = Depends(get_session)):
    db_post = Post.from_orm(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@app.get('/posts', response_model=List[Post])
def get_posts(session: Session = Depends(get_session)):
    return session.exec(select(Post)).all()

@app.get('/posts/{id}', response_model=Post)
def get_post(id: int, session: Session = Depends(get_session)):
    post = session.exec(select(Post).where(Post.id == id)).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return post

@app.get('/users', response_model=List[User])
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@app.put('/posts/{id}',response_model=Post)
def update_post(id: int, updated_post: UpdatePost, session: Session = Depends(get_session)):
    db_post = session.exec(select(Post).where(Post.id == id)).all()
    if not db_post:
        raise HTTPException(status_code=404, detail='Post Not Found')
    db_post = db_post[0]
    db_post.title = updated_post.title
    db_post.body = updated_post.body
    db_post.updated_at = datetime.now(timezone.utc)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@app.delete('/posts/{id}', response_model=Post)
def delet_post(id: int, session: Session = Depends(get_session)):
    post = session.exec(select(Post).where(Post.id == id)).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post Not Found')    
    session.delete(post)
    session.commit()
    return post

@app.get('/')
async def root():
	return {'message': "Hello World!!!"}
