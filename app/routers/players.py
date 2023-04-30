from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from ..functions import get_db
from ..database.schemas import PlayerDb, AllInfoDb, PlayerBase  
from ..database import crud_players

router = APIRouter(prefix='/players', tags=['Players'])

#######GETS

@router.get("", response_model=list[PlayerDb])
def get_players(db: Session = Depends(get_db)): 
    return crud_players.read_players(db)

#tämä on rikki, koska koitan keksiä miten saa eventin mukaan
@router.get('/{id}', response_model=AllInfoDb)
def get_players_by_id(id: int, db: Session = Depends(get_db)):
    return crud_players.fetch_players(db, id)

#######POSTS

@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase, db: Session = Depends(get_db)):
    return crud_players.create_player(db, player_in)

#####ROOT huvin ja urheilun vuoksi

@router.get('/')
def root():
    return {'message': 'if you see only this, you have to go to 127.0.0.1:8000/docs'}

#######DELETE

# @router.delete('/{id}')
# def delete_player(id: int):
#     pid = get_player_index(id)
#     del players[pid]
#     return {'message': f'Player id {id} deleted'}