# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session

from utils import util

class HomeDao:
    def __init__(self,db:Session):
        self.db = db


    def create_home(self, home : schemas.HomeModel,current_user:tables.User) -> schemas.HomeModelResponse:
        home_obj = tables.Home(**home.model_dump())

        home_obj.user = current_user    

        self.db.add(home_obj)
        self.db.commit()
        self.db.refresh(home_obj)

        return home_obj


    def get_homes(self) ->list[schemas.HomeModelResponse]:
        home_list = self.db.query(tables.Home).all()

        return home_list
    
    def get_user_created_homes(self,current_user:tables.User)-> list[schemas.HomeModelResponse]:
        home_list = self.db.query(tables.Home).filter(tables.Home.user_id == current_user.id).all()

        return home_list