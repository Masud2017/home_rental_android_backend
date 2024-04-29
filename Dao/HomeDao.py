# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session

from utils import util

class UserDao:
    def __init__(self,db:Session):
        self.db = db


    def create_home(self, home : schemas.HomeModel) -> schemas.HomeModel:
        pass