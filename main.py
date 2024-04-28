from fastapi import FastAPI,Depends
from models import tables,schemas
from models.DB import engine
from sqlalchemy.orm import Session

from services.UserService import UserService
from services.AuthService import AuthService
from models.seeder import add_role_seed_event

# including controllers
from controllers.UserController import user_controller_router

add_role_seed_event()
tables.Base.metadata.create_all(bind = engine)

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_controller_router)

# @app.post("/signup",response_model = None)
# def signup():
#     pass

# @app.get("/getusers", response_model = schemas.User)
# def get_users(db: Session = Depends(get_db)):
#     user_service = UserService(db)
#     return user_service.get_users()