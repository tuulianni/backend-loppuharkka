from fastapi import status, APIRouter

from ..functions import get_player_index, save_player
from ..database.models import *  
from ..database.database import players

router = APIRouter(prefix='/players', tags=['Players'])

#######GETS

#kutsuttaessa polkua tämä funktio triggaa
@router.get("", response_model=list[PlayerDb])
def get_players(): 
    return players

#palauttaa vain yhden tietyn asian id:perusteella
@router.get('/{id}', response_model=AllInfoDb)
def get_players(id: int):
    pid = get_player_index(id)
    return players[pid]

#######POSTS

@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase):
    return save_player(player_in)



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