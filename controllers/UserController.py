from fastapi import APIRouter,Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao
from services.UserService import UserService

from . import pwd_context
from models.DB import get_db
from utils.util import get_current_active_user,save_file_to_disk
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
    
    @user_controller_router.get("/getmyrole")
    @staticmethod
    def get_my_role(current_user: Annotated[tables.User, Depends(get_current_active_user)], db:Session = Depends(get_db)) -> schemas.RoleResponse:
        user_service = UserService(db)

        return schemas.RoleResponse(role = user_service.get_my_role(current_user))
    

    @user_controller_router.post("/upload_profile_pic")
    @staticmethod
    def upload_profile_pic(
        image : UploadFile = File(),
        user_id : int = File(),
        db:Session = Depends(get_db)
    ):
        user_service = UserService(db)

        return user_service.upload_profile_pic(user_id, image)

# /addaddress (do both update and add)
    @user_controller_router.get("/addaddress")
    @staticmethod
    def add_address(current_user: Annotated[tables.User, Depends(get_current_active_user)],  address: schemas.UserAddresssModel, db:Session = Depends(get_db)) -> bool:
        user_service = UserService(db)

        return user_service.add_address(current_user,address)