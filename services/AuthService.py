from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext


from Dao.UserDao import UserDao
from sqlalchemy.orm import Session
from models import schemas

from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]
ALGORITHM = os.environ["JWT_ALGORITHM"]
SECRET_KEY = os.environ["app_secret"]


class AuthService:
    def __init__(self,db:Session):
        self.user_dao = UserDao(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def authenticate(self,user : schemas.UserCreate) -> schemas.UserWithAuthToken:
        existing_user = self.user_dao.get_user_by_email(user.email)
        if existing_user != None:
            if self.pwd_context.verify(user.password, existing_user.password):
                to_encode = {"sub":user.email}
                access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

                if access_token_expires:
                    expire = datetime.now(timezone.utc) + access_token_expires
                else:
                    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
                to_encode.update({"exp": expire})
                encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
                return schemas.UserWithAuthToken(email = to_encode["sub"],expires=to_encode["exp"], access_token=encoded_jwt)
                

            else:
                #failed
                return schemas.UserWithAuthToken(email = "",expires=0, auth_token= "")
 
        else:
            return schemas.UserWithAuthToken(email = "",expires=0, auth_token= "")


    