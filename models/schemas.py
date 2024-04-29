# Schemas are basically sets of pydantic models that is being used to validate and parse data from http request object

from typing import Union,Tuple,List
from pydantic import BaseModel


class UserHistory(BaseModel):
    id:int
    owner_id :int
    
    class Config:
        # orm_mode = True
        from_attributes = True

class UserWallet(BaseModel):
    id:int
    balance:int
    class Config:
        # orm_mode = True
        from_attributes = True

class UserBase(BaseModel):
    name:str
    email:str
    class Config:
        # orm_mode = True
        from_attributes = True


class UserCreate(UserBase):
    password:str
    class Config:
        # orm_mode = True
        from_attributes = True


    class Config:
        # orm_mode = True
        from_attributes = True



class User(UserBase):
    id : int
    is_active: bool
    # user_histories : list[UserHistory] = []
    # user_wallet: UserWallet = None

    class Config:
        # orm_mode = True
        from_attributes = True

class UserWithAuthToken(BaseModel):
    email:str
    expires:int
    auth_token:str

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    email:str

    class Config:
        from_attributes = True

class HomeModel(BaseModel):
    name : str
    desc : str
    price:int
    address:str
    flat_count:int
    is_soled:bool

    class Config:
        from_attributes = True

class HomeModelResponse(HomeModel):
    id :int

    class Config:
        from_attributes = True


class RechargeWallet(BaseModel):
    class Config:
        from_attributes = True


class WalletRechargeHistory(BaseModel):
    msg:str
    payment_amount:int
    payment_platform:str # Bkash, Nagad, Rocket
    class Config:
        from_attributes = True