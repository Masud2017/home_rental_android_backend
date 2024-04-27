# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session

class UserDao:
    def __init__(self,db:Session):
        self.db = db

    def get_users(self) -> schemas.User:
        return self.db.query(tables.User).all()