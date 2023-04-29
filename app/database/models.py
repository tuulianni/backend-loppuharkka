from sqlalchemy import Column, Integer, String

from .database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)
    player_id = Column(Integer, nullable=False)