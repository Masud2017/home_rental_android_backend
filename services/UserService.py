from sqlalchemy.orm import Session
from models import schemas
from Dao.UserDao import UserDao

class UserService:
    def __init__(self,db:Session):
        self.db = db
        self.user_dao = UserDao(self.db)

    def get_users(self) -> schemas.User:
        return self.user_dao.get_users()
    
    def get_users(self,user : schemas.UserCreate) -> schemas.User:
        return self.user_dao.add_user(user)