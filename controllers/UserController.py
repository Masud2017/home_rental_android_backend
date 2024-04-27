from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao

from models.DB import get_db

user_controller_router = APIRouter()


class UserController:
    @user_controller_router.get("/getusers")
    @staticmethod
    def get_users(db:Session = Depends(get_db)) -> list[schemas.User]:
        
        user_dao = UserDao(db)
        return user_dao.get_users()
    