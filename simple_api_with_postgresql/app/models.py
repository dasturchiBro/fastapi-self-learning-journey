from sqlmodel import Field, Session, SQLModel, select, Relationship
from pydantic import EmailStr, BaseModel
from datetime import datetime, timezone
from typing import Optional, List

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False, max_length=50)
    email: EmailStr = Field(index=True, unique=True, nullable=False)
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

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool  
    created_at: datetime
    updated_at: datetime

class PostBase(SQLModel):
    title: str
    body: str

class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    

    author: Optional[User] = Relationship(back_populates="posts")

class UpdatePost(SQLModel):
    title: str  
    body: str  

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str  
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None