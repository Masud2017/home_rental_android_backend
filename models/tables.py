from .DB import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String)

    user_histories = relationship("UserHistory", back_populates="owner")
    user_wallet = relationship("UserWallet", back_populates="user",uselist=False) # one to one relation with user and user wallet
    roles = relationship("Role", secondary="user_role", back_populates='users')
    homes = relationship("Home", back_populates='user')
    home_inventories = relationship("HomeInventory", back_populates='user')
    user_address = relationship("UserAddress", back_populates="user", uselist=False)
    image = relationship("Image", back_populates="user", uselist=False)

    recharge_histories = relationship("RechargeHistory", back_populates="user")

    transaction_histories = relationship("TransactionHistory", back_populates="user")



class UserHistory(Base):
    __tablename__ = "user_histories"

    id = Column(Integer, primary_key=True)

    # specifying bi-directional access
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="user_histories")


class Home(Base):
    __tablename__ = "homes"

    id = Column(Integer, primary_key=True)

    name = Column(String, index=True)
    desc = Column(String, index=True)
    price = Column(Integer, index=True)
    address = Column(String,nullable=False)
    image = Column(String,nullable=True)
    flat_count = Column(Integer, nullable= False)
    is_soled = Column(Boolean, nullable=False)
    expiry_date = Column(DateTime,nullable=True)
    created_at =Column(DateTime, default= datetime.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="homes")

class UserWallet(Base):
    __tablename__ = "user_wallets"
    id = Column(Integer, primary_key=True)
    balance = Column(Integer,unique=False,index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="user_wallet")

class UserAddress(Base):
    __tablename__ = "user_addresses"

    id = Column(Integer, primary_key=True)
    zip_code = Column(Integer,unique=False)
    street = Column(String, nullable= False)
    state = Column(String , nullable=False)
    country = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="user_address")


class HomeInventory(Base):
    __tablename__ = "home_inventories"

    id = Column(Integer, primary_key = True)
    payment_date = Column(DateTime,nullable=False, default = datetime.now())
    flat_count = Column(Integer)
    image = Column(String)
    name = Column(String)

    user_id = Column(Integer, ForeignKey("users.id")) # buyer user id 
    user = relationship("User", back_populates="home_inventories")

    home = relationship("Home") # his home relation will contain the home owner id
    home_id = Column(Integer, ForeignKey("homes.id"))



class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="image")

class RechargeHistory(Base):
    __tablename__ = "recharge_histories"

    id = Column(Integer, primary_key=True)
    msg = Column(String)
    payment_amount = Column(Integer)
    payment_platform = Column(String)
    recharge_date = Column(DateTime,default=datetime.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="recharge_histories")
    

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key= True)
    users = relationship("User", secondary="user_role", back_populates='roles')
    role = Column(String, nullable=True,unique=True)


user_role = Table('user_role', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True)
)

class TransactionHistory(Base):
    __tablename__ = "transaction_histories"

    id = Column(Integer, primary_key= True)
    
    user_id_second = Column(Integer)
    msg = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship("User", back_populates="transaction_histories")


