from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from Dao.UserDao import UserDao
from services.AuthService import AuthService

from models.DB import get_db

auth_controller_router = APIRouter()

class AuthController:
    @auth_controller_router.post("/authenticate")
    @staticmethod
    def authenticate(user : schemas.UserCreate,db:Session = Depends(get_db)) -> schemas.UserWithAuthToken:
        auth_service = AuthService(db)

        return auth_service.authenticate(user)