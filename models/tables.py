from .DB import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
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
    roles = relationship("Role", secondary="user_role", back_populates='users')



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

class HomeInventory(Base):
    __tablename__ = "home_inventories"

    id = Column(Integer, primary_key = True)
    user_name = Column(String, nullable = True)
    second_user_name = Column(String , nullable= True)
    rent_price = Column(Integer, nullable=False)
    payment_date = Column(DateTime,nullable=False)

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable = False)

class RechargeHistory(Base):
    __tablename__ = "recharge_histories"

    id = Column(Integer, primary_key=True)
    

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
