from sqlalchemy import event
from sqlalchemy.orm import Session
from typing import Annotated

from . import tables
from controllers import pwd_context
from Dao.UserDao import UserDao
from models.DB import SessionLocal
from fastapi import Depends


SEED_DATA = {
      'roles': [
            {
                  'role': 'user',
            },
            {
                  'role': 'seller',
            },
            {
                  'role': 'root',
            }
      ],
      
}




def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in SEED_DATA and len(SEED_DATA[tablename]) > 0:
      connection.execute(target.insert(), SEED_DATA[tablename])

      

def add_role_seed_event():
    event.listen(tables.Role.__table__,"after_create",initialize_table)
