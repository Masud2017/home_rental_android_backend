# Dao is the logic behind fetching, updating and creating record in database using {tables} from models folder

from models import schemas
from models import tables
from sqlalchemy.orm import Session
import traceback
from utils import util

class WalletDao:
    def __init__(self,db:Session):
        self.db = db

    def get_wallet_info(self,current_user:tables.User) -> schemas.UserWallet:
        res = self.db.query(tables.UserWallet).filter(tables.UserWallet.user_id == current_user.id).all()

        if len(res) == 0:
            return None
        else:
            return res[0]
        

    def update_wallet(self,wallet:schemas.UserWallet, current_user : tables.UserWallet) -> schemas.UserWallet:
        res = self.db.query(tables.UserWallet).filter(tables.UserWallet.user_id == current_user.id).all()

        if len(res) == 0:
            return None
        else:
            try:
                res[0].balance = wallet.balance

                self.db.commit()
                return res[0]
            except Exception:
                print(traceback.format_exc())
                return None