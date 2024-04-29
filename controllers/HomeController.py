from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import schemas
from models import tables
from services.HomeService import HomeService

from . import pwd_context
from models.DB import get_db
from utils.util import get_current_active_user
from typing import Annotated

home_controller_router = APIRouter()



class HomeController:
    @home_controller_router.get("/gethomes")
    @staticmethod
    def get_homes(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> list[schemas.HomeModelResponse]:
       home_service = HomeService(db)
       return home_service.get_homes()

    @home_controller_router.post("/addhome")
    @staticmethod
    def create_home(home :schemas.HomeModel, current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> schemas.HomeModelResponse:
        print("Printing the value : ",type(current_user.roles[0].role))
        home_service= HomeService(db)
        return home_service.create_home(home,current_user)
    
    @home_controller_router.get("/myhomelist")
    @staticmethod
    def get_user_created_homes(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> list[schemas.HomeModelResponse]:
        home_service = HomeService(db)
        return home_service.get_user_created_homes(current_user)