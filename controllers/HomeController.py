from fastapi import APIRouter,Depends,HTTPException,status
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
    def get_homes(db:Session = Depends(get_db)) -> list[schemas.HomeModelResponse]:
       home_service = HomeService(db)
       return home_service.get_homes()

    @home_controller_router.post("/addhome")
    @staticmethod
    def create_home(home :schemas.HomeModel, current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> schemas.HomeModelResponse:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid permission. You should be a seller to add a new home.",
        )
        if current_user.roles[0].role == "seller":
            home_service= HomeService(db)
            return home_service.create_home(home,current_user)
        else:
            raise exception
    
    @home_controller_router.get("/myhomelist")
    @staticmethod
    def get_user_created_homes(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> list[schemas.HomeModelResponse]:
        home_service = HomeService(db)
        return home_service.get_user_created_homes(current_user)
    
    @home_controller_router.delete("/deletehome/{home_id}")
    @staticmethod
    def delete_home(home_id:int,current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> schemas.HomeModelResponse:
        exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user has no home registered by that home id.",
        )

        home_service = HomeService(db)
        deleted_home_obj = home_service.delete_home(home_id,current_user)
        if deleted_home_obj == None:
            raise exception

        return deleted_home_obj