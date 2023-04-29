from fastapi import FastAPI
from .routers import players, events

from .database.database import engine
from .database.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)