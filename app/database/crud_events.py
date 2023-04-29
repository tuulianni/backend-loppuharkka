from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def read_events(db: Session):
    return db.query(models.Event).all()

def fetch_events(db: Session, player_id):
    event = db.query(models.Event).fillter(models.Event.id == player_id).all()
    if event is None:
        raise HTTPException(
            status_code=404, detail=f"Event with player_id {id} not found"
        )
    return event

def create_event(db: Session, event_in: schemas.EventsIn):
    event = models.Event(**event_in.dict(), timestamp = "aika tähän")
    db.add(event)
    db.commit()
    db.refresh(event)
    return event