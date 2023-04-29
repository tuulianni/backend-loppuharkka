from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def read_players(db: Session):
    return db.query(models.Player).all()

def create_player(db: Session, player_in: schemas.PlayerBase):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def fetch_players(db: Session, id):
    player = db.query(models.Player).filter(models.Player.id == id).first()
    if player is None:
        raise HTTPException(
            status_code=404, detail=f"Player with id {id} not found"
        )
    return player