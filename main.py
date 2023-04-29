from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel #luokka joka tarjoaa apuja tekemisessä

app = FastAPI()

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
    id: int
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventsDb(EventsBase):
   player_id: int

events = [
    {'id': 1, 'type': 'level_started', 'detail': "level_001", 'timestamp': '2023-01-13', 'player_id': 0}
]

players = [
    {'id': 0, 'name': 'Pekka Puupää', 'event': {'id': 1, 'type': 'level_started', 'detail': "level_001", 'timestamp': '2023-01-13', 'player_id': id}},
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
            status_code=404, detail=f"Player with id {id} not found")
    return pid

def get_event_index(id):
    eid = None
    for index, event in enumerate(events):
        if event['player_id'] == id:
            eid = index
            break
    if eid is None:
        raise HTTPException(
            status_code=404, detail=f"Event with player_id {id} not found")
    return eid

#kutsuttaessa polkua tämä funktio triggaa
@app.get("/players", response_model=list[PlayerDb])
def get_players(): 
    return players

@app.get("/events", response_model=list[EventsDb])
def get_events():
    return events

@app.get("/types")
def get_types():
    return types

#palauttaa vain yhden tietyn asian id:perusteella
@app.get('/players/{id}', response_model=AllInfoDb)
def get_players(id: int):
    pid = get_player_index(id)
    return players[pid]

@app.get('/players/{id}/events', response_model=EventsDb)
def get_events(player_id: int):
    eid = get_event_index(player_id)
    return events[eid]

#######

# @app.delete('/players/{id}')
# def delete_player(id: int):
#     pid = get_player_index(id)
#     del players[pid]
#     return {'message': f'Player id {id} deleted'}

#######

@app.post('/players', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id = new_id)

    players.append(player.dict())
    return player

@app.post('/players/{id}/events', response_model=EventsDb, status_code=status.HTTP_201_CREATED)
def create_event(event_in: EventsBase):
    new_id = len(events)
    event = EventsDb(**event_in.dict(), id = new_id)

    events.append(event.dict())
    return event

@app.get('/')
def root():
    return {'message': 'if you see only this, you have to go to 127.0.0.1:8000/docs'}