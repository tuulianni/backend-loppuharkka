from pydantic import BaseModel

# Eventtien tulostukseen
class EventsBase(BaseModel):
    type: str
    detail: str
    timestamp: str
    id: int

    class Config:
        orm_mode = True

class EventsDb(EventsBase):
    player_id: int

#pelaajan luomiseen ja tulostukseen
class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PlayerDb(PlayerBase):
    id: int 

#Eventin luomiseen
class EventsIn(BaseModel):
    type: str
    detail: str
    player_id: int

    class Config:
        orm_mode = True

class EventsInDb(EventsIn):
    id: int
    timestamp: str

#kaikkien tietojen tulostukseen
class AllInfoBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class AllInfoDb(AllInfoBase):
    id: int 
    events: list[EventsBase]
    
    