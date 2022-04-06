from fastapi import FastAPI # To create the app.

#Now, let's add the routers
from routes.create import app_create
from routes.get import app_get
from routes.update import app_update
from routes.delete import app_delete

app = FastAPI()

@app.get("/")
def welcome_message():
    return "Welcome to another API to manage users."

app.include_router(app_create)
app.include_router(app_get)
app.include_router(app_update)
app.include_router(app_delete)
