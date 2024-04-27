from .DB import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    user_histories = relationship("UserHistory", back_populates="owner")
    user_wallet = relationship("UserWallet", back_populates="owner",uselist=False) # one to one relation with user and user wallet


class UserHistory(Base):
    __tablename__ = "user_histories"

    id = Column(Integer, primary_key=True)

    # specifying bi-directional access
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="user_histories")


class Home(Base):
    __tablename__ = "homes"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, index=True)
    desc = Column(String, unique=True, index=True)
    price = Column(Integer, unique=True, index=True)
    count = Column(Integer, unique=True, index=True)

class UserWallet(Base):
    __tablename__ = "user_wallets"
    id = Column(Integer, primary_key=True)
    balance = Column(Integer,unique=False,index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="user_wallet")

class UserAddress(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True)
    zip_code = Column(Integer,unique=False)
