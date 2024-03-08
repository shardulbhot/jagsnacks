from fastapi import FastAPI
from . import models
from .database import engine

from .routers import order,user,auth


app=FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(order.router)
app.include_router(user.router)
app.include_router(auth.router)



