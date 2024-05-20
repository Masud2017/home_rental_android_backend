from sqlalchemy.orm import Session
from models import schemas
from Dao.HomeDao import HomeDao
from controllers import pwd_context
from models import tables

from utils.util import get_current_active_user

class HomeService:
    def __init__(self,db:Session):
        self.db = db
        self.home_dao = HomeDao(self.db)

    def get_homes(self) -> list[schemas.HomeModelResponse]:
        return self.home_dao.get_homes()

    def create_home(self,home:schemas.HomeModel,current_user:tables.User) -> schemas.HomeModelResponse:
        return self.home_dao.create_home(home=home,current_user=current_user)
    
    def get_user_created_homes(self,current_user:tables.User) -> list[schemas.HomeModelResponse]:
        return self.home_dao.get_user_created_homes(current_user)
    
    def delete_home(self,home_id,current_user) -> schemas.HomeModelResponse:
        return self.home_dao.delete_home(home_id,current_user)
    
    def get_home(self,home_id:int) -> schemas.HomeModelResponse:
        return self.home_dao.get_home(home_id)
    

    def update_home(self,home_id:int,home:schemas.HomeModel, current_user : tables.User) -> bool:
        return self.home_dao.update_home(home_id,home,current_user)
    

    def buy_home(self,home_id:int, current_user : tables.User):
        return self.home_dao.buy_home(home_id,current_user)
    
    def add_home_image(self):
        pass
    def cancel_home(self,inventory_id:int,current_user:tables.User) -> bool:
        return self.home_dao.cancel_home(inventory_id,current_user)
    
    def add_home_image(self,home_id, image,current_user):
        return self.home_dao.add_home_image(home_id,image,current_user)
    
    def get_inventory_list(self,current_user) -> list[schemas.HomeInventory]:
        return self.home_dao.get_inventory_list(current_user)