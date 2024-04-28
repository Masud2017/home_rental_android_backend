from sqlalchemy.orm import Session
from models import schemas
from Dao.UserDao import UserDao
from controllers import pwd_context

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
