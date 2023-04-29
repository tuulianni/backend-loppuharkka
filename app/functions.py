import time
from fastapi import HTTPException

from .database.models import EventsDb, PlayerDb, EventsInDb
from .database.database import players, events


######GET FUNCTIONS
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

#rikki, palauttaa vain yhden ja haluaisin et palauttaa kaikki
def get_event_index(id):
    eid = None
    for index, event in enumerate(events):
         if event['player_id'] == id:
             eid = index
    if eid is None:
         raise HTTPException(
             status_code=404, 
             detail=f"Events with player_id {id} not found")
    return eid

####POST FUNCTIONS

def save_player(player_in):
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id = new_id)
    players.append(player.dict())
    return player

def save_event(event_in):
    new_id = len(events)
    new_timestamp = time.time()
    event = EventsInDb(**event_in.dict(), id = new_id, timestamp = new_timestamp)

    events.append(event.dict())