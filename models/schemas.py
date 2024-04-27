# Schemas are basically sets of pydantic models that is being used to validate and parse data from http request object

from typing import Union,Tuple,List
from pydantic import BaseModel,ConfigDict


class UserHistory(BaseModel):
    id:int
    owner_id :int
    
    class Config:
        # orm_mode = True
        from_attributes = True

class UserWallet(BaseModel):
    id:int
    balance:int
    owner_id:int

    class Config:
        # orm_mode = True
        from_attributes = True

class UserBase(BaseModel):
    email:str
    class Config:
        # orm_mode = True
        from_attributes = True


class UserCrete(UserBase):
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
    # user_wallet: UserWallet

    model_config = ConfigDict(extra='allow')


    # class Config:
    #     orm_mode = True
    #     # from_attributes = True

