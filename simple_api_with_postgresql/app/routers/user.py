from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, SQLModel, select
from typing import List
from ..models import UserOut, UserBase, User
from ..pass_hash import pwd_context
from ..db import get_session

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', response_model=List[UserOut])
def get_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

@router.post('/', response_model=UserOut)
def create_user(user: UserBase, session: Session = Depends(get_session)):
    db_user = User.from_orm(user)
    check = session.exec(select(User).where(User.email == db_user.email or User.username == db_user.username)).first()
    if check:
        raise HTTPException(status_code=409, detail="User with this email or username already exists!")
    db_user.password_hash = pwd_context.hash(db_user.password_hash)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user



