from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao

from . import pwd_context
from models.DB import get_db

user_controller_router = APIRouter()



class UserController:
    @user_controller_router.get("/getusers")
    @staticmethod
    def get_users(db:Session = Depends(get_db)) -> list[schemas.User]:
        user_dao = UserDao(db)

        return user_dao.get_users()
    
    @user_controller_router.post("/adduser")
    @staticmethod
    def add_user(user:schemas.UserCreate,db:Session = Depends(get_db))-> schemas.UserBase:
        user.password = pwd_context.encrypt(user.password)
        user_dao = UserDao(db)

        return user_dao.add_user(user)
    