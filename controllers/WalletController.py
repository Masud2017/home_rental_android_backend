from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import Annotated
from utils.util import get_current_active_user


from models import schemas
from models import tables
from services.WalletService import WalletService
from models.DB import get_db

wallet_controller_router = APIRouter()

class AuthController:
    @staticmethod
    @wallet_controller_router.get("/getwallet")
    def get_wallet_info(current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> schemas.UserWallet:
        exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user does not have any wallet.",
        )

        wallet_service = WalletService(db)
        wallet_obj = wallet_service.get_wallet_info(current_user)
        if wallet_obj == None:
            raise exception

        return wallet_obj
    
    @staticmethod
    @wallet_controller_router.patch("/updatewallet")
    def update_wallet(wallet:schemas.UserWallet,current_user: Annotated[tables.User, Depends(get_current_active_user)] , db:Session = Depends(get_db)) -> schemas.UserWallet:
        exception = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user does not have any wallet.",
        )

        wallet_service = WalletService(db)
        wallet_obj = wallet_service.update_wallet(wallet,current_user)
        if wallet_obj == None:
            raise exception

        return wallet_obj    
    