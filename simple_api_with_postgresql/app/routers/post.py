from fastapi import Depends, HTTPException, APIRouter, status
from sqlmodel import Session, SQLModel, select
from typing import List
from ..models import Post, PostBase, UpdatePost, User
from ..db import get_session
from .. import oauth2
from datetime import datetime, timezone

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('', response_model=List[Post])
def get_posts(session: Session = Depends(get_session)):
    return session.exec(select(Post)).all()

@router.get('/{id}', response_model=Post)
def get_post(id: int, session: Session = Depends(get_session)):
    post = session.exec(select(Post).where(Post.id == id)).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return post

@router.post('/', response_model=Post)
def create_post(post: PostBase, session: Session = Depends(get_session), user: User = Depends(oauth2.get_current_user)):
    db_post = Post(**post.dict(), author_id = user.id)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post

@router.put('/{id}',response_model=Post)
def update_post(id: int, updated_post: UpdatePost, session: Session = Depends(get_session), user: User = Depends(oauth2.get_current_user)):
    db_post = session.exec(select(Post).where(Post.id == id)).first()
    if not db_post:
        raise HTTPException(status_code=404, detail='Post Not Found')
    if not (db_post.author_id is user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not Authorized to perform this request!')
    db_post.title = updated_post.title
    db_post.body = updated_post.body
    db_post.updated_at = datetime.now(timezone.utc)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.delete('/{id}', response_model=Post)
def delet_post(id: int, session: Session = Depends(get_session), user: User = Depends(oauth2.get_current_user)):
    post = session.exec(select(Post).where(Post.id == id)).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post Not Found')    
    if not (post.author_id is user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not Authorized to perform this request!')
    session.delete(post)
    session.commit()
    return post
