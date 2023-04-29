from fastapi import HTTPException, status, APIRouter
from pydantic import BaseModel

router = APIRouter()

class PlayerBase(BaseModel):
    name: str

class PlayerDb(PlayerBase):
    id: int

class AllInfoBase(BaseModel):
    name: str
    event: dict

class AllInfoDb(AllInfoBase):
    id: int  

class EventsBase(BaseModel):
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventsDb(EventsBase):
   id: int

class EventIn(BaseModel):
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventInDb(EventIn):
    id: int

events = [
    {'id': 1, 'type': 'level_started', 'detail': "level_001", 'timestamp': '2023-01-13', 'player_id': 0}
]

players = [
    {'id': 0, 'name': 'Pekka Puupää', 'event': 'dont have'},
    {'id': 1, 'name': 'Jukka Juupää', 'event': 'dont have'},
]

types = ['level_started', 'level_solved']

def get_player_index(id):
    pid = None
    for index, player in enumerate(players):
        if player['id'] == id:
            pid = index
            break
    if pid is None:
        raise HTTPException(
            status_code=404, 
            detail=f"Player with id {id} not found")
    return pid

#rikki
def get_event_index(id):
    eid = None
    for index, event in enumerate(events):
         if event['player_id'] == id:
             eid = index
             return eid
    if eid is None:
         raise HTTPException(
             status_code=404, 
             detail=f"Events with player_id {id} not found")
   # return eid

#kutsuttaessa polkua tämä funktio triggaa
@router.get("/players", response_model=list[PlayerDb])
def get_players(): 
    return players

@router.get("/events", response_model=list[EventsDb])
def get_events():
    return events

@router.get("/types")
def get_types():
    return types

#palauttaa vain yhden tietyn asian id:perusteella
@router.get('/players/{id}', response_model=AllInfoDb)
def get_players(id: int):
    pid = get_player_index(id)
    return players[pid]

@router.get('/players/{id}/events', response_model=EventsDb)
def get_events(player_id: int):
    eid = get_event_index(player_id)
    return events[eid]

#######

# @router.delete('/players/{id}')
# def delete_player(id: int):
#     pid = get_player_index(id)
#     del players[pid]
#     return {'message': f'Player id {id} deleted'}

#######

@router.post('/players', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id = new_id)

    players.append(player.dict())
    return player

#jos player id ei ole olemassa? jos type ei ole olemassa?
@router.post('/players/{id}/events', response_model=EventsDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventsBase):
    new_id = len(events)
    event = EventsDb(**event_in.dict(), id = new_id)

    events.append(event.dict())
    return event

@router.get('/')
def root():
    return {'message': 'if you see only this, you have to go to 127.0.0.1:8000/docs'}