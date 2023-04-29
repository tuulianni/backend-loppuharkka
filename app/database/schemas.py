from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

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

class EventsIn(BaseModel):
    type: str
    detail: str
    player_id: int

class EventsInDb(EventsIn):
    timestamp: str
    id: int
    
    