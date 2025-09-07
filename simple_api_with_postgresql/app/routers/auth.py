from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, db, pass_hash, oauth2
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
	tags = ['Authentication']
)

@router.post('/login', response_model = models.Token)
def login(user: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(db.get_session)):
	user.password = pass_hash.hash(user.password)
	result = session.exec(select(models.User).where(models.User.email == user.username and models.User.password_hash == user.password)).first()
	if not result:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials')

	access_token = oauth2.create_access_token(data={'user_id': result.id})
	return {'access_token': access_token, 'token_type': 'bearer'}