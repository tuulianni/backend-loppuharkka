from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session

from ..functions import get_db
from ..database.schemas import *  
#from ..database.database import players
from ..database.crud_players import create_player, read_players
from ..database.models import Player

router = APIRouter(prefix='/players', tags=['Players'])

#######GETS

@router.get("", response_model=list[PlayerDb])
def get_players(db: Session = Depends(get_db)): 
    return read_players(db)

#palauttaa vain yhden tietyn asian id:perusteella
@router.get('/{id}', response_model=AllInfoDb)
def get_players(db: Session, id):
    player = db.query(Player).filter(Player.id == id).first()
    if player is None:
        raise HTTPException(
            status_code=404, detail=f"Player with id {id} not found"
        )
    return player

#######POSTS

@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return create_player(db, player_in)


#####ROOT

@router.get('/')
def root():
    return {'message': 'if you see only this, you have to go to 127.0.0.1:8000/docs'}

#######DELETE

# @router.delete('/{id}')
# def delete_player(id: int):
#     pid = get_player_index(id)
#     del players[pid]
#     return {'message': f'Player id {id} deleted'}