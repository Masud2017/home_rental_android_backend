from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao

from models.DB import get_db

auth_controller_router = APIRouter()

class AuthController:
    @staticmethod
    def authenticate(db:Session = Depends(get_db)) -> schemas.UserWithAuthToken:
        pass