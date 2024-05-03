# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session
import traceback

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
    
    def delete_home(self,home_id:int,current_user:tables.User) -> schemas.HomeModelResponse:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if len(res) == 0:
            return None
        else:
            if res[0].user.id == current_user.id:
                try:
                    self.db.delete(res[0])
                    self.db.commit()
                    return res[0]
                except Exception:
                    print(traceback.format_exc())
                    return None
            else:
                return None
            
    def get_home(self,home_id:int) -> schemas.HomeModelResponse:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if len(res) == 0:
            return None
        else:
            return res[0]
        

    def update_home(self,home_id:int,home : schemas.HomeModel, current_user : tables.User) -> bool :
        res = self.query(tables.Home).filter(tables.Home.id == home_id).all()

        if (len(res) == 0):
            return False
        else:
            home_obj = res[0]

            if home.name != "":
                home_obj.name = home.name
                
            if (home.desc != ""):
                home_obj.desc = home.desc
            if (home.price != 0):
                home_obj.price = home.price
            if (home.address != ""):
                home_obj.address = home.address

            if (home.flat_count != 0):
                home_obj.flat_count = home.flat_count

            home_obj.is_soled = home.is_soled

            self.db.commit()

            return True
        
    def buy_home(self,home_id:int, current_user:tables.User)->bool:
        res = self.db.query(tables.Home).filter(tables.Home.id == home_id).all()

        if (len(res) == 0):
            return False
        else:
            home = res[0]
            home_inventory = tables.HomeInventory()
            home_inventory.home = home
            home_inventory.user = current_user

            self.db.add(home_inventory)
            self.db.commit()
            self.db.refresh(home_inventory)
            return True
        
    def add_home_image(self):
        pass
    def cancel_home(self):
        pass
        