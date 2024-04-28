from models.DB import get_db
from models import tables
from sqlalchemy.orm import Session



def get_role_object_by_role_name(role_name:str, db:Session):
    role_obj = db.query(tables.Role).filter(tables.Role.role == role_name).all()

    return role_obj[0]