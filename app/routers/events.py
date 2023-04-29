from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

from ..functions import get_db
from ..database.schemas import EventsDb, EventsInDb, EventsIn
from ..database.database import types
from ..database import crud_events

router = APIRouter(prefix='/events', tags=['Events'])

####GETS 

@router.get("", response_model=list[EventsDb])
def get_events(db: Session = Depends(get_db)):
    return crud_events.read_events(db)

@router.get("/types")
def get_types():
    return types

@router.get('/{id}', response_model=EventsDb)
def get_events(player_id: int, db: Session = Depends(get_db)):
    return crud_events.fetch_events(db, player_id)

#jos player id ei ole olemassa? jos type ei ole olemassa?
@router.post('/{id}', response_model=EventsInDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventsIn, db: Session = Depends(get_db)):
    return crud_events.create_event(db, event_in)