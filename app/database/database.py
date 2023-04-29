from .models import PlayerDb, EventsDb

types = ['level_started', 'level_solved']

events = [
    {'id': 1, 'type': 'level_started', 'detail': "level_001", 'timestamp': '2023-01-13', 'player_id': 0}
]

players = [
    {'id': 0, 'name': 'Pekka Puupää', 'event': 'dont have'},
    {'id': 1, 'name': 'Jukka Juupää', 'event': 'dont have'},
]

