from models.DB import get_db
from models import tables
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from models import schemas
from Dao import UserDao

from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]
ALGORITHM = os.environ["JWT_ALGORITHM"]
SECRET_KEY = os.environ["app_secret"]


def get_role_object_by_role_name(role_name:str, db:Session):
    role_obj = db.query(tables.Role).filter(tables.Role.role == role_name).all()

    return role_obj[0]




async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db:Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        user_dao = UserDao.UserDao(db)
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = schemas.TokenData(email=username)
        except JWTError:
            raise credentials_exception
        
        user = user_dao.get_user_by_email(email=token_data.email)
        if user is None:
            raise credentials_exception
        return user
    
async def get_current_active_user(
current_user: Annotated[tables.User, Depends(get_current_user)],
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
