from datetime import date, timedelta
from pydantic import BaseModel
from pydantic.validators import int_validator

class DayThisYear():

    @classmethod
    def __get_validators__(cls):
        yield int_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: int):
        date_to_str = date.today().replace(month=1, day=1) + timedelta(days=v)
        return date_to_str.strftime("%Y-%m-%d")

#####

class EventsBase(BaseModel):
    type: str
    detail: str
    timestamp: str
    id: int

    class Config:
        orm_mode = True

class EventsDb(EventsBase):
    player_id: int

class PlayerBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PlayerDb(PlayerBase):
    id: int

class AllInfoBase(BaseModel):
    name: str
    events: EventsBase

    class Config:
        orm_mode = True

class AllInfoDb(AllInfoBase):
    id: int  

class EventsIn(BaseModel):
    type: str
    detail: str
    player_id: int

    class Config:
        orm_mode = True

class EventsInDb(EventsIn):
    id: int
    timestamp: str
    
    