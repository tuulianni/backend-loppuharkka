from fastapi import status, APIRouter

from ..functions import get_event_index, save_event
from ..database.schemas import EventsDb, EventsInDb, EventsIn
from ..database.database import events, types

router = APIRouter(prefix='/events', tags=['Events'])

@router.get("", response_model=list[EventsDb])
def get_events():
    return events

@router.get("/types")
def get_types():
    return types

@router.get('/{id}', response_model=EventsDb)
def get_events(player_id: int):
    eid = get_event_index(player_id)
    return events[eid]

#jos player id ei ole olemassa? jos type ei ole olemassa?
@router.post('/{id}', response_model=EventsInDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventsIn):
    return save_event(event_in)