from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def read_events(db: Session):
    return db.query(models.Event).all()

def fetch_events(db: Session, player_id):
    temp = db.query(models.Event).filter(models.Event.player_id == player_id).all()
    if temp is None:
        raise HTTPException(
            status_code=404, detail=f"Event with player_id {player_id} not found"
        )
    return temp

def fetch_with_type(db: Session, type: str):
    temp = db.query(models.Event).filter(models.Event.type == type).all()
    if temp is None:
            raise HTTPException(
            status_code=404, detail=f"This type of events cannot be found"
        )
    return temp

def create_event(id: int, db: Session, event_in: schemas.EventsIn):
    today = date.today()
    day = date(today.year, 1, 1) + (today - date(today.year, 1, 1))
    new_ts = day.isoformat()
    temp = models.Event(**event_in.dict(), player_id = id, timestamp = new_ts)
    db.add(temp)
    db.commit()
    db.refresh(temp)
    return temp