from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao
from services.UserService import UserService

from . import pwd_context
from models.DB import get_db
from utils.util import get_current_active_user
from typing import Annotated

user_controller_router = APIRouter()



class UserController:
    @user_controller_router.get("/getusers")
    @staticmethod
    def get_users(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> list[schemas.User]:
        user_dao = UserDao(db)

        print("Name of the current user is : ",current_user.name)


        return user_dao.get_users()
    
    @user_controller_router.post("/adduser")
    @staticmethod
    def add_user(user:schemas.UserCreate,db:Session = Depends(get_db))-> schemas.UserBase:
        user_service = UserService(db)

        return user_service.add_user(user)
    
    @user_controller_router.post("/addselleruser")
    @staticmethod
    def add_seller_user(user:schemas.UserCreate, db:Session = Depends(get_db)) -> schemas.UserBase:
        user_service = UserService(db)

        return user_service.add_seller_user(user)
    
    @user_controller_router.post("/addrootuser")
    @staticmethod
    def add_root_user(user:schemas.UserCreate, db:Session = Depends(get_db)) -> schemas.UserBase:
        
        # user_dao = UserDao(db)
        user_service = UserService(db)


        return user_service.add_root_user(user)