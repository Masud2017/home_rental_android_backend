from fastapi import FastAPI,Depends
from models import tables,schemas
from models.DB import engine, SessionLocal
from sqlalchemy.orm import Session

from services.UserService import UserService
from services.AuthService import AuthService


tables.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/signup",response_model = None)
def signup():
    pass

@app.get("/getusers", response_model = schemas.User)
def get_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_users()