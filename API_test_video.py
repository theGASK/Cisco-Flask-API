import requests

BASE = 'http://127.0.0.1:5000/' 

# r = requests.get(BASE + 'Video_Streaming/1')

r = requests.put(BASE + 'Video_Streaming/1', {'spectators': 1, 'participant': 'GASK', 'room': 'ABCD1234'})
print(r.json()) 

# just to wait for user input
video_id = input('> ')

r = requests.get(BASE + f'Video_Streaming/{video_id}')
print(r.json()) 
