from fastapi import FastAPI
from models import tables
from models.DB import engine

from models.seeder import add_role_seed_event

# including controllers
from controllers.UserController import user_controller_router
from controllers.AuthController import auth_controller_router

add_role_seed_event()
tables.Base.metadata.create_all(bind = engine)

app = FastAPI()



@app.get("/deny_permission")
async def root():
    return {"message": "Sorry you don't have permission to access this resource."}

from fastapi.responses import RedirectResponse


app.include_router(user_controller_router)
app.include_router(auth_controller_router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=4444, reload=False, log_level="debug")