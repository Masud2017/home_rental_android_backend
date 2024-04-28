# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session

from utils import util

class UserDao:
    def __init__(self,db:Session):
        self.db = db

    def get_users(self) -> list[schemas.User]:
        return self.db.query(tables.User).all()
    
    def add_user(self,user : schemas.UserCreate) -> schemas.UserBase:
        user_obj = tables.User()
        user_obj.email = user.email
        user_obj.password = user.password
        user_obj.name = user.name
        user_obj.user_wallet = None
        user_obj.user_histories = list()
        self.db.add(user_obj)
        # self.db.commit()
        # self.db.refresh(user_obj)

        role_obj = util.get_role_object_by_role_name("user",self.db)

        user_obj.roles.append(role_obj)

        # The wallet can be persisted in this way too.
        wallet = tables.UserWallet()
        wallet.balance = 0
        user_obj.user_wallet = wallet
        self.db.add(wallet)


        self.db.commit()
        self.db.refresh(wallet)
        self.db.refresh(user_obj)


        #For note: alternative way to persisting wallet with user object

        # wallet = tables.UserWallet()
        # wallet.balance = 0
        # wallet.user = user_obj
        # self.db.add(wallet)
        # self.db.commit()
        # self.db.refresh(wallet)

        
        return user_obj
    
    def add_seller_user(self, user: schemas.UserCreate) -> schemas.UserBase:
        user_obj = tables.User()
        user_obj.email = user.email
        user_obj.password = user.password
        user_obj.name = user.name
        user_obj.user_wallet = None
        user_obj.user_histories = list()
        self.db.add(user_obj)

        role_obj = util.get_role_object_by_role_name("seller",self.db)

        user_obj.roles.append(role_obj)

        self.db.commit()
        self.db.refresh(user_obj)

        wallet = tables.UserWallet()
        wallet.balance = 0
        wallet.user = user_obj
        self.db.add(wallet)
        self.db.commit()
        self.db.refresh(wallet)

    def add_root_user(self, user :schemas.UserCreate) -> schemas.UserBase:
        user_obj = tables.User()
        user_obj.name = user.name
        user_obj.email = user.email
        
        user_obj.password = user.password
        user_obj.user_wallet = None
        user_obj.user_histories = list()
        
        self.db.add(user_obj)

        role_obj = util.get_role_object_by_role_name("root",self.db)
        user_obj.roles.append(role_obj)
        self.db.commit()
        self.db.refresh(user_obj)

        return user_obj
    
    def get_user_by_email(self,email :str):
        result = self.db.query(tables.User).filter(tables.User.email == email).all()

        if len(result) == 0:
            return None
        else:
            return result[0]