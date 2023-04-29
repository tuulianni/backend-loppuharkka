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