from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PlayerDb(PlayerBase):
    id: int

class AllInfoBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class AllInfoDb(AllInfoBase):
    id: int  

class EventsBase(BaseModel):
    type: str
    detail: str
    timestamp: str
    id: int

    class Config:
        orm_mode = True

class EventsDb(EventsBase):
    player_id: int

class EventsIn(BaseModel):
    type: str
    detail: str
    player_id: int

    class Config:
        orm_mode = True

class EventsInDb(EventsIn):
    timestamp: str
    id: int
    
    