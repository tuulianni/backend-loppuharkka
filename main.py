from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel #luokka joka tarjoaa apuja tekemisessä

app = FastAPI()

class PlayerBase(BaseModel):
    name: str

class PlayerDb(PlayerBase):
    id: int

class AllInfoBase(BaseModel):
    name: str
    event: str

class AllInfoDb(AllInfoBase):
    id: int
   

class EventsBase(BaseModel):
    events: str

class EventsDb(EventsBase):
    id: int

players = [
    {'id': 0, 'name': 'Pekka Puupää', 'event': 'dont have'},
    {'id': 1, 'name': 'Jukka Juupää', 'event': 'dont have'},
]

events = [
    {'id': 1, 'type': 'level_started', 'detail': "level_1212_001", 'timestamp': '2023-01-13', 'player_id': 0}
]

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

#kutsuttaessa polkua tämä funktio triggaa
@app.get("/players", response_model=list[PlayerDb])
def get_players(): 
    return players

#palauttaa vain yhden tietyn asian id:perusteella
@app.get('/players/{id}', response_model=AllInfoDb)
def get_players(id: int):
    pid = get_player_index(id)
    return players[pid]

@app.get('/players/{id}/events', response_model=EventsDb)
def get_events(id: int):
    pid = get_player_index(id)
    return players[pid]

#######

@app.delete('/players/{id}')
def delete_player(id: int):
    pid = get_player_index(id)
    del players[pid]
    return {'message': f'Player id {id} deleted'}

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

@app.get('/')
def root():
    return {'message': 'if you see only this, you have to go to 127.0.0.1:8000/docs'}