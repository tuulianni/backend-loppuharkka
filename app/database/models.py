from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str

class PlayerDb(PlayerBase):
    id: int

class AllInfoBase(BaseModel):
    name: str
    event: str

class AllInfoDb(AllInfoBase):
    id: int  

class EventsBase(BaseModel):
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventsDb(EventsBase):
   id: int

class EventIn(BaseModel):
    type: str
    detail: str
    timestamp: str
    player_id: int

class EventInDb(EventIn):
    id: int