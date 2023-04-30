from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    events = relationship('Event', back_populates='player')

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))

    player = relationship('Player', back_populates='events')

#yritän kovakoodata nämä, 
class Type(Base):
    __tablename__ = 'types'

    type = Column(String, primary_key=True)

    def __init__(self):
        self.types = '.'.join(['level_started', 'level_solved'])



