from datetime import datetime
from fastapi import HTTPException

from .database.schemas import EventsInDb
from .database.database import SessionLocal, events

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

######GET FUNCTIONS
#def get_player_index(id):
#     pid = None
#     for index, player in enumerate(players):
#         if player['id'] == id:
#             pid = index
#             break
#     if pid is None:
#         raise HTTPException(
#             status_code=404, 
#             detail=f"Player with id {id} not found")
#     return pid

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

def save_event(event_in):
    new_id = len(events)
    now = datetime.now()
    new_timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(new_timestamp)
    event = EventsInDb(**event_in.dict(), id = new_id, timestamp = new_timestamp)

    events.append(event.dict())