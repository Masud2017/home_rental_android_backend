from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext


from Dao.WalletDao import WalletDao
from sqlalchemy.orm import Session
from models import schemas,tables

from dotenv import load_dotenv
load_dotenv()
import os
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]
ALGORITHM = os.environ["JWT_ALGORITHM"]
SECRET_KEY = os.environ["app_secret"]


class WalletService:
    def __init__(self,db:Session):
        self.wallet_dao = WalletDao(db)
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def get_wallet_info(self,current_user:tables.User) -> schemas.UserWallet:
        return self.wallet_dao.get_wallet_info(current_user)
    
    
    def update_wallet(self, wallet:schemas.UserWallet, current_user :tables.User)-> schemas.UserWallet:
        return self.wallet_dao.update_wallet(wallet,current_user)
    
    def add_wallet_recharge_history(self,wallet_recharge_history:schemas.WalletRechargeHistory,current_user:tables.User) -> schemas.WalletRechargeHistory:
        return self.wallet_dao.add_wallet_recharge_history(wallet_recharge_history,current_user)
    

    def add_transaction_history(self,transaction_history : schemas.TransactionHistory, current_user : tables.User)->bool:
        return self.wallet_dao.add_transaction_history(transaction_history,current_user)
    
    def get_transaction_histories(self,current_user) -> list[schemas.TransactionHistory]:
        return self.wallet_dao.get_transaction_histories(current_user)
    
    def get_recharge_histories(self,current_user) -> list[schemas.WalletRechargeHistory]:
        return self.wallet_dao.get_recharge_histories(current_user)