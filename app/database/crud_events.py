from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def read_events(db: Session):
    return db.query(models.Event).all()

#miten saan ne kaikki tulostettua, all() ei toiminu :(
def fetch_events(db: Session, player_id):
    event = db.query(models.Event).filter(models.Event.player_id == player_id).first()
    if event is None:
        raise HTTPException(
            status_code=404, detail=f"Event with player_id {player_id} not found"
        )
    return event

def fetch_with_type(db: Session, type: str):
    temp = db.query(models.Event).filter(models.Event.type == type).all()
    if temp is None:
            raise HTTPException(
            status_code=404, detail=f"This type of events cannot be found"
        )
    return temp

#ei toimi
# def fetch_with_type(db: Session, type):
#     event = db.query(models.Event).filter(models.Event.type == type).first()
#     if event is None:
#         raise HTTPException(
#             status_code=404, detail=f"This type of events cannot be found"
#         )
#     return event

def create_event(db: Session, event_in: schemas.EventsIn):
    today = date.today()
    day = date(today.year, 1, 1) + (today - date(today.year, 1, 1))
    new_ts = day.isoformat()
    event = models.Event(**event_in.dict(), timestamp = new_ts)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event