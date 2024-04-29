from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated


from models import schemas
from models import tables
from Dao.UserDao import UserDao
from services.AuthService import AuthService
from models.DB import get_db

auth_controller_router = APIRouter()

class AuthController:
    @staticmethod
    @auth_controller_router.post("/authenticate")
    def authenticate(user : schemas.UserCreate,db:Session = Depends(get_db)) -> schemas.UserWithAuthToken:
        auth_service = AuthService(db)
        return auth_service.authenticate(user)
    

    @staticmethod
    @auth_controller_router.post("/authenticate_swagger")
    def authenticate(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db:Session = Depends(get_db)) -> schemas.UserWithAuthToken:
        user = schemas.UserCreate(name = "",email = form_data.username,password=form_data.password)
        auth_service = AuthService(db)
        return auth_service.authenticate(user)
    