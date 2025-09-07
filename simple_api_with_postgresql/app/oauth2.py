import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from . import models, db
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "TG9yZW0gSXBzdW0gaXMgc2ltcGx5IGR1bW15IHRleHQgb2YgdGhlIHByaW50aW5nIGFuZCB0eXBlc2V0dGluZyBpbmR1c3RyeS4gTG9yZW0gSXBzdW0g"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
	to_encode = data.copy()

	expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_encode.update({'exp': expire})

	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(db.get_session)):
	credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials!", headers={'WWW-Authenticate': 'Bearer'})
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		id: int = payload.get('user_id')
		if id is None:
			raise credentials_exception
		token_data = models.TokenData(id=id)
	except InvalidTokenError:
		raise credentials_exception
	user = session.exec(select(models.User).where(models.User.id == token_data.id)).first()
	if not user:
		raise credentials_exception
	return user


