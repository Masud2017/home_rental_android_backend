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

home_controller_router = APIRouter()



class HomeController:
    @home_controller_router.get("/getusers")
    @staticmethod
    def get_homes(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> list[schemas.Home]:
       pass