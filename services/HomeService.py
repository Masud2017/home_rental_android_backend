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