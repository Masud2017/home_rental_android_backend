from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao
from passlib.context import CryptContext

from models.DB import get_db

user_controller_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:
    @user_controller_router.get("/getusers")
    @staticmethod
    def get_users(db:Session = Depends(get_db)) -> list[schemas.User]:
        user_dao = UserDao(db)

        return user_dao.get_users()
    
    @user_controller_router.post("/adduser")
    @staticmethod
    def add_user(user:schemas.UserCreate,db:Session = Depends(get_db))-> schemas.UserBase:
        user_dao = UserDao(db)

        return user_dao.add_user(user)
    