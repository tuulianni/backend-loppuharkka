from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./playersapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

types = ['level_started', 'level_solved']

events = [
    {'id': 1, 'type': 'level_started', 'detail': "level_001", 'timestamp': '2023-01-13', 'player_id': 0}
]

# players = [
#     {'id': 0, 'name': 'Pekka Puupää', 'event': 'dont have'},
#     {'id': 1, 'name': 'Jukka Juupää', 'event': 'dont have'},
# ]

