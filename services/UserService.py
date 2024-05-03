from sqlalchemy.orm import Session
from models import schemas
from Dao.UserDao import UserDao
from controllers import pwd_context
from models import tables
from fastapi import UploadFile

from utils.util import get_current_active_user,save_file_to_disk

class UserService:
    def __init__(self,db:Session):
        self.db = db
        self.user_dao = UserDao(self.db)

    def get_users(self) -> schemas.User:
        return self.user_dao.get_users()
    
    def add_user(self,user : schemas.UserCreate) -> schemas.UserBase:
        user.password = pwd_context.encrypt(user.password)
        return self.user_dao.add_user(user)
    
    def add_seller_user(self,user:schemas.UserCreate) -> schemas.UserBase:
        user.password = pwd_context.encrypt(user.password)
        return self.user_dao.add_seller_user(user)

    def add_root_user(self, user: schemas.UserCreate) -> schemas.UserBase:
        user.password = pwd_context.encrypt(user.password)
        return self.user_dao.add_root_user(user)

    def get_my_role(self,current_user:tables.User) -> str:
        return current_user.roles[0].role
    
    def upload_profile_pic(self,user_id : int,image:UploadFile):
        res = self.db.query(tables.User).filter(tables.User.id == user_id).all()

        if len(res) == 0:
            return False
        else:
            user = res[0]
            image_obj = tables.Image()
            file_name = save_file_to_disk(image,user.email)
            image_obj.image_url = file_name
            image_obj.user = user

            self.db.add(image_obj)
            self.db.commit()
            self.db.refresh(image_obj)

            return True
        
    def add_address(self,home_id,current_user:tables.User, address: tables.UserAddress) -> bool:
        return self.user_dao.add_address(home_id,current_user,address)